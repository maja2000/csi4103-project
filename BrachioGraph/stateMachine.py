# File to store main state machine of system
from transitions import Machine


class PenPlotter(object):


    states = ['IDLE', 
        'GETTING_USER_INPUT', 
        'CONVERTING_JPG_TO_JSON', 
        'FORMATTING_JSON',
        'BAD_INPUT',
        'SENDING_INSTRUCTIONS_TO_ARDUINO',
        'AWAIT_BEGIN',
        'RECEIVING_FROM_ARDUINO'
        'E_STOP'
        'DEFAULT'
        ]

    def __init__(self, plotterState):

        # Initialize in the Idle state.
        self.machine = Machine(model=self, states=PenPlotter.states, initial='IDLE')

        # When the machine receives user input, transition to the GETTING_USER_INPUT
        # TODO: Define this better, what makes the GETTING_USER_INPUT what it is?
        self.machine.add_transition(trigger='user_input_received', source='IDLE', dest='GETTING_USER_INPUT')

        # When the machine has received all it needs from User input, it can then proceed to the next stage.
        self.machine.add_transition(trigger='input_finalized', source='GETTING_USER_INPUT', dest='CONVERTING_JPG_TO_JSON')

        # When the file selected throws an error, we go to the BAD_INPUT.
        self.machine.add_transition(trigger='file_load_failure', source='GETTING_USER_INPUT',
                                    dest='BAD_INPUT')

        # When the conversion fails, we go to the BAD_INPUT stage.
        self.machine.add_transition(trigger='conversion_failure', source='CONVERTING_JPG_TO_JSON',
                                    dest='BAD_INPUT')

        # When the formatting fails, we go to BAD_INPUT state.
        self.machine.add_transition(trigger='formatting_error', source='FORMATTING_JSON',
                                    dest='BAD_INPUT')

        # When the user confirms that the problem exists, return to the import step.
        self.machine.add_transition(trigger='failure_acknowledged', source='BAD_INPUT',
                                    dest='GETTING_USER_INPUT')

        # The machine has finished converting the image to a JSON file.
        # Next we will need to format the JSON into a workable code.
        # TODO: Define this better.
        self.machine.add_transition(trigger='finished_conversion', source='CONVERTING_JPG_TO_JSON', dest='FORMATTING_JSON')


        self.machine.add_transition(trigger='formatting_complete', source='FORMATTING_JSON',
                                    dest='AWAIT_BEGIN')

        self.machine.add_transition(trigger='begin_accepted', source='AWAIT_BEGIN',
                                    dest='RECEIVING_FROM_ARDUINO')

        # Do we need a E_Stop state?
        self.machine.add_transition(trigger='emergency_stop', source='RECEIVING_FROM_ARDUINO',
                                    dest='IDLE')

        # We need to figure out the Default State.







