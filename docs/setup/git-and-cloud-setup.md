# Git 仓库与云资源准备说明

## Git 仓库

当前工作区还不是 Git 仓库。建议先把整个项目初始化为仓库，再开始工程代码开发。

### Git 放在哪里

Git 仓库不要放在 FAI 平台里维护，应该放在代码托管平台：

- 首选：公司内部 Git 平台。
- 备选：GitHub、GitLab、Gitee。

原因：

- Git 负责代码版本管理、分支、回滚、协作审查。
- FAI 更适合做运行、部署、数据库和微应用管理，不适合替代正式代码仓库。
- 最稳妥的方式是：`本地开发 -> Git 仓库托管 -> 选择 FAI 或云环境部署`。

### 本地初始化

在项目根目录执行：

```powershell
git init
git add .
git commit -m "chore: initialize toddler assessment workspace"
```

### 连接远程仓库

先在 GitHub、GitLab、Gitee 或公司 Git 平台创建一个空仓库，然后执行：

```powershell
git remote add origin <你的远程仓库地址>
git branch -M main
git push -u origin main
```

### 推荐分支

- `main`：生产可发布代码。
- `develop`：日常集成。
- `feature/h5-shell`：前端横屏框架。
- `feature/api-core`：后端核心 API。
- `feature/content-import`：题目导入和种子数据。

V1 时间紧，也可以只用 `main` + 小步提交，但每次可运行版本都要提交。

## POC 阶段到底在哪个平台做

POC 阶段建议分成 3 个平台，各做各的事：

| 事项 | 在哪做 | 为什么 |
| --- | --- | --- |
| 代码版本管理 | GitHub / GitLab / 公司 Git | 负责代码历史、分支、协作 |
| 前后端与数据 POC | FAI 平台 | 验证公司内部平台能不能承载这个项目 |
| 本地开发与调试 | 你的电脑当前工作区 | 方便快速改代码、整理模板、跑本地验证 |

### 一句话原则

- `Git` 放代码仓库。
- `FAI` 做部署能力验证。
- `本地工作区` 做开发和准备。

## POC 执行表

下面这张表就是下一步我们应该怎么做。

### 第 1 步：建立正式代码仓库

- 平台：`本地 + GitHub/GitLab/公司 Git`
- 你要做的事：
  - 在代码托管平台创建一个空仓库。
  - 在本地项目根目录执行 Git 初始化。
  - 绑定远程仓库并首次推送。
- 操作：

```powershell
git init
git add .
git commit -m "chore: initialize toddler assessment workspace"
git remote add origin <你的远程仓库地址>
git branch -M main
git push -u origin main
```

- 产出：
  - 一个可访问的远程 Git 仓库。
  - 当前项目的第一版基线代码。
- 通过标准：
  - 你能在代码托管平台看到 `docs/`、`UI设计/` 等文件。

### 第 2 步：整理最小内容数据

- 平台：`本地工作区`
- 你要做的事：
  - 按模板填一条最小可跑链路的数据。
- 重点文件：
  - `docs/data-templates/questions.template.csv`
  - `docs/data-templates/question-groups.template.csv`
  - `docs/data-templates/stage-intros.template.csv`
  - `docs/data-templates/stage-papers.template.csv`
  - `docs/data-templates/pack-groups.template.json`
- 最小目标：
  - 1 个基础包试卷组。
  - 第 1 关至少 2 道题。
  - 1 个关卡导言音频。
  - 1 个题组首题 VO。
- 产出：
  - 一套能驱动首页 -> 第一关导言 -> 两道题的数据。
- 通过标准：
  - 模板字段填完整，音频/图片路径能一一对应素材文件。

### 第 3 步：验证 FAI 能不能承载 H5

- 平台：`FAI`
- 你要做的事：
  - 创建一个最小微应用，确认 FAI 能托管前端页面。
- 在 FAI 里怎么做：
  - 打开平台首页。
  - 进入“微应用”页签。
  - 点击“创建微应用”。
  - 选择 `default（基础应用）` 模板。
  - 创建后进入“管理文件”。
  - 放一个最简单的 `index.html` 页面。
- 产出：
  - 一个可访问的微应用地址，例如：
    `https://fai.fltrp.com/ms/apps/{uid}/{appName}/`
- 通过标准：
  - 浏览器能打开这个页面。
  - 页面可以展示一段静态文本或简单 UI。

### 第 4 步：验证 FAI 数据库

- 平台：`FAI`
- 你要做的事：
  - 申请 PostgreSQL 数据库。
  - 确认能建立最小业务表。
- 在 FAI 里怎么做：
  - 找到“数据库连接管理”。
  - 申请 PostgreSQL 数据库。
  - 确认系统生成 `/mnt1/fltrpop/data/{uid}/db.json`。
  - 用平台支持的微服务代码或示例，连库执行一条建表 SQL 和一条查询 SQL。
