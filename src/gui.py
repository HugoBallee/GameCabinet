import tkinter as tk

def rgb2TkinterColor(r, g, b):
	red = hex(round(r*255))[2:].rjust(2, '0')
	green = hex(round(g*255))[2:].rjust(2, '0')
	blue = hex(round(b*255))[2:].rjust(2, '0')
	return f'#{red}{green}{blue}'

class Application(tk.Frame):
	def __init__(self, master=None, width=8, height=8):
		super().__init__(master)
		self.master = master
		self.width = width
		self.height = height
		self.master.bind("<Key>", self.key)
		self.master.bind("<Right>", self.rightEvent)
		self.master.bind("<Left>", self.leftEvent)
		self.master.bind("<Up>", self.upEvent)
		self.master.bind("<Down>", self.downEvent)
		self.cells = []
		self.create_widgets()

	def create_widgets(self):
		for r in range(self.height):
			for c in range(self.width):
				lbl = tk.Label(self.master,
					text=f'     ',
					borderwidth=1)
				lbl.grid(row=r, column=c)
				lbl['bg'] = f'{rgb2TkinterColor(r/(self.height-1), c/(self.width-1), 0)}'
				self.cells.append(lbl)
		for c in range(self.width):
			self.master.grid_columnconfigure(c, weight=1)

	def say_hi(self):
		print("hi there, everyone!")

	def key(self, event):
		print(f'{repr(event.char)} pressed')
	def rightEvent(self, event):
		self.cells[0]['bg'] = f'{rgb2TkinterColor(0, 0, 1)}'
		print('right pressed')
	def leftEvent(self, event):
		self.cells[32*32-1]['bg'] = f'{rgb2TkinterColor(0, 0, 1)}'
		print('left pressed')
	def upEvent(self, event):
		self.cells[31]['bg'] = f'{rgb2TkinterColor(0, 0, 1)}'
		print('up pressed')
	def downEvent(self, event):
		self.cells[32*31]['bg'] = f'{rgb2TkinterColor(0, 0, 1)}'
		print('down pressed')

root = tk.Tk()
app = Application(master=root, width=32, height=32)
app.mainloop()