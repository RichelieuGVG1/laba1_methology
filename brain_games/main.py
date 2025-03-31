import argparse
from brain_games.game_engine import ask_name, play_game
from brain_games.games import lcm, progression

def main():
    parser = argparse.ArgumentParser(description="Brain Games")
    parser.add_argument("--game", choices=["lcm", "progression"], required=True, help="Choose a game: 'lcm' or 'progression'")
    args = parser.parse_args()
    
    name = ask_name()
    
    if args.game == "lcm":
        game_logic, game_question = lcm.get_game()
    elif args.game == "progression":
        game_logic, game_question = progression.get_game()
    
    play_game(game_logic, game_question, name)

if __name__ == "__main__":
    main()