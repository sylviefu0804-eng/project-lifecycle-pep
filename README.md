# Project Lifecycle + PEP

用项目生命周期、明确的批准记录和可验证的门控，管理持续迭代的复杂任务。

A personal Codex skill package for project maturity, baseline continuation, visual review, and evidence verification.

版本：**1.0.0**。当前发布目标为私有 GitHub 仓库。

## 包含的三个 Skill

| Skill | 负责什么 | 典型场景 |
| --- | --- | --- |
| `project-lifecycle-pep` | 判断生命周期、恢复项目状态、执行 PEP、管理资产与基线 | 多阶段任务、跨会话继续、成熟项目增量更新 |
| `visual-project-review` | 先分析结构、文案和视觉，再决定修改；检查文字可读性与版式漂移 | PPT、展陈、视觉系统审查 |
| `evidence-gate` | 查证姓名与肖像对应、政策、引语、历史事实与企业资料 | 史料展示、研究、企业报告 |

## 工作方式

项目生命周期决定工作强度：

- `GENESIS`：目标、素材和规则仍需发现。
- `CALIBRATION`：已有批准方向，正在补齐代表性场景与验证。
- `MATURE`：已有合格 Baseline 和延续规则，优先做有边界的增量更新。

每轮工作遵循 `discover → review → freeze → verify → validate`。PEP 阶段和项目成熟度分别记录，因此一个成熟项目仍可能有验证失败的候选稿。

资产状态为 `Candidate / Approved / Baseline / Rejected`。`FAIL` 或 `NOT_CHECKED` 阻断受影响范围的验收与基线替换。跨项目借鉴需要记录明确意图、来源和目标项目审查。

## 使用示例

```text
使用 $project-lifecycle-pep 恢复这个项目，判断生命周期，说明当前 Baseline、PEP 阶段和下一步。
```

```text
使用 $visual-project-review 审查这份展陈方案，先分别诊断结构、文案和视觉，并检查文字可读性。
```

```text
使用 $evidence-gate 查证这些人物姓名与照片的对应关系。无法确认的素材给出替代方案。
```

## 安装

本仓库同时保留标准 `skills/` 目录和 Codex 兼容 Plugin 清单 `.codex-plugin/plugin.json`。

### 从 GitHub 安装三个 Skill

在能够访问本私有仓库的 Codex 环境中，提供本仓库链接和需要的提交或标签，然后请求：

```text
使用 $skill-installer，先审查此仓库，再从指定提交安装：
skills/project-lifecycle-pep
skills/visual-project-review
skills/evidence-gate
```

私有仓库需要使用者自己的 GitHub 访问权限。安装完成后，在新任务中使用这些 Skill。默认允许自动选择；也可以显式调用。

### 作为一个 Plugin 安装

克隆仓库后，请 Codex 使用 `$plugin-creator`，将该目录注册到个人 Marketplace，并安装 `project-lifecycle-pep`。仓库包含 Plugin 清单；工具负责生成符合本机位置的 Marketplace 条目。

不要同时通过独立 Skill 和 Plugin 两种方式安装相同的三个 Skill，以免重复发现。

## 项目状态

状态模板位于：

```text
skills/project-lifecycle-pep/assets/project-state.example.json
```

在目标项目需要持久化状态时，将其作为 `.pep/project-state.json` 的起点，填写真实项目标识与决策记录。示例数据本身不代表任何项目已经获批。

从本仓库根目录运行状态检查：

```sh
python3 skills/project-lifecycle-pep/scripts/validate_project_state.py /path/to/project/.pep/project-state.json
```

## 本地验证

仅需 Python 标准库；无需安装运行依赖。

```sh
python3 -m unittest discover -s skills/project-lifecycle-pep/scripts -p 'test_*.py'
python3 skills/project-lifecycle-pep/scripts/validate_project_state.py skills/project-lifecycle-pep/assets/project-state.example.json
python3 scripts/validate_eval_suite.py evals/cases.json
```

状态检查器执行有限的结构与一致性检查，不能证明文件内容、批准记录、证据来源或实际可读性。`validate_eval_suite.py` 检查案例集结构与主题覆盖，不会调用模型执行行为测试。

## 验证证据与边界

项目所有者报告，这套方法已用于两个真实项目。发布包使用通用的企业演示、体育展陈和非视觉评估场景，不包含客户素材或真实项目档案。

`evals/cases.json` 保存 19 个场景和行为预期，覆盖生命周期分类、Baseline Continuation、项目隔离、handoff/bootstrap、Evidence Gate 和阻断传播。

`evals/results.json` 保留原制作会话的历史评估摘要。此前报告的 19/19 和 100% 来自场景回答的人工式评分：评测代理共享了先前会话背景，其中一位参与过案例设计；原始回答和完整评测元数据没有随仓库保存。因此该结果不属于独立盲测、可复算的准确率或真实项目重放。详见 [评估说明](evals/README.md)。

## 范围与扩展

这套 Plugin 提供方法和验证辅助，没有 MCP 服务、自动执行 hooks、联网脚本或新增工具权限。

Handoff 文件可以由项目自行维护；核心 Skill 会检查其与当前状态是否一致。第三方 Handoff Skill 及其安装器、安全审查材料不在本包内。

后续新增领域能力时，在 `skills/` 下增加独立目录，并补充对应 eval；修改状态语义或门控规则时应重新验证已有案例。

## 许可证

当前为私有项目，尚未选择开源许可证。是否公开以及采用何种许可证，由项目所有者后续决定。
