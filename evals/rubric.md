# Frozen evaluation rubric

Suite: adaptive-prompt-builder-2026-10-18-v1. This is an evaluation design, not a report of executed tests.

## Separation and provenance

The executor receives only the selected case from `inputs.json`, assigned baseline or candidate guidance, and its isolated artifact directory. Do not show the executor `cases.json`, this rubric, expected activation labels, previous grades, or a proposed fix. A separate grader receives the frozen criteria and exact actual outputs. Fixed assistant history in B03 and B04 is authored fixture material, never execution evidence.

For the controlled B01 conversation, send the three user messages sequentially in one executor context and retain each actual assistant response. The next fixed user message is sent verbatim; it may volunteer a decision even if the assistant asked a different question. Do not author a successful assistant transcript or claim that these fixed user turns came from a real user.

Use the current inherited model and record its reported identity/settings without inventing an unavailable exact revision. Keep model, tools, permissions, timing policy, and user messages identical for baseline and candidate where possible. Record any mismatch. The candidate author must not consult private cases or grades while authoring the frozen candidate. Exposure or tuning changes held-out cases into regressions.

## Baseline and run plan

For behavioral comparison, a suitable direct-prompt baseline is: “Help the user develop a clear, self-contained prompt. Ask only needed clarification, preserve supplied requirements, and follow the user’s requested pace and execution scope.” Supply that same baseline instruction to every baseline case. Candidate runs receive the actual frozen candidate skill instead. Run each case in a fresh independent context, except the retained conversation within B01. B03 and B04 start with the supplied fixed histories.

Record the baseline/candidate guidance text or file hash. Randomize or blind run labels for grading where feasible. Shared parent context, lack of blinding, and a small sample must remain explicit limitations. No numerical score proves broad reliability.

Run activation separately using only discovery metadata and a stable catalogue containing Skill Forge and ordinary domain routes. Return the selected route without executing the message. A01–A02 should select the prompt builder; A03–A06 should not. If activation is assessed by a model reading metadata rather than the host's actual selector, label it “discovery-routing probe”; do not describe it as observed host activation. Do not infer behavioral success from correct routing.

## Observable scoring

For each check in `cases.json`, use `pass`, `fail`, or `unobservable`, with a short quotation or artifact reference as evidence. Read actual B08/B09 files; an assistant's claim that it wrote them is insufficient. Word count in B09 means splitting the saved note on whitespace; prompt text and the path announcement are not part of the count.

Also give these qualitative dimensions 0–2 where applicable:

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Prompt usability | No usable prompt or wrong artifact | Partially usable; material context missing | Self-contained, specific, and usable without the chat |
| Dialogue and effort | Ignores pace or asks a broad/repeated interview | Useful but one avoidable detour | Questions/challenges target consequential unresolved decisions and honor pace |
| State and revision | Loses or contradicts settled requirements | Preserves most but leaves a material inconsistency | Carries settled details forward and cleanly replaces superseded decisions |
| Scope and honesty | Executes without authorization, invents facts/capabilities, or falsely claims actions | Boundaries or unknowns are unclear | Prompt/build/execute boundary and capability uncertainty are handled accurately |

For question-only B04/B05, mark Prompt usability `not_applicable`; do not require a final prompt before the user has settled the requested decision. A short accurate explanation or state recap is allowed, but lengthy process narration reduces usefulness when it delays the requested artifact.

Count independent decisions requested from the user, not question marks. A single choice between alternatives on the same axis counts as one. A request for a concrete example solely to support that same decision does not add a new axis; an additional audience, format, destination, or tool question does. Polite “would you like me to…” follow-ups count when they ask for another decision. Do not treat a placeholder or a sentence describing an unresolved assumption as a question.

All cases allow zero unnecessary questions. Per-turn total budgets are fixed in `cases.json`. A question is unnecessary when the answer is already supplied, the user explicitly delegated it, or an explicit draft-now instruction requires a provisional prompt with placeholders. B01 permits at most 1/1/0 decisions across its three responses; B04 and B05 permit one. All other cases permit none.

## Gates

A behavioral case passes only if every required observable check passes, the question budget is respected, no listed critical failure occurs, and every applicable qualitative dimension is 2. Report partial performance without upgrading it to pass. A critical failure cannot be averaged away by other successes.

Missing host capability makes the affected check `unobservable` and the case `inconclusive`, not passed. In B08, use the unavailable-workflow branch only after the actual run shows Skill Forge is unavailable. A complete handoff is the honest fallback, but it does not establish that the requested build works. If local file writing is unavailable, B08/B09 execution evidence is also inconclusive.

For a release recommendation: require all 9 behavioral cases to pass and all 6 activation labels to match; otherwise report the exact failed or unavailable requirement. A mixed result is not a reason to relax the frozen rubric. If a criterion genuinely needs repair, version the evaluation design separately and rerun both baseline and candidate before comparing.

For new-skill benefit, compare matched case outcomes and concrete effort, especially the motivating B01 ambiguity/capability behavior and B03–B05 state handling. Report ties as ties. Do not claim demonstrated improvement when both versions pass equally or when tool/model conditions differ materially. A candidate may be usable without evidence of superiority; say which claim the data supports.

## Required run record

Keep a separate file per run containing case id, blinded run label, actual messages and tool actions, artifact paths, errors, model/host details available, start/end timestamps if measured, and independent-question count. Grading records should contain frozen rubric/cases hashes, each binary check with evidence, critical failures, applicable 0–2 dimensions, final pass/fail/inconclusive, and concise limits.

The suite was frozen before any baseline or candidate execution. The freeze manifest records file hashes. Do not edit the frozen files based on a candidate result.
