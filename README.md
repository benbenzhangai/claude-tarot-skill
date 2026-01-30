# Tarot Reflection Skill for Claude

A reflective tarot reading skill for Claude that provides structured decision support and personal insight through position-aware card interpretations, actionable guidance, and appropriate epistemic guardrails.

## 🎯 What This Does

This skill enables Claude to perform thoughtful tarot readings that:
- ✨ Clarify decisions through symbolic reflection
- 🎴 Provide position-aware card interpretations (same card, different meanings based on context)
- 🎬 Generate actionable next steps (not fortune-telling)
- 🛡️ Maintain epistemic humility and encourage real-world verification
- 🔄 Support multiple spread types (1-card through Celtic Cross)

**Philosophy**: Tarot as a reflective decision-support tool, not deterministic prediction. All readings emphasize user agency, probabilistic thinking, and real-world validation.

## 📸 Example Reading

See [EXAMPLE_READING.md](EXAMPLE_READING.md) for a complete sample reading showing:
- Position-aware interpretations
- Narrative synthesis across cards
- 6 specific, actionable next steps
- Appropriate guardrails and reality checks

## 🚀 Quick Start

### Installation

1. **Download the skill file**: Get `tarot-reflection.skill` from the [releases page](../../releases)

2. **Install in Claude**:
   - Go to [claude.ai](https://claude.ai)
   - Navigate to Settings → Skills
   - Click "Add Skill"
   - Upload `tarot-reflection.skill`

3. **Start using**:
   ```
   "Do a tarot reading about my job change"
   "Pull 3 cards for my relationship situation"
   "Celtic Cross for: Should I move cities?"
   ```

### Common Triggers

The skill activates when you mention:
- "tarot reading"
- "pull cards"
- "interpret these cards"
- "what does the tarot say"
- "do a spread"

## 📋 Features

### Supported Spreads

| Spread | Cards | Best For |
|--------|-------|----------|
| **1-card** | 1 | Daily guidance, quick check-ins |
| **3-card (Past/Present/Future)** | 3 | Timeline-based exploration |
| **3-card (Situation/Action/Outcome)** | 3 | Action-focused decisions |
| **5-card (Decision)** | 5 | Comparing two paths |
| **Celtic Cross** | 10 | Complex, multi-faceted situations |

### Key Capabilities

- **Position-Aware Interpretations**: Same card means different things in "Past" vs "Advice" positions
- **Reversals** (optional): ~50% chance per card; represents blocked/internalized/excessive energy
- **User-Provided Cards**: "Here are my cards: X, Y, Z — interpret them"
- **Actionable Guidance**: Every reading includes 3-7 specific, testable next steps
- **Appropriate Guardrails**: Escalating warnings for high-stakes topics (medical/legal/financial)

## 🎴 Example Usage

### Simple Daily Guidance
```
You: "Pull 1 card for my day and keep it practical"

Claude: [Draws card, provides 2-3 practical suggestions and a lens for the day]
```

### Decision Support
```
You: "3-card spread: past/present/future for my interview process"

Claude: 
- Draws three cards
- Interprets each in context
- Synthesizes narrative
- Provides actionable next steps
- Includes appropriate guardrails
```

### User-Provided Cards
```
You: "Here are my cards: Death upright (Advice), Five of Wands (Obstacle), 
      Star (Outcome). Interpret."

Claude: [Skips drawing, interprets your specific cards by position]
```

## 🛠️ Customization

The skill is designed to be easily modified:

```
tarot-reflection/
├── SKILL.md                      # Core workflow & instructions
├── scripts/
│   └── tarot_deck.py            # Card drawing logic
└── references/
    └── card_meanings.md         # Card interpretations
```

### Customize Card Meanings

Edit `references/card_meanings.md` to:
- Add your own interpretive lens
- Include deck-specific meanings (Thoth, Marseille, etc.)
- Expand synthesis guidelines

### Add New Spreads

Edit `scripts/tarot_deck.py`:

```python
SPREADS = {
    # Existing spreads...
    "my-custom-spread": ["Position1", "Position2", "Position3"]
}
```

### Use Different Cards

Modify `MAJOR_ARCANA` and `MINOR_ARCANA` in `scripts/tarot_deck.py` to use:
- Different tarot decks
- Oracle cards
- Custom card systems

### Adjust Guardrails

Edit the guardrail language in `SKILL.md` to strengthen/weaken epistemic warnings or add domain-specific cautions.

## 📚 Documentation

- **[USAGE_GUIDE.md](USAGE_GUIDE.md)** - Comprehensive usage documentation
- **[EXAMPLE_READING.md](EXAMPLE_READING.md)** - Full sample reading with annotations
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Guidelines for contributors

## 🏗️ Skill Architecture

### Progressive Disclosure Design

The skill uses a three-level loading system for efficiency:

1. **Metadata** (always loaded): Name + description (~100 words)
2. **SKILL.md** (loaded when triggered): Core workflow (<500 lines)
3. **Bundled resources** (loaded as needed): Scripts and references

This keeps Claude's context window usage minimal while providing comprehensive capabilities.

### Design Principles

- **Reflection, not fortune-telling**: Probabilistic language, emphasis on agency
- **Position-aware interpretation**: Context matters more than card alone
- **Actionable over abstract**: Concrete next steps every reading
- **Appropriate guardrails**: Reality checks scaled to question stakes

## 🤝 Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Useful contributions might include:**
- Additional spread types
- Enhanced card interpretations
- Domain-specific guidance (career, relationship, creative)
- Improved synthesis algorithms
- Better guardrail language

## 📜 License

MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- Built using the [Anthropic Skills Framework](https://docs.claude.com)
- Card meanings based on the Rider-Waite-Smith tradition
- Inspired by reflective decision-making practices

## ⚠️ Important Notice

This skill provides **reflective guidance, not deterministic predictions**. Use it to:
- ✅ Clarify your thinking
- ✅ Explore different perspectives
- ✅ Generate actionable experiments
- ✅ Identify blind spots

Always:
- ❌ Validate insights through real-world action
- ❌ Consult professionals for medical/legal/financial decisions
- ❌ Remember you have agency—cards illuminate, they don't dictate

## 🐛 Issues & Support

- **Bug reports**: [Open an issue](../../issues)
- **Questions**: [Start a discussion](../../discussions)
- **Feature requests**: [Open an issue](../../issues) with the "enhancement" label

## 📊 Version History

- **v1.0.0** (2026-01-29): Initial release
  - 5 spread types
  - 78-card RWS deck
  - Position-aware interpretations
  - Actionable guidance system
  - Appropriate guardrails

---

**Remember**: This is a tool for decision support and reflection, not a deterministic prediction system. Use it to sharpen your thinking, but always validate insights through real-world experiments and concrete information. You have agency; the cards illuminate dynamics, they don't dictate outcomes.
