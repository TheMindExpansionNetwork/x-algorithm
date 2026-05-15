# X Post Improvement Game Plan

> Fork context: this plan is derived from the open-source `xai-org/x-algorithm` repo, especially the For You feed stages: retrieval, filtering, multi-action scoring, author diversity, out-of-network weighting, and repeated-impression suppression.
>
> Status: manual-review only. No automated posting, replies, DMs, paid promotion, or scheduling should happen without explicit human approval and working X API credentials.

## What the repo implies for post strategy

The repo is not a turnkey post scheduler. It is a recommendation/feed-ranking system. The useful takeaways for improving posts are behavioral:

1. **Multi-action quality matters.** Ranking combines predicted probabilities for likes, replies, reposts, quotes, clicks, profile clicks, shares, dwell, video views, follows, and negative actions like not-interested/block/mute/report.
2. **Dwell and click depth matter.** Posts should make people pause, expand, click through, watch, or reply instead of scrolling past.
3. **Negative feedback is costly.** Bait, confusing claims, too many low-signal posts, or off-brand spam can train the system against you.
4. **Author diversity attenuates repeats.** Flooding the feed from the same account can reduce marginal value. Use fewer, stronger posts with enough spacing.
5. **Previously seen / served posts get filtered.** Reposting the same idea without a new angle is less useful than making a true sequel, quote, clip, proof asset, or update.
6. **Out-of-network discovery needs topic clarity.** Posts that clearly bind to a topic/community are easier to retrieve for people who do not already follow you.
7. **Media and summaries matter.** Grox-style content understanding points toward posts with legible text, strong visuals/video, and easy-to-summarize intent.

## Content pillars for MindExpander / Sonic-Forage

Use a weekly ratio instead of random posting:

- **40% Build-in-public proof:** demos, screenshots, audio/video clips, repo links, model cards, command-center receipts.
- **25% Scene/worldbuilding:** Sonic-Forage lore, DJ host voice, old-timey radio framing, PLUR/Kandi/RFID gig language, behind-the-scenes artifact drops.
- **20% Utility/tutorial:** exact commands, architecture diagrams, lessons from Hermes/Modal/vLLM-Omni/Qwen3-TTS workflows.
- **15% Conversation/open loops:** polls, taste questions, collaboration asks, remix prompts, “which version hits harder?” comparisons.

## Daily schedule template

All times local/Pacific unless changed.

### Morning — 7:00–9:00

**Goal:** proof-of-life + useful hook.

Post one of:
- “Today’s build target” with a concrete deliverable.
- 20–40 second demo clip/audio preview.
- one screenshot with a crisp caption.
- a short technical lesson from yesterday’s build.

Format:
- 1 sentence hook.
- 1 proof artifact.
- 1 specific next step or question.

### Midday — 12:00–2:00

**Goal:** conversation and out-of-network reach.

Post one of:
- question/poll tied to the morning artifact.
- quote/reply to a relevant community post with real detail.
- mini-thread explaining one decision.

Do not dump links only. Add a viewpoint first.

### Evening — 5:00–8:00

**Goal:** recap and retention.

Post one of:
- before/after comparison.
- “receipt” thread: what changed, what broke, what shipped.
- short teaser for tomorrow.
- best clip of the day.

End with a simple prompt: “Want the raw pack?”, “Which voice should host this?”, “Should this be a live room or a sample pack?”

## Weekly cadence

### Monday — Positioning

- Pin or refresh the top proof post.
- Announce the week’s build arc.
- Ship one repo/model/deck link if ready.

### Tuesday — Technical credibility

- Thread: architecture or workflow breakdown.
- Show one failure + fix.
- Ask for niche feedback from builders.

### Wednesday — Media drop

- Release a clip, voice comparison, DJ transition, or small pack preview.
- Use a visual/audio asset; avoid text-only if possible.

### Thursday — Community/collab

- Ask for remixers/testers/listeners.
- Quote/reply to relevant AI music, open model, creative coding, or agent posts.

### Friday — Proof recap

- “What shipped this week” thread.
- Include links, screenshots, and one next ask.

### Weekend — Weird/high-signal experimentation

- More playful posts: Beavis & Butthead/old-timey radio energy, Sonic-Forage lore, tests of unusual voices.
- Keep claims grounded; make it entertaining, not spammy.

## Per-post checklist

Before posting, score the draft 0–2 for each:

- **Hook:** Would a stranger understand why to stop scrolling?
- **Proof:** Is there a visual/audio/link/receipt, not just a claim?
- **Topic clarity:** Would the algorithm know who should see it?
- **Conversation:** Is there a real question or take people can respond to?
- **Shareability:** Would someone quote/repost this to explain a trend/tool?
- **Low negative risk:** Is it free of fake claims, spammy tags, bait, or confusion?

Post only if total is **8+/12**. Rewrite if lower.

## Post formats to rotate

1. **Proof clip:** “This is [artifact]. Built with [stack]. The weird part is [specific].”
2. **Failure receipt:** “I tried X. It broke because Y. Fix was Z. Lesson: …”
3. **Tiny tutorial:** “If you want X, the shortest path I found is: 1/ 2/ 3/”
4. **Taste test:** “A/B: which voice/transition/logo hits harder?”
5. **Manifest drop:** “Here’s the repo/model/deck. What’s inside: … What’s still closed-gated: …”
6. **Lore hook:** “Transmission from Sonic-Forage: [world frame] + actual proof asset.”

## Measurement loop

Track each post after 24h and 7d:

- impressions
- engagement rate
- replies
- reposts/quotes
- profile clicks/follows
- media views or link clicks
- negative signals if visible: mutes/unfollows/reports, or obvious reply sentiment
- format/pillar/time slot

Weekly decision rule:

- Double down on formats with replies + reposts + follows.
- Keep media styles that produce watch time or strong replies.
- Kill formats that get impressions but no replies/follows.
- Space posts if engagement drops from same-author saturation.

## Recommended automation boundary

Safe to automate:
- draft generation
- content calendar creation
- local markdown/JSON manifests
- reminder pings
- analytics import/export
- manual review packets

Do not automate without explicit approval:
- posting
- replies/DMs
- quote-tweets
- paid promotion
- deleting posts
- claiming revenue, affiliation, attendance, sponsorship, medical/legal/safety outcomes

## Next implementation steps

1. Create `docs/social/X_CONTENT_CALENDAR.md` with 14 days of concrete draft prompts.
2. Create `docs/data/x-post-calendar.json` with status, slot, pillar, proof path, and approval state.
3. Add a simple verifier that rejects drafts missing proof, approval status, or risk gates.
4. If X API credentials are later configured, keep posting manual until an explicit approval gate is opened.
