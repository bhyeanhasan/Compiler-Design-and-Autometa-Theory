class NFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def is_accepted(self, input_str):
        current_states = {self.start_state}
        count = 0
        # for symbol in input_str:
        for symbol in range(len(input_str)):

            next_states = set()
            for state in current_states:
                if (state, input_str[symbol]) in self.transitions:
                    next_states.update(self.transitions[(state, input_str[symbol])])
                    current_states = next_states
                    print('Current state ' + str(state))
                    print('Possible moves ' + str(next_states))
                    print('-----------------------------------------')

                    if symbol == len(input_str) - 1:
                        count += 1
                        print(str(count) + ' Final state ' + str(current_states))
                        if current_states == accept_states:
                            print('accepted')
                        else:
                            print('not accepted')
                else:
                    count += 1
                    print('Current state ' + str(state))
                    print('No Possible moves ')
                    print(str(count) + " Stuck at " + str(state))
                    print('-----------------------------------------')
                    continue


def okok(state, input):
    if (state, input) in transitions:
        for s in transitions[(start_state, input_str[0])]:
            okok(s, input_str[x + 1])
    else:
        print(state)
        return 0

def start():
    okok(start_state, input_str[x])



x = 0
# Example usage:
states = {'q0', 'q1', 'q2'}
alphabet = {'0', '1'}
transitions = {
    ('q0', '0'): {'q0', 'q1'},
    ('q0', '1'): {'q0'},
    ('q1', '1'): {'q2'}
}
start_state = 'q0'
accept_states = {'q2'}

nfa = NFA(states, alphabet, transitions, start_state, accept_states)

input_str = '01'
nfa.is_accepted(input_str)

start()