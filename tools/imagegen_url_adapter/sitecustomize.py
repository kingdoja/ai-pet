"""Normalize URL-only Image API responses for the bundled imagegen CLI."""

from __future__ import annotations

import base64
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from openai.resources.images import Images


_MAX_IMAGE_BYTES = 100 * 1024 * 1024
_ORIGINAL_EDIT = Images.edit
_ORIGINAL_GENERATE = Images.generate


def _download_image(url: str) -> bytes:
    parsed = urlparse(url)
    if parsed.scheme != "https" or not parsed.netloc:
        raise ValueError("Image API returned a non-HTTPS image URL")

    request = Request(url, headers={"User-Agent": "CodexImagegenURLAdapter/1.0"})
    with urlopen(request, timeout=180) as response:
        content_type = response.headers.get_content_type()
        if not content_type.startswith("image/"):
            raise ValueError(f"Image URL returned unexpected content type: {content_type}")
        payload = response.read(_MAX_IMAGE_BYTES + 1)

    if len(payload) > _MAX_IMAGE_BYTES:
        raise ValueError("Image URL response exceeded 100 MiB")
    if not payload:
        raise ValueError("Image URL response was empty")
    return payload


def _normalize_response(result):
    for item in result.data:
        if item.b64_json is None and item.url:
            item.b64_json = base64.b64encode(_download_image(item.url)).decode("ascii")
    return result


def _edit_with_url_support(self, *args, **kwargs):
    return _normalize_response(_ORIGINAL_EDIT(self, *args, **kwargs))


def _generate_with_url_support(self, *args, **kwargs):
    return _normalize_response(_ORIGINAL_GENERATE(self, *args, **kwargs))


Images.edit = _edit_with_url_support
Images.generate = _generate_with_url_support
