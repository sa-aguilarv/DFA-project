# Evaluation

The Deteministic Finite Automaton (DFA) implementation in Python followed these evaluation criteria:

1. Order
- It has an access point (system's execution module).
- It is organized in functions.
- The functions are organized in modules depending on their utility.

2. Documentation
- All modules are documented based on their main objective.
- All functions are documented based on their objective, input and output parameters.
- The user's interface allows to show the system's documentation for guidance using the command <help>.

3. DFA Functionality
 - System's outputs correspond to expected results in validated strings.
 - The program reads different definitions of DFA.
 - The program doesn't loop indefinitely and always responds to an accepting or rejecting state.

4. Functional requirements
 - Information is read through a configuration file.
 - The information is written/shown through CLI or an output file as indicated by the user.
 - The comparisons (calculated vs expected result) show in tabular form.

5. Input validation
- Transition function (states and input string) is validated.
- Set of final states are validated.
- Start state is validated.
- Execution command has the minimum parameters to run.