import random

def monthly_hall_game(switch: bool):
    """
    Simulates one round of the Monty Hall game and returns whether the player won the car or not.

    Parameters:

    switch (bool): Whether the player switches their choice after one door is revealed.
    Returns:

    (bool): True if the player won the car, False otherwise.
    Example:

    monthly_hall_game(True) False 
    """
    doors = ['car', 'goat', 'goat']
    random.shuffle(doors)

    initial_choice = random.choice(range(3))

    if switch:
        doors_revealed = [i for i in range(3) if i != initial_choice and doors[i] != "car"]
        door_revealed = random.choice(doors_revealed)
        final_choice = [i for i in range(3) if i != initial_choice and i != door_revealed][0]
    else:
        final_choice = initial_choice
    return doors[final_choice] == 'car'


def simulation(number_games):
    """Simulates a number of rounds of the Monty Hall game and returns the number of wins for each strategy.

    Parameters:

    number_games (int): The number of rounds to simulate.
    Returns:

    (tuple): A pair of integers representing the number of wins with and without switching.
    Example:

    simulation(1000) (667, 333)"""
    num_wins_without_switch = sum([monthly_hall_game(False) for _ in range(number_games)])
    num_wins_with_switch = sum([monthly_hall_game(True) for _ in range(number_games)])

    return num_wins_with_switch, num_wins_without_switch


if __name__ == "__main__":
    number = 10000
    win_witout_switch, win_with_switch = simulation(number)
    print(win_witout_switch, win_with_switch)