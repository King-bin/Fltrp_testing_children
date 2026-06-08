# 外研定级测幼儿版 6月30日生产交付方案

## 目标

在 2026-06-30 前交付一套可面向真实用户使用的《外研定级测·幼儿版》生产级 V1：包含移动端强制横屏 H5、后端服务、数据存储、资源上传/访问、基础部署、日志监控和上线验收流程。

V1 的核心判断标准不是“所有设想都做完”，而是“用户可完成一次完整测评，数据可追踪，结果可生成，服务可部署和回滚”。

## 交付边界

### V1 必做

- H5 用户端：登录/协议/学段采集、首页、基础包地图页、关卡导言页、四类题型、基础包 80% 分流、增强包、基础包完成页、增强包完成页、报告入口。
- 横屏适配：移动端强制横屏提示或旋转容器；桌面 Web 也按横屏比例适配。
- 小程序嵌入预留：运行环境识别、WebView bridge 适配层、关闭页面/打开设置/登录态透传接口预留。
- 后端 API：认证、测评会话、试卷组随机、题目下发、答题提交、录音上传、算分分流、报告结果查询。
- 数据存储：用户、儿童学段、测评会话、试卷组、关卡试卷、题目、作答记录、录音文件、涂色结果、报告结果。
- 内容配置：先用种子数据和轻量管理接口导入题目/试卷/试卷组，保证教研可替换内容；完整拖拽后台延期。
- 部署：前端静态托管，后端服务部署，数据库部署，对象存储接入，环境变量和密钥管理，日志与基础监控。
- 验收：真机横屏、微信 WebView 预检、录音权限、弱网重试、重复点击防抖、核心接口幂等。

### V1 暂不做

- 完整可视化教研后台，包括拖拽组卷、穿梭框、复杂权限体系。
- 复杂商业化报告和推课转化链路。
- 高复杂 IP 骨骼动画/Lottie 全套动作库。
- 微信小程序原生壳完整开发和上架；V1 只保证 H5 可嵌入。
- 语音批改引擎深度评测策略；V1 先完成录音采集、上传、回放、结果字段预留，若声通接口及时提供再接入。

## 产品流程

1. 用户打开 H5。
2. 系统进入横屏适配层，加载首页背景和基础资源。
3. 用户点击“开始森林寻宝”。
4. 未登录则弹出手机号验证码登录；新用户登录后必须选择学段：小班、中班、大班、幼小衔接。
5. 后端创建测评会话，随机选择基础包试卷组。
6. 进入基础包：地图页 -> 关卡导言页 -> 答题组件。
7. 用户完成基础包题目后，前端提交基础包答案，后端计算正确率。
8. 正确率 < 80%：进入基础包完成页，生成基础报告。
9. 正确率 >= 80%：进入森林游乐场过渡页，后端随机增强包试卷组，继续增强包。
10. 完成增强包后进入增强包完成页，生成全维报告。

## UI/UX 方案

- 视觉基调沿用现有素材：沉浸式自然绘本感、森林寻宝、森林游乐场。
- 页面比例使用 16:9 横屏画布：`width: min(100vw, 177.78vh)`，`height: min(100vh, 56.25vw)`，居中 letterbox。
- 页面采用三层结构：
  - Layer 0：背景图。
  - Layer 1：题型核心交互。
  - Layer 2：返回、IP、下一题、弹窗、全局状态。
- 题型组件按四大类实现：
  - BinaryJudge：音图判断、纯音判断、图文判断、绘本判断。
  - Selection：听音选图、看词选图、看图选词。
  - VoiceRecord：听音跟读、看图跟读、看图说话。
  - Coloring：互动涂色，两套 SVG 题单独开发。
- 交互原则：
  - 所有关键按钮 300ms 防抖。
  - 题目未完成前“下一题”不可点。
  - 返回必须二次确认。
  - 音频/VO 播放期间锁定相关操作。
  - 录音期间关闭 BGM 和示范音入口。

## 前端架构

推荐技术栈：

- React + TypeScript + Vite。
- Zustand 或轻量自研 store 管理测评状态。
- React Router 或状态机式页面控制器。
- CSS Modules 或普通 CSS 变量，避免引入重型 UI 框架。
- Web Audio API + HTMLAudioElement 组合实现音频播放。
- MediaRecorder 实现浏览器录音，封装为 AudioService。

