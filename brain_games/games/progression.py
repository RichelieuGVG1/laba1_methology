import random

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

def get_game():
    return game_progression, "What number is missing in the progression?"