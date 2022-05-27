"""The test module contains several functions to validate input data from config file.
    ------------
    Functions
    ------------
    validate_transitions:
        Organizes transition functions in DataFrame object.
    check_empty_transition:
        Raises error for empty transition.
    check_incomplete_transitions:
        Raises error for incomplete transitions function.
    validate_start_state:
        Validates start state input value.
    validate_final_states:
        Validates final state(s) input value(s).
    validate_test_strings:
        Validates test strings input values.
    """


import re
import pandas as pd


TRANSITION_CHECK = "\(([a-zA-Z]+\d)\s*(\w)\)\s*->\s*([a-zA-Z]+\d)"


def validate_transitions(transitions,states,sigma) -> pd.DataFrame:
    """Organizes transition functions in DataFrame object.

    Args:
        transitions (list): transition functions.

    Returns:
        pd.DataFrame: table where each row is a transition and given columns show before and after states, as well as their transition string.
    """
    before_state = []
    after_state = []
    transition_string = []
    
    for transition in transitions:
        re_obj = re.compile(TRANSITION_CHECK)
        result = re_obj.search(transition)
        before_state.append(result.group(1))
        transition_string.append(result.group(2))
        after_state.append(result.group(3))
    
    for item in before_state:
        if item not in states:
            print("\nValueError: transition state <"+item+"> not in available states "+str(states)+".")
            raise SystemExit(0)
    
    for item in after_state:
        if item not in states:
            print("\nValueError: transition state <"+item+"> not in available states "+str(states)+".")
            raise SystemExit(0)
    
    for item in transition_string:
        if item not in sigma:
            print("\nValueError: transition string <"+item+"> not in sigma "+str(sigma)+".")
            raise SystemExit(0)
    
    transitions_dict = {"before": before_state,
                        "input": transition_string, 
                        "after": after_state}
    
    transitions_df = pd.DataFrame(transitions_dict)
    return transitions_df


def check_empty_transition(transitionID,transitionFunction):
    """Raises error for empty transition.

    Args:
        transitionID (str): empty transition ID in configuration file.
        transitionFunction (str): empty transition's definition.

    Raises:
        SystemExit: if empty string was found.
    """
    print("\nValueError: transition function is empty: "+transitionID+"="+transitionFunction)
    raise SystemExit(0)


def check_incomplete_transitions():
    """Raises error for incomplete transitions function.

    Raises:
        SystemExit: if incomplete transitions function is found.
    """
    print("\nValueError: given transition functions are insufficient for DFA to work properly.")
    raise SystemExit(0)


def validate_start_state(start_state, states) -> list:
    """Validates start state input value.

    Args:
        start_state (list): start state value, should be <q1>.
        states (list): available states.

    Raises:
        SystemExit: if start state is incorrect.

    Returns:
        list: start state validated input value.
    """
    if start_state[0] != "q1":
        print("\nValueError: start state <"+start_state[0]+"> is incorrect, should be <q1>.")
        raise SystemExit(0)
    if start_state[0] not in states:
        print("\nValueError: start state <"+start_state[0]+"> is not in available states "+str(states)+".")
        raise SystemExit(0)
    return start_state


def validate_final_states(final_state, states) -> list:
    """Validates final state(s) input value(s).

    Args:
        final_state (list): final state value(s).
        states (list): available states.

    Raises:
        SystemExit: if final state is found not in states.

    Returns:
        list: final state(s) validated input value(s).
    """
    error_states = []
    for item in final_state:
        condition = states.__contains__(item)
        if condition == False:
            error_states.append(item)
    if len(error_states) != 0:
        print("\nValueError: final state(s) "+str(error_states) +" not in available states "+str(states)+".")
        raise SystemExit(0)
    return final_state

def validate_test_strings(test_strings, sigma) -> list:
    """Validates test strings input values.
    Args:
        test_strings (list): words list to evaluate the DFA's performance.
        sigma (list): alphabet.

    Raises:
        SystemExit: if letter in word isn't part of the alphabet.

    Returns:
        list: validated test strings.
    """
    for word in test_strings:
        for letter in word:
            if letter not in sigma:
                print("\nValueError: letter "+letter+" in word <"+word+"> isn't part of alphabet "+str(sigma)+".")
                raise SystemExit(0)
    return test_strings