核心模块：

- `AppShell`：横屏容器、环境识别、全局弹窗。
- `JourneyController`：测评流程状态机。
- `AudioService`：BGM、VO、题干音频、录音互斥、权限检测。
- `ApiClient`：H5/小程序 WebView 共用接口层。
- `BridgeService`：微信小程序嵌入预留。
- `AssetPreloader`：背景图、题目图、音频预加载。
- `QuestionRenderer`：按题型渲染对应组件。
- `AnswerStore`：本地临时答案、断点和提交状态。

## 后端架构

推荐技术栈：

- Node.js + NestJS 或 Fastify + TypeScript。
- PostgreSQL 作为主数据库。
- Redis 用于验证码、防刷、短期会话缓存和幂等锁。
- 对象存储用于录音文件和题目素材。
- Prisma 或 Drizzle 管理 schema 和迁移。

核心服务：

- AuthService：手机号验证码登录、协议确认、token 刷新。
- ProfileService：儿童学段采集与查询。
- AssessmentService：创建测评、随机试卷组、流程状态推进。
- QuestionService：题目和关卡内容下发。
- AnswerService：答题提交、幂等校验、涂色结果保存。
- RecordingService：录音上传签名、文件绑定、语音评测结果字段预留。
- ScoringService：基础包 80% 分流、增强包完成结算。
- ReportService：报告结果生成和查询。
- AdminSeedService：V1 内容导入和试卷组配置。

## 数据模型

核心表：

- `users`：手机号、登录状态、创建时间。
- `child_profiles`：用户 ID、学段、年龄段、首次填写时间。
- `assessment_sessions`：用户、学段、状态、基础包组、增强包组、分流结果、开始/结束时间。
- `pack_groups`：基础包/增强包、组名、启用状态。
- `stage_papers`：关卡、试卷名称、题量、启用状态。
- `pack_group_papers`：试卷组和关卡试卷映射。
- `questions`：题型、变体、题干、素材、音频、标准答案、排序字段。
- `question_groups`：同组 VO 配置。
- `answers`：会话、题目、答案 JSON、是否正确、耗时、提交时间。
- `recordings`：会话、题目、对象存储 key、时长、格式、评测状态。
- `coloring_results`：会话、题目、path/color JSON。
- `reports`：会话、等级、分数摘要、报告 JSON、生成时间。
- `audit_logs`：关键操作日志。

关键约束：

- `answers` 对 `(session_id, question_id)` 唯一，重复提交走幂等更新或拒绝。
- `assessment_sessions` 状态只能按流程推进，防止跳关。
- 所有上传文件必须绑定 `session_id` 和 `question_id`。

## API 清单

- `POST /api/auth/send-code`
- `POST /api/auth/login`
- `POST /api/profile/stage`
- `GET /api/profile/me`
- `POST /api/assessments/start`
- `GET /api/assessments/:sessionId/current`
- `GET /api/assessments/:sessionId/stages/:stageNo`
- `POST /api/assessments/:sessionId/answers`
- `POST /api/assessments/:sessionId/recordings/sign`
- `POST /api/assessments/:sessionId/recordings/complete`
- `POST /api/assessments/:sessionId/base/submit`
- `POST /api/assessments/:sessionId/advanced/start`
- `POST /api/assessments/:sessionId/final-submit`
- `GET /api/reports/:sessionId`
- `POST /api/admin/import-seed`
- `POST /api/admin/pack-groups/:id/enable`

## 部署方案

最低生产方案：

- 前端：静态资源部署到 CDN/对象存储或 Nginx。
- 后端：Docker 化部署到云服务器或容器服务。
- 数据库：云 PostgreSQL 或自建 PostgreSQL，开启每日备份。
- Redis：云 Redis 或同机 Redis，生产建议托管。
- 对象存储：录音、题目素材、报告静态资源。
- 域名：H5 域名和 API 域名分离，HTTPS 强制。
- CI/CD：至少提供一键构建、一键部署、回滚到上一版本。
- 监控：后端错误日志、接口耗时、5xx 告警、上传失败率、录音权限失败率。

### 当前云资源决策

当前云资源尚未准备。V1 推荐先按单云厂商最小生产组合采购，避免 6 月 30 日前被多云配置拖慢：

