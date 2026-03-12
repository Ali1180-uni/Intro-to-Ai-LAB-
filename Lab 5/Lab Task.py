import string as s
import random as r

def initi():
    return r.randint(10,30)

def poss_new_state(state):
    return [state - take for take in (1,2,3) if take <= state]

def check(state, is_maxmize):
    if state == 0:
        return 1 if is_maxmize else -1
    return None

def minimax(state, is_maxmize):
    score = check(state, is_maxmize)
    if score is not None:
        return score
    
    moves = [minimax(new_state, not is_maxmize) for new_state in poss_new_state(state)]
    return max(moves) if is_maxmize else min(moves)

def best_move(state):
    return max(poss_new_state(state), key=lambda s: minimax(s, False))

def game_over(score):
    print(f"Game Over! Final score: {score}")

def get_move(choice, text = "Choose: "):
    inputs = dict(zip(s.ascii_letters, choice))
    for letter, choice in inputs.items():
        print(f"{letter}: {choice}")
    while True:
        c = input(text)
        if c in inputs:
            return inputs[c]
        print(f"Select one of {', '.join(inputs)}")

def play_nim():
    state = initi()
    while True:
        print(f"Current state: {state}")
        state = get_move(poss_new_state(state))
        score = check(state, is_maxmize=False)
        if score is not None:
            return game_over(score)
        ai_move = best_move(state)
        print(f"I move from {state} to {ai_move}")
        state = ai_move
        score = check(state, is_maxmize=True)
        if score is not None:
            return game_over(score)

play_nim()