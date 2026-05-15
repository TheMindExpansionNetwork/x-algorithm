#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
required = [
    root / "docs/social/POST_IMPROVEMENT_GAME_PLAN.md",
    root / "docs/social/X_CONTENT_CALENDAR_14_DAY_DRAFT.md",
    root / "docs/data/x-post-calendar.json",
]
missing = [str(p.relative_to(root)) for p in required if not p.exists()]
if missing:
    raise SystemExit("missing required files: " + ", ".join(missing))

manifest = json.loads((root / "docs/data/x-post-calendar.json").read_text())
assert manifest["manual_post_required"] is True
assert manifest["auto_post_enabled"] is False
assert manifest["requires_human_approval"] is True
assert manifest["closed_gates"]["public_posting"] is False
assert manifest["closed_gates"]["mutates_cron"] is False
for rel in manifest["proof_paths"]:
    if not (root / rel).exists():
        raise SystemExit(f"proof path missing: {rel}")

plan = (root / "docs/social/POST_IMPROVEMENT_GAME_PLAN.md").read_text()
for needle in ["Multi-action quality", "Daily schedule template", "Per-post checklist", "Measurement loop"]:
    if needle not in plan:
        raise SystemExit(f"plan missing section/content: {needle}")

calendar = (root / "docs/social/X_CONTENT_CALENDAR_14_DAY_DRAFT.md").read_text()
for day in range(1, 15):
    if f"Day {day}" not in calendar:
        raise SystemExit(f"calendar missing Day {day}")

print("social plan verification passed")
