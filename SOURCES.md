# Research provenance

Reviewed: 2026-11-02. The package uses original prose and synthetic examples. No upstream skill text, code or templates have been copied. Conceptual similarity is not a claim of novelty. Licensing an original package does not relicense its sources.

| Source | Research use | License evidence / limit | Version pin |
|---|---|---|---|
| [Agent Skills specification](https://agentskills.io/specification) | Folder/frontmatter/disclosure format | Specification repository separates documentation/code licensing; no documentation prose copied | Retrieval date only; commit not yet pinned |
| [Context Engineering skills](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | Select/offload/compress/isolate/evaluate categories | MIT LICENSE checked in prior research; no text copied | Observed commit [6dbe1a1d868eab51a3bc9011b0f55e2891513e40](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/commit/6dbe1a1d868eab51a3bc9011b0f55e2891513e40); not asserted current branch tip |
| [planning-with-files](https://github.com/OthmanAdi/planning-with-files) | Task identity, phase checkpoints, restore before create | MIT LICENSE checked; no scripts or three-file template copied | Observed commit [1ec8f4eb5c683e31644856d98f9abde0d5a53448](https://github.com/OthmanAdi/planning-with-files/commit/1ec8f4eb5c683e31644856d98f9abde0d5a53448); not asserted current branch tip |
| [handoff-skill](https://github.com/jumpifequal/handoff-skill) | Preserve decisions, exact needed work, evidence and next step | MIT declaration; exact revision/license file must be pinned before any reuse | Pending verification |
| [pi-context](https://github.com/ttttmr/pi-context) | Checkpoint/timeline/compact decision model; external state distinction | Explicit license not confirmed in research; no code/text copied | Unpinned; copying excluded |
| [context-mode](https://github.com/mksglu/context-mode) | Large-output/source-scoped retrieval and capability diagnostics | ELv2, not treated as permissive open source; no code/text copied | Unpinned; no runtime dependency |

If a future change copies any material, record the exact path, reviewed commit, license, copied scope and required notices before merging it. Missing license, ambiguous provenance or incompatible terms block that copying path. Reading a repository or possessing an installed skill is not a redistribution permission.

Research does not establish performance, safety or host compatibility. Pins and remaining investigation are tracked in PROGRESS.md, not invented from branch names.

## Bounded source recheck, 2026-11-02

This records observed revisions, not guaranteed current branch tips. No third-party material was adopted or copied.

- Agent Skills repository: observed [69ef37e9424c0a7ea9dd2293b559e43ec8176379](https://github.com/agentskills/agentskills/commit/69ef37e9424c0a7ea9dd2293b559e43ec8176379); its [LICENSE](https://github.com/agentskills/agentskills/blob/69ef37e9424c0a7ea9dd2293b559e43ec8176379/LICENSE) is identified as Apache-2.0. This is repository license evidence, not a blanket assertion about every separately licensed document.
- handoff-skill: the [main LICENSE page](https://github.com/jumpifequal/handoff-skill/blob/main/LICENSE) displays MIT; a retrieved README/SKILL statement that no license is included conflicts with it. The exact full revision was not retrieved. Keep reuse blocked pending exact-version reconciliation.
- pi-context: observed [7bcce4164ab6a504db9c4ed7b00c3732bffa9048](https://github.com/ttttmr/pi-context/commit/7bcce4164ab6a504db9c4ed7b00c3732bffa9048). The [pinned package metadata](https://github.com/ttttmr/pi-context/blob/7bcce4164ab6a504db9c4ed7b00c3732bffa9048/package.json) declares MIT, while no standalone LICENSE was found in the checked main location. Metadata alone is retained as limited evidence; no copying.
- context-mode: the [LICENSE page](https://github.com/mksglu/context-mode/blob/main/LICENSE) states Elastic License 2.0. The checked release had only a short revision available and was behind main; it is not a full branch-tip pin. No copying or runtime dependency.

Retrieval/cache failures and contradictory source statements remain unresolved evidence, not inferred permissions. A future copied component needs its own exact-version review.
