# AI 宠物素材工程

面向 Codex 的动画宠物素材与制作记录。项目以角色参考图为起点，经过姿态生成、透明背景处理、精灵图集组装和自动校验，产出可直接接入 Codex 的 v2 宠物资源。

当前仓库包含两套已通过 v2 图集校验的最终资源：

| 宠物 | 角色定位 | 图集规格 | 校验 |
| --- | --- | --- | --- |
| **青岚·原比例** (`qinglan-original`) | 蓝衣古风剑客，成人比例、束发、背剑 | 8 × 11，单格 192 × 208 | `ok: true` |
| **吕洞宾** (`baxian-lvdongbin`) | 电影《八仙！》角色风格的青蓝长袍剑客 | 8 × 11，单格 192 × 208 | `ok: true` |

## 资源内容

每套 v2 图集尺寸为 **1536 × 2288 px**，包含：

- 9 个标准动画状态：`idle`、`running-right`、`running-left`、`waving`、`jumping`、`failed`、`waiting`、`running`、`review`；
- 16 个顺时针视线方向（`000`–`337.5`，分布在第 10、11 行）；
- RGBA 透明背景、纯色键清理和透明像素残留校验；
- `sprite_version_number: 2` 的宠物描述与校验记录。

最终可交付文件位于 [`release/pets`](./release/pets)：每套资源都提供 PNG（无损）、WebP（体积更小）、宠物描述和校验结果。通常接入时优先使用 WebP，需要无损编辑时再使用 PNG。

## 目录结构

```text
.
├── release/pets/                 # 可迁移、可发布的最终宠物包
│   ├── qinglan-original/
│   └── baxian-lvdongbin/
├── 角色素材/                     # 角色参考图与官方素材
├── 角色设定/                     # 用户提供的角色设定图/视频
├── tools/imagegen_url_adapter/   # 图像生成 URL 适配工具
├── .env.example                  # 本地生成所需环境变量示例
└── README.md
```

`output/` 和 `tmp/` 是生成过程中的中间结果、逐帧拆解和 QA 草稿，已加入 `.gitignore`。最终包已单独整理到 `release/`，因此换机器时不依赖这些本地临时目录。

## 在另一台 Codex 上迁移

```bash
git clone https://github.com/kingdoja/ai-pet.git
cd ai-pet
```

打开项目后，从 `release/pets/<pet-id>/` 取用最终图集；若要继续生成或修复，使用 `角色素材/`、`角色设定/` 作为参考，并在新的 Codex 环境中重新生成 `output/`。不要把真实 API Key 写进仓库；按 `.env.example` 创建本地 `.env` 即可。

## 本地检查

校验记录保存在各宠物目录的 `validation-*.json` 中。快速确认最终包：

```bash
jq '{ok, sprite_version_number, columns, rows, width, height, errors, warnings}' \
  release/pets/baxian-lvdongbin/validation-extended-v11.json
```

预期结果是 `ok: true`、`sprite_version_number: 2`、`columns: 8`、`rows: 11`。

## 参考素材与使用说明

`角色素材/` 中部分图片来自用户提供的参考或片方公开发布素材，仅用于角色外观研究和本地生成流程。发布或再分发前，请确认相应版权、肖像/角色授权和平台使用条款；不要把参考图中的水印、字幕、片名或宣传文案带入宠物图集。

## 状态

本仓库的首个 Git 提交用于固化当前工作区：源参考、工具、配置示例和两套最终 v2 宠物包均纳入版本控制；本地密钥、虚拟环境和生成中间文件不纳入版本控制。
