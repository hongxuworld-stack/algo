---
name: leetcode-study-tracker
description: Interpret, synchronize, and maintain the user's LeetCode study records, especially the coding_times file, and recommend review or new problems based on those records. Use when reading or updating coding_times, scanning the repository for question files, discussing review history, selecting practice problems, or updating algorithm study progress.
---

# LeetCode Study Tracker

## Interpret `coding_times`

- Treat the number after each problem path as the number of times the user has reviewed that problem.
- Never interpret the number as mistakes, failed attempts, or times answered incorrectly.
- Treat a larger number as more review history, not weaker performance.
- Preserve parenthetical notes as separate study reminders. For example, `2 (note:res init value)` means two reviews plus a reminder about result initialization.
- Do not infer mastery or weakness from review count alone. Use explicit notes, code quality, or user feedback when evaluating weak points.

## Recommend Problems

- For review selections, balance previously reviewed problems across important patterns instead of assuming high-count problems were frequently wrong.
- Explain selections using traversal pattern, topic coverage, difficulty, recency, or explicit notes.
- Separate existing review problems from new problems.
- Check the repository before labeling a problem as new.

## Update Records

- Increment a problem's number only when the user indicates another review was completed.
- Keep the existing `path: count` format.
- Add concise parenthetical notes only when the user asks or a concrete review reminder is established.

## Synchronize `coding_times`

When asked to update or synchronize `coding_times`:

1. Scan the repository for numbered question files such as `unionFind/1202.py`, `Graph/934.py`, and `Graph/BFS/542.py`.
2. Add each new question missing from `coding_times` with review count `0`.
3. Remove entries whose question files no longer exist.
4. Keep all existing review counts and notes unchanged.
5. Group entries by top-level category or directory, separated by one blank line.

If the same problem number appears in multiple files within the same category, include it only once. Prefer the plain filename, such as `Heap/295.py`, over variants such as `Heap/295(hard_another_method).py`. If no plain filename exists, keep one existing variant.

Exclude files that are not numbered question files, including:

- `basic`
- `python_basic`
- `zip_explain`
- `coding_times`
- Descriptive utility files such as `fraud_union.py`
