# 严格测试脚本：跨窗口验证 skill 是否在生效

> 这个文档教你在**另一个 Claude Code 窗口**真实测试 skill 的有效性。
> 我（写 SKILL.md 的那个 Claude）已经在自己上下文里见过 SKILL.md，自我评估有偏差。
> 真正严格的测试是让一个干净的 Claude 跑同样的输入。

---

## 测试流程

### 步骤 1：开两个 Claude Code 窗口

| 窗口 A：基线 | 窗口 B：带 skill |
|---|---|
| 在一个**没有这个 skill** 的目录启动 `claude` | 在 ai-shortfilm-prompts 仓库内启动 `claude` |
| 或：cd 到任意空文件夹再启动 | 或：把 skill 拷到 `~/.claude/skills/` 后启动 |

### 步骤 2：两个窗口都跑同一个 Case

从 `examples/` 挑一个 case，把"用户输入"原封不动粘贴给两边。

推荐用 `01-mecha-energy-shield.md`（女机甲 + 雷暴 + 绿色能量护盾）—— 难度适中，5 段式表现差异最明显。

### 步骤 3：用 10 条 checklist 给两边打分

把每个输出打印一份，逐项打勾：

| # | 项目 | 窗口 A（基线） | 窗口 B（带 skill） |
|---|---|---|---|
| 1 | 5 段结构齐全 | □ | □ |
| 2 | 有摄影机型号 + 镜头型号 | □ | □ |
| 3 | 有"如呼吸般的镜头浮动"完整句式 | □ | □ |
| 4 | 有"声音：不需要配乐，仅保留同期声" | □ | □ |
| 5 | ≥2 处瑕疵描述 | □ | □ |
| 6 | 结尾不堆特效，留白 | □ | □ |
| 7 | 没有"完美/震撼/史诗/帅气/4K"空泛词 | □ | □ |
| 8 | 没 IP 名 OR 有则有拦截提示 | □ | □ |
| 9 | 单镜头≤15s / 多镜头≤8 分镜 | □ | □ |
| 10 | 末尾给目标模型兼容性建议 | □ | □ |

**期望结果**：
- 窗口 A：通过 ≤ 3 条（基线很差）
- 窗口 B：通过 ≥ 9 条（skill 有效）

如果窗口 B 通过率不足 9 条 → SKILL.md 还有漏洞，需要补硬规则。

---

## 测试发现的 Bug 怎么处理

### Bug 类型 1：硬规则没被执行

**症状**：明明 SKILL.md 写了"必须有摄影机型号"，但输出里没有。
**原因**：规则不够显式，AI 把它当作"建议"而非"强制"。
**修复**：把规则改成 "❌ 不写就重做" 的强语气，并加 "自检：搜输出里是否包含 'IMAX' 或 'Panavision' 或 '索尼威尼斯' —— 没有就补"。

### Bug 类型 2：用户输入模糊时，AI 偷懒不问

**症状**：用户只说"做一个机器人变身"，AI 直接照默认值开干，没用 AskUserQuestion。
**原因**：第 2 步的触发条件写得不够明确。
**修复**：在 SKILL 的第 1 步加 "判断条件：以下 5 项中缺少 ≥2 项必须问问题"。

### Bug 类型 3：触发 IP 词时没加拦截提示

**症状**：用户说"做一个钢铁侠风格的"，AI 照写了，但末尾没加"可能被 Seedance 拦截"。
**原因**：规则 7 的提示位置不够显眼。
**修复**：在"输出格式"段加一条"如果输出包含任何 IP 名，必须在末尾加拦截提示"。

---

## 用 LLM-as-judge 自动化测试（高级）

如果你想做 CI，可以这么做：

```python
# pseudo-code
import anthropic

def evaluate_prompt(prompt_input, prompt_output):
    judge_response = anthropic.complete(
        model="claude-opus-4-7",
        system="你是 AI 视频提示词质量评审员。根据 10 条 checklist 给输出打分，返回 JSON: {passes: [...], fails: [...], score: N}",
        messages=[
            {"role": "user", "content": f"""
            用户输入：{prompt_input}

            待评审输出：
            {prompt_output}

            checklist:
            1. 5 段结构齐全
            2. 有摄影机型号 + 镜头型号
            3. 有"如呼吸般的镜头浮动"完整句式
            4. 有"声音：不需要配乐，仅保留同期声"
            5. ≥2 处瑕疵描述
            6. 结尾不堆特效，留白
            7. 没空泛词
            8. 没 IP 名 OR 有拦截提示
            9. 时长合理
            10. 末尾给模型建议
            """}
        ]
    )
    return judge_response

# 跑所有 examples
for case in glob("examples/*.md"):
    user_input = extract_user_input(case)
    skill_output = run_claude_with_skill(user_input)
    result = evaluate_prompt(user_input, skill_output)
    assert result.score >= 9, f"Skill failed on {case}: {result.fails}"
```

可以接到 GitHub Actions 上，每次 PR 自动跑。

---

## 报告问题

跑出来失败的 case，欢迎提 issue：
- 仓库：https://github.com/jnMetaCode/ai-shortfilm-prompts/issues
- 模板：附上"用户输入 + 实际输出 + 缺失的 checklist 项 + 你认为应该怎么改"
