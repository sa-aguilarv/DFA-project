# Deteministic Finite Automaton (DFA)

The DFA works based on a definition that is in a given configuration file (see __inputs__ folder to see example files).

Output files are in *.csv format (see __automata_correct_results.csv__)

# Evaluation

The Deteministic Finite Automaton (DFA) implementation in Python followed these evaluation criteria:

**1. Order**
- It has an access point (system's execution module). [DONE]
- It is organized in functions. [DONE]
- The functions are organized in modules depending on their utility. [DONE]

**2. Documentation**
- All modules are documented based on their main objective. [DONE]
- All functions are documented based on their objective, input and output parameters. [DONE]
- The user's interface allows to show the system's documentation for guidance using the command <help>. [DONE]

**3. DFA Functionality**
 - System's outputs correspond to expected results in validated strings. [DONE]
 - The program reads different definitions of DFA. [DONE]
 - The program doesn't loop indefinitely and always responds to an accepting or rejecting state. [DONE]

**4. Functional requirements**
 - Information is read through a configuration file. [DONE]
 - The information is written/shown through CLI [DONE] or an output file as indicated by the user [DONE].
 - The comparisons (calculated vs expected result) show in tabular form. [DONE]

**5. Input validation**
- Transition function (states and input string) is validated [DONE].
- Set of final states are validated [DONE].
- Start state is validated [DONE].
- Execution command has the minimum parameters to run [DONE].