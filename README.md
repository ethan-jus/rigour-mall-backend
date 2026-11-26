# 瑞盖体育商城后端

负责商城后台及小程序所需的服务端能力，采用模块化单体、多实例部署。模块最终构建为一个可执行 JAR 与应用镜像，模块之间使用 Java API。

本仓库已初始化协作规范与基础 CI，尚未创建应用工程或业务实现。

关联仓库：[rigour-mall-admin-web](https://github.com/ethan-jus/rigour-mall-admin-web)。

## 已确定技术基线

- Java：Eclipse Temurin 25.0.5.1+2 LTS。
- Spring Boot：4.1.3。
- MySQL Server：8.4.13.1 LTS。
- MyBatis-Plus：3.5.18.1，使用 Boot 4 专用 starter。
- Maven：3.9.16。
- Docker Engine：29.10.1；Compose：5.7.2。

以上为 2026-11-26 架构方案基线，当前仓库尚未包含或运行这些应用依赖。首次工程初始化必须锁定依赖并完成 Java 25 / MySQL 的实际集成验证。

## 开发协作

先阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 和 [AGENTS.md](AGENTS.md)。使用功能分支提交 PR；远端只允许 Squash 合并，合并后自动删除源分支。

当前检查为 `repository-policy`，仅检查仓库规范，不代表应用已编译或业务测试已通过。

**仓库已公开，main 分支保护已启用。** 所有变更必须通过 PR，由另一位有写权限的同事批准，且 GitHub Actions 的 `repository-policy` 检查通过后才能合并；管理员同样受约束。详细规则见 CONTRIBUTING.md。

## 成员邀请

所有者可以在[成员管理入口](https://github.com/ethan-jus/rigour-mall-backend/settings/access)选择 Add people，按 GitHub 用户名或邮箱定向邀请；对方接受后获得协作写入权限。公开代码无需邀请即可阅读，该入口不是免邀请获得写权限的链接。

仓库为公开，代码、提交历史及 Actions 日志可被查看。未发布开源许可证，不代表授予任意使用或再分发权利。
