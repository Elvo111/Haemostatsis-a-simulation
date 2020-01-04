from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

import random

cellquantity = 10000

# init values of the window
def window():
	app = QApplication(sys.argv)
	win = QMainWindow()
	win.setGeometry(200, 200, 800, 200)
	win.setWindowTitle("Haeomstatsis")

	win.show()
	sys.exit(app.exec_())

class platelets:
	"""to create platelets"""
	#color = (a,b,c) #orange
	def __init__(self,x,y,r,mass):
		self.radius = random.randint(1,5)
		self.mass = self.radius * self.radius

		self.x = x
		self.y = y

	#move the cell
	def move():
		pass

	#check collision with other cells
	def collision():
		pass

	#check activation of the platelet
	def aggregation():
		pass

	#draw the platelet
	def draw():
		pass



		
# Actual Simulation
def simulation():
	cells=[]

	# Generates all platlets and initalizes them
	for i in range(cellquantity):
		cells.append(platelets(x,y,r,mass))


	done = False

	#while done == False:
	
	pass


window()
