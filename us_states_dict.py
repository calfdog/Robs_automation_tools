""" When you need a U.S. states Dict with state names (keys)
    and abbreviations (values), just roll your own.

    Also get a random US state
    By Rob Marchetti
"""
import random


class USStates:

    def __init__(self):
        pass

    @staticmethod
    def get_states_dict():
        """Create a U.S. states dictionary with states
            and states(key abbreviations(value)
        """

        with open("data/states_data.txt", "r") as states:
            us_states = []
            for state in states:
                us_states.append(state.strip())

        with open("data/states_abv.txt", "r") as states_abv:
            us_states_abv = []
            for state in states_abv:
                us_states_abv.append(state.strip())
        state_dict = dict(zip(us_states, us_states_abv))

        return state_dict

    @staticmethod
    def get_random_us_state():
        """return a random state"""
        with open("data/states_data.txt", "r") as states:
            us_states = []
            for state in states:
                us_states.append(state.strip())
            return random.choice(us_states)



