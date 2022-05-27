"""The input_output module contains several functions to load files and to format the DFA outputs.
    ------------
    Functions
    ------------
    load_config_file:
        Reads the config file and creates a dictionary with the configuration information for use in DFA.
    parse_input:
        Reads the arguments of DFA.
    write_output_file:
        Saves output as *csv file.
"""


import argparse
import re
import test
import pandas as pd


SIGMA = "(@sigma)\s*=\s*(\{\w+(\s*,\s*\w*)*\})" 
STATES = "(@Q)\s*=\s*(\{[a-zA-Z]+\d+(\s*,\s*[a-zA-Z]+\d*)*\})" 
TRANSITIONS = "(@f)\s*=\s*({\([a-zA-Z]+\d\s*\w\)\s*->\s*[a-zA-Z]+\d+(\s*,\s*\([a-zA-Z]+\d\s*\w\)\s*->\s*[a-zA-Z]+\d)*\})"
START_STATE = "(@q0)\s*=\s*([a-zA-Z]+\d)"  
FINAL_STATE ="(@F)\s*=\s*(\{\w+(,\s?\w*)*\})" 
TEST_STRINGS ="(@test)\s*=\s*(\{\w+(,\s?\w*)*\})"
REAL_STRINGS ="(@result)\s*=\s*(\{\w+(,\s?\w*)*\})"
TRANSITION_INCOMPLETE = "(@f)\s*=\s*\{(\([a-zA-Z]+\d\s*\d\)->\s*,?)"

PATTERNS_CONFIG_FILE = [SIGMA,
                        STATES,
                        TRANSITIONS,
                        START_STATE,
                        FINAL_STATE,
                        TEST_STRINGS,
                        REAL_STRINGS 
]


def load_config_file(file_path: str) -> dict:
    """Load config file
    Reads the config file and creates a dictionary with the configuration information for use in DFA.
    Args:
        file_path (str): File path and name of the configuration file
    Returns:
        dict: Dictionary with the information stored in the configuration file.
    """
    config_dict = {}
    f = open(file_path, 'r')
    text = f.read()
    f.close()

    for pattern in PATTERNS_CONFIG_FILE:
        re_obj = re.compile(pattern)
        result = re_obj.search(text)
        if result is None:
            re_obj = re.compile(TRANSITION_INCOMPLETE)
            result = re_obj.search(text)
            transitionID = result.group(1)
            transitionFunction = result.group(2)
            test.check_empty_transition(transitionID,transitionFunction)
        config_dict[result.group(1)] = result.group(2)
    return config_dict    


def parse_input() -> argparse.Namespace:
    """Reads the arguments of DFA.
    Returns:
        argparse.Namespace: The object argparse.Namespace where the command line arguments are stored.
    """
    parser = argparse.ArgumentParser(
        description='Time comparison of several sorting algorithms')
    parser.add_argument('-i',
                        '--input',
                        help='Config file path',
                        required=True)
    parser.add_argument(
        '-o',
        '--output',
        help='Path and file name were the results are written. '
        'If not indicated, the results are written in the standard output')
    return parser.parse_args()


def write_output_file(answer, output_df):
    """Saves output as *csv file.

    Args:
        answer (str): [y/n] option given by user. If 'y', *.csv file is saved.
        output_df (pd.DataFrame): table with DFA's performance results.
    """
    answer = answer.lower()
    if answer == "y":
        name = input("\nType in output's filename (*.csv extension will be added): ")
        output_df.to_csv(name+".csv")
    else:
        print("ValueError: incorrect answer. Please run again and type [y/n].")