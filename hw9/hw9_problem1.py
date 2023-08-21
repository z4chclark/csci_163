

import queue

def get_next_states(state):
    eight_pint, five_pint, three_pint = state
    next_states = []

    # Fill 5-pint jug from 8-pint jug
    if eight_pint > 0 and five_pint < 5:
        amount_to_pour = min(eight_pint, 5 - five_pint)
        next_states.append((eight_pint - amount_to_pour, five_pint + amount_to_pour, three_pint))

    # Fill 3-pint jug from 8-pint jug
    if eight_pint > 0 and three_pint < 3:
        amount_to_pour = min(eight_pint, 3 - three_pint)
        next_states.append((eight_pint - amount_to_pour, five_pint, three_pint + amount_to_pour))

    # Pour water from 5-pint jug to 8-pint jug
    if five_pint > 0 and eight_pint < 8:
        amount_to_pour = min(five_pint, 8 - eight_pint)
        next_states.append((eight_pint + amount_to_pour, five_pint - amount_to_pour, three_pint))

    # Pour water from 3-pint jug to 8-pint jug
    if three_pint > 0 and eight_pint < 8:
        amount_to_pour = min(three_pint, 8 - eight_pint)
        next_states.append((eight_pint + amount_to_pour, five_pint, three_pint - amount_to_pour))

    # Pour water from 5-pint jug to 3-pint jug
    if five_pint > 0 and three_pint < 3:
        amount_to_pour = min(five_pint, 3 - three_pint)
        next_states.append((eight_pint, five_pint - amount_to_pour, three_pint + amount_to_pour))

    # Pour water from 3-pint jug to 5-pint jug
    if three_pint > 0 and five_pint < 5:
        amount_to_pour = min(three_pint, 5 - five_pint)
        next_states.append((eight_pint, five_pint + amount_to_pour, three_pint - amount_to_pour))

    return next_states

# use breath search to reach a state where any jug has exactly 4 pints of water
def breadth_search():
    start_state = (8, 0, 0)
    goal_amount = 4
    visited = set()
    state_queue = queue.Queue()

    state_queue.put(start_state)
    visited.add(start_state)

    while state_queue:
        current_state = state_queue.get()
        visited.add(current_state)
        print(current_state)
        
        if goal_amount in current_state:
            print("Solution: " + str(current_state))
            return current_state
        
        for next_state in get_next_states(current_state):
            if next_state not in visited:
                state_queue.put(next_state)

    return None


solution = breadth_search()