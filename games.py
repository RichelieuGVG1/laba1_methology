import random
import math
import argparse

def ask_name():
    """Запрашивает имя пользователя."""
    print("Welcome to the Brain Games!\n")
    name = input("May I have your name? ")
    print(f"Hello, {name}!\n")
    return name

def play_game(game_logic, game_question, name):
    """Основной цикл игры, использующий переданную логику игры."""
    print(game_question + "\n")
    
    for _ in range(3):
        question, correct_answer = game_logic()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")
        
        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("Correct!\n")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")

def lcm(a, b):
    """Вычисляет наименьшее общее кратное двух чисел."""
    return abs(a * b) // math.gcd(a, b)

def game_lcm():
    """Генерирует три случайных числа и вычисляет их НОК."""
    numbers = [random.randint(1, 100) for _ in range(3)]
    lcm_value = lcm(lcm(numbers[0], numbers[1]), numbers[2])  # Находим НОК для трех чисел
    return ' '.join(map(str, numbers)), lcm_value

def game_progression():
    """Генерирует геометрическую прогрессию со случайной длиной и скрытым элементом."""
    length = random.randint(5, 10)
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    progression = [start * (ratio ** i) for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    return ' '.join(map(str, progression)), correct_answer

def main():
    parser = argparse.ArgumentParser(description="Brain Games")
    parser.add_argument("--game", choices=["lcm", "progression"], required=True, help="Choose a game: 'lcm' or 'progression'")
    args = parser.parse_args()
    
    name = ask_name()
    
    if args.game == "lcm":
        play_game(game_lcm, "Find the smallest common multiple of given numbers.", name)
    elif args.game == "progression":
        play_game(game_progression, "What number is missing in the progression?", name)

if __name__ == "__main__":
    main()
