import random
import math

def lcm(a, b):
    """Вычисляет наименьшее общее кратное двух чисел."""
    return abs(a * b) // math.gcd(a, b)

def game_lcm():
    """Генерирует три случайных числа и вычисляет их НОК."""
    numbers = [random.randint(1, 100) for _ in range(3)]
    lcm_value = lcm(lcm(numbers[0], numbers[1]), numbers[2])
    return ' '.join(map(str, numbers)), lcm_value

def get_game():
    return game_lcm, "Find the smallest common multiple of given numbers."