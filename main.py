from tkinter import *
import random

class TicTacToe:
	def __init__(self, window):
		self.window = window

		self.players = ['X', 'o']
		self.player = random.choice(self.players)
		self.buttons = [[0, 0, 0], 
				  		[0, 0, 0],
						[0, 0, 0]]
		
		self.create_widgets()

	def create_widgets(self):
		self.window.title('Tic-Tac-Toe')
		# self.window.resizable(False, False)
		self.window.configure(bg='black')

		self.label = Label(self.window, text=self.player + ' turn', font=('consolas', 40), 
					 	   bg='black', fg='white')
		self.label.pack(side='top')

		self.reset_button = Button(self.window, text='restart', font=('consolas', 20),
							 	   bg='black', fg='white', activebackground='black', activeforeground='black',
							 	   command=self.new_game)
		self.reset_button.pack(side='top')

		self.frame = Frame(self.window)
		self.frame.pack()

		for row in range(3):
			for column in range(3):
				self.buttons[row][column] = Button(self.frame, text='', font=('consolas', 40), bg='black', fg='white',
									   			   activeforeground='black', activebackground='black', width=5, 
									   			   height=2, command=lambda row=row, column=column: self.next_turn(row, column))
				self.buttons[row][column].grid(row=row, column=column)

	def next_turn(self, row, column):
		if self.buttons[row][column]['text'] == '' and self.check_winner() is False:
			
			if self.player == self.players[0]:
				self.buttons[row][column]['text'] = self.player
				
				if self.check_winner() is False:
					self.player = self.players[1]
					self.label.config(text=(self.players[1] + ' turn'))
					
				elif self.check_winner() is True:
					self.label.config(text=(self.players[0] + ' wins'))
					
				elif self.check_winner() == 'Tie':
					self.label.config(text='Tie!')
					
			else:
				self.buttons[row][column]['text'] = self.player
				
				if self.check_winner() is False:
					self.player = self.players[0]
					self.label.config(text=(self.players[0] + ' turn'))
					
				elif self.check_winner() is True:
					self.label.config(text=(self.players[1] + ' wins'))
					
				elif self.check_winner() == 'Tie':
					self.label.config(text='Tie!')
	
	def check_winner(self):
		# Check for horizontal win
		for row in range(3):
			if self.buttons[row][0]['text'] == self.buttons[row][1]['text'] == self.buttons[row][2]['text'] != '':
				self.buttons[row][0].config(bg='green')
				self.buttons[row][1].config(bg='green')
				self.buttons[row][2].config(bg='green')
				return True
		
		# Check for vertical win
		for column in range(3):
			if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == self.buttons[2][column]['text'] != '':
				self.buttons[0][column].config(bg='green')
				self.buttons[1][column].config(bg='green')
				self.buttons[2][column].config(bg='green')
				return True

		# Check for diagonal win	
		if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != '':
			self.buttons[0][0].config(bg='green')
			self.buttons[1][1].config(bg='green')
			self.buttons[2][2].config(bg='green')
			return True
			
		elif self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != '':
			self.buttons[0][2].config(bg='green')
			self.buttons[1][1].config(bg='green')
			self.buttons[2][0].config(bg='green')
			return True
		
		# Check for tie
		elif self.empty_spaces() is False:
			
			for row in range(3):
				for column in range(3):
					self.buttons[row][column].config(bg='yellow')	
			return 'Tie'
			
		else:
			return False
		
	def empty_spaces(self):
		# Check number of playable spaces left
		spaces = 9

		for row in range(3):
			for column in range(3):
				if self.buttons[row][column]['text'] != '':
					spaces -= 1
					
		if spaces == 0:
			return False
		
		else:
			return True
	
	def new_game(self):
		# Reset playing field
		self.player = random.choice(self.players)
		
		self.label.config(text=self.player + ' turn')
		
		for row in range(3):
			for column in range(3):
				self.buttons[row][column].config(text='', bg='black')

if __name__ == '__main__':	
	window = Tk()
	game = TicTacToe(window)
	window.mainloop()
