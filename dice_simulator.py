from random import randint
import PySimpleGUI as sg

class DiceSimulator:
    def __init__(self):
        self.min_value = 1
        self.max_value = 6
        self.playing = True
        self.results = list()
        self.result = ''
        # Layout
        sg.theme('DarkBrown5')
        self.layout = [
            [sg.Text('Dice Simulator', size=(30, 1), font=("Arial", 14, "bold"), justification='center', pad=(0, 10))],
            [sg.Button('Roll Dice', size=(34, 1)), sg.Text('Sides:'), sg.Input('6', size=(3, 1), key='sides')],
            [sg.Output(size=(50, 10))],
            [sg.Push(), sg.Button('Save Results', size=(14, 1))]]
        
            
    def Start(self):
        # Create the window
        self.window = sg.Window('Dice Simulator', self.layout, element_justification='c')
        while True:
            while self.playing:
                self.events, self.values = self.window.read()
                self.max_value = int(self.values['sides'])
                if self.events == 'Roll Dice':
                    print(self.GenerateDiceValue())
                elif self.events == 'Save Results':
                    self.SaveResults()
                elif self.events == sg.WIN_CLOSED:
                    self.playing = False
                    break  
            break    
            print('An error occurred while receiving your response.')
    
    def SaveResults(self):
        with open('Results.txt', 'w') as file:
            file.write('\n'.join(str(r) for r in self.results))
    
    def GenerateDiceValue(self):
        self.result = randint(self.min_value, self.max_value)
        self.results.append(self.result)
        return self.result
        
game = DiceSimulator()
