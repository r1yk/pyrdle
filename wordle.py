"""
Here lies a quick command line interface for playing Wordle.
You can even play more than once a day if you want!
"""

import random
import re
from words import words

random.seed()


def main():
    """Start a game of Wordle."""
    wordle = Wordle()
    wordle.play()


class Wordle:
    """https://www.nytimes.com/2022/01/03/technology/wordle-word-game-creator.html"""
    correct = '🟩'
    partial = '🟨'
    incorrect = '⬜'

    def __init__(self):
        self.word = self.get_word()
        self.guesses = 6
        self.guess_results = []
        self.solved = False
        self.remaining_letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
                                  'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
                                  'z', 'x', 'c', 'v', 'b', 'n', 'm']

    def play(self) -> None:
        """Start the game."""
        while not self.solved and self.guesses > 0:
            self.print_remaining_letters()
            guess = self.get_guess()
            guess_result = self.evaluate_guess(guess)
            self.guess_results.append(guess_result)
            self.print_guesses()
            self.guesses -= 1
            if guess_result.get('result').count(Wordle.correct) == 5:
                self.solved = True

        if self.solved:
            print('Winner!')
        else:
            print('Loser!')
            print(f'The answer was {self.word.upper()}.')

    def get_word(self) -> str:
        """Return a random 5-letter word from a predefined list."""
        random_index = random.randint(0, len(words) - 1)
        return words[random_index]

    def get_guess(self) -> str:
        """Return a five-letter guess from the user."""
        guess = input('Enter guess: ').lower()
        # Remove any non-letter characters
        guess = re.sub('[^a-z]', '', guess)
        if len(guess) == 5:
            return guess

        print('Error! Guess must be 5 letters')
        return self.get_guess()

    def evaluate_guess(self, guess: str) -> dict:
        """
        Compare the guess against the solution, and append both the guess
        and the result to `guess_results`
        """
        word_letters = list(self.word)
        result = []
        for i in range(0, 5):
            letter = guess[i]
            if letter == self.word[i]:
                result.append(Wordle.correct)
                word_letters.remove(letter)

            elif letter in word_letters:
                result.append(Wordle.partial)
                word_letters.remove(letter)

            else:
                result.append(Wordle.incorrect)
                if letter in self.remaining_letters:
                    letter_index = self.remaining_letters.index(letter)
                    self.remaining_letters[letter_index] = ' '

        return {
            'guess': guess,
            'result': result
        }

    def print_guesses(self) -> None:
        """Display the graphical results about which letters are fully or partially correct."""
        for guess_result in self.guess_results:
            print('  '.join(guess_result.get('guess').upper()))
            print(' '.join(guess_result.get('result')))
        print()

    def print_remaining_letters(self) -> None:
        """Print a QWERTY keyboard where any incorrectly-guessed letters have been removed."""
        row_1 = [letter.upper() for letter in self.remaining_letters[0:10]]
        row_2 = [letter.upper() for letter in self.remaining_letters[10:19]]
        row_3 = [letter.upper() for letter in self.remaining_letters[19:26]]
        print(' '.join(row_1))
        print(' ' + ' '.join(row_2))
        print('  ' + ' '.join(row_3))
        print('')


if __name__ == '__main__':
    main()
