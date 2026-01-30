# Tarot Reflection Skill - Usage Guide

## What This Skill Does

The **Tarot Reflection** skill enables Claude to provide structured, reflective tarot readings for decision support and personal insight. It's designed to:

- Help clarify decisions through symbolic reflection
- Provide position-aware card interpretations
- Generate actionable guidance (not fortune-telling)
- Maintain appropriate epistemic humility
- Encourage real-world verification

## Installation

1. Download the `tarot-reflection.skill` file
2. In Claude.ai, go to Settings → Skills
3. Click "Add Skill" and upload the `.skill` file
4. The skill will now be available for use

## How to Trigger the Skill

The skill activates when you ask for tarot-related guidance:

**Example triggers:**
- "Do a tarot reading about my job change"
- "Pull 3 cards for my relationship situation"
- "What does the tarot say about whether I should accept this offer?"
- "Give me a reflective reading for my next 30 days"
- "Use Celtic Cross for this question: Should I move cities?"
- "Here are my cards: The Tower (reversed), Two of Cups, The Hermit — interpret them"

## Supported Spreads

1. **1-card**: Quick daily guidance or single-focus questions
2. **3-card (Past/Present/Future)**: Timeline-based exploration
3. **3-card (Situation/Action/Outcome)**: Action-focused decisions
4. **5-card (Decision)**: Comparing two paths
5. **Celtic Cross**: Complex, multi-faceted situations (10 cards)

## Features

### Position-Aware Interpretations
Each card is interpreted based on its position in the spread, not just its inherent meaning. The same card means different things in "Past" vs "Advice" positions.

### Reversals (Optional)
By default, cards can appear reversed (~50% chance). Reversals indicate modulation—blocked energy, internalization, or excess—not simple negation.

To disable: "Do a reading without reversals" or "upright cards only"

### Actionable Guidance
Every reading includes 3-7 specific, testable next steps designed to reduce uncertainty and encourage agency.

### Appropriate Guardrails
All readings include reality-checking language that:
- Frames readings as reflective tools, not deterministic predictions
- Encourages validation through real-world action
- Acknowledges uncertainty and user agency
- Escalates warnings for high-stakes topics (medical/legal/financial)

## Example Usage

### Example 1: Simple Request
**You:** "Pull 1 card for my day and keep it practical"

**Claude will:**
1. Draw one card
2. Interpret it for daily guidance
3. Provide 2-3 practical suggestions
4. Include a "what to notice today" lens

### Example 2: Decision Support
**You:** "3-card spread: past/present/future for my interview process"

**Claude will:**
1. Confirm the spread choice
2. Draw three cards
3. Interpret each in context (Past = what led here, Present = current dynamics, Future = likely trajectory)
4. Synthesize into a coherent narrative
5. Provide actionable next steps
6. Include appropriate guardrails

### Example 3: User-Provided Cards
**You:** "Here are my cards: Death upright (Advice), Five of Wands (Obstacle), Star (Outcome). Interpret."

**Claude will:**
1. Skip the drawing step
2. Interpret each card by position
3. Synthesize the narrative
4. Provide guidance based on your specific cards

## Customizing the Skill

The skill is designed to be easily modified. Here's the structure:

```
tarot-reflection/
├── SKILL.md                      # Main workflow and instructions
├── scripts/
│   └── tarot_deck.py            # Card drawing logic
└── references/
    └── card_meanings.md         # Comprehensive card interpretations
```

### To Customize Card Meanings

Edit `references/card_meanings.md`:
- Add your own interpretive lens
- Include deck-specific meanings (if using non-RWS deck)
- Add custom position guidance
- Expand synthesis guidelines

### To Add New Spreads

Edit `scripts/tarot_deck.py` and add to the `SPREADS` dictionary:

```python
SPREADS = {
    # Existing spreads...
    "my-custom-spread": ["Position1", "Position2", "Position3", ...]
}
```

### To Change Card Pool

Modify the `MAJOR_ARCANA` and `MINOR_ARCANA` constants in `scripts/tarot_deck.py` to use:
- Different deck systems (Thoth, Marseille, etc.)
- Oracle cards
- Custom decks

### To Adjust Guardrails

Edit the guardrail language in `SKILL.md` under "Step 7: Apply Guardrails" to:
- Strengthen/weaken epistemic humility
- Add domain-specific warnings
- Customize for different use cases

## Philosophy & Design Principles

This skill is built on several key principles:

### 1. Reflection, Not Fortune-Telling
The skill treats tarot as a reflective decision-support tool, not a deterministic prediction system. It:
- Uses probabilistic language ("suggests", "indicates", "supports")
- Emphasizes user agency
- Encourages real-world verification

### 2. Position-Aware Interpretation
The same card means different things in different positions. The skill always contextualizes card meanings based on:
- Position in spread
- User's specific question
- Surrounding cards

### 3. Actionable Over Abstract
Every reading includes concrete next steps that are:
- Specific and testable
- Time-bounded when appropriate
- Designed to reduce uncertainty
- Framed with agency

### 4. Progressive Disclosure
The skill uses a lean design:
- Core workflow in `SKILL.md` (loads when triggered)
- Detailed card meanings in `references/` (loads as needed)
- Drawing utilities in `scripts/` (may execute without loading)

This keeps context window usage efficient.

## Advanced Features

### Seed-Based Reproducibility
For testing or record-keeping, you can request readings with specific seeds:

**You:** "Do a 3-card reading with seed=42"

Claude will use `draw_cards(3, seed=42)` to generate reproducible results.

### Partial User Input
You can provide some cards and ask Claude to draw the rest:

**You:** "I drew The Fool for Position 1. Draw the other two cards for a 3-card spread."

### Spread Recommendation
If you don't specify a spread, Claude will suggest the most appropriate one based on your question's complexity.

## Troubleshooting

**Q: Claude isn't using the skill**  
A: Make sure your request includes clear triggers like "tarot reading", "pull cards", or "interpret these cards"

**Q: Interpretations feel generic**  
A: Provide more context in your question. Instead of "What about my job?", try "Should I accept the senior role at Company X, which offers more pay but requires relocation?"

**Q: I want different card meanings**  
A: Edit `references/card_meanings.md` with your preferred interpretations. The skill will use your updated meanings.

**Q: Can I use this with oracle cards?**  
A: Yes! Modify `scripts/tarot_deck.py` to replace the card pool with your oracle deck.

## License

This skill is provided as open-source. You're free to:
- Use it personally
- Modify it for your needs
- Share your modifications
- Incorporate it into other skills

## Contributing

If you create useful modifications (new spreads, enhanced interpretations, additional guardrails), consider sharing them with the community!

## Support

For questions or issues:
1. Check that your `.skill` file is properly formatted
2. Verify the skill is enabled in Claude's settings
3. Ensure your prompts include clear tarot-related triggers

---

**Remember**: This is a reflective tool for decision support, not a deterministic prediction system. Use it to sharpen your thinking, but always validate insights through real-world action and concrete information. You have agency—the cards illuminate dynamics, they don't dictate outcomes.
