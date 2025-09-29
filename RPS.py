# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    from collections import defaultdict
    opponent_history.append(prev_play)
    transition_table = defaultdict(lambda: {"R": 0,"P":0,"S":0}
    if len(opponent_history) > 2:
        last_two = "".join(opponent_history[-3:1])
        transition_table[last_two][opponent_history[-1]] += 1
        prediction = max(transition_table[last_two], key=transition_table[last_two].get)
    else:
        predictiion = "R"

    counter_moves = {"R":"P","P":"S","S":"R"}
    return counter_moves[prediction]
