# 涂色 SVG 制作规则

涂色题需要前端识别并修改 SVG path 的 `fill`，因此 SVG 必须按以下规则制作。

## 必须规则

- 需要幼儿点击涂色的区域必须是封闭 path。
- 每个可涂色 path 必须有稳定 ID，例如 `flower`、`teddy_bear`。
- 不需要涂色但需要展示颜色的 path 可以预设 `fill`。
- 可涂色 path 初始建议为 `fill="#ffffff"`，描边为深色。
- 不要把多个可涂色物体合并成一个 path。
- 不要依赖图层名称，前端只读取 path 的 `id`。

## 示例

```svg
<svg viewBox="0 0 800 600" xmlns="http://www.w3.org/2000/svg">
  <path id="sun" d="..." fill="#FFD84D" stroke="#333333" />
  <path id="flower" d="..." fill="#ffffff" stroke="#333333" />
  <path id="teddy_bear" d="..." fill="#ffffff" stroke="#333333" />
</svg>
```

## 答案配置示例

```json
{
  "requiredColors": {
    "flower": "#FF8BC7"
  }
}
```

如果一题要求多个区域：

```json
{
  "requiredColors": {
    "flower": "#FF8BC7",
    "teddy_bear": "#FFD84D"
  }
}
```
