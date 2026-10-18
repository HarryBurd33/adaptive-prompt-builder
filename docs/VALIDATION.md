# Validation

Validation date: 2026-10-18. This is a small, recorded behavioral comparison in Codex desktop, not a guarantee of reliability across models or hosts.

## Static and package checks

The official skill-creator format validator passed for the canonical skill and an extracted package. The package helper checks packaged relative references, generates a self-contained portable prompt, builds a deterministic ZIP, verifies archive integrity, and checks generated-file drift. Negative probes confirmed that a missing skill reference and a modified portable prompt are rejected. The runtime skill has no Python or API dependency; Python 3.9+ is for package maintenance only.

## Behavioral method

The cases, inputs, and rubric were prepared independently and frozen before execution. Baseline and earlier-candidate source snapshots and full model replies are retained locally. The repository includes synthetic case definitions, grading metadata, and this summarized validation report. The existing Skill Forge prompt-builder example was the baseline. Separate executor contexts used the same inherited model/settings and tools. The exact model revision was not exposed.

B01's three scripted user turns were delivered sequentially, retaining actual assistant replies. B02–B09 are single-turn or fixed-history synthetic fixtures, batched within each condition's executor context. They are not independent per-case model trials. The fixed assistant histories are authored inputs, not execution evidence. An independent reviewer graded the actual saved replies and inspected actual local artifacts. Color labels were used, but the records indirectly revealed assignment, so the review is not fully blinded.

The original suggested execution protocol was adjusted to use an existing-skill baseline and shared contexts; a local protocol addendum records those deviations without changing the behavioral checks or release gate. One briefly launched child was interrupted and its work excluded; each condition's case replies were produced by its parent executor.

## First candidate

Both the baseline and first candidate passed 8 of 9 main behavioral cases and all 6 metadata routing probes. They failed the strict B01 first-turn check. The baseline asked for the rough idea again, despite it already being supplied. The first candidate asked about the meaning of usage but did not explicitly distinguish a cost/spending budget. The first grading recorded the failure rather than treating a near match as a pass.

A narrow revision added a general instruction to unpack consequential ambiguous shorthand, with quota/context/token-or-cost budget as an example. The revised source was frozen before a new non-checkpoint ambiguity case was authored. The original cases are regressions for that revision; the new H01 case was held out from the candidate author at patch time. It is one synthetic probe, not broad generalization evidence.

## Final results

| Condition | Main behavior cases | Held-out H01 | Metadata routing |
| --- | --- | --- | --- |
| Existing example baseline | 8/9 | Pass | 6/6 |
| First candidate | 8/9 | Not run | 6/6 |
| Published revision | 9/9 | Pass | 6/6, reused unchanged metadata |

The published revision clears the frozen release gate and passes the additional ambiguity probe. The independent final grading inspected the actual replies and local artifacts. The active skill hashes match the frozen revised executor snapshot. This public report summarizes that evidence; source snapshots and full response logs remain local.

The demonstrated improvement is narrow: the motivating first-turn clarification now meets the full check without re-asking for an idea already provided. The other eight main cases are ties with the baseline, and both conditions pass H01. This small comparison does not establish overall superiority across tasks or models.

## Practical limits

These tests assess prompt construction, questioning, state preservation, scope, and small authorized local executions. B08 actually creates a tiny local skill through the available Skill Forge workflow, while honoring that fixture's research/evaluation skip. B09 actually writes and verifies a local welcome note. Those are not tests of every artifact type or connector.

Activation is a **metadata-only model routing probe**, not observation of native Codex automatic discovery. Discovery metadata is unchanged in the revision, so the routing probe is reused explicitly. Installation on the user's computer, other LLM hosts, and broad user usability were not tested. The portable file is generated from canonical instructions and checked for drift; it is not evidence of cross-model equivalence.

The evaluations used synthetic inputs. This repository publishes the finished skill, package, and summarized validation evidence. Baseline and earlier-candidate source snapshots, full response logs, private session records, and user transcripts are excluded. No claim is made that this skill guarantees automatic triggers, quota prediction, or tools in the future workflows it helps describe.
