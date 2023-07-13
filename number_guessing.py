from random import randint
import PySimpleGUI as sg

class GuessTheNumber:
    def __init__(self):
        self.random_number = 0
        self.min_value = 1
        self.max_value = 10
        self.playing = True
        self.attempts = 0
        self.dashes = '-=-' * 15
        
    def Start(self):
        # Layout
        sg.theme('DarkTeal9')
        self.layout = [
            [sg.Text('Guess a number from 1 to 10',size=(25,1),font=("Arial", 14, "bold"),justification='center')],
            [sg.Input('1', size=(3,0),key='Guess'), sg.Button('Guess!',size=(32,0))],
            [sg.Output(size=(40,10))]]
        # Criar a janela
        self.window = sg.Window('Guess the Number', self.layout, resizable=True,finalize=True, element_justification='c')
        self.GenerateRandomNumber()
        while True:
            # Read user input
            self.events, self.values = self.window.Read()
            if self.events == sg.WIN_CLOSED:
                break
            if self.events == 'Guess!':
                if self.values['Guess'] not in map(str, range(1, 11)):
                    print('Guess a valid number.')
                else:
                    self.guess = int(self.values['Guess'])
                    self.attempts += 1
                    while self.playing == True:
                        if self.guess > self.random_number:
                            print('Guess a lower number!')
                            break
                        elif self.guess < self.random_number:
                            print('Guess a higher number!')
                            break 
                        elif self.guess == self.random_number:
                            print(f'{self.dashes}\nYou guessed it after {self.attempts} attempts, congratulations!\n{self.dashes}')
                            self.playing = False
                            break        
            
    def GenerateRandomNumber(self):
        self.random_number = randint(self.min_value,self.max_value)
    
game = GuessTheNumber()