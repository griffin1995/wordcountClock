class WordClockLayout:
    def __init__(self, words):
        self.words = words
        self.grid_size = 20  # Initial arbitrary grid size, might need adjustment
        self.grid = self.initialize_grid(self.grid_size)
        self.placements = []

    def initialize_grid(self, size):
        return [[' ' for _ in range(size)] for _ in range(size)]

    def can_place_word(self, word, row, col, horizontal=True):
        """Check if the word can be placed at the specified location."""
        if horizontal:
            if col + len(word) > self.grid_size:
                return False
            return all(self.grid[row][c] in [' ', letter] for c, letter in enumerate(word, start=col))
        else:  # Vertical placement
            if row + len(word) > self.grid_size:
                return False
            return all(self.grid[r][col] in [' ', letter] for r, letter in enumerate(word, start=row))

    def place_word(self, word, row, col, horizontal=True):
        """Place the word on the grid at the specified location."""
        if horizontal:
            for c, letter in enumerate(word, start=col):
                self.grid[row][c] = letter
        else:  # Vertical placement
            for r, letter in enumerate(word, start=row):
                self.grid[r][col] = letter
        self.placements.append((word, row, col, horizontal))

    def find_placement_for_word(self, word):
        """Attempt to place a word in the first available spot with the most overlap."""
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                # Try horizontal and vertical placements
                for horizontal in [True, False]:
                    if self.can_place_word(word, row, col, horizontal):
                        self.place_word(word, row, col, horizontal)
                        return True
        return False

    def generate_layout(self):
        """Generate the word clock layout by placing all words."""
        for word in self.words:
            self.find_placement_for_word(word)

    def print_grid(self):
        """Print the grid for visualization."""
        for row in self.grid:
            print(''.join(row))

def main():
    words = ["ITIS", "HALF", "TEN", "QUARTER", "TWENTY", "FIVE", "MINUTES", "PAST", "TO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "ELEVEN", "TWELVE", "OCLOCK"]
    layout = WordClockLayout(words)
    layout.generate_layout()
    layout.print_grid()

main()
