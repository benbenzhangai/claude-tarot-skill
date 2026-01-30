# Contributing to Tarot Reflection Skill

Thank you for considering contributing to this project! This document provides guidelines and information for contributors.

## 🌟 Ways to Contribute

### 1. Report Issues
- **Bugs**: Card drawing errors, interpretation issues, formatting problems
- **Feature requests**: New spreads, enhanced interpretations, better guidance
- **Documentation**: Unclear instructions, missing examples

### 2. Improve Documentation
- Fix typos or clarify existing docs
- Add more examples
- Improve installation instructions
- Translate documentation

### 3. Enhance the Skill
- Add new spread types
- Improve card interpretations
- Enhance synthesis guidelines
- Add domain-specific guidance (career, relationship, creative)
- Improve guardrail language

### 4. Test and Provide Feedback
- Use the skill on real questions
- Report what works well
- Suggest improvements
- Share interesting use cases

## 🚀 Getting Started

### Prerequisites
- Access to Claude.ai with Skills enabled
- Python 3.8+ (for testing scripts)
- Git basics

### Development Setup

1. **Fork the repository**
   ```bash
   git fork https://github.com/yourusername/tarot-reflection-skill
   cd tarot-reflection-skill
   ```

2. **Understand the structure**
   ```
   tarot-reflection/
   ├── SKILL.md                  # Core workflow
   ├── scripts/
   │   └── tarot_deck.py        # Card logic
   └── references/
       └── card_meanings.md     # Interpretations
   ```

3. **Test your changes**
   ```bash
   # Test card drawing script
   python3 scripts/tarot_deck.py
   
   # Package the skill
   python3 /path/to/package_skill.py tarot-reflection/
   
   # Install in Claude and test
   ```

## 📝 Making Changes

### Skill Modifications

#### Adding a New Spread

1. Edit `scripts/tarot_deck.py`:
   ```python
   SPREADS = {
       # Existing spreads...
       "relationship-dynamics": [
           "You", "Them", "Relationship", 
           "Challenge", "Potential", "Advice"
       ]
   }
   ```

2. Add guidance in `SKILL.md` under "Select the Spread":
   ```markdown
   **Relationship Dynamics (6-card)**: Understanding interpersonal dynamics
   ```

3. Test thoroughly with various questions

#### Enhancing Card Meanings

1. Edit `references/card_meanings.md`
2. Keep format consistent:
   ```markdown
   **Card Name (Upright)**: Core meanings, themes
   **Card Name (Reversed)**: Modulation meanings
   **Advice context**: When in advice position
   **Obstacle context**: When in obstacle position
   ```

3. Ensure interpretations are:
   - Contextual (not just keyword lists)
   - Actionable (what this means for decisions)
   - Balanced (avoid overly negative/positive)

#### Improving Workflows

1. Edit `SKILL.md` workflow steps
2. Keep language:
   - Imperative/infinitive form
   - Concise (no fluff)
   - Actionable (clear instructions)

3. Test with edge cases:
   - Vague questions
   - High-stakes decisions
   - User-provided partial cards

### Code Quality Standards

#### Python Scripts
```python
# Good practices:
- Type hints for function signatures
- Docstrings for all functions
- Clear variable names
- Error handling for edge cases

# Example:
def draw_cards(
    count: int,
    seed: Optional[int] = None,
    allow_reversals: bool = True
) -> List[Tuple[str, str]]:
    """
    Draw cards with optional reversals.
    
    Args:
        count: Number of cards to draw
        seed: Random seed for reproducibility
        allow_reversals: If True, cards can be reversed
    
    Returns:
        List of (card_name, orientation) tuples
    """
```

#### Markdown Documentation
- Use clear headers (##, ###)
- Include examples for complex concepts
- Keep paragraphs short (3-5 sentences)
- Use lists for multi-item content
- Code blocks for all code snippets

### Testing Checklist

Before submitting changes:

- [ ] Scripts run without errors
- [ ] Skill packages successfully
- [ ] Tested in Claude with 3+ different questions
- [ ] Documentation updated
- [ ] Examples still work
- [ ] No broken references between files
- [ ] Maintains backward compatibility (unless breaking change)

## 🔄 Pull Request Process

### 1. Create a Branch
```bash
git checkout -b feature/your-feature-name
# or
git checkout -b fix/issue-description
```

### 2. Make Your Changes
- Follow style guidelines above
- Keep commits focused and atomic
- Write clear commit messages

### 3. Test Thoroughly
- Package the skill
- Test in Claude with varied questions
- Verify documentation accuracy

### 4. Submit PR
- Clear title describing the change
- Description explaining:
  - What changed
  - Why it changed
  - How to test it
- Link related issues

### 5. Code Review
- Respond to feedback constructively
- Make requested changes promptly
- Keep discussion focused on the code

## 💡 Contribution Ideas

### High-Impact Contributions

1. **Domain-Specific Spreads**
   - Career transitions
   - Creative projects
   - Relationship dynamics
   - Personal growth milestones

2. **Enhanced Interpretations**
   - More position-specific guidance
   - Better synthesis patterns
   - Nuanced reversal meanings

3. **Improved Actionability**
   - Domain-specific action templates
   - Better uncertainty reduction strategies
   - More concrete experiment designs

4. **Better Guardrails**
   - Context-sensitive warnings
   - Clearer epistemic language
   - Better validation prompts

### Documentation Needs

- Video tutorial (installation & basic use)
- More diverse example readings
- FAQ section
- Troubleshooting guide
- Translations (Spanish, French, etc.)

## 🎨 Style Guide

### Writing Style
- **Clarity over cleverness**: Simple, direct language
- **Active voice**: "Draw three cards" not "Three cards are drawn"
- **Concise**: Remove unnecessary words
- **Specific**: "Set a 2-week deadline" not "Decide soon"

### Tarot Interpretation Style
- **Reflective, not deterministic**: "suggests" not "predicts"
- **Empowering**: Emphasize user agency
- **Balanced**: Acknowledge challenges without fear-mongering
- **Contextual**: Connect cards to specific situations

### Code Style
- PEP 8 for Python
- Type hints where helpful
- Docstrings for public functions
- Comments for complex logic only

## ⚠️ Important Guidelines

### What NOT to Change

**Don't remove or weaken guardrails** - The skill's epistemic humility is a core feature

**Don't add deterministic language** - Keep probabilistic framing

**Don't make medical/legal claims** - Always defer to professionals

### Breaking Changes

If your change breaks backward compatibility:
1. Discuss in an issue first
2. Update version number (major bump)
3. Provide migration guide
4. Update all examples

## 🏆 Recognition

Contributors will be:
- Listed in README acknowledgments
- Credited in release notes
- Thanked in commit messages

Significant contributors may be invited as collaborators.

## 📞 Questions?

- **General questions**: [Start a discussion](../../discussions)
- **Specific issues**: [Open an issue](../../issues)
- **Quick questions**: Comment on relevant PR/issue

## 📜 Code of Conduct

### Our Pledge

We're committed to making participation in this project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

**Positive behaviors:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what's best for the community
- Showing empathy towards others

**Unacceptable behaviors:**
- Trolling, insulting/derogatory comments, personal attacks
- Public or private harassment
- Publishing others' private information
- Other conduct reasonably considered inappropriate

### Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by opening an issue or contacting project maintainers. All complaints will be reviewed and investigated promptly and fairly.

## 🙏 Thank You!

Every contribution, no matter how small, helps make this skill better for everyone. We appreciate your time and effort!

---

**Questions about contributing?** Open an issue or start a discussion—we're happy to help!
