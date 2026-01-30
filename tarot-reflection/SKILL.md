---
name: tarot-reflection
description: Reflective tarot readings for decision support and personal insight. Use when users request tarot readings, card interpretations, or reflective guidance on decisions, relationships, career choices, or personal growth. Triggers include "do a tarot reading", "pull cards for", "tarot spread", "interpret these cards", or questions about what tarot says. Supports 1-card, 3-card, 5-card, and Celtic Cross spreads. Provides position-aware interpretations, synthesis, actionable guidance, and appropriate guardrails (no deterministic fortune-telling, encourages real-world verification).
---

# Tarot Reflection Reading (Decision Support)

This skill provides structured, reflective tarot readings that support decision-making and personal insight while maintaining epistemic humility and encouraging real-world verification.

## Core Workflow

Follow these steps for every reading:

### 1. Clarify the Question

Parse the user's request into a clear decision or reflection frame:
- **Decision support**: "Should I take this job?" → Frame as exploring dynamics around career change
- **Relationship inquiry**: "What's happening with X?" → Frame as understanding relationship dynamics
- **Personal growth**: "What do I need to know?" → Frame as reflection on current life chapter

If the question is vague, propose a clarified frame and confirm before proceeding.

### 2. Select the Spread

Choose based on complexity and question type:

**1-card**: Single-focus questions, daily guidance, quick check-ins  
**3-card (Past/Present/Future)**: Timeline-based questions, understanding progression  
**3-card (Situation/Action/Outcome)**: Action-focused decisions  
**5-card (Decision)**: Comparing two paths or complex choices  
**Celtic Cross**: Multi-faceted situations requiring deep exploration

If user specifies a spread, use it. Otherwise, suggest the most appropriate one.

### 3. Draw or Receive Cards

**If user provides cards**: Skip drawing, proceed to interpretation  
**If drawing needed**: Use `scripts/tarot_deck.py` with appropriate parameters

```python
from scripts.tarot_deck import draw_cards, format_draw, get_spread

# Example: 3-card reading with reversals
cards = draw_cards(3, seed=None, allow_reversals=True)
positions = get_spread("3-card-past-present-future")
reading = format_draw(cards, positions)
```

**Reversal handling**: Default to allowing reversals unless user requests "no reversals" or "upright only"

### 4. Interpret Each Card (Position-Aware)

For each card, consult `references/card_meanings.md` and synthesize:

1. **Card's core themes** (from reference)
2. **Position context** (what this position asks)
3. **Orientation** (upright vs reversed if applicable)
4. **Question relevance** (how it applies to user's specific situation)

Write 2-4 sentences per card that connect the card meaning to the position and question.

**Example**:
```
Position: Past
Card: Eight of Pentacles (Upright)
Interpretation: "You've been investing in skill-building and steady, focused work. 
This foundation of competence and dedication has brought you to this decision point. 
The craftsmanship you've developed is not in question—it's a solid base to build from."
```

### 5. Synthesize Across Cards

Create a coherent narrative that:
- Identifies **dominant themes** (which element/energy leads?)
- Highlights **tensions or conflicts** between cards
- Tracks **progression** (how energy flows through the spread)
- Notes **Major Arcana weight** (soul-level themes vs everyday matters)
- Reveals **the through-line** (what story do these cards tell together?)

Write 3-5 sentences that weave the cards into a unified perspective.

### 6. Generate Actionable Guidance

Provide 3–7 concrete next steps or experiments:

**Good actions are**:
- Specific and testable
- Time-bounded when appropriate
- Designed to reduce uncertainty
- Framed with agency (what user can do, not what will happen to them)

**Examples**:
- ✅ "Set a 2-week decision deadline and define 3 criteria for choosing"
- ✅ "Run a 'commitment test': schedule a conversation with the hiring manager to gauge your excitement level"
- ✅ "Journal for 10 minutes on: What am I avoiding by not choosing?"
- ❌ "The universe will guide you" (too passive)
- ❌ "You will meet someone important" (deterministic)

### 7. Apply Guardrails

Every reading ends with reality-checking language that:
- Frames reading as **reflective tool, not deterministic prediction**
- Encourages **validation through real-world action/data**
- Acknowledges **uncertainty and user agency**
- Avoids **medical, legal, or financial certainty**

**Standard guardrail template**:
```
This reading is reflective guidance, not fate or certainty. Use it to sharpen your thinking, 
but validate insights through real-world experiments and concrete information. You have agency; 
the cards illuminate dynamics, they don't dictate outcomes. If this touches on medical, legal, 
or financial decisions, consult qualified professionals.
```

Adapt intensity based on question stakes (higher stakes = stronger guardrails).

## Output Format

Structure every reading as follows:

```
### Tarot Reading: [Question Frame]

**Spread**: [Spread name]  
**Reversals**: [Enabled/Disabled]

---

#### Cards Drawn

1. **[Position]**: [Card Name] ([Orientation])
2. **[Position]**: [Card Name] ([Orientation])
[...etc]

---

#### Interpretations

**[Position 1]**: [Card interpretation in context, 2-4 sentences]

**[Position 2]**: [Card interpretation in context, 2-4 sentences]

[...etc]

---

#### Synthesis

[Narrative weaving cards together, identifying themes/tensions/progression, 3-5 sentences]

---

#### Actionable Guidance

- [Concrete action/experiment 1]
- [Concrete action/experiment 2]
- [Concrete action/experiment 3]
[...3-7 total]

---

#### Guardrails & Reality Check

[Reality-checking language acknowledging uncertainty, encouraging verification, 
affirming user agency]
```

## Special Handling

### User-Provided Cards

When user says "Here are my cards: X, Y, Z":
1. Skip drawing step
2. Parse cards carefully (check spelling, handle variations)
3. If positions not specified, ask or use spread context
4. If orientation not specified, assume upright or ask

### Reversals On/Off

- **Default**: Reversals enabled (~50% chance per card)
- **User request "no reversals"**: Set `allow_reversals=False`
- **Interpretation shift**: Reversals = modulation (blocked, internalized, excessive), not negation

### Avoid Fortune-Telling Language

Replace deterministic phrasing with probabilistic/reflective phrasing:

❌ "You will succeed"  
✅ "Success is supported if you leverage your existing skills"

❌ "This person is your soulmate"  
✅ "This relationship has potential for deep alignment, if both parties invest"

❌ "The cards say don't do it"  
✅ "The cards suggest obstacles—proceed with caution and gather more information"

### High-Stakes Questions

For medical, legal, financial, or safety questions:
1. Provide reading as normal
2. **Strengthen guardrails significantly**
3. Explicitly state: "This is reflection, not professional advice—consult [relevant professional]"

## Resources

- **`scripts/tarot_deck.py`**: Card drawing utilities, deck definitions, spread templates
- **`references/card_meanings.md`**: Comprehensive card interpretations with position guidance

## Quality Checklist

Before delivering a reading, verify:

- [ ] Question is clearly framed
- [ ] Spread matches question complexity
- [ ] Each card interpretation is position-aware
- [ ] Synthesis creates coherent narrative
- [ ] Actions are specific, testable, agency-focused
- [ ] Guardrails are present and appropriate to stakes
- [ ] No deterministic fortune-telling language
- [ ] Output follows standard format
