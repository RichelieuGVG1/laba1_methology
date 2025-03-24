import random
import math

def get_lcm(numbers):
    """Вычисляет наименьшее общее кратное (НОК) для списка чисел."""
    lcm = numbers[0]
    for num in numbers[1:]:
        lcm = lcm * num // math.gcd(lcm, num)
    return lcm

def play_game():
    """Основная логика игры."""
    print("Welcome to the Brain Games!\n")
    name = input("May I have your name? ")
    print(f"Hello, {name}!\n")
    print("Find the smallest common multiple of given numbers.\n")
    
    for _ in range(3):
        numbers = [random.randint(1, 100) for _ in range(3)]
        correct_answer = get_lcm(numbers)
        print(f"Question: {' '.join(map(str, numbers))}")
        user_answer = input("Your answer: ")
        
        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("Correct!\n")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    play_game()