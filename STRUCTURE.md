# Repository Structure

This document explains the organization of the Tarot Reflection Skill repository.

## 📁 Directory Tree

```
tarot-reflection-skill/
│
├── 📄 README.md                    # Main landing page (what people see first)
├── 📄 LICENSE                      # MIT License
├── 📄 .gitignore                   # Git ignore rules
├── 📄 CHANGELOG.md                 # Version history
├── 📄 CONTRIBUTING.md              # Contribution guidelines
├── 📄 USAGE_GUIDE.md               # Comprehensive user documentation
├── 📄 EXAMPLE_READING.md           # Sample reading with annotations
├── 📄 QUICK_REFERENCE.md           # Cheat sheet for users
├── 📄 GITHUB_SETUP.md              # How to publish (delete after setup)
│
├── 📂 tarot-reflection/            # THE ACTUAL SKILL (this is what gets packaged)
│   ├── 📄 SKILL.md                 # Core workflow and instructions
│   ├── 📂 scripts/                 # Executable code
│   │   └── 📄 tarot_deck.py        # Card drawing utilities
│   └── 📂 references/              # Reference documentation
│       └── 📄 card_meanings.md     # Comprehensive card interpretations
│
├── 📂 .github/                     # GitHub-specific files (optional)
│   ├── 📂 ISSUE_TEMPLATE/
│   │   ├── 📄 bug_report.md
│   │   └── 📄 feature_request.md
│   └── 📂 workflows/               # GitHub Actions (future)
│       └── 📄 validate-skill.yml
│
└── 📂 releases/                    # Pre-built .skill files (optional)
    └── 📄 tarot-reflection.skill   # v1.0.0 release
```

## 📋 File Purposes

### Root-Level Files

| File | Purpose | Audience |
|------|---------|----------|
| `README.md` | Main documentation, first impression | Everyone |
| `LICENSE` | Legal terms (MIT) | Developers, lawyers |
| `.gitignore` | Files to exclude from Git | Git users |
| `CHANGELOG.md` | Version history | Users, contributors |
| `CONTRIBUTING.md` | How to contribute | Contributors |
| `USAGE_GUIDE.md` | Detailed usage instructions | End users |
| `EXAMPLE_READING.md` | Sample reading | Prospective users |
| `QUICK_REFERENCE.md` | Cheat sheet | Active users |
| `GITHUB_SETUP.md` | Publishing guide | Repository maintainer |

### Skill Directory (`tarot-reflection/`)

This is the **actual skill** that gets packaged into `.skill` file:

| File/Directory | Purpose | Loaded When |
|---------------|---------|-------------|
| `SKILL.md` | Core workflow instructions | Skill triggers |
| `scripts/tarot_deck.py` | Card drawing logic | As needed |
| `references/card_meanings.md` | Card interpretations | As needed |

### GitHub-Specific (`.github/`)

Optional but recommended:

| File | Purpose |
|------|---------|
| `ISSUE_TEMPLATE/bug_report.md` | Standardize bug reports |
| `ISSUE_TEMPLATE/feature_request.md` | Standardize feature requests |
| `workflows/validate-skill.yml` | Auto-validate changes (future) |

## 🎯 What Gets Packaged

When creating `tarot-reflection.skill`, **only** include:

```
tarot-reflection/
├── SKILL.md
├── scripts/
│   └── tarot_deck.py
└── references/
    └── card_meanings.md
```

**Do NOT include** in `.skill` file:
- Root-level documentation (README, CONTRIBUTING, etc.)
- `.github/` directory
- `.git/` directory
- Test files
- Build artifacts

## 📦 What Gets Committed to Git

**DO commit:**
- All documentation files
- The skill directory (`tarot-reflection/`)
- `.gitignore`, `LICENSE`, etc.
- Issue templates

**DON'T commit:**
- `.skill` files (add to releases instead)
- Python cache (`__pycache__/`)
- Virtual environments (`venv/`)
- IDE files (`.vscode/`, `.idea/`)
- Temporary files

## 🔄 Workflow

### For End Users
1. Download `tarot-reflection.skill` from releases
2. Install in Claude
3. Refer to `USAGE_GUIDE.md` and `QUICK_REFERENCE.md`

### For Contributors
1. Clone repository
2. Navigate to `tarot-reflection/` directory
3. Edit `SKILL.md`, `scripts/`, or `references/`
4. Test changes
5. Package new `.skill` file
6. Submit PR

### For Maintainers
1. Review PRs
2. Update `CHANGELOG.md`
3. Increment version
4. Package new `.skill` file
5. Create GitHub release
6. Update documentation

## 📝 File Size Guidelines

| Directory/File | Target Size | Limit |
|---------------|-------------|-------|
| `SKILL.md` | < 5,000 words | 10,000 words |
| `references/card_meanings.md` | ~3,000 words | No limit |
| `scripts/tarot_deck.py` | < 500 lines | 1,000 lines |
| Total `.skill` file | < 100 KB | 500 KB |

## 🎨 Documentation Hierarchy

```
Primary Entry → README.md
                ├─→ QUICK_REFERENCE.md (for quick starts)
                ├─→ USAGE_GUIDE.md (for comprehensive guidance)
                ├─→ EXAMPLE_READING.md (for demonstrations)
                └─→ CONTRIBUTING.md (for contributors)

Skill Entry   → SKILL.md
                ├─→ references/card_meanings.md
                └─→ scripts/tarot_deck.py
```

## 🔧 Maintenance Checklist

When updating the repository:

- [ ] Update version in `CHANGELOG.md`
- [ ] Update `SKILL.md` if workflow changes
- [ ] Rebuild `.skill` file if skill changes
- [ ] Update `README.md` if features added
- [ ] Update `USAGE_GUIDE.md` if usage changes
- [ ] Add entry to `CHANGELOG.md`
- [ ] Test thoroughly
- [ ] Create GitHub release
- [ ] Update documentation links

## 📊 Common Operations

### Adding a New Spread

1. Edit `scripts/tarot_deck.py` → add to `SPREADS` dict
2. Update `SKILL.md` → document in "Select the Spread"
3. Update `USAGE_GUIDE.md` → add to spread table
4. Update `QUICK_REFERENCE.md` → add quick command
5. Test new spread thoroughly
6. Update `CHANGELOG.md`

### Improving Card Meanings

1. Edit `references/card_meanings.md`
2. Maintain consistent format
3. Test with example readings
4. Update `CHANGELOG.md`

### Fixing Bugs

1. Identify issue location (SKILL.md vs scripts vs references)
2. Make fix
3. Test thoroughly
4. Update `CHANGELOG.md` → Fixed section
5. Create patch release if significant

## 🎯 Quick Navigation

- **Getting started?** → `README.md`
- **Want to use it?** → `USAGE_GUIDE.md`
- **See an example?** → `EXAMPLE_READING.md`
- **Need quick help?** → `QUICK_REFERENCE.md`
- **Want to contribute?** → `CONTRIBUTING.md`
- **Publishing to GitHub?** → `GITHUB_SETUP.md`
- **Understanding the skill?** → `tarot-reflection/SKILL.md`

---

**Remember**: The `tarot-reflection/` directory is the actual skill. Everything else is documentation and tooling to support it!
