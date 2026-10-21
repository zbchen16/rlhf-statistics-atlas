# Statistical RLHF engineering learning path (research-oriented)

**Objective:** from a statistically specified estimand to a trustworthy, reproducible preference-learning experiment. Not building a generic Agent UI or training an LLM from scratch.

## Stage 1 — estimation on fixed features (no GPU required)

Build a pairwise preference-data loader and validate chosen/rejected, prompt/group identifiers, annotator IDs if available, and source partitions. Fit Bradley–Terry logistic preference estimator and a simple noise-aware baseline with simulated data. Verify gradients, parameter identifiability constraints, and probability calibration. Evaluate held-out log-loss, Brier score, accuracy, subgroup metrics, and confidence intervals. Save seeds/config/metrics; prevent prompt-group leakage.

## Stage 2 — implement DPO loss and verify

Implement DPO loss from frozen chosen/rejected sequence log probabilities. Compare against a reference library loss on a tiny synthetic batch. Test chosen/rejected swap, all-equal log probabilities, mask/sequence-length conventions, and beta scaling. Distinguish reward-model accuracy from policy quality. Use unit tests before any full training.

## Stage 3 — small-model post-training only if compute permits

Use Hugging Face Transformers/TRL and optionally PEFT for a 0.5B-class instruct model on a small preference subset. Reproduce baseline DPO/RewardTrainer via published recipes; do not pretrain. Maintain separate train/validation/test roles and reserve test for the final reported result. Make architecture, seeds, precision, hardware, packages, dataset revision, and prompt template reproducible. If hardware cannot support training, finish a sound reward-model experiment on frozen embeddings instead.

## Stage 4 — one statistics-motivated extension

Examples: instance-dependent preference-label noise (with identifiability discussion), repeated annotator heterogeneity, cyclic pairwise preferences, reward distribution via quantile regression, data selection bias. First develop synthetic DGP and theoretical estimand, then compare on aligned data/seeds and metrics. Report sensitivity to misspecification and failures; do not call a direct loss tweak a novel discovery without prior-art checking.

## Stage 5 — paper-style results

Record all configurations and provenance. Repeat simulations across fixed independent seeds; summarize failure counts, central tendency, dispersion and meaningful uncertainty. Compare with aligned baselines on identical splits. Show effect sizes and failure cases alongside averages. Write a clear reproduction report and a short list of testable unanswered questions for your advisor.

**Reference code:** [TRL](https://github.com/huggingface/trl), [Alignment Handbook](https://github.com/huggingface/alignment-handbook), [RewardBench](https://github.com/allenai/reward-bench). Check version-specific APIs before applying recipes.
