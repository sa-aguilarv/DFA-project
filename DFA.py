"""DFA's execution functions and performance evaluation.
    The DFA works based on a definition that is built through given parameters: transitions_df, start_state, final_state, test_strings.
    ------------
    Functions
    ------------
    generate_automaton:
        Builds working DFA machine and given a collection of test words its performance is evaluated.
"""

import pandas as pd
import test

def generate_automaton(transitions_df,
                        start_state,
                        final_state,
                        test_strings) -> list:
    """Builds working DFA machine and given a collection of test words its performance is evaluated.

    Args:
        transitions_df (pd.DataFrame): table defining possible transitions.
        start_state (list): DFA start state.
        final_state (list): DFA final state(s).
        test_strings (list): collection of test words.

    Returns:
        list: predictions based on DFA machine's performance.
    """
    predictions = []
    #print("\nTransitions = ")
    #print(transitions_df)
    for word in test_strings:
        #print("\n<---------------")
        #print("Test word = "+word)
        current_state = start_state[0] # str
        for letter in word:
            #print(type(letter)) # str
            #print("\nTransition's input letter = "+letter)
            #print("\nCurrent state = "+current_state)
            #print("\nPossible transitions = ")
            try:
                transition_df = transitions_df.loc[(transitions_df['before'] == current_state) & (transitions_df['input'] == letter)]
                #print(transition_df)
                next_state = transition_df['after'].values
                next_state = str(next_state[0]) # str
                current_state = next_state
            except:
                test.check_incomplete_transitions()
        if (current_state in final_state):
            #print("\n-> Word "+ word +" is part of the language.")
            predictions.append(True)
        else:
            #print("\n-> Word "+ word +" isn't part of the language.")
            predictions.append(False)
        #print("---------------\>")
    #print(predictions)
    return predictions