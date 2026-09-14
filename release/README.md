# 最终宠物包

这里存放可直接迁移到另一台 Codex 的最终资源。每个子目录对应一个 `pet_id`，包含：

- `spritesheet-extended.webp`：推荐运行时使用的 RGBA v2 图集；
- `spritesheet-extended.png`：无损版本；
- `pet_request.json`：宠物身份、图集尺寸与动画行定义；
- `manifest.json`：本仓库使用的相对路径清单与校验摘要；
- `validation-*.json`：生成流程留下的完整校验记录。

中间生成图、逐帧 QA 草稿和临时提示词仍保留在本机的 `output/`、`tmp/`（默认不提交），避免仓库膨胀。
