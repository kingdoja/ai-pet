# AI Pet Assets

> Turn a character into a living Codex AI pet.

A user- and creator-friendly collection of animated pet assets. It ships ready-to-migrate v2 sprite sheets, standard animation states, look directions, pet descriptors, and validation records. Character references and the image-generation adapter are included so you can continue creating, repairing, or extending the pets on another Codex machine.

**Language / 语言:** [中文](README.md) · English (current)

## Why use this repository

- **Ready to use:** two complete pet packages that already pass v2 validation.
- **Useful motion set:** 9 standard animation states for idle, movement, waving, jumping, failure, waiting, and review flows.
- **Full orientation support:** 16 clockwise look directions make interactive pets feel more responsive.
- **Production-friendly delivery:** WebP for a smaller runtime footprint, PNG for lossless editing, plus JSON descriptors, manifests, and validation results.
- **Easy to migrate:** final deliverables live in `release/pets/` and do not depend on local generation intermediates.

## Pet preview

<table>
  <tr>
    <td align="center"><strong>Qinglan · Original Proportions</strong><br><img src="release/pets/qinglan-original/spritesheet-extended.webp" width="360" alt="Qinglan sprite sheet"></td>
    <td align="center"><strong>Lü Dongbin</strong><br><img src="release/pets/baxian-lvdongbin/spritesheet-extended.webp" width="360" alt="Lü Dongbin sprite sheet"></td>
  </tr>
</table>

| Pet | Character concept | Package | Validation |
| --- | --- | --- | --- |
| **Qinglan · Original Proportions** (`qinglan-original`) | Blue-robed ancient-style swordsman with tied hair and a back sword | [Open package](release/pets/qinglan-original/) | `ok: true` |
| **Lü Dongbin** (`baxian-lvdongbin`) | Ancient-style swordsman in a blue-teal robe with a back sword | [Open package](release/pets/baxian-lvdongbin/) | `ok: true` |

## Get started in 5 minutes

```bash
git clone https://github.com/kingdoja/ai-pet.git
cd ai-pet
```

Choose a pet under `release/pets/<pet-id>/`:

- Use `spritesheet-extended.webp` for runtime delivery;
- Use `spritesheet-extended.png` when you need lossless editing or re-exporting;
- Read `pet_request.json` or `manifest.json` for atlas dimensions, animation rows, and file metadata.

## Asset specification

Each atlas follows the Codex v2 pet asset convention:

- **Atlas:** 1536 × 2288 px; 8 columns × 11 rows; each cell is 192 × 208 px;
- **Animation states:** `idle`, `running-right`, `running-left`, `waving`, `jumping`, `failed`, `waiting`, `running`, `review`;
- **Look directions:** 16 clockwise directions (`000`–`337.5`) in rows 10 and 11;
- **Format:** RGBA with transparent-pixel RGB residue removed;
- **Version:** `sprite_version_number: 2`.

## Repository layout

```text
.
├── release/pets/                 # Final, publishable, portable pet packages
│   ├── qinglan-original/
│   └── baxian-lvdongbin/
├── 角色素材/                     # Character references and public materials
├── 角色设定/                     # Character design images and video
├── tools/imagegen_url_adapter/   # Image-generation URL adapter
├── .env.example                  # Local generation environment template
├── README.md                     # Chinese documentation
└── README.en.md                  # English documentation
```

`output/` and `tmp/` contain frame intermediates, QA drafts, and temporary prompts. They are ignored by default and are not required when migrating the final assets.

## Move to another Codex machine

1. Clone the repository and open the project directory.
2. Use the final sprite sheets directly from `release/pets/`.
3. To continue generation or repair, copy `.env.example` to a local `.env`, add a new API key, and use `角色素材/` and `角色设定/` as references.
4. Regenerate `output/` and `tmp/` in the new environment if needed; they do not need to be copied from the old machine.

> Never commit a real API key. Access to this private repository also requires signing in to GitHub on the new machine.

## Local validation

Print a validation summary for both packages:

```bash
for f in release/pets/*/validation-*.json; do
  jq '{ok, sprite_version_number, columns, rows, width, height, errors, warnings}' "$f"
done
```

Expected values are `ok: true`, `sprite_version_number: 2`, `columns: 8`, and `rows: 11`.

## References and usage

Some images under `角色素材/` were supplied by the user or published by the film/distribution team. They are included only for appearance research and the local generation workflow. Confirm copyright, likeness/character permissions, and platform terms before publishing or redistributing; do not carry watermarks, subtitles, titles, or promotional copy from reference images into a pet atlas.

## Project status

The repository currently preserves two portable v2 pet packages, their references, the generation adapter, and validation records. You can build new characters or animation variants on top of these assets.
