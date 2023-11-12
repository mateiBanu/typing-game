import time
from typing import Tuple
from word_set import WordSet


def attempt_word(word: str) -> Tuple[float, int]:
    start = time.time()

    mistake_count = 0
    attempt = input(word + ": ")
    while attempt != word:
        mistake_count += 1
        attempt = input(word + ": ")
    
    end = time.time()
    elapsed = end - start

    return elapsed, mistake_count


def run_game(word_file: str, word_count: int):
    word_set = WordSet(word_file)
    total_time = 0
    inaccurate_words = 0
    
    input("Press Enter to start...")

    for i in range(word_count):
        time_taken, mistakes = attempt_word(word_set.get())
        total_time += time_taken
        inaccurate_words += 1 if mistakes > 0 else 0

    print("Average time: " + str(total_time / word_count) + " seconds")
    print("Accuracy: " + str(100 * (word_count - inaccurate_words) / word_count) + "%")