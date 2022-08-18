from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Board():
    def __init__(self, skt, machine):
        self.skt = skt
        self.machine = machine
        self.players_username = ''
        self.last_user = 'Player 1'
        self.Winner = -1
        self.numgames = 0
        self.p1wins = 0
        self.p2wins = 0
        self.ties = 0
        self.p1losses = 0
        self.p2losses = 0
        self.p1 = []  # what player one selected
        self.p2 = []  # what player two selected
        self.gameBoard = Tk()
        self.gameBoard.title(f'Tic Tac Toe ({self.machine})')


    def createBoard(self):
        self.b1 = ttk.Button(self.gameBoard, text='  ')
        self.b1.grid(row=2, column=0, sticky='snew', ipadx=50, ipady=50)
        self.b1.config(command=lambda: self.buttonClick(1))

        self.b2 = ttk.Button(self.gameBoard, text='  ')
        self.b2.grid(row=2, column=1, sticky='snew', ipadx=50, ipady=50)
        self.b2.config(command=lambda: self.buttonClick(2))

        self.b3 = ttk.Button(self.gameBoard, text='  ')
        self.b3.grid(row=2, column=2, sticky='snew', ipadx=50, ipady=50)
        self.b3.config(command=lambda: self.buttonClick(3))

        self.b4 = ttk.Button(self.gameBoard, text='  ')
        self.b4.grid(row=3, column=0, sticky='snew', ipadx=50, ipady=50)
        self.b4.config(command=lambda: self.buttonClick(4))

        self.b5 = ttk.Button(self.gameBoard, text='  ')
        self.b5.grid(row=3, column=1, sticky='snew', ipadx=50, ipady=50)
        self.b5.config(command=lambda: self.buttonClick(5))

        self.b6 = ttk.Button(self.gameBoard, text='  ')
        self.b6.grid(row=3, column=2, sticky='snew', ipadx=50, ipady=50)
        self.b6.config(command=lambda: self.buttonClick(6))

        self.b7 = ttk.Button(self.gameBoard, text='  ')
        self.b7.grid(row=4, column=0, sticky='snew', ipadx=50, ipady=50)
        self.b7.config(command=lambda: self.buttonClick(7))

        self.b8 = ttk.Button(self.gameBoard, text='  ')
        self.b8.grid(row=4, column=1, sticky='snew', ipadx=50, ipady=50)
        self.b8.config(command=lambda: self.buttonClick(8))

        self.b9 = ttk.Button(self.gameBoard, text='  ')
        self.b9.grid(row=4, column=2, sticky='snew', ipadx=50, ipady=50)
        self.b9.config(command=lambda: self.buttonClick(9))

        bquit = ttk.Button(self.gameBoard, text='Quit')
        bquit.grid(row=5, column=2, sticky='snew')
        bquit.config(command=lambda: self.quitProgram())

        p1_label = Label(self.gameBoard, text = 'Player 1 Name').grid(row=0)
        p2_label = Label(self.gameBoard, text = 'Player 2 Name').grid(row=1)

        p1_username = Entry(self.gameBoard)
        p2_username = Entry(self.gameBoard)

        p1_username.grid(row=0, column=1)
        p2_username.grid(row=1, column=1)

        submit_username = ttk.Button(self.gameBoard, text='Play Game')
        submit_username.grid(row=1, column=2)
        submit_username.config(command=lambda: submitButton())


        def submitButton():
            self.p1name = p1_username.get()
            self.p2name = p2_username.get()
            if self.machine == 'client':
                self.players_username = self.p1name
            else:
                self.players_username = self.p2name
                self.gameBoard.after(100, self.receiveMove)
            self.gameBoard.title(f'Tic Tac Toe ({self.machine}) {self.p1name}\'s Turn')
            self.last_user = self.p1name

    def quitProgram(self):
        self.skt.close()
        self.gameBoard.destroy()

    def resetGameBoard(self):
        self.b1['state'] = NORMAL
        self.b2['state'] = NORMAL
        self.b3['state'] = NORMAL
        self.b4['state'] = NORMAL
        self.b5['state'] = NORMAL
        self.b6['state'] = NORMAL
        self.b7['state'] = NORMAL
        self.b8['state'] = NORMAL
        self.b9['state'] = NORMAL

        self.b1['text'] = '  '
        self.b2['text'] = '  '
        self.b3['text'] = '  '
        self.b4['text'] = '  '
        self.b5['text'] = '  '
        self.b6['text'] = '  '
        self.b7['text'] = '  '
        self.b8['text'] = '  '
        self.b9['text'] = '  '

        self.p1 = []
        self.p2 = []

    def buttonClick(self, position):
        #when a button is clicked
        if (self.last_user == self.p1name):
            self.updateGameBoard(position, 'X')
            self.p1.append(position)
            self.gameBoard.title(f'Tic Tac Toe ({self.machine}) {self.p2name}\'s Turn')
            self.last_user = self.p2name
        elif (self.last_user == self.p2name):
             self.updateGameBoard(position, 'O')
             self.p2.append(position)
             self.gameBoard.title(f'Tic Tac Toe ({self.machine}) {self.p1name}\'s Turn')
             self.last_user = self.p1name
        self.skt.sendall(str(position).encode())
        self.isWinner()
        #when move is received over network, display on board, check again for winner
        if self.Winner == -1:       #if there is no winner
             self.gameBoard.after(100, self.receiveMove)



    def updateGameBoard(self, position, player_symbol): #update board functiion
        if position == 1:
            self.b1.config(text=player_symbol)
            self.b1['state'] = DISABLED
        elif position == 2:
            self.b2.config(text=player_symbol)
            self.b2['state'] = DISABLED
        elif position == 3:
            self.b3.config(text=player_symbol)
            self.b3['state'] = DISABLED
        elif position == 4:
            self.b4.config(text=player_symbol)
            self.b4['state'] = DISABLED
        elif position == 5:
            self.b5.config(text=player_symbol)
            self.b5['state'] = DISABLED
        elif position == 6:
            self.b6.config(text=player_symbol)
            self.b6['state'] = DISABLED
        elif position == 7:
            self.b7.config(text=player_symbol)
            self.b7['state'] = DISABLED
        elif position == 8:
            self.b8.config(text=player_symbol)
            self.b8['state'] = DISABLED
        elif position == 9:
            self.b9.config(text=player_symbol)
            self.b9['state'] = DISABLED

    def isWinner(self):
        self.gameBoard.update()
        game_running = True
        winner_exists = False

        if ((1 in self.p1) and (2 in self.p1) and (3 in self.p1)):
            self.Winner = 1
        if ((1 in self.p2) and (2 in self.p2) and (3 in self.p2)):
            self.Winner = 2
        if ((4 in self.p1) and (5 in self.p1) and (6 in self.p1)):
            self.Winner = 1
        if ((4 in self.p2) and (5 in self.p2) and (6 in self.p2)):
            self.Winner = 2
        if ((7 in self.p1) and (8 in self.p1) and (9 in self.p1)):
            self.Winner = 1
        if ((7 in self.p2) and (8 in self.p2) and (9 in self.p2)):
            self.Winner = 2


        if ((1 in self.p1) and (4 in self.p1) and (7 in self.p1)):
            self.Winner = 1
        if ((1 in self.p2) and (4 in self.p2) and (7 in self.p2)):
            self.Winner = 2
        if ((2 in self.p1) and (5 in self.p1) and (8 in self.p1)):
            self.Winner = 1
        if ((2 in self.p2) and (5 in self.p2) and (8 in self.p2)):
            self.Winner = 2
        if ((3 in self.p1) and (6 in self.p1) and (9 in self.p1)):
            self.Winner = 1
        if ((3 in self.p2) and (6 in self.p2) and (9 in self.p2)):
            self.Winner = 2

        if ((1 in self.p1) and (5 in self.p1) and (9 in self.p1)):
            self.Winner = 1
        if ((1 in self.p2) and (5 in self.p2) and (9 in self.p2)):
            self.Winner = 2
        if ((3 in self.p1) and (5 in self.p1) and (7 in self.p1)):
            self.Winner = 1
        if ((3 in self.p2) and (5 in self.p2) and (7 in self.p2)):
            self.Winner = 2

        if self.Winner == 1:
            game_running = False
            messagebox.showinfo(title='Game Over', message=f'{self.p1name} is the winner')
            winner_exists = True
            self.p1wins += 1
            self.p2losses +=1

        elif self.Winner == 2:
            game_running = False
            messagebox.showinfo(title='Game Over', message=f'{self.p2name} is the winner')
            winner_exists = True
            self.p2wins += 1
            self.p1losses +=1


        elif self.Winner == -1 and (len(self.p1) + len(self.p2)) == 9:
            self.Winner = 0 # tie = 0
            game_running = False
            messagebox.showinfo(title='Game Over', message='Tie!')

        if game_running == False:
            play_again = messagebox.askquestion(message='Would you like to play again?')
            if play_again == 'yes':
                self.resetGameBoard()
                self.p1 = []
                self.p2 = []
                self.updateGamesPlayed(1)
            elif play_again == 'no':
                self.quitProgram()
                self.printStats()

        if winner_exists == True:
            self.updateGamesPlayed(1)

    def printStats(self):
        self.stats = Tk()
        T = Text(self.stats, height=20, width=50, padx=45)
        T.pack()
        T.configure(font=('Courier', 16))
        T.insert(END, f'       Fun Times! GAME STATISTICS   \n\n Players Usernames: {self.players_username} \n\n Last User: {self.last_user} \n\n Number of Games: {self.numgames} \n\n Wins: {self.p1name}-{self.p1wins} , {self.p2name}-{self.p2wins} \n\n Losses: {self.p1name}-{self.p1losses} , {self.p2name}-{self.p2losses} \n\n Ties: {self.ties}')


    def updateGamesPlayed(self, new_games_amt):
        self.numgames += new_games_amt

    def receiveMove(self):
        opponentmove = int(self.skt.recv(1024).decode('ascii'))##
        if self.last_user == self.p1name:
            self.updateGameBoard(opponentmove, 'X')
            self.p1.append(opponentmove)
            self.gameBoard.title(f'Tic Tac Toe ({self.machine}) {self.p2name}\'s Turn')
            self.last_user = self.p2name
        elif self.last_user == self.p2name:
            self.updateGameBoard(opponentmove, 'O')
            self.p2.append(opponentmove)
            self.gameBoard.title(f'Tic Tac Toe ({self.machine}) {self.p1name}\'s Turn')
            self.last_user = self.p1name
        self.isWinner()

    def boardIsFull(self):
        if len(self.p1) and len(self.p2) == 9:
            return True

    def mainLoop(self):
        self.gameBoard.mainloop()

if __name__ == '__main__':
    b = Board()
