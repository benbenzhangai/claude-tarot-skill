# Changelog

All notable changes to the Tarot Reflection Skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Additional spread types (Horseshoe, Tree of Life)
- Enhanced card combination interpretations
- Domain-specific guidance modules (career, relationship, creative)

---

## [1.0.0] - 2026-01-29

### 🎉 Initial Release

#### Added
- **Core Workflow**: 7-step reading process (clarify, select spread, draw, interpret, synthesize, guide, guardrails)
- **5 Spread Types**:
  - 1-card (daily guidance)
  - 3-card Past/Present/Future
  - 3-card Situation/Action/Outcome
  - 5-card Decision (comparing paths)
  - Celtic Cross (10-card deep dive)
- **78-Card RWS Deck**: Complete Rider-Waite-Smith deck with Major & Minor Arcana
- **Position-Aware Interpretations**: Same card interpreted differently based on spread position
- **Reversal Support**: Optional reversed cards (~50% chance) with modulation meanings
- **Actionable Guidance System**: 3-7 concrete next steps per reading
- **Epistemic Guardrails**: Reality-checking language scaled to question stakes
- **User-Provided Cards**: Support for interpreting user's own card draws
- **Comprehensive Card Meanings**: Detailed reference file with position-specific guidance
- **Card Drawing Script**: Python utility for reproducible draws with seed support

#### Features
- Position-aware synthesis across cards
- Dominant theme identification
- Tension/conflict highlighting
- Major Arcana weight assessment
- Progressive disclosure design (lean SKILL.md, detailed references loaded as needed)

#### Documentation
- Complete usage guide
- Example reading with annotations
- Contributing guidelines
- Quick reference card
- GitHub setup instructions

#### Quality Standards
- No deterministic fortune-telling language
- Probabilistic framing throughout
- Professional consultation recommendations for high-stakes decisions
- User agency emphasis
- Real-world validation encouragement

---

## Version History Guidelines

### Types of Changes

- **Added**: New features
- **Changed**: Changes to existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Vulnerability fixes

### Version Numbering

- **Major (X.0.0)**: Breaking changes, incompatible API changes
- **Minor (1.X.0)**: New features, backward-compatible
- **Patch (1.0.X)**: Bug fixes, backward-compatible

### Example Future Entries

```markdown
## [1.1.0] - YYYY-MM-DD

### Added
- Horseshoe spread (7 cards)
- Enhanced relationship dynamics interpretation
- Career-specific action templates

### Changed
- Improved synthesis algorithm for better narrative coherence
- Updated guardrail language for medical questions

### Fixed
- Card drawing script handles edge case with user-excluded cards
- Position parsing for user-provided cards now case-insensitive

## [1.0.1] - YYYY-MM-DD

### Fixed
- Typo in Two of Swords interpretation
- Celtic Cross position 6 description clarified
- Package script validation error message improved
```

---

## Links

- [Repository](https://github.com/YOUR-USERNAME/tarot-reflection-skill)
- [Issues](https://github.com/YOUR-USERNAME/tarot-reflection-skill/issues)
- [Discussions](https://github.com/YOUR-USERNAME/tarot-reflection-skill/discussions)
- [Releases](https://github.com/YOUR-USERNAME/tarot-reflection-skill/releases)

## Contributors

Thank you to all contributors who have helped improve this skill!

- [Your Name] - Initial work

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to contribute.
