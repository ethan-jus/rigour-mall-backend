# 多人协作流程

## 分支与合并

默认分支为 main。每项任务从最新 main 创建短期分支，例如 feat/order-query、fix/payment-callback、chore/update-ci；多人或 AI 并行任务分别使用分支或 worktree。

```sh
git switch main
git pull --ff-only
git switch -c feat/your-task
```

提交后创建 PR，由另一位具有仓库写权限的同事审核。作者不能批准自己的 PR，多人不得共用账号代替独立审核。处理讨论并通过检查后，由维护者使用 Squash and merge 合并；源分支自动删除。暂不引入长期 develop 分支，也不把合并 main 自动等同于生产部署。

PR 标题描述最终变更，可使用 feat:、fix:、chore:、docs: 前缀。一个 PR 聚焦一个可评审任务，不提交无关格式化。通过合并 main 更新自己的共享分支；仅对自己独占的功能分支整理历史，不强推 main。

## 当前检查范围

repository-policy 检查必要协作文件、意外提交的敏感配置/构建文件、合并冲突标记及 Git 空白问题。它不是全面的密钥扫描，也不证明应用已构建或测试通过。

本地运行：

```sh
python3 scripts/repository_policy.py
git diff --check
git diff --cached --check
```

Actions 使用 Ubuntu 24.04 托管运行器、只读 GITHUB_TOKEN 和固定提交 SHA 的 checkout；不运行 pull_request_target，不允许 Actions 自动批准 PR。

## 首次引入应用工程

首次引入应用工程的 PR 必须同时添加真实构建与有效测试工作流，并更新本地验证命令。后端新增 backend-verify，使用已确定的 Java 25 工具链执行真实 Maven verify；Web 新增 web-verify，锁定运行时和包管理器，执行锁文件安装、类型检查（采用 TypeScript 时）和生产构建，并运行已有测试。

维护者必须在首次工程 PR 合并前，把新的检查名称加入远端必需检查并确认实际成功。当前这一步由维护者人工执行，仓库脚本不会自动启用应用门禁。repository-policy 不能代替应用验证。禁止用 continue-on-error、吞掉退出码或“没有工程文件所以跳过”伪装构建成功。没有测试时明确说明，不声称业务测试通过。

## 审核人与访问权限

CODEOWNERS 暂由 @ethan-jus 维护，成员到位后分配模块负责人。初始目标规则要求一位同事批准，暂不强制所有 PR 必须由 CODEOWNERS 批准，以免唯一负责人提交自己的 PR 时无人可审。不要在 CODEOWNERS 中填写没有仓库权限的人。

仓库已经公开，任何人都可阅读代码；协作写入权限按 GitHub 用户名或邮箱定向邀请，接受后获得。公司组织建立后再迁移，并分配后端、Web 和维护者团队。

## 分支保护状态

截至 2026-11-26，仓库已改为公开，main 的服务端分支保护已通过 GitHub API 启用并回读验证。必须经 PR、至少一位有写权限的同事批准、基于最新 main 的 repository-policy 检查通过且讨论全部解决后，才能使用 Squash 合并。新提交撤销旧批准，最后推送必须由其他人批准；管理员同样受约束，禁止强推和删除 main。

CI 检查来源绑定 GitHub Actions（app_id=15368）。该检查当前只验证仓库规范；首次应用工程 PR 必须按上文增加真实构建门禁。CODEOWNERS 审核不是额外强制条件，另一位有写权限的同事即可完成所需批准。

已应用的配置保存在 .github/branch-protection.json；修改该文件不会自动修改远端规则。后续经审核调整时，由维护者执行并回读验证：

```sh
gh api --method PUT repos/{owner}/{repo}/branches/main/protection   --input .github/branch-protection.json
gh api repos/{owner}/{repo}/branches/main/protection
```

修改协作文件也必须走 PR，不得为了合并自己的 PR 临时关闭保护或降低审核人数。仓库所有者仍有修改设置的能力，保护不是不可撤销的权限隔离。
