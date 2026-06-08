# 内容数据导入模板说明

这组模板用于把题目、音频、图片、答案、涂色 SVG 和试卷组整理成后端可导入的种子数据。

## 文件清单

- `questions.template.csv`：题目主表，所有题型都在这里登记。
- `stage-intros.template.csv`：每一关关卡页/导言页播放的关卡引导音频。
- `question-groups.template.csv`：每一关内部题目分组，以及分组第一题加载时播放的组 VO。
- `stage-papers.template.csv`：单关试卷配置。
- `pack-groups.template.json`：基础包/增强包试卷组配置。
- `asset-manifest.template.csv`：素材文件清单，用于检查图片、音频、SVG 是否齐全。
- `coloring-svg-requirements.md`：涂色 SVG 制作规则。

## 题型枚举

- `binary_judge`
- `selection`
- `voice_record`
- `coloring`

## 题型变体枚举

- `audio_image_judge`：音图判断
- `audio_only_judge`：纯音判断
- `image_text_judge`：图文判断
- `picture_book_judge`：绘本判断
- `listen_choose_image`：听音选图
- `word_choose_image`：看词选图
- `image_choose_word`：看图选词
- `listen_repeat`：听音跟读
- `image_repeat`：看图跟读
- `image_speaking`：看图说话
- `instruction_coloring`：互动涂色

## 导入约定

- 所有 ID 使用稳定字符串，不要用中文做 ID。
- 素材路径统一相对 `assets/`，例如 `assets/images/q001-cat.png`。
- `answer_json` 必须是合法 JSON 字符串。
- 录音题如果 6/30 前未接入声通，`answer_json` 可以配置假评分策略。
- 涂色题的 SVG path 必须有稳定 `id`。

## 音频字段说明

- `stage-intros.template.csv` 的 `intro_audio`：用于每一关的关卡页/导言页，例如“第一关，打开森林之门”。
- `question-groups.template.csv` 的 `group_vo_audio`：用于同一题组的通用画外音，一般在该分组第一道题加载时播放一次。
- `questions.template.csv` 的 `item_audio`：用于具体题目的题干音频、示范音或指令音。
- `questions.template.csv` 的 `vo_audio`：只在某一道题有特殊 VO 时使用；一般情况下留空，优先使用题组 VO。
