import time

def calculate_typing_speed(text, elapsed_time):
    words = text.split()
    num_words = len(words)
    num_characters = sum(len(word) for word in words)
    speed = (num_characters / elapsed_time) * 60
    return num_words, num_characters, speed

def run_typing_test():
    print("Welcome to the Speed Typing Test!")
    print("You will be given a random sentence to type.")
    print("Type the sentence as fast as you can and press Enter.")
    print("Let's get started!\n")

    sentence = "The quick brown fox jumps over the lazy dog."
    print(f"Sentence: {sentence}\n")

    input("Press Enter when you're ready to start the timer.")
    start_time = time.time()

    user_input = input("Type the sentence here: ")
    end_time = time.time()
    elapsed_time = end_time - start_time

    num_words, num_characters, speed = calculate_typing_speed(user_input, elapsed_time)

    print("\nTyping test results:")
    print(f"Time elapsed: {elapsed_time:.2f} seconds")
    print(f"Number of words: {num_words}")
    print(f"Number of characters: {num_characters}")
    print(f"Typing speed: {speed:.2f} characters per minute")

run_typing_test()
