# Foundations and provenance

Reviewed on 2026-10-18. This package reuses a bounded foundation review of the same interview and prompt-building workflow. Adding repository and ZIP delivery does not change those foundations. This is a targeted review, not an exhaustive survey.

## Adapted baseline

The starting point is the Skill Forge example [`examples/adaptive-prompt-builder/SKILL.md`](https://github.com/HarryBurd33/skill-forge/blob/c5c28fc138484d57f703478abe99f0d99455efba/examples/adaptive-prompt-builder/SKILL.md), inspected in a local checkout at revision `c5c28fc138484d57f703478abe99f0d99455efba`. The example and root license were unchanged from that checkout revision when checked.

The baseline already supports a running brief, questions ordered by their dependencies, drafts with labeled assumptions, format changes, user-controlled depth, resumption and honest reporting of tests. It is adapted rather than installed as a runtime dependency. The intended additions make material clarity, constructive challenge, decision changes and artifact requirements more explicit.

The inspected [root license](https://github.com/HarryBurd33/skill-forge/blob/c5c28fc138484d57f703478abe99f0d99455efba/LICENSE) is MIT, copyright © 2026 Skill Forge contributors. The example also declares MIT. Distribution of substantial adapted material must retain the applicable copyright and full permission notice. A new license notice does not replace that attribution.

## Interview design reference

The review inspected Matt Pocock's [`grill-me`](https://github.com/mattpocock/skills/blob/main/skills/productivity/grill-me/SKILL.md) and [`grilling`](https://github.com/mattpocock/skills/blob/main/skills/productivity/grilling/SKILL.md) instructions, root license and file history. The useful general ideas are resolving prerequisite decisions before dependent ones, investigating discoverable facts, offering concrete proposals and updating the interview after answers.

These are conceptual references; no upstream instruction text is copied into this package. Neither skill is a dependency. This design uses one consequential question at a time, stops at material clarity and supports prompt delivery without mandatory execution. It does not inherit the upstream wrapper's host-specific invocation or require exhaustive questioning.

The historical [`grilling` snapshot](https://raw.githubusercontent.com/mattpocock/skills/85f83d3fde1d3a90d5c9a657f6998c79a6c37308/skills/productivity/grilling/SKILL.md) and [license](https://raw.githubusercontent.com/mattpocock/skills/85f83d3fde1d3a90d5c9a657f6998c79a6c37308/LICENSE) were inspected at revision `85f83d3fde1d3a90d5c9a657f6998c79a6c37308` (2026-08-20). The license is MIT, copyright © 2026 Matt Pocock. Current upstream HEAD was **not confirmed**: retrieved branch snapshots differed slightly and API access failed. A root NOTICE URL was unavailable; the review does not claim that no notice exists.

## Prompt design references

- [OpenAI: Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering) informed clear separation of instructions, supplied context and examples, plus representative checks.
- [Anthropic: Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview) informed defining success criteria, making a draft tangible and checking it against expected outcomes.

These living documentation pages are references, not dependencies. Their immutable revisions and reusable-content licenses were not verified. Documentation prose is not copied, and provider-specific APIs or model requirements are not imposed.

## Review scope and limits

The review used local file inspection and primary-source web inspection. Public searches were `site:github.com/mattpocock/skills grill-me grilling` and `site:docs.anthropic.com prompt engineering interactive prompt development clarify`. Secondary mirrors and popularity lists were skipped because primary sources were accessible. Hugging Face was skipped because this workflow needs no model or dataset dependency. No retrieved code was executed.

This provenance review establishes foundations and reuse considerations. It does not establish behavioral reliability, successful installation or execution of generated prompts; those require separately reported validation. The package should remain usable without Skill Forge, Skill Finder or the reference skills installed. Skill Forge handoff is an explicit option for reusable skill-building requests, not the default destination for every prompt.
