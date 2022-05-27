"""Access point to the Deterministic Finite Automaton (DFA)
    The DFA works based on a definition that is in a given config file.
    ------------
    Functions
    ------------
    main:
        Access point to the DFA system. It controls the program's workflow.
"""

import pandas as pd

def generate_automaton(sigma,
                            states,
                            transitions_df,
                            start_state,
                            final_state,
                            test_strings):
    predictions = []
    print("\nTransitions = ")
    print(transitions_df)
    for word in test_strings:
        print("\n<---------------")
        print("Test word = "+word)
        current_state = start_state[0] # str
        for letter in word:
            #print(type(letter)) # str
            print("\nTransition's input letter = "+letter)
            print("\nCurrent state = "+current_state)
            print("\nPossible transitions = ")
            transition_df = transitions_df.loc[(transitions_df['before'] == current_state) & (transitions_df['input'] == letter)]
            print(transition_df)
            next_state = transition_df['after'].values
            next_state = str(next_state[0]) # str
            current_state = next_state
        if (current_state in final_state):
            print("\n-> Word "+ word +" is part of the language.")
            predictions.append(True)
        else:
            predictions.append(False)
        print("---------------\>")
    print(predictions)