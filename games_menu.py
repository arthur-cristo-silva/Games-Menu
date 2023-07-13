import PySimpleGUI as sg
import number_guessing
import dice_simulator

class GamesMenu:
    def __init__(self):
        sg.theme('Reds')
        self.font = "Bahnschrift", "bold"
        self.layout = [
            [sg.Text('Games Menu', size=(15, 1), font=(self.font, 24), justification='center', pad=(0, 10))],
            [sg.Button('Guessing Game', size=(10, 2), font=(self.font, 10), pad=(20, 10)), sg.Button('Dice Simulator', size=(10, 2), font=(self.font, 10), pad=(20, 10))]
        ]
    
    def Start(self):
        self.window = sg.Window('Games Menu', self.layout, element_justification='c')
        while True:
            self.events, self.values = self.window.read()
            if self.events == sg.WIN_CLOSED:
                break
            if self.events == 'Guessing Game':
                number_guessing.game.Start()
                self.window.close()
                break
            if self.events == 'Dice Simulator':
                dice_simulator.game.Start()
                self.window.close()
                break
            
GamesMenu().Start()
