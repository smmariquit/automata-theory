class DFA:
    def __init__(self, states, alphabet, transition_function, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transition_function = transition_function
        self.current_state = start_state
        self.accept_states = accept_states

    def transition(self, symbol):
        if symbol not in self.alphabet:
            raise ValueError(f"Symbol {symbol} not in alphabet")
        self.current_state = self.transition_function[self.current_state][symbol]

    def is_accepted(self):
        return self.current_state in self.accept_states

    def reset(self):
        self.current_state = 'q0'

# Define the DFA for strings ending with "01"
states = {'q0', 'q1', 'q2'}
alphabet = {'0', '1'}
transition_function = {
    'q0': {'0': 'q0', '1': 'q1'},
    'q1': {'0': 'q2', '1': 'q0'},
    'q2': {'0': 'q2', '1': 'q2'}
}
start_state = 'q0'
accept_states = {'q2'}

# Create the DFA
dfa = DFA(states, alphabet, transition_function, start_state, accept_states)

# Test the DFA~~````
test_strings = ['01', '001', '101', '100', '0101', '1100']

for s in test_strings:
    dfa.reset()
    for symbol in s:
        dfa.transition(symbol)
    print(f"String '{s}': {'Accepted' if dfa.is_accepted() else 'Rejected'}")
