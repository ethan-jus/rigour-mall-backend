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

**分支保护尚未启用：GitHub 返回套餐限制，需要账号升级 GitHub Pro。** 目标保护配置已保存，启用方法见 CONTRIBUTING.md。不要把当前协作约定当成已经生效的服务端保护。

## 成员邀请

所有者可以在[成员管理入口](https://github.com/ethan-jus/rigour-mall-backend/settings/access)选择 Add people，按 GitHub 用户名或邮箱定向邀请；对方接受后获得访问权限。该入口不是免邀请加入链接。

仓库为私有。未发布开源许可证，不代表授予公开使用或再分发权利。
