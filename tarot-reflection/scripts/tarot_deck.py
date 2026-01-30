#!/usr/bin/env python3
"""
Tarot deck definition and drawing utilities.
Ensures consistent card selection with optional seed for reproducibility.
"""

import random
from typing import List, Tuple, Optional

# 78-card Rider-Waite-Smith deck
MAJOR_ARCANA = [
    "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
    "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
    "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
    "The Devil", "The Tower", "The Star", "The Moon", "The Sun",
    "Judgement", "The World"
]

MINOR_ARCANA = {
    "Wands": ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
              "Page", "Knight", "Queen", "King"],
    "Cups": ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
             "Page", "Knight", "Queen", "King"],
    "Swords": ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
               "Page", "Knight", "Queen", "King"],
    "Pentacles": ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                  "Page", "Knight", "Queen", "King"]
}

def get_full_deck() -> List[str]:
    """Return complete 78-card deck."""
    deck = MAJOR_ARCANA.copy()
    for suit, ranks in MINOR_ARCANA.items():
        deck.extend([f"{rank} of {suit}" for rank in ranks])
    return deck

def draw_cards(
    count: int,
    seed: Optional[int] = None,
    allow_reversals: bool = True,
    exclude: Optional[List[str]] = None
) -> List[Tuple[str, str]]:
    """
    Draw cards with optional reversals.
    
    Args:
        count: Number of cards to draw
        seed: Random seed for reproducibility (None = truly random)
        allow_reversals: If True, cards can be reversed (~50% chance each)
        exclude: Cards to exclude from draw (for user-provided partial readings)
    
    Returns:
        List of (card_name, orientation) tuples
        Example: [("The Tower", "Upright"), ("Two of Cups", "Reversed")]
    """
    if seed is not None:
        random.seed(seed)
    
    deck = get_full_deck()
    if exclude:
        deck = [card for card in deck if card not in exclude]
    
    drawn = random.sample(deck, min(count, len(deck)))
    
    results = []
    for card in drawn:
        if allow_reversals and random.random() < 0.5:
            orientation = "Reversed"
        else:
            orientation = "Upright"
        results.append((card, orientation))
    
    return results

def format_draw(cards: List[Tuple[str, str]], positions: List[str]) -> List[dict]:
    """
    Format cards with their positions.
    
    Args:
        cards: List of (card_name, orientation) tuples
        positions: Position names matching card count
    
    Returns:
        List of dicts with position, card, and orientation
    """
    return [
        {
            "position": pos,
            "card": card,
            "orientation": orientation
        }
        for (card, orientation), pos in zip(cards, positions)
    ]

# Spread definitions
SPREADS = {
    "1-card": ["Present/Focus"],
    "3-card-past-present-future": ["Past", "Present", "Future"],
    "3-card-situation-action-outcome": ["Situation", "Action", "Outcome"],
    "5-card-decision": ["Current State", "Path A", "Path B", "Advice", "Likely Outcome"],
    "celtic-cross": [
        "Present", "Challenge", "Past", "Future", "Above/Goal",
        "Below/Foundation", "Advice", "External", "Hopes/Fears", "Outcome"
    ]
}

def get_spread(spread_name: str) -> List[str]:
    """Get position names for a spread."""
    return SPREADS.get(spread_name, SPREADS["3-card-past-present-future"])

if __name__ == "__main__":
    # Example usage
    print("Drawing 3 cards with seed=42:")
    cards = draw_cards(3, seed=42, allow_reversals=True)
    positions = get_spread("3-card-past-present-future")
    reading = format_draw(cards, positions)
    
    for card_data in reading:
        print(f"{card_data['position']}: {card_data['card']} ({card_data['orientation']})")
