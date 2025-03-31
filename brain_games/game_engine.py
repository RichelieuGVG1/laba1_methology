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