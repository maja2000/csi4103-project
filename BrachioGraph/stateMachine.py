# File to store main state machine of system
from transitions import Machine


class PenPlotter(object):


    states = ['IDLE', 
        'GETTING_USER_INPUT', 
        'CONVERTING_JPG_TO_JSON', 
        'FORMATTING_JSON', 
        'SLICING', 
        'SENDING_INSTRUCTIONS_TO_ARDUINO',
        'RECEIVING_FROM_ARDUINO'
        'E_STOP'
        'DEFAULT'
        ]

    def __init__(self, plotterState):