- 最小建表建议：
  - `users`
  - `assessment_sessions`
- 产出：
  - 一个可连接的 PostgreSQL 实例。
  - 至少两张表成功创建。
- 通过标准：
  - 能插入一条测试数据，再查出来。

### 第 5 步：验证 FAI 文件和素材访问

- 平台：`FAI`
- 你要做的事：
  - 上传 1 张图片和 1 个音频。
  - 确认前端页面能访问。
- 在 FAI 里怎么做：
  - 使用平台文件上传能力，把文件放到微应用可访问目录或平台规定的静态资源目录。
  - 在 `index.html` 中引用图片和音频。
- 产出：
  - 一个带图片和音频的静态页面。
- 通过标准：
  - 图片正常显示。
  - 音频可以播放。

### 第 6 步：验证 FAI API 能力

- 平台：`FAI`
- 你要做的事：
  - 做 2 个最小接口。
- 接口建议：
  - `GET /health`
  - `POST /api/assessments/start`
- 目标：
  - 前端能调用接口。
  - 接口能返回 JSON。
- 产出：
  - 一个最小前后端联通的微应用。
- 通过标准：
  - 页面调用后能拿到正常 JSON 响应。

### 第 7 步：决定最终部署路线

- 平台：`本地评审`
- 我们根据前 6 步结果做选择：
  - 如果 FAI 同时满足前端、后端、数据库、文件访问、接口开发，优先用 FAI。
  - 如果 FAI 在某个关键能力上卡住，比如文件访问、接口性能、部署限制，就改走云服务器方案。

## 你现在最先做哪一步

最先做的是：

1. 在 `GitHub/GitLab/公司 Git` 创建空仓库。
2. 在 `FAI` 创建一个最小微应用。

这两步不要互相替代：

- Git 仓库是代码源头。
- FAI 是部署候选平台。

## 云资源最小清单

建议使用同一家云厂商，减少跨云配置成本。阿里云、腾讯云、华为云均可。

如果公司内部 AI 开放平台 FAI 能满足生产要求，也可以优先走内部平台。根据当前可访问文档，它支持微应用、前端页面、后端微服务、文件上传下载、模板部署、备份恢复、PostgreSQL 数据库和面向 AI 工具的部署 API。它更像内部 PaaS，不是传统云服务器；如果采用它，后端实现方式需要按平台支持的微应用/Charlang/PostgreSQL 形态重新设计，而不是默认 NestJS + Docker 直接部署。

### FAI 平台试用验证项

在正式决定替代外部云资源前，建议先做一个 1 天 POC：

- 创建一个微应用，确认 H5 静态页面可访问。
- 创建 PostgreSQL 数据库，确认可建表、读写、备份。
- 上传一张图片和一段音频，确认 H5 可稳定访问素材。
- 实现 2 个 API：`GET /health` 和 `POST /api/assessments/start`。
- 确认平台是否支持自定义域名、HTTPS、访问日志、错误日志和发布回滚。
- 确认是否有文件大小、请求超时、并发、数据库容量和外部接口访问限制。

POC 通过后，V1 可以考虑用 FAI 承载测试环境或生产环境；如果 POC 不通过，仍按云服务器 + PostgreSQL + Redis + 对象存储方案推进。

### 必备

| 资源 | 用途 | V1 建议 |
| --- | --- | --- |
| 云服务器 ECS/CVM | 后端服务、Nginx、部署脚本 | 2 核 4G 起步，Ubuntu LTS |
| PostgreSQL | 主业务数据库 | 托管数据库优先，开启自动备份 |
| Redis | 验证码、防刷、幂等锁 | 托管 Redis 1G 起步 |
| 对象存储 OSS/COS | 图片、音频、录音文件 | 私有桶 + 签名上传/访问 |
| CDN | H5 静态资源加速 | 绑定 H5 域名 |
| 域名 | 用户访问和 API | `h5.xxx.com`、`api.xxx.com` |
| HTTPS 证书 | 微信 WebView 和生产安全 | 免费证书可起步 |

### 推荐部署结构

```text
用户浏览器/微信 WebView
  -> CDN / Nginx 静态 H5
  -> api.xxx.com / Nginx 反向代理
  -> Node.js API Docker 容器
  -> PostgreSQL / Redis / 对象存储
```

### 需要你准备的信息

- 云厂商账号和区域。
- 域名是否已有，以及是否可做备案/解析。
- 是否允许我按 Docker + Nginx + PostgreSQL + Redis 的方式设计部署。
- 短信服务商选择：复用旧接口、阿里云短信、腾讯云短信，或先开发假验证码。

## 生产前注意

- 不要把云账号 AccessKey、短信密钥、数据库密码发到聊天或写进代码。
- 密钥只放服务器环境变量或云平台密钥管理。
- 生产数据库必须开启自动备份。
- 对象存储录音桶建议私有读写，通过后端签名访问。
