# Adaptive Prompt Builder

Turn a rough idea into a prompt another LLM can use. The skill asks focused questions, challenges assumptions, drafts a prompt, and refines it as feedback reveals gaps. It works across writing, research, planning, spreadsheets, software, and other workflows.

It produces a prompt first. It carries out the prompt only when you ask. When your goal is a reusable skill, it can prepare a self-contained prompt for **Skill Forge** to build it.

## Install in Codex

Ask Codex:

> Use $skill-installer to install the skill at skills/adaptive-prompt-builder from https://github.com/HarryBurd33/adaptive-prompt-builder.

Download the [installable skill ZIP](dist/adaptive-prompt-builder-v0.1.0.zip) and extract it into your skill directory, or download this repository using **Code → Download ZIP**, then copy the complete `skills/adaptive-prompt-builder` folder into your personal `~/.agents/skills/` directory. For a project installation, place it inside that project's `.agents/skills/` directory. Keep the references and template alongside `SKILL.md`. If it does not appear in the skill selector, restart Codex.

These locations follow the [current Codex skills documentation](https://learn.chatgpt.com/docs/build-skills). Installation was not performed on your computer by publishing this repository.

## Start a prompt

```text
Use $adaptive-prompt-builder to refine this idea into a reusable prompt:
[describe your rough idea]. Ask focused questions and challenge weak assumptions.
```

For a skill you want Skill Forge to build:

```text
Use $adaptive-prompt-builder to refine my idea for a checkpoint skill that saves
unfinished work before usage runs out. Produce a standalone prompt I can give
to Skill Forge. Help clarify which usage limit matters and what can activate
automatically; do not build the checkpoint skill yet.
```

Answer the questions and react to drafts. Then copy the finished prompt into a chat where Skill Forge is available. You can also say: `Now use Skill Forge to carry out the finalized prompt.`

## Control the depth

| Say | Effect |
|---|---|
| `Quick` | Resolve blockers and draft sooner. |
| `Thorough` | Explore material requirements and failure cases. |
| `Expert challenge` | Stress assumptions and compare alternatives. |
| `Draft now` | Get a provisional prompt with assumptions labeled. |
| `Go deeper` | Explore a consequential uncertainty. |
| `Skip` or `Use your judgment` | Record an assumption or delegate routine choices. |
| `Actually, make the output an Excel workbook` | Revise the artifact and dependent requirements while retaining settled answers. |
| `Save a brief` / `Resume from this brief` | Preserve or restore decisions when files or supplied text are available. |
| `Now carry it out` | Execute the completed prompt within available tools and authorization. |

The skill adapts its depth by default. It can deliver immediately when a prompt request is already complete. It keeps refining while an answer could materially change the result, without forcing an endless interview.

## Use in other LLMs

Paste or upload [the portable prompt](portable/adaptive-prompt-builder.md), then describe your idea. It contains the core instructions and supporting guidance. Other hosts that load standard Agent Skills can use the skill folder with their own installation procedure. No scripts, paid APIs, or Skill Forge installation are needed for prompt building; Skill Forge is needed only when you choose that handoff.

Files, browsing, external apps, persistence, and independent testing depend on the host. A prompt cannot supply missing tools or guarantee automatic activation of a future skill. Publishing or editing an external artifact requires appropriate authorization. Cross-host behavior and automatic discovery are not guaranteed.

## Evidence and development

See [validation](docs/VALIDATION.md) for executed checks and limitations, and [foundations](docs/FOUNDATIONS.md) for source provenance. Evaluations use synthetic inputs. Baseline source snapshots, full response logs, and private interview state remain local; the repository includes synthetic test definitions and summarized validation evidence.

`python3 scripts/package.py` (Python 3.9+) rebuilds the portable prompt and installable ZIP; `python3 scripts/package.py --check` checks for drift, local links, and package integrity. Python is needed only for maintaining packages, not for using the skill.

MIT licensed. The skill adapts the MIT-licensed Skill Forge example; its copyright and permission notice are retained in [LICENSE](LICENSE).
