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
    print(transitions_df)