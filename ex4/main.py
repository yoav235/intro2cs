import hangman
import hangman_helper

words = hangman_helper.load_words()
hangman.run_single_game(words, 10)