- 云服务器：2 核 4G 起步，用于 Docker 部署后端和 Nginx。
- 云数据库 PostgreSQL：2 核 4G 或同等级托管实例，开启自动备份。
- Redis：可先使用 1G 托管 Redis；预算紧张时测试环境可与后端同机，生产不建议。
- 对象存储：用于题目图片、音频、录音文件、报告静态资源。
- CDN：用于 H5 静态资源和大图加速。
- 域名和 HTTPS 证书：至少准备 H5 域名和 API 域名。

详见 `docs/setup/git-and-cloud-setup.md`。

## 性能与兼容

- 首屏关键背景图提前压缩到合理尺寸，移动端优先 WebP/PNG。
- 关卡导言页期间预加载下一题图片和音频。
- 音频播放响应目标小于 150ms，允许 V1 在低端机记录延迟但不阻塞上线。
- iOS Safari、Android Chrome、微信 WebView 必测。
- 横屏策略优先使用 CSS 适配和方向提示；不要依赖所有浏览器都支持强制锁屏 API。

## 测试策略

- 单元测试：状态机、算分、API 参数校验、数据模型。
- 集成测试：登录、开始测评、答题提交、基础包分流、报告生成。
- 前端 E2E：主流程、返回弹窗、未答不可下一题、录音权限失败。
- 真机测试：至少覆盖 iPhone Safari、安卓 Chrome、微信内置浏览器。
- 生产验收：部署后使用测试手机号完整跑通基础包熔断和增强包通关两条路径。

## 里程碑

### 6/7-6/9：方案定版与工程初始化

- 定版 V1 范围。
- 创建前端、后端、数据库工程。
- 资产目录规范和种子数据格式确定。
- 数据库 schema 和 API 契约初稿完成。

### 6/10-6/16：主流程打通

- H5 横屏框架、首页、登录、学段采集。
- 后端认证、测评会话、基础包试卷组随机。
- 首页 -> 地图 -> 关卡导言 -> mock 题目答题流程跑通。
- 部署测试环境。

### 6/17-6/23：题型与分流闭环

- 完成 BinaryJudge、Selection、VoiceRecord、Coloring。
- 完成答题提交、录音上传、涂色结果保存。
- 完成基础包 80% 分流和增强包流程。
- 完成基础包完成页和增强包完成页。

### 6/24-6/27：生产化

- 接入真实素材和题目种子数据。
- 完成资源预加载、弱网重试、幂等、防刷。
- 完成日志、备份、部署脚本、HTTPS 配置。
- 微信 WebView 嵌入预检。

### 6/28-6/30：验收与上线

- 全路径真机测试。
- 修复 P0/P1 问题。
- 准备上线检查表和回滚方案。
- 上线生产 V1。

## 主要风险

- 时间风险：23 天内做完整后台和复杂报告不现实，必须把 V1 控制为用户端闭环和轻量内容配置。
- 语音引擎风险：声通或自研接口若未及时给出，V1 先存录音并预留评测状态。
- 微信嵌入风险：小程序原生能力和 WebView 权限存在差异，V1 必须通过 BridgeService 隔离。
- 素材风险：音频、题目图、SVG 涂色 path 若不完整，会影响题型上线；需要尽早资产盘点。
- 部署风险：若没有云资源和域名证书，6/30 只能上线测试环境，不能真正公开发布。

## 需要立即确认的问题

1. 云资源：当前没有，需要从零规划和采购。
2. 短信验证码：是否复用现有小初版接口暂不确定，V1 需要同时支持真实短信服务和开发假验证码。
3. 语音评测：声通能接入最好；若 6/30 前接口或联调不稳定，V1 允许使用假评分数据，先保证录音采集、上传、回放和结果字段闭环。
4. 报告页：V1 做基础报告，只展示级别和简要结果。
5. 内容数据：题目、音频、答案、SVG 已有，需要按导入模板整理。

## 推荐决策

按“生产可用 V1”推进：先做 H5 用户端完整测评闭环、后端和数据可追踪、部署可回滚；完整教研后台、复杂报告、深度语音评测和小程序原生壳放入 7 月迭代。这样 6 月 30 日上线成功概率最高，且不会把架构做死。
