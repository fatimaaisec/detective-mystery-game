class Clue:
    def __init__(self, description, evidence):
        self.description = description
        self.evidence = evidence


def get_all_clues():
    """Return list of all clues in the game"""
    clues = [
        Clue(
            description="Found a muddy footprint near the safe",
            evidence="Size 11 shoe - matches Professor Morgan's shoe size"
        ),
        Clue(
            description="Discovered a key card in the corridor",
            evidence="Key card with Professor Morgan's ID number"
        ),
        Clue(
            description="Security camera footage shows suspicious activity",
            evidence="Video shows someone entering the vault at 2:15 AM - wearing Professor Morgan's jacket"
        ),
        Clue(
            description="Found a torn piece of fabric by the window",
            evidence="Blue fabric matches Professor Morgan's lab coat"
        ),
        Clue(
            description="Discovered a note with gambling debts",
            evidence="Note found in Professor Morgan's office mentioning $2 million in debts"
        )
    ]
    return clues
