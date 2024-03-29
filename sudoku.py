#--------------------Imports del programa--------------------
"""
Aqui se realizan todos los imports que vaya a utilizar dentro del programa
Entradas: Los modulos a los que llamo
Salidas: Las funciones para los cuales los llame
Restricciones: Estan basados en la version python 3.7
"""
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import webbrowser as wb
from random import *
import pickle

memoriaFaciles=[]
memoriaIntermedios=[]
memoriaDificiles=[]


plantillasFaciles={1:[["","2","","","9","3","","1","8"],
				["","1","","","7","","6","",""],
				["7","4","","","","6","","","2"],
				["","","","","","","","","7"],
				["8","","2","","","1","5","4","9"],
				["4","","3","5","8","","","",""],
				["6","","","9","","","","2",""],
				["","","","","","","8","",""],
				["","3","7","","2","8","","","5"]],
			 2:[["5","","","","8","6","","","1"],
			 	["","","2","7","","1","6","",""],
			 	["","7","1","","","","2","5",""],
			 	["9","1","","","2","","","7",""],
			 	["3","","","1","4","5","","","6"],
			 	["","6","","","9","","","2","4"],
			 	["","5","3","","","","4","6",""],
			 	["","","8","9","","3","5","",""],
			 	["2","","","5","1","","","","7"]],
			 3:[["7","","","3","","","","",""],
			 	["","1","9","4","","","2","",""],
			 	["8","","2","","","1","3","4",""],
			 	["","2","","","","","","",""],
			 	["","","3","8","","7","5","1",""],
			 	["","4","","","1","","9","7","6"],
			 	["","8","","9","7","2","1","","3"],
			 	["9","3","","","","4","","",""],
			 	["","","6","","","5","8","",""]]}

diccFaciles={1:[["","2","","","9","3","","1","8"],
				["","1","","","7","","6","",""],
				["7","4","","","","6","","","2"],
				["","","","","","","","","7"],
				["8","","2","","","1","5","4","9"],
				["4","","3","5","8","","","",""],
				["6","","","9","","","","2",""],
				["","","","","","","8","",""],
				["","3","7","","2","8","","","5"]],
			 2:[["5","","","","8","6","","","1"],
			 	["","","2","7","","1","6","",""],
			 	["","7","1","","","","2","5",""],
			 	["9","1","","","2","","","7",""],
			 	["3","","","1","4","5","","","6"],
			 	["","6","","","9","","","2","4"],
			 	["","5","3","","","","4","6",""],
			 	["","","8","9","","3","5","",""],
			 	["2","","","5","1","","","","7"]],
			 3:[["7","","","3","","","","",""],
			 	["","1","9","4","","","2","",""],
			 	["8","","2","","","1","3","4",""],
			 	["","2","","","","","","",""],
			 	["","","3","8","","7","5","1",""],
			 	["","4","","","1","","9","7","6"],
			 	["","8","","9","7","2","1","","3"],
			 	["9","3","","","","4","","",""],
			 	["","","6","","","5","8","",""]]}


diccIntermedio={1:[["6","","","","","","","",""],
				["","1","9","","8","3","","","4"],
				["7","3","","1","","","","9",""],
				["","","","","6","","","4",""],
				["9","","","3","","","","","1"],
				["4","","","8","","9","","5",""],
				["","","8","9","","","","2",""],
				["3","","2","6","","8","","",""],
				["1","","","","4","","6","","3"]],
			 2:[["","","5","","","2","","",""],
			 	["","2","","7","3","4","","",""],
			 	["","6","","8","","","","","9"],
			 	["","9","","1","2","8","7","",""],
			 	["","","7","","","6","","","2"],
			 	["","8","4","","","3","1","",""],
			 	["","7","","3","5","","","8",""],
			 	["","","","4","","","2","",""],
			 	["5","","","","","","6","1",""]],
			 3:[["","9","","","","","5","3",""],
			 	["7","","","8","1","","","4",""],
			 	["","","","5","","","8","","7"],
			 	["","","4","","6","","","1",""],
			 	["","","","","","","","",""],
			 	["","1","","","","","7","","3"],
			 	["","","7","4","5","","9","6","2"],
			 	["9","4","","","","6","1","8",""],
			 	["","","6","","8","2","","",""]]}
plantillasIntermedio={1:[["6","","","","","","","",""],
				["","1","9","","8","3","","","4"],
				["7","3","","1","","","","9",""],
				["","","","","6","","","4",""],
				["9","","","3","","","","","1"],
				["4","","","8","","9","","5",""],
				["","","8","9","","","","2",""],
				["3","","2","6","","8","","",""],
				["1","","","","4","","6","","3"]],
			 2:[["","","5","","","2","","",""],
			 	["","2","","7","3","4","","",""],
			 	["","6","","8","","","","","9"],
			 	["","9","","1","2","8","7","",""],
			 	["","","7","","","6","","","2"],
			 	["","8","4","","","3","1","",""],
			 	["","7","","3","5","","","8",""],
			 	["","","","4","","","2","",""],
			 	["5","","","","","","6","1",""]],
			 3:[["","9","","","","","5","3",""],
			 	["7","","","8","1","","","4",""],
			 	["","","","5","","","8","","7"],
			 	["","","4","","6","","","1",""],
			 	["","","","","","","","",""],
			 	["","1","","","","","7","","3"],
			 	["","","7","4","5","","9","6","2"],
			 	["9","4","","","","6","1","8",""],
			 	["","","6","","8","2","","",""]]}

diccDificiles={1:[["","","","","","","","","9"],
				["","","","","","7","","1",""],
				["7","6","","9","","","3","","8"],
				["","","1","6","","","4","3",""],
				["","","","","","","","","6"],
				["","5","","","7","","","8",""],
				["","","3","","","1","","2",""],
				["9","1","","","","3","","",""],
				["","","","","","5","1","9",""]],
			 2:[["","6","","","1","","5","",""],
			 	["1","","","","","5","","7",""],
			 	["","9","8","","","4","","",""],
			 	["8","","","","","","","",""],
			 	["","4","","","","","","","6"],
			 	["","","","","","3","","9","1"],
			 	["9","","","3","","2","","",""],
			 	["","","7","5","","8","","","3"],
			 	["","","","1","","","2","","4"]],
			 3:[["2","","6","","","1","","",""],
			 	["9","4","","8","","","","",""],
			 	["","","","","","9","","","7"],
			 	["","","","","7","","","","1"],
			 	["3","","","","","5","4","2",""],
			 	["","1","4","","","","3","","8"],
			 	["","","1","4","9","","8","",""],
			 	["","","","","","","","","5"],
			 	["4","8","","","","","","",""]]}
plantillasDificiles={1:[["","","","","","","","","9"],
				["","","","","","7","","1",""],
				["7","6","","9","","","3","","8"],
				["","","1","6","","","4","3",""],
				["","","","","","","","","6"],
				["","5","","","7","","","8",""],
				["","","3","","","1","","2",""],
				["9","1","","","","3","","",""],
				["","","","","","5","1","9",""]],
			 2:[["","6","","","1","","5","",""],
			 	["1","","","","","5","","7",""],
			 	["","9","8","","","4","","",""],
			 	["8","","","","","","","",""],
			 	["","4","","","","","","","6"],
			 	["","","","","","3","","9","1"],
			 	["9","","","3","","2","","",""],
			 	["","","7","5","","8","","","3"],
			 	["","","","1","","","2","","4"]],
			 3:[["2","","6","","","1","","",""],
			 	["9","4","","8","","","","",""],
			 	["","","","","","9","","","7"],
			 	["","","","","7","","","","1"],
			 	["3","","","","","5","4","2",""],
			 	["","1","4","","","","3","","8"],
			 	["","","1","4","9","","8","",""],
			 	["","","","","","","","","5"],
			 	["4","8","","","","","","",""]]}

partidaActual=""
matrizActual=""
option=""

configReloj=True
horas=0
minutos=0
segundos=0
proceso=0

dificultadDePartida="Facil"
tipoDePartida="Numeros"

cargado=False
juegoIniciado=False
listaWidgets=[]

#--------------------Funcion de Jugar esto engomera toda la interfaz de jugar--------------------
def jugarMenu():
	global tipoDePartida
	global configReloj
	global horas
	global minutos
	global segundos
	global dificultadDePartida
	#----------Grid de ayuda para colocar la interfaz---------
	"""
	Este grid al cambiarse el color de White a otro que se note, se mostrara una cuadricula que es 
	la que se va a utilizar dentro del programa para ayudar a colocar todo de manera ordenada.
	Entradas: El root donde se dibuja la cuadricula
	Salidas: La cuadricula dibujada
	Restricciones: No tiene
	"""
	n=30
	for k in range(0, n):
		frameAyuda = Frame(root, width=1, height=650, bg= "#9ACD32")
		frameAyuda.grid(row= 0, column=k, rowspan=n, sticky= "NW")
		frameAyuda = Frame(root, width=650, height=1, bg= "#9ACD32")
		frameAyuda.grid(row= k, column=0, columnspan=n, sticky= "NW")



	#----------Frame del area de Juego---------
	"""
	Este frame es el que va a contener el juego con la matriz de 9x9 creada con botones
	Entradas: No recibe
	Salidas: El frame con una cuadricula de 9x9
	Restricciones: No tiene
	"""
	frameSudoku=Frame(root, bg="Grey")
	frameSudoku.grid(row=1, column=1, rowspan=18, columnspan=18, sticky="NSEW")
	nS=9
	for kS in range(0, nS):
		frameAyuda = Frame(frameSudoku, width=1, height=390, bg= "#9ACD32")
		frameAyuda.grid(row= 0, column=kS, rowspan=nS, sticky= "NW")
		frameAyuda = Frame(frameSudoku, width=390, height=1, bg= "#9ACD32")
		frameAyuda.grid(row= kS, column=0, columnspan=nS, sticky= "NW")
	
	#----------------------------Configuracion de Juego Numeros----------------------
	"""
	En caso de que el jugador decida jugar al clasico sudoku de numeros, 
	se llamara a esta funcion y colocara todo el juego segun los numeros 
	del mismo juego
	Entradas: No recibe
	Salida: Dibuja la matriz de Numeros
	Restricciones: No tiene
	"""
	def validacionGanar():
		global matrizActual
		global horas, minutos, segundos
		global dificultadDePartida

		for row in matrizActual:
			for column in row:
				if column=="":
					return False
		
		return True

	def validacionDeSudoku(fila, columna):
		"""
		Esta funcion es a la que va a validar que un numero se pueda o no se pueda poner
		en la casilla que el jugador decida hacer clickear, en caso que no se pueda se le
		avisara con un respectivo mensaje el por que no se puede.
		Entradas: La matriz actual
		Salidas: Si se puede dejara la jugada y si no marcara que no se puede
		Restricciones: No tiene
		"""	
		global matrizActual

		Xfila=True
		Xcolumna=True
		Xsubmatriz=True
		#esta es la parte que validara que el elemento no se encuentre en la fila donde se coloco
		contador=0
		for elemento in matrizActual[fila]:
			if str(elemento)==str(matrizActual[fila][columna]):
				contador+=1
		if contador>1:
			Xfila=False

		
		#esta es la parte que validara que el elemento no se encuentre en la columna donde se coloco
		contador=0
		i=0
		while True:
			try:
				if str(matrizActual[fila][columna])==str(matrizActual[i][columna]):
					contador+=1
					i+=1
				else:
					i+=1
			except IndexError:
				if contador>1:
					Xcolumna=False
				break

		#esta es la parte que validara que el elemento no se encuentre en la submatriz a la que pertenece ese elemento
		contador=0
		if fila>=0 and fila<=2:#si el elemento esta en las submatrices de la fila 0 a la 2 verificara la columna para saber exactamente en cual otra se encuentra
			if columna>=0 and columna<=2:
				for i in range(0,3):
					for k in range(0,3):
						if str(matrizActual[i][k])==str(matrizActual[fila][columna]):
							contador+=1
				if contador>1:
					Xsubmatriz=False
			elif columna>=3 and columna<=5:
				for i in range(0,3):
					for k in range(3,6):
						if str(matrizActual[i][k])==str(matrizActual[fila][columna]):
							contador+=1
				if contador>1:
					Xsubmatriz=False
			else:
				for i in range(0,3):
					for k in range(6,9):
						if str(matrizActual[i][k])==str(matrizActual[fila][columna]):
							contador+=1
				if contador>1:
					Xsubmatriz=False
		elif fila>=3 and fila<=5:#si el elemento esta en las submatrices de la fila 3 a la 5 verificara la columna para saber exactamente en cual otra se encuentra
			if columna>=0 and fila<=2:
				for i in range(3,6):
					for k in range(0,3):
						if str(matrizActual[i][k])==str(matrizActual[fila][columna]):
							contador+=1
				if contador>1:
					Xsubmatriz=False
			elif columna>=3 and columna<=5:
				for i in range(3,5):
					for k in range(3,6):
						if str(matrizActual[i][k])==str(matrizActual[fila][columna]):
							contador+=1
				if contador>1:
					Xsubmatriz=False
			else:
				for i in range(3,6):
					for k in range(6,9):
						if str(matrizActual[i][k])==str(matrizActual[fila][columna]):
							contador+=1
				if contador>1:
					Xsubmatriz=False
		else:#si el elemento esta en las submatrices de la fila 6 a la 8 verificara la columna para saber exactamente en cual otra se encuentra
			if columna>=0 and fila<=2:
				for i in range(6,9):
					for k in range(0,3):
						if str(matrizActual[i][k])==str(matrizActual[fila][columna]):
							contador+=1
				if contador>1:
					Xsubmatriz=False
			elif columna>=3 and columna<=5:
				for i in range(6,9):
					for k in range(3,6):
						if str(matrizActual[i][k])==str(matrizActual[fila][columna]):
							contador+=1
				if contador>1:
					Xsubmatriz=False
			else:
				for i in range(6,9):
					for k in range(6,9):
						if str(matrizActual[i][k])==str(matrizActual[fila][columna]):
							contador+=1
				if contador>1:
					Xsubmatriz=False
		if Xfila==False:
			messagebox.showerror("ERROR", "El elemento ya se encuentra dentro de la fila")
			return False
		elif Xcolumna==False:
			messagebox.showerror("ERROR", "El elemento ya se encuentra dentro de la columna")
			return False
		elif Xsubmatriz==False:
			messagebox.showerror("ERROR", "El elemento ya se encuentra dentro de la submatriz")
			return False
		else:
			return True


	def configuracionNumeros():
		global cargado
		global tipoDePartida
		def modificaMatrizNumeros(widget):
			"""
			Esta funcion coloca el texto en cada boton al que se le haga click
			dependiendo de lo que el usuario quiera seleccionar, ademas de actualizar
			la matriz de la partida actual
			Entradas: El boton seleccionado
			Salidas: La matriz actual actualizada y el texto en los botones
			Restricciones: No tiene
			"""
			global matrizActual
			global option
			global juegoIniciado
			global partidaActual
			global listaWidgets

			if option=="":
				messagebox.showerror("ERROR", "Falta que seleccione el elemento")
			else:
				x, y=widget.position
				texto=widget.cget("text")
				listaWidgets.append(widget)
				if option==texto:
					widget.config(text="")
					matrizActual[x][y]=""
				else:
					widget.config(text=option)
					matrizActual[x][y]=option
					verificacion=validacionDeSudoku(x, y)
					if verificacion==True:
						validaGane=validacionGanar()
						if validaGane==True:
							messagebox.showinfo("FELICITACIONES", "Excelente! Juego completado")
							jugador=jugadoresTOP10(EntryNombreJugador.get(), "{}:{}:{}".format(horas, minutos, segundos), dificultadDePartida)
						else:
							pass
					else:
						widget.config(text="")
						matrizActual[x][y]=""
			
		def creaSudokuFaciles():#Crea la matriz si el usuario decide crear una partida facil
			global matrizActual
			global memoriaFaciles
			global partidaActual

			if partidaActual=="":
				partida=randint(1,3)
				contador=0
				while partida in memoriaFaciles:
					partida=randint(1,3)
					contador+=1
					if contador==10:
						memoriaFaciles=[]
						creaSudokuFaciles()
				partidaActual=partida
			else:
				partida=partidaActual
			memoriaFaciles.append(partida)
			matrizActual=diccFaciles[partida]

			i=0
			k=0
			for linea in plantillasFaciles[partida]:#essta funcion sirve para dibujar la matriz, desde 0 ya que esta funcion solo realiza eso
				for elemento in linea:
					if elemento=="":
						botonSudoku=Button(frameSudoku)
						botonSudoku.config(command=lambda widget=botonSudoku: modificaMatrizNumeros(widget))
						botonSudoku.grid(row=i, column=k, sticky="NSEW")
						botonSudoku.position=(i, k)
						k+=1
					else:
						botonSudoku=Button(frameSudoku, text=plantillasFaciles[partida][i][k], state="disable").grid(row=i, column=k, sticky="NSEW")
						k+=1
				i+=1
				k=0

		def creaSudokuIntermedio():#Crea la matriz si el usuario decide crear una partida intermedia
			global matrizActual
			global memoriaIntermedios
			global partidaActual

			if partidaActual=="":
				partida=randint(1,3)
				contador=0
				while partida in memoriaIntermedios:
					partida=randint(1,3)
					contador+=1
					if contador==10:
						memoriaIntermedios=[]
						creaSudokuIntermedio()
				partidaActual=partida
			else:
				partida=partidaActual
			memoriaIntermedios.append(partida)
			matrizActual=diccIntermedio[partida]
			
			i=0
			k=0
			for linea in plantillasIntermedio[partida]:
				for elemento in linea:
					if elemento=="":
						botonSudoku=Button(frameSudoku)
						botonSudoku.config(command=lambda widget=botonSudoku: modificaMatrizNumeros(widget))
						botonSudoku.grid(row=i, column=k, sticky="NSEW")
						botonSudoku.position=(i, k)
						k+=1
					else:
						botonSudoku=Button(frameSudoku, text=plantillasIntermedio[partida][i][k], state="disable").grid(row=i, column=k, sticky="NSEW")
						k+=1
				i+=1
				k=0

		def creaSudokuDificiles():#crea la matriz si el usuario decide crear una partida dificil
			global matrizActual
			global memoriaDificiles
			global partidaActual
			global dificultadDePartida

			if partidaActual=="":
				partida=randint(1,3)
				contador=0
				while partida in memoriaDificiles:
					partida=randint(1,3)
					contador+=1
					if contador==10:
						memoriaDificiles=[]
						creaSudokuDificiles()
				partidaActual=partida
			else:
				partida=partidaActual
			memoriaDificiles.append(partida)
			matrizActual=diccDificiles[partida]
			
			i=0
			k=0
			for linea in plantillasDificiles[partida]:
				for elemento in linea:
					if elemento=="":
						botonSudoku=Button(frameSudoku)
						botonSudoku.config(command=lambda widget=botonSudoku: modificaMatrizNumeros(widget))
						botonSudoku.grid(row=i, column=k, sticky="NSEW")
						botonSudoku.position=(i, k)
						k+=1
					else:
						botonSudoku=Button(frameSudoku, text=plantillasDificiles[partida][i][k], state="disable").grid(row=i, column=k, sticky="NSEW")
						k+=1
				i+=1
				k=0

		#--------------------Botones de Juego Numeros-----------------
		"""
		Estos son los botones que el jugador va a tener para poder jugar al sudoku,
		estos botones son los que se utilizaran en caso que el jugador desee jugar
		al clasico sudoku con numeros
		Entradas: No recibe
		Salidas: Los botones de juego
		Restricciones: No tiene
		"""
		def colocaOptionNumeros(widget):
			global option
			global juegoIniciado

			if juegoIniciado==False:
				messagebox.showerror("ERROR", "Debe iniciar el juego antes de poder jugar")
			else:
				option=widget["text"]

		def botonesNumeros():
			f=1
			k1=22
			k2=24
			n=1
			for i in range(1,10):
				if n==1:
					boton=Button(root, text=i)
					boton.config(command=lambda widget=boton: colocaOptionNumeros(widget))
					boton.grid(row=f, column=k1, rowspan=2, columnspan=4, sticky="NSEW")
					f+=2
					n-=1
				else:
					boton=Button(root, text=i)
					boton.config(command=lambda widget=boton: colocaOptionNumeros(widget))
					boton.grid(row=f, column=k2, rowspan=2, columnspan=4, sticky="NSEW")
					f+=2
					n+=1

		def dibujaMatrizGuardada():
			global matrizActual
			global nombreJugador
			global partidaActual
			global dificultadDePartida

			if dificultadDePartida=="Facil":
				i=0
				k=0
				for linea in matrizActual:#esta funcion sirve para dibujar la matriz, desde la partida guardada
					for elemento in linea:
						if elemento=="" or elemento!=plantillasFaciles[partidaActual][i][k]:
							botonSudoku=Button(frameSudoku)
							botonSudoku.config(text=matrizActual[i][k], command=lambda widget=botonSudoku: modificaMatrizNumeros(widget))
							botonSudoku.grid(row=i, column=k, sticky="NSEW")
							botonSudoku.position=(i, k)
							k+=1
						else:
							botonSudoku=Button(frameSudoku, text=plantillasFaciles[partidaActual][i][k], state="disable").grid(row=i, column=k, sticky="NSEW")
							k+=1
					i+=1
					k=0
			elif dificultadDePartida=="Intermedio":
				i=0
				k=0
				for linea in matrizActual:#esta funcion sirve para dibujar la matriz, desde la partida guardada
					for elemento in linea:
						if elemento=="" or elemento!=plantillasIntermedio[partidaActual][i][k]:
							botonSudoku=Button(frameSudoku)
							botonSudoku.config(command=lambda widget=botonSudoku: modificaMatrizNumeros(widget))
							botonSudoku.config(text=matrizActual[i][k])
							botonSudoku.grid(row=i, column=k, sticky="NSEW")
							botonSudoku.position=(i, k)
							k+=1
						else:
							botonSudoku=Button(frameSudoku, text=plantillasIntermedio[partidaActual][i][k], state="disable").grid(row=i, column=k, sticky="NSEW")
							k+=1
					i+=1
					k=0
			else:
				i=0
				k=0
				for linea in matrizActual:#esta funcion sirve para dibujar la matriz, desde la partida guardada
					for elemento in linea:
						if elemento=="" or elemento!=plantillasDificiles[partidaActual][i][k]:
							botonSudoku=Button(frameSudoku)
							botonSudoku.config(command=lambda widget=botonSudoku: modificaMatrizNumeros(widget))
							botonSudoku.config(text=matrizActual[i][k])
							botonSudoku.grid(row=i, column=k, sticky="NSEW")
							botonSudoku.position=(i, k)
							k+=1
						else:
							botonSudoku=Button(frameSudoku, text=plantillasDificiles[partidaActual][i][k], state="disable").grid(row=i, column=k, sticky="NSEW")
							k+=1
					i+=1
					k=0

		if cargado==False:
			if dificultadDePartida=="Facil":
				creaSudokuFaciles()
			elif dificultadDePartida=="Intermedio":
				creaSudokuIntermedio()
			else:
				creaSudokuDificiles()
			botonesNumeros()
		else:
			dibujaMatrizGuardada()

	#----------------------------Configuracion de Juego Letras----------------------
	"""
	En caso de que el jugador decida jugar con una de las modificaciones
	como lo es jugar con Letras en vez de numeros, se llamara a esta funcion 
	y colocara todo el juego segun las letras del juego
	Entradas: No recibe
	Salida: Dibuja la matriz de Letras
	Restricciones: No tiene
	"""
	def configuracionLetras():
		global cargado
		global tipoDePartida
		def modificaMatrizLetras(widget):
			"""
			Esta funcion coloca el texto en cada boton al que se le haga click
			dependiendo de lo que el usuario quiera seleccionar, ademas de actualizar
			la matriz de la partida actual
			Entradas: El boton seleccionado
			Salidas: La matriz actual actualizada y el texto en los botones
			Restricciones: No tiene
			"""
			global matrizActual
			global option

			if option=="":
				messagebox.showerror("ERROR", "Falta que seleccione el elemento")
			else:
				listaLetras=["","A","B","C","D","E","F","G","H","I"]
				x, y=widget.position
				texto=listaLetras.index(widget.cget("text"))
				if option==texto:
					widget.config(text="")
					matrizActual[x][y]=""
				else:
					widget.config(text=listaLetras[option])
					matrizActual[x][y]=option
					verificacion=validacionDeSudoku(x, y)
					if verificacion==True:
						pass
					else:
						widget.config(text="")
						matrizActual[x][y]=""
				

		def creaSudokuFaciles():#Crea la matriz si el usuario decide crear una partida facil
			global matrizActual
			global memoriaFaciles
			global partidaActual

			if partidaActual=="":
				partida=randint(1,3)
				contador=0
				while partida in memoriaFaciles:
					partida=randint(1,3)
					contador+=1
					if contador==10:
						memoriaFaciles=[]
						creaSudokuFaciles()
				partidaActual=partida
			else:
				partida=partidaActual
			memoriaFaciles.append(partida)
			matrizActual=diccFaciles[partida]
			listaLetras=["","A","B","C","D","E","F","G","H","I"]

			i=0
			k=0
			for linea in plantillasFaciles[partida]:#essta funcion sirve para dibujar la matriz, desde 0 ya que esta funcion solo realiza eso
				for elemento in linea:
					if elemento=="":
						botonSudoku=Button(frameSudoku)
						botonSudoku.config(command=lambda widget=botonSudoku: modificaMatrizLetras(widget))
						botonSudoku.grid(row=i, column=k, sticky="NSEW")
						botonSudoku.position=(i, k)
						k+=1
					else:
						botonSudoku=Button(frameSudoku, text=listaLetras[int(plantillasFaciles[partida][i][k])], state="disable").grid(row=i, column=k, sticky="NSEW")
						k+=1
				i+=1
				k=0

		def creaSudokuIntermedio():#Crea la matriz si el usuario decide crear una partida intermedio
			global matrizActual
			global memoriaIntermedios
			global partidaActual

			if partidaActual=="":
				partida=randint(1,3)
				contador=0
				while partida in memoriaIntermedios:
					partida=randint(1,3)
					contador+=1
					if contador==10:
						memoriaIntermedios=[]
						creaSudokuFaciles()
				partidaActual=partida
			else:
				partida=partidaActual
			memoriaIntermedios.append(partida)
			matrizActual=diccIntermedio[partida]
			listaLetras=["","A","B","C","D","E","F","G","H","I"]

			i=0
			k=0
			for linea in plantillasIntermedio[partida]:#essta funcion sirve para dibujar la matriz, desde 0 ya que esta funcion solo realiza eso
				for elemento in linea:
					if elemento=="":
						botonSudoku=Button(frameSudoku)
						botonSudoku.config(command=lambda widget=botonSudoku: modificaMatrizLetras(widget))
						botonSudoku.grid(row=i, column=k, sticky="NSEW")
						botonSudoku.position=(i, k)
						k+=1
					else:
						botonSudoku=Button(frameSudoku, text=listaLetras[int(plantillasIntermedio[partida][i][k])], state="disable").grid(row=i, column=k, sticky="NSEW")
						k+=1
				i+=1
				k=0

		def creaSudokuDificiles():#Crea la matriz si el usuario decide crear una partida dificil
			global matrizActual
			global memoriaDificiles
			global partidaActual

			if partidaActual=="":
				partida=randint(1,3)
				contador=0
				while partida in memoriaDificiles:
					partida=randint(1,3)
					contador+=1
					if contador==10:
						memoriaDificiles=[]
						creaSudokuFaciles()
				partidaActual=partida
			else:
				partida=partidaActual
			memoriaDificiles.append(partida)
			matrizActual=diccDificiles[partida]
			listaLetras=["","A","B","C","D","E","F","G","H","I"]

			i=0
			k=0
			for linea in plantillasDificiles[partida]:#essta funcion sirve para dibujar la matriz, desde 0 ya que esta funcion solo realiza eso
				for elemento in linea:
					if elemento=="":
						botonSudoku=Button(frameSudoku)
						botonSudoku.config(command=lambda widget=botonSudoku: modificaMatrizLetras(widget))
						botonSudoku.grid(row=i, column=k, sticky="NSEW")
						botonSudoku.position=(i, k)
						k+=1
					else:
						botonSudoku=Button(frameSudoku, text=listaLetras[int(plantillasDificiles[partida][i][k])], state="disable").grid(row=i, column=k, sticky="NSEW")
						k+=1
				i+=1
				k=0

		#--------------------Botones de Juego Letras-----------------
		"""
		Estos son los botones que el jugador va a tener para poder jugar al sudoku,
		estos botones son los que se utilizaran en caso que el jugador desee jugar
		con letras dentro del Sudoku
		Entradas: No recibe
		Salidas: Los botones de juego
		Restricciones: No tiene
		"""
		def colocaOptionLetras(widget):
			global option

			if juegoIniciado==False:
				messagebox.showerror("ERROR", "Debe iniciar el juego antes de poder jugar")
			else:
				listaLetras=["","A","B","C","D","E","F","G","H","I"]
				option=listaLetras.index(widget["text"])

		def botonesLetras():
			f=1
			k1=22
			k2=24
			n=1
			listaLetras=["","A","B","C","D","E","F","G","H","I"]
			
			for i in range(1,10):
				if n==1:
					boton=Button(root, text=listaLetras[i])
					boton.config(command=lambda widget=boton: colocaOptionLetras(widget))
					boton.grid(row=f, column=k1, rowspan=2, columnspan=4, sticky="NSEW")
					f+=2
					n-=1
				else:
					boton=Button(root, text=listaLetras[i])
					boton.config(command=lambda widget=boton: colocaOptionLetras(widget))
					boton.grid(row=f, column=k2, rowspan=2, columnspan=4, sticky="NSEW")
					f+=2
					n+=1

		def dibujaMatrizGuardada():
			global matrizActual
			global nombreJugador
			global partidaActual
			global dificultadDePartida
			global partidaActual

			listaLetras=["","A","B","C","D","E","F","G","H","I"]
			if dificultadDePartida=="Facil":
				i=0
				k=0
				for linea in matrizActual:#esta funcion sirve para dibujar la matriz, desde la partida guardada
					for elemento in linea:
						if elemento=="":
							botonSudoku=Button(frameSudoku)
							botonSudoku.config(text="", command=lambda widget=botonSudoku: modificaMatrizLetras(widget))
							botonSudoku.grid(row=i, column=k, sticky="NSEW")
							botonSudoku.position=(i, k)
							k+=1
						elif elemento!=plantillasFaciles[partidaActual][i][k]:
							botonSudoku=Button(frameSudoku)
							botonSudoku.config(text=listaLetras[int(matrizActual[i][k])], command=lambda widget=botonSudoku: modificaMatrizLetras(widget))
							botonSudoku.grid(row=i, column=k, sticky="NSEW")
							botonSudoku.position=(i, k)
							k+=1
						else:
							botonSudoku=Button(frameSudoku, text=listaLetras[int(plantillasFaciles[partidaActual][i][k])], state="disable").grid(row=i, column=k, sticky="NSEW")
							k+=1
					i+=1
					k=0
			elif dificultadDePartida=="Intermedio":
				i=0
				k=0
				for linea in matrizActual:#esta funcion sirve para dibujar la matriz, desde la partida guardada
					for elemento in linea:
						if elemento=="" or elemento!=plantillasIntermedio[partidaActual][i][k]:
							botonSudoku=Button(frameSudoku)
							botonSudoku.config(command=lambda widget=botonSudoku: modificaMatrizLetras(widget))
							botonSudoku.config(text=listaLetras[int(matrizActual[i][k])])
							botonSudoku.grid(row=i, column=k, sticky="NSEW")
							botonSudoku.position=(i, k)
							k+=1
						else:
							botonSudoku=Button(frameSudoku, text=listaLetras[int(plantillasIntermedio[partidaActual][i][k])], state="disable").grid(row=i, column=k, sticky="NSEW")
							k+=1
					i+=1
					k=0
			else:
				i=0
				k=0
				for linea in matrizActual:#esta funcion sirve para dibujar la matriz, desde la partida guardada
					for elemento in linea:
						if elemento=="" or elemento!=plantillasDificiles[partidaActual][i][k]:
							botonSudoku=Button(frameSudoku)
							botonSudoku.config(command=lambda widget=botonSudoku: modificaMatrizLetras(widget))
							botonSudoku.config(text=listaLetras[matrizActual[i][k]])
							botonSudoku.grid(row=i, column=k, sticky="NSEW")
							botonSudoku.position=(i, k)
							k+=1
						else:
							botonSudoku=Button(frameSudoku, text=listaLetras[plantillasDificiles[partidaActual][i][k]], state="disable").grid(row=i, column=k, sticky="NSEW")
							k+=1
					i+=1
					k=0

		if cargado==False:
			if dificultadDePartida=="Facil":
				creaSudokuFaciles()
			elif dificultadDePartida=="Intermedio":
				creaSudokuIntermedio()
			else:
				creaSudokuDificiles()
			botonesLetras()
		else:
			dibujaMatrizGuardada()

	#----------------------------Configuracion de Juego Colores----------------------
	"""
	En caso de que el jugador decida jugar con una de las modificaciones
	como lo es jugar con colores en vez de numeros, se llamara a esta funcion 
	y colocara todo el juego segun los colores
	Entradas: No recibe
	Salida: Dibuja la matriz de colores
	Restricciones: No tiene
	"""
	def configuracionColores():
		global cargado
		global tipoDePartida
		def modificaMatrizColores(widget):
			"""
			Esta funcion coloca el color en cada boton al que se le haga click
			dependiendo de lo que el usuario quiera seleccionar, ademas de actualizar
			la matriz de la partida actual
			Entradas: El boton seleccionado
			Salidas: La matriz actual actualizada y el color en los botones
			Restricciones: No tiene
			"""
			global matrizActual
			global option

			if option=="":
				messagebox.showerror("ERROR", "Falta que seleccione el elemento")
			else:
				listaColores=["SystemButtonFace","Blue","Light Grey","#ffa502","Light Green","Brown","Red","Yellow","Purple","Black"]
				x, y=widget.position
				texto=listaColores.index(widget.cget("bg"))
				if option==texto:
					widget.config(bg="SystemButtonFace")
					matrizActual[x][y]=""
				else:
					widget.config(bg=listaColores[option])
					matrizActual[x][y]=option
					verificacion=validacionDeSudoku(x, y)
					if verificacion==True:
						pass
					else:
						widget.config(bg="SystemButtonFace")
						matrizActual[x][y]=""
			
		def creaSudokuFaciles():#Crea la matriz si el usuario decide crear una partida facil
			global matrizActual
			global memoriaFaciles
			global partidaActual

			if partidaActual=="":
				partida=randint(1,3)
				contador=0
				while partida in memoriaFaciles:
					partida=randint(1,3)
					contador+=1
					if contador==10:
						memoriaFaciles=[]
						creaSudokuFaciles()
				partidaActual=partida
			else:
				partida=partidaActual
			memoriaFaciles.append(partida)
			matrizActual=diccFaciles[partida]
			listaColores=["SystemButtonFace","Blue","Light Grey","#ffa502","Light Green","Brown","Red","Yellow","Purple","Black"]

			i=0
			k=0
			for linea in plantillasFaciles[partida]:
				for elemento in linea:
					if elemento=="":
						botonSudoku=Button(frameSudoku)
						botonSudoku.config(command=lambda widget=botonSudoku: modificaMatrizColores(widget))
						botonSudoku.grid(row=i, column=k, sticky="NSEW")
						botonSudoku.position=(i, k)
						k+=1
					else:
						botonSudoku=Button(frameSudoku, bg=listaColores[int(plantillasFaciles[partida][i][k])], state="disable").grid(row=i, column=k, sticky="NSEW")
						k+=1
				i+=1
				k=0

		def creaSudokuIntermedio():#Crea la matriz si el usuario decide crear una partida intermedio
			global matrizActual
			global memoriaDificiles
			global partidaActual

			if partidaActual=="":
				partida=randint(1,3)
				contador=0
				while partida in memoriaDificiles:
					partida=randint(1,3)
					contador+=1
					if contador==10:
						memoriaDificiles=[]
						creaSudokuFaciles()
				partidaActual=partida
			else:
				partida=partidaActual
			memoriaDificiles.append(partida)
			matrizActual=diccIntermedio[partida]
			listaColores=["SystemButtonFace","Blue","Light Grey","#ffa502","Light Green","Brown","Red","Yellow","Purple","Black"]

			i=0
			k=0
			for linea in plantillasIntermedio[partida]:
				for elemento in linea:
					if elemento=="":
						botonSudoku=Button(frameSudoku)
						botonSudoku.config(command=lambda widget=botonSudoku: modificaMatrizColores(widget))
						botonSudoku.grid(row=i, column=k, sticky="NSEW")
						botonSudoku.position=(i, k)
						k+=1
					else:
						botonSudoku=Button(frameSudoku, bg=listaColores[int(plantillasIntermedio[partida][i][k])], state="disable").grid(row=i, column=k, sticky="NSEW")
						k+=1
				i+=1
				k=0

		def creaSudokuDificiles():#Crea la matriz si el usuario decide crear una partida dificil
			global matrizActual
			global memoriaDificiles
			global partidaActual

			if partidaActual=="":
				partida=randint(1,3)
				contador=0
				while partida in memoriaDificiles:
					partida=randint(1,3)
					contador+=1
					if contador==10:
						memoriaDificiles=[]
						creaSudokuFaciles()
				partidaActual=partida
			else:
				partida=partidaActual
			memoriaDificiles.append(partida)
			matrizActual=diccDificiles[partida]
			listaColores=["SystemButtonFace","Blue","Light Grey","#ffa502","Light Green","Brown","Red","Yellow","Purple","Black"]

			i=0
			k=0
			for linea in plantillasDificiles[partida]:
				for elemento in linea:
					if elemento=="":
						botonSudoku=Button(frameSudoku)
						botonSudoku.config(command=lambda widget=botonSudoku: modificaMatrizColores(widget))
						botonSudoku.grid(row=i, column=k, sticky="NSEW")
						botonSudoku.position=(i, k)
						k+=1
					else:
						botonSudoku=Button(frameSudoku, bg=listaColores[int(plantillasDificiles[partida][i][k])], state="disable").grid(row=i, column=k, sticky="NSEW")
						k+=1
				i+=1
				k=0

		#--------------------Botones de Juego Letras-----------------
		"""
		Estos son los botones que el jugador va a tener para poder jugar al sudoku,
		estos botones son los que se utilizaran en caso que el jugador desee jugar
		con colores dentro del Sudoku
		Entradas: No recibe
		Salidas: Los botones de juego
		Restricciones: No tiene
		"""
		def colocaOptionColores(widget):
			global option
			global juegoIniciado

			if juegoIniciado==False:
				messagebox.showerror("ERROR", "Debe iniciar el juego antes de poder jugar")
			else:
				listaColores=["SystemButtonFace","Blue","Light Grey","#ffa502","Light Green","Brown","Red","Yellow","Purple","Black"]
				option=listaColores.index(widget["bg"])

		def botonesColores():
			f=1
			k1=22
			k2=24
			n=1
			listaColores=["SystemButtonFace","Blue","Light Grey","#ffa502","Light Green","Brown","Red","Yellow","Purple","Black"]
			
			for i in range(1,10):
				if n==1:
					boton=Button(root, bg=listaColores[i])
					boton.config(command=lambda widget=boton: colocaOptionColores(widget))
					boton.grid(row=f, column=k1, rowspan=2, columnspan=4, sticky="NSEW")
					f+=2
					n-=1
				else:
					boton=Button(root, bg=listaColores[i])
					boton.config(command=lambda widget=boton: colocaOptionColores(widget))
					boton.grid(row=f, column=k2, rowspan=2, columnspan=4, sticky="NSEW")
					f+=2
					n+=1

		def dibujaMatrizGuardada():
			global matrizActual
			global nombreJugador
			global partidaActual
			global dificultadDePartida
			global partidaActual

			listaColores=["SystemButtonFace","Blue","Light Grey","#ffa502","Light Green","Brown","Red","Yellow","Purple","Black"]
			if dificultadDePartida=="Facil":
				i=0
				k=0
				for linea in matrizActual:#esta funcion sirve para dibujar la matriz, desde la partida guardada
					for elemento in linea:
						if elemento=="":
							botonSudoku=Button(frameSudoku)
							botonSudoku.config(bg="SystemButtonFace", command=lambda widget=botonSudoku: modificaMatrizColores(widget))
							botonSudoku.grid(row=i, column=k, sticky="NSEW")
							botonSudoku.position=(i, k)
							k+=1
						elif elemento!=plantillasFaciles[partidaActual][i][k]:
							botonSudoku=Button(frameSudoku)
							botonSudoku.config(bg=listaColores[int(matrizActual[i][k])], command=lambda widget=botonSudoku: modificaMatrizColores(widget))
							botonSudoku.grid(row=i, column=k, sticky="NSEW")
							botonSudoku.position=(i, k)
							k+=1
						else:
							botonSudoku=Button(frameSudoku, bg=listaColores[int(plantillasFaciles[partidaActual][i][k])], state="disable").grid(row=i, column=k, sticky="NSEW")
							k+=1
					i+=1
					k=0
			elif dificultadDePartida=="Intermedio":
				i=0
				k=0
				for linea in matrizActual:#esta funcion sirve para dibujar la matriz, desde la partida guardada
					for elemento in linea:
						if elemento=="":
							botonSudoku=Button(frameSudoku)
							botonSudoku.config(bg="SystemButtonFace", command=lambda widget=botonSudoku: modificaMatrizColores(widget))
							botonSudoku.grid(row=i, column=k, sticky="NSEW")
							botonSudoku.position=(i, k)
							k+=1
						elif elemento!=plantillasIntermedio[partidaActual][i][k]:
							botonSudoku=Button(frameSudoku)
							botonSudoku.config(bg=listaColores[int(matrizActual[i][k])], command=lambda widget=botonSudoku: modificaMatrizLetras(widget))
							botonSudoku.grid(row=i, column=k, sticky="NSEW")
							botonSudoku.position=(i, k)
							k+=1
						else:
							botonSudoku=Button(frameSudoku, bg=listaColores[int(plantillasIntermedio[partidaActual][i][k])], state="disable").grid(row=i, column=k, sticky="NSEW")
							k+=1
					i+=1
					k=0
			else:
				i=0
				k=0
				for linea in matrizActual:#esta funcion sirve para dibujar la matriz, desde la partida guardada
					for elemento in linea:
						if elemento=="":
							botonSudoku=Button(frameSudoku)
							botonSudoku.config(bg="SystemButtonFace", command=lambda widget=botonSudoku: modificaMatrizColores(widget))
							botonSudoku.grid(row=i, column=k, sticky="NSEW")
							botonSudoku.position=(i, k)
							k+=1
						elif elemento!=plantillasDificiles[partidaActual][i][k]:
							botonSudoku=Button(frameSudoku)
							botonSudoku.config(bg=listaColores[int(matrizActual[i][k])], command=lambda widget=botonSudoku: modificaMatrizLetras(widget))
							botonSudoku.grid(row=i, column=k, sticky="NSEW")
							botonSudoku.position=(i, k)
							k+=1
						else:
							botonSudoku=Button(frameSudoku, bg=listaColores[int(plantillasDificiles[partidaActual][i][k])], state="disable").grid(row=i, column=k, sticky="NSEW")
							k+=1
					i+=1
					k=0

		if cargado==False:
			if dificultadDePartida=="Facil":
				creaSudokuFaciles()
			elif dificultadDePartida=="Intermedio":
				creaSudokuIntermedio()
			else:
				creaSudokuDificiles()
			botonesColores()
		else:
			dibujaMatrizGuardada()

	if tipoDePartida=="Numeros":
		configuracionNumeros()
	elif tipoDePartida=="Letras":
		configuracionLetras()
	else:
		configuracionColores()

	#----------Boton y funcion de Borrar Jugada---------
	"""
	Entradas: No recibe
	Salidas: Despliega el boton de borrar Jugada dentro del root
	Restricciones: No tiene
	"""
	def borrarJugada():
		"""
		Esta funcion sirve para hacer un tipo de undo a la ultima jugada que se ha hecho,
		de esta forma va a devolver a la anterior jugada
		Entradas: Recibe el evento del click del boton
		Salidas: Elimina la ultima jugada que se hizo
		Restricciones: No tiene
		"""
		global listaWidgets
		global matrizActual

		if juegoIniciado==True:
			if listaWidgets==[]:
				messagebox.showerror("ERROR", "No hay mas jugadas para eliminar")
			else:
				boton=listaWidgets[-1]
				boton.config(text="")
				x, y=boton.position
				matrizActual[x][y]=""
				listaWidgets.pop()
		else:
			messagebox.showerror("ERROR", "El juego no ha iniciado")

	botonBorrarJugada=Button(root, bg="#6B8E23", text="Borrar\nJugada", font="Arial, 12", fg="White", command=borrarJugada).grid(row=20, column=7, rowspan=2, columnspan=4, sticky="NSEW")
	
	#----------Boton y funcion de Terminar---------
	"""
	Entradas: No recibe
	Salidas: Despliega el boton de terminar dentro del root
	Restricciones: No tiene
	"""
	def terminar():
		"""
		Esta funcion sirve para dar por finalizado el juego en el momento que el usuario lo desee,
		se le va a preguntar 
		Entradas: Recibe el evento del click del boton
		Salidas: Empieza a correr el reloj y permite al jugador jugar
		Restricciones: No tiene
		"""
		global juegoIniciado
		global partidaActual

		if juegoIniciado==True:
			verifica=messagebox.askyesno("ALERTA", "Seguro que desea terminar el juego?")
			if verifica==True:
				juegoIniciado=False
				partidaActual=""
				jugarMenu()
			else:
				pass
		else:
			messagebox.showerror("ERROR","No se ha iniciado el juego")

	botonTerminar=Button(root, bg="#008000", text="Terminar\nJuego", font="Arial, 12", fg="White", command=terminar).grid(row=20, column=13, rowspan=2, columnspan=4, sticky="NSEW")
	
	#----------Boton y funcion de Borrar Juego---------
	"""
	Entradas: No recibe
	Salidas: Despliega el boton de borrar juego dentro del root
	Restricciones: No tiene
	"""
	def borrarJuego():
		global juegoIniciado
		global partidaActual

		if juegoIniciado==True:
			verifica=messagebox.askyesno("ALERTA", "Seguro que desea borrar el juego?")
			if verifica==True:
				juegoIniciado=False
				jugarMenu()
			else:
				pass
		else:
			messagebox.showerror("ERROR", "No se ha iniciado el juego")

	botonBorrarJuego=Button(root, bg="#6B8E23", text="Borrar\nJuego", font="Arial, 12", fg="White", command=borrarJuego).grid(row=20, column=19, rowspan=2, columnspan=4, sticky="NSEW")
	
	#----------Boton y funcion de Top 10---------
	"""
	Entradas: No recibe
	Salidas: Despliega el boton de top 10 dentro del root
	Restricciones: No tiene
	"""
	def top10():
		class jugadoresTOP10():
			"""
			Esta es la clase que va a mantener y recibir a los jugadores 
			en forma de POO, cada jugador va a tener de caracteristicas:
			un nombre, un tiempo y una dificultad y el programa los debe
			organizar y ordenar.
			"""
			def __init__(self, n, t, d):
				self.nombre=n
				self.tiempo=t
				self.dificultad=d

			def asignaTOP(self):
				if self.dificultad=="Facil":
					listaFaciles.append((self.nombre, self.tiempo))
				elif self.dificultad=="Intermedio":
					listaIntermedio.append((self.nombre, self.tiempo))
				else:
					listaDificiles.append((self.nombre, self.tiempo))

		def topFacil():
			"""
			Esta funcion se encarga e crear el topLevel del Top para la
			dificultad facil, junto con los jugadores creados de objetos
			y sus tiempos.
			Entradas: El evento del boton
			Salidas: El topLevel
			Restricciones: No tiene
			"""
			ventanaFacil=Toplevel()
			ventanaFacil.geometry("400x500")
			ventanaFacil.title("Nivel Facil")
			ventanaFacil.config(bg="#9ACD32")
			def creaTop():
				archivo=open("sudoku2019top10.dat", "rb")
				n=14
				for k in range(0,n):
					frameAyuda = Frame(ventanaFacil, width=1, height=500, bg= "#9ACD32")
					frameAyuda.grid(row= 0, column=k, rowspan=n, sticky= "NW")
					frameAyuda = Frame(ventanaFacil, width=400, height=1, bg= "#9ACD32")
					frameAyuda.grid(row= k, column=0, columnspan=n, sticky= "NW")
				labelNOMBRETOP=Label(ventanaFacil, bg="#9ACD32", text="JUGADOR", font="Arial, 14").grid(row=0, column=0, columnspan=7, rowspan=2, sticky="NSEW")
				labelTIEMPOTOP=Label(ventanaFacil, bg="#9ACD32", text="TIEMPO", font="Arial, 14").grid(row=0, column=7, columnspan=7, rowspan=2, sticky="NSEW")
				fila=2
				while True:
					try:
						jugador=pickle.load(archivo)
						Label(ventanaFacil, bg="#9ACD32", text=jugador, font="Arial, 14").grid(row=fila, column=0, columnspan=14, rowspan=2, sticky="NSEW")
						fila+=2
					except EOFError:
						break
				archivo.close()

			creaTop()
			ventanaFacil.mainloop()

		def topIntermedio():
			"""
			Esta funcion se encarga e crear el topLevel del Top para la
			dificultad intermedio, junto con los jugadores creados de objetos
			y sus tiempos.
			Entradas: El evento del boton
			Salidas: El topLevel
			Restricciones: No tiene
			"""
			ventanaIntermedio=Toplevel()
			ventanaIntermedio.geometry("400x500")
			ventanaIntermedio.title("Nivel Intermedio")
			ventanaIntermedio.config(bg="#9ACD32")
			def creaTop():
				archivo=open("sudoku2019top10.dat", "rb")
				n=14
				for k in range(0,n):
					frameAyuda = Frame(ventanaIntermedio, width=1, height=500, bg= "#9ACD32")
					frameAyuda.grid(row= 0, column=k, rowspan=n, sticky= "NW")
					frameAyuda = Frame(ventanaIntermedio, width=400, height=1, bg= "#9ACD32")
					frameAyuda.grid(row= k, column=0, columnspan=n, sticky= "NW")
				labelNOMBRETOP=Label(ventanaIntermedio, bg="#9ACD32", text="JUGADOR", font="Arial, 14").grid(row=0, column=0, columnspan=7, rowspan=2, sticky="NSEW")
				labelTIEMPOTOP=Label(ventanaIntermedio, bg="#9ACD32", text="TIEMPO", font="Arial, 14").grid(row=0, column=7, columnspan=7, rowspan=2, sticky="NSEW")
				fila=2
				while True:
					try:
						jugador=pickle.load(archivo)
						Label(ventanaIntermedio, bg="#9ACD32", text=jugador, font="Arial, 14").grid(row=fila, column=0, columnspan=14, rowspan=2, sticky="NSEW")
						fila+=2
					except EOFError:
						break
				archivo.close()

			creaTop()
			ventanaIntermedio.mainloop()

		def topDificil():
			"""
			Esta funcion se encarga e crear el topLevel del Top para la
			dificultad dificil, junto con los jugadores creados de objetos
			y sus tiempos.
			Entradas: El evento del boton
			Salidas: El topLevel
			Restricciones: No tiene
			"""
			ventanaDificil=Toplevel()
			ventanaDificil.geometry("400x500")
			ventanaDificil.title("Nivel Dificil")
			ventanaDificil.config(bg="#9ACD32")
			def creaTop():
				archivo=open("sudoku2019top10.dat", "rb")
				n=14
				for k in range(0,n):
					frameAyuda = Frame(ventanaDificil, width=1, height=500, bg= "#9ACD32")
					frameAyuda.grid(row= 0, column=k, rowspan=n, sticky= "NW")
					frameAyuda = Frame(ventanaDificil, width=400, height=1, bg= "#9ACD32")
					frameAyuda.grid(row= k, column=0, columnspan=n, sticky= "NW")
				labelNOMBRETOP=Label(ventanaDificil, bg="#9ACD32", text="JUGADOR", font="Arial, 14").grid(row=0, column=0, columnspan=7, rowspan=2, sticky="NSEW")
				labelTIEMPOTOP=Label(ventanaDificil, bg="#9ACD32", text="TIEMPO", font="Arial, 14").grid(row=0, column=7, columnspan=7, rowspan=2, sticky="NSEW")
				fila=2
				while True:
					try:
						jugador=pickle.load(archivo)
						Label(ventanaDificil, bg="#9ACD32", text=jugador, font="Arial, 14").grid(row=fila, column=0, columnspan=14, rowspan=2, sticky="NSEW")
						fila+=2
					except EOFError:
						break
				archivo.close()

			creaTop()
			ventanaDificil.mainloop()
				
		ventanaTop=Toplevel()
		ventanaTop.geometry("400x600")
		ventanaTop.config(bg="#9ACD32")
		ventanaTop.title("TOP 10")
		ventanaTop.iconbitmap("top10.ico")
		vinetas= Menu()
		ventanaTop.config(menu=vinetas)

		BarraFacil=Menu(vinetas, tearoff=False)
		vinetas.add_command(label="Facil", command=topFacil)

		BarraIntermedio=Menu(vinetas, tearoff=False)
		vinetas.add_command(label="Intermedio", command=topIntermedio)

		BarraDificil=Menu(vinetas, tearoff=False)
		vinetas.add_command(label="Dificil", command=topDificil)



	botonTOP10=Button(root, bg="#008000", text="TOP 10", font="Arial, 12", fg="White", command=top10).grid(row=20, column=25, rowspan=2, columnspan=4, sticky="NSEW")
	
	#----------Boton y funcion de Guardar---------
	"""
	Entradas: No recibe
	Salidas: Despliega el boton de guardar dentro del root
	Restricciones: No tiene
	"""	
	def guardar():
		global matrizActual
		global nombreJugador
		global horas
		global minutos
		global segundos
		global partidaActual
		global tipoDePartida

		archivo=open("sudoku2019juegoactual.dat", "wb")
		pickle.dump(matrizActual, archivo)
		pickle.dump(partidaActual, archivo)
		pickle.dump(dificultadDePartida, archivo)
		pickle.dump(tipoDePartida, archivo)
		pickle.dump(EntryNombreJugador.get(), archivo)
		pickle.dump(horas, archivo)
		pickle.dump(minutos, archivo)
		pickle.dump(segundos, archivo)
		archivo.close()
		verificacion=messagebox.askyesno("PARTIDA GUARDADA", "Partida guardada con exito, desea seguir jugando?")
		if verificacion==True:
			pass
		else:
			jugarMenu()

	botonGuardar=Button(root, bg="#6B8E23", text="Guardar\nJuego", font="Arial, 12", fg="White", command=guardar).grid(row=26, column=3, rowspan=2, columnspan=4, sticky="NSEW")
	
	#----------Boton y funcion de Cargar---------
	"""
	Entradas: No recibe
	Salidas: Despliega el boton de cargar dentro del root
	Restricciones: No tiene
	"""	
	def cargar():
		global matrizActual
		global nombreJugador
		global horas
		global minutos
		global segundos
		global partidaActual
		global tipoDePartida
		global cargado
		global option
		global juegoIniciado

		archivo=open("sudoku2019juegoactual.dat", "rb")
		matrizActual=pickle.load(archivo)
		partidaActual=pickle.load(archivo)
		dificultadDePartida=pickle.load(archivo)
		tipoDePartida=pickle.load(archivo)
		nombreJugador=pickle.load(archivo)
		horas=pickle.load(archivo)
		minutos=pickle.load(archivo)
		segundos=pickle.load(archivo)
		archivo.close()
		cargado=True
		juegoIniciado=False
		option=""

		if tipoDePartida=="Numeros":
			configuracionNumeros()
		elif tipoDePartida=="Letras":
			configuracionLetras()
		else:
			configuracionColores()


	botonCargar=Button(root, bg="#008000", text="Cargar\nJuego", font="Arial, 12", fg="White", command=cargar).grid(row=26, column=10, rowspan=2, columnspan=4, sticky="NSEW")
	
	#----------Despliegue del Nombre y Entry del jugador---------
	"""
	Entradas: No recibe
	Salidas: Despliega el label y el entry de jugador dentro del root
	Restricciones: No tiene
	"""	

	def character_limit(entry_text):
		if len(entry_text.get()) > 0:
			entry_text.set(entry_text.get()[:30])

	entry_text=StringVar()
	EntryNombreJugador=Entry(root, bg="White", font="Arial, 12", textvariable=entry_text)
	entry_text.trace("w", lambda *args: character_limit(entry_text))
	EntryNombreJugador.grid(row=23, column=9, rowspan=2, columnspan=10, sticky="NSEW")
	labelNombreJugador=Label(root, bg="#9ACD32", text="Nombre del Jugador:", font="Arial, 12", fg="White").grid(row=23, column=1, rowspan=2, columnspan=7, sticky="NSEW")
	
	#----------Boton y funciones de Timer y Reloj---------
	"""
	Entradas: No recibe
	Salidas: Despliega el label que muestra el timer y el reloj dentro del root
	Restricciones: No tiene
	"""
	def timer(h=int(horas), m=int(minutos), s=int(segundos)):
		global proceso
		global horas
		global minutos
		global segundos

		if s <= 0:
			s=59
			m=m-1
			if m <= 0:
				m=0
				h=h-1
				if h <= 0:
					h=0
		time['text'] = str(h)+":"+str(m)+":"+str(s)
		proceso=time.after(1000, timer, (h), (m), (s-1))
		horas=h
		minutos=m
		segundos=s

	def reloj(h=0, m=0, s=0):
		global proceso
		global horas
		global minutos
		global segundos

		if s >= 60:
			s=0
			m+=1
			if m >= 60:
				m=0
				h+=1
		if h >= 99:
			h=0
		time['text'] = str(h)+":"+str(m)+":"+str(s)
		proceso=time.after(1000, reloj, (h), (m), (s+1))

	labelHoras=Label(root, bg="#808e9b", text="Horas", font="Arial, 11").grid(row=23, column=20, rowspan=2, columnspan=3, sticky="NSEW")
	labelMinutos=Label(root, bg="#d2dae2", text="Minutos", font="Arial, 11").grid(row=23, column=23, rowspan=2, columnspan=3, sticky="NSEW")
	labelSegundos=Label(root, bg="#808e9b", text="Segundos", font="Arial, 11").grid(row=23, column=26, rowspan=2, columnspan=3, sticky="NSEW")
	time = Label(root, fg="Black", font=("","38"))
	time.grid(row=25, column=20, rowspan=2, columnspan=9, sticky="NSEW")


	#----------Boton y funcion de Iniciar partida---------
	"""
	Entradas: No recibe
	Salidas: Despliega el boton de iniciar dentro del root
	Restricciones: No tiene
	"""
	def iniciar():
		"""
		Esta funcion sirve principalmente para empezar la partida, esto conlleva
		iniciar el temporizador o el reloj depende de la configuracion que el usuario
		haya escogido
		Entradas: Recibe el evento del click del boton
		Salidas: Empieza a correr el reloj y permite al jugador jugar
		Restricciones: No tiene
		"""
		global juegoIniciado
		global cargado
		global nombreJugador

		if cargado==False:
			nombreJugador=EntryNombreJugador.get()
		else:
			entry_text.set(nombreJugador)
		if nombreJugador=="":
			messagebox.showerror("ERROR", "Debe dar un nombre de jugador antes de comenzar")
		else:
			juegoIniciado=True
			if configReloj==True:
				botonIniciar.config(state="disable")
				reloj()
			elif configReloj=="Timer":
				botonIniciar.config(state="disable")
				timer()
			else:
				botonIniciar.config(state="disable")

	botonIniciar=Button(root, bg="#008000", text="Iniciar\nJuego", font="Arial, 12", fg="White", command=iniciar)
	botonIniciar.grid(row=20, column=1, rowspan=2, columnspan=4, sticky="NSEW")
	
	LabelINDDificultad=Label(root, bg="#9ACD32", borderwidth=1, text="Dificultad: {}".format(dificultadDePartida), font="Arial, 12", fg="White").grid(row=27, column=20, rowspan=2, columnspan=9, sticky="NSEW")



#--------------------Funciones del Menu desplegable (Basicas)--------------------
#---Funcion de Configurar--
def configurarMenu():
	"""
	Esta funcion es la que va a desplegar todo el menu de configurar, incluyendo 
	la configuracion de dificultad, reloj y tipo de partida para que el usuario pueda
	seleccionar toda la configuracion del como desea jugar.
	"""
	def aceptarConfiguracion():
		"""
		Esta funcion lo que realiza es colocar en las variables globales de los tiempos
		el tiempo que el usuario haya definido
		Entradas: El evento del boton
		Salidas: Toda la configuracion definida
		Restricciones: No tiene
		"""
		global configReloj
		global horas
		global minutos
		global segundos

		if configReloj=="Timer":
			if int(EntryHoras.get())>4 or int(EntryMinutos.get())>=60 or int(EntrySegundos.get())>=60:
				messagebox.showerror("ERROR", "HORAS ENTRE (0-4), MINUTOS ENTRE (0-59), SEGUNDOS (0-59)")
			else:
				horas=EntryHoras.get()
				minutos=EntryMinutos.get()
				segundos=EntrySegundos.get()
				ventanaConfigurar.destroy()
		else:
			ventanaConfigurar.destroy()

	def seleccTipoPartida():
		"""
		Esta seccion es la que permite al usuario escoger el tipo de partida con el que 
		desee jugar
		Entradas: El evento del boton
		Salidas: El Toplevel para la escogencia del tipo
		Restricciones no tiene
		"""
		def tipoNumeros():#Elige que se juega con numeros
			global tipoDePartida

			tipoDePartida="Numeros"

		def tipoLetras():#Elige que se juega con Letras
			global tipoDePartida

			tipoDePartida="Letras"

		def tipoColores():#Elige que se juega con Colores
			global tipoDePartida

			tipoDePartida="Colores"

		def tipoElegible():#Elige que se juega con la que el programador desee
			pass


		ventanaTipoPartida=Toplevel()
		ventanaTipoPartida.geometry("700x400")
		ventanaTipoPartida.title("TIPO DE PARTIDA")
		ventanaTipoPartida.config(bg="#9ACD32")
		
		n=23
		for k in range(0,n):
			frameAyuda = Frame(ventanaTipoPartida, width=1, height=400, bg= "#9ACD32")
			frameAyuda.grid(row= 0, column=k, rowspan=n, sticky= "NW")
			frameAyuda = Frame(ventanaTipoPartida, width=700, height=1, bg= "#9ACD32")
			frameAyuda.grid(row= k, column=0, columnspan=n, sticky= "NW")

		RBNumeros=Radiobutton(ventanaTipoPartida, bg="#9ACD32", fg="Black", text="Numeros", font="Arial, 12", command=tipoNumeros)
		RBNumeros.grid(row=0, column=1, rowspan=2, columnspan=3, sticky="NSEW")
		RBLetras=Radiobutton(ventanaTipoPartida, bg="#9ACD32", fg="Black", text="Letras", font="Arial, 12", command=tipoLetras)
		RBLetras.grid(row=0, column=7, rowspan=2, columnspan=3, sticky="NSEW")
		RBColores=Radiobutton(ventanaTipoPartida, bg="#9ACD32", fg="Black", text="Colores", font="Arial, 12", command=tipoColores)
		RBColores.grid(row=0, column=13, rowspan=2, columnspan=3, sticky="NSEW")
		RBElegible=Radiobutton(ventanaTipoPartida, bg="#9ACD32", fg="Black", text="Elegible", font="Arial, 12", command=tipoElegible)
		RBElegible.grid(row=0, column=19, rowspan=2, columnspan=3, sticky="NSEW")

		#Dibuja los botones de muestra de los numeros
		n=1
		f=3
		k=1
		for i in range(0, 9):
			if k==1:
				Button(ventanaTipoPartida, text=n, font="Arial, 12").grid(row=f, column=1, rowspan=2, columnspan=2, sticky="NSEW")
				f+=2
				n+=1
				k+=1
			else:
				Button(ventanaTipoPartida, text=n, font="Arial, 12").grid(row=f, column=2, rowspan=2, columnspan=2, sticky="NSEW")
				f+=2
				n+=1
				k-=1

		#Dibuja los botones de muestra de las letras
		listaLetras=["","A","B","C","D","E","F","G","H","I"]
		n=1
		f=3
		k=1
		for i in range(0, 9):
			if k==1:
				Button(ventanaTipoPartida, text=listaLetras[n], font="Arial, 12").grid(row=f, column=7, rowspan=2, columnspan=2, sticky="NSEW")
				f+=2
				n+=1
				k+=1
			else:
				Button(ventanaTipoPartida, text=listaLetras[n], font="Arial, 12").grid(row=f, column=8, rowspan=2, columnspan=2, sticky="NSEW")
				f+=2
				n+=1
				k-=1

		#Dibuja los botones de muestra de los colores
		listaColores=["SystemButtonFace","Blue","Light Grey","#ffa502","Light Green","Brown","Red","Yellow","Purple","Black"]
		n=1
		f=3
		k=1
		for i in range(0, 9):
			if k==1:
				Button(ventanaTipoPartida, bg=listaColores[n]).grid(row=f, column=13, rowspan=2, columnspan=2, sticky="NSEW")
				f+=2
				n+=1
				k+=1
			else:
				Button(ventanaTipoPartida, bg=listaColores[n]).grid(row=f, column=14, rowspan=2, columnspan=2, sticky="NSEW")
				f+=2
				n+=1
				k-=1

		ventanaTipoPartida.mainloop()

	def dificultadFacil():#Coloca la dificultad del juego en facil
		global dificultadDePartida

		dificultadDePartida="Facil"

	def dificultadoIntermedio():#Coloca la dificulado del juego en Intermedio
		global dificultadDePartida

		dificultadDePartida="Intermedio"

	def dificultadDificil():#Coloca la dificultad del juego en Dificil
		global dificultadDePartida

		dificultadDePartida="Dificil"
	
	def relojSI():#Coloca la configuracion del reloj en que si se quiere
		global configReloj

		configReloj=True

	def relojNO():#oloca la configuracion del reloj en que no se quiere
		global configReloj

		configReloj=False

	def relojTIMER():#Coloca la configuracion del reloj en modo Timer
		global configReloj

		messagebox.showinfo("RECOMENDACION", "Para nivel Facil: 30 min\nPara nivel Intermedio: 1 hora\nPara nivel Dificil: 2 horas")
		configReloj="Timer"

	ventanaConfigurar=Toplevel()
	ventanaConfigurar.title("CONFIGURACION")
	ventanaConfigurar.iconbitmap("configuracion.ico")
	ventanaConfigurar.geometry("700x550")
	ventanaConfigurar.config(bg="#9ACD32")
	n=16
	for k in range(15):
		frameAyuda = Frame(ventanaConfigurar, width=1, height=550, bg= "#9ACD32")
		frameAyuda.grid(row= 0, column=k, rowspan=n, sticky= "NW")
		frameAyuda = Frame(ventanaConfigurar, width=700, height=1, bg= "#9ACD32")
		frameAyuda.grid(row= k, column=0, columnspan=n, sticky= "NW")
	
	botonAceptarConfig=Button(ventanaConfigurar, bg="#9ACD32", fg="Black", text="Aceptar Configuracion", font="Arial, 12", command=aceptarConfiguracion)
	botonAceptarConfig.grid(row=2, column=10, columnspan=5, sticky="NSEW")

	labelDificultad=Label(ventanaConfigurar, bg="#9ACD32", fg="Black", text="1. Nivel: ", font="Arial, 12").grid(row=1, column=0, rowspan=2, columnspan=4, sticky="NSEW")
	RBFacil=Radiobutton(ventanaConfigurar, bg="#9ACD32", fg="Black", text="Facil", font="Arial, 12", command=dificultadFacil)
	RBFacil.grid(row=1, column=4, columnspan=4, sticky="NSEW")
	RBFacil.select()
	RBIntermedio=Radiobutton(ventanaConfigurar, bg="#9ACD32", fg="Black", text="Intermedio", font="Arial, 12", command=dificultadoIntermedio)
	RBIntermedio.grid(row=2, column=4, columnspan=4, sticky="NSEW")
	RBIntermedio.deselect()
	RBDificil=Radiobutton(ventanaConfigurar, bg="#9ACD32", fg="Black", text="Dificil", font="Arial, 12", command=dificultadDificil)
	RBDificil.grid(row=3, column=4, columnspan=4, sticky="NSEW")
	RBDificil.deselect()
	
	labelReloj=Label(ventanaConfigurar, bg="#9ACD32", fg="Black", text="2. Reloj: ", font="Arial, 12").grid(row=6, column=0, rowspan=2, columnspan=4, sticky="NSEW")
	RBSI=Radiobutton(ventanaConfigurar, bg="#9ACD32", fg="Black", text="Si", font="Arial, 12", command=relojSI)
	RBSI.grid(row=6, column=4, columnspan=4, sticky="NSEW")
	RBSI.select()
	RBNO=Radiobutton(ventanaConfigurar, bg="#9ACD32", fg="Black", text="No", font="Arial, 12", command=relojNO)
	RBNO.grid(row=7, column=4, columnspan=4, sticky="NSEW")
	RBNO.deselect()
	RBTimer=Radiobutton(ventanaConfigurar, bg="#9ACD32", fg="Black", text="Timer", font="Arial, 12", command=relojTIMER)
	RBTimer.grid(row=8, column=4, columnspan=4, sticky="NSEW")
	RBTimer.deselect()
	labelHoras=Label(ventanaConfigurar, bg="#808e9b", fg="Black", text="Horas", font="Arial, 12").grid(row=6, column=9, columnspan=2, sticky="NSEW")
	labelMinutos=Label(ventanaConfigurar, bg="#d2dae2", fg="Black", text="Minutos", font="Arial, 12").grid(row=6, column=11, columnspan=2, sticky="NSEW")
	labelSegundos=Label(ventanaConfigurar, bg="#808e9b", fg="Black", text="Segundos", font="Arial, 12").grid(row=6, column=13, columnspan=2, sticky="NSEW")
	EntryHoras=Entry(ventanaConfigurar, bg="White", font="Arial, 12", width=2, justify="center")
	EntryHoras.grid(row=7, column=9, columnspan=2, sticky="NSEW")
	EntryMinutos=Entry(ventanaConfigurar, bg="White", font="Arial, 12", width=2, justify="center")
	EntryMinutos.grid(row=7, column=11, columnspan=2, sticky="NSEW")
	EntrySegundos=Entry(ventanaConfigurar, bg="White", font="Arial, 12", width=2, justify="center")
	EntrySegundos.grid(row=7, column=13, columnspan=2, sticky="NSEW")

	labelTipo=Label(ventanaConfigurar, bg="#9ACD32", fg="Black", text="3. Tipo de Partida: ", font="Arial, 12").grid(row=11, column=0, rowspan=2, columnspan=4, sticky="NSEW")
	botonTipo=Button(ventanaConfigurar, bg="#9ACD32", fg="Black", text="Seleccionar tipo de partida", font="Arial, 12", command=seleccTipoPartida)
	botonTipo.grid(row=11, column=5, rowspan=2, columnspan=6, sticky="NSEW")

	ventanaConfigurar.mainloop()

#---Funcion de Ayuda---
def ayudaMenu():
	"""
	Esta funcion es la que muestra el manual de usuario
	Entradas: No recibe
	Salidas: El manual de usuario
	Restricciones: No tiene
	"""
	wb.open_new(r"C:\Users\carlo\OneDrive\Escritorio\TEC\Segundo Semestre\Intro y Taller\Taller\Proyectos\3er proyecto\Sudoku\manual_de_usuario_sudoku.pdf")


#---Funcion de Salir---
def salirMenu():
	"""
	Esta pequena funcion basica lo unico que realiza es que a la hora
	de que se quiera salir del juego, este lo termina eliminando la 
	raiz con todo aquello que tenga dentro
	Entradas: No recibe
	Salidas: La raiz quitada
	Restricciones: No tiene
	"""
	root.quit()

#---Funcion Acerca De---
def acercaDeMenu():
	"""
	El acerca de es una parte del menu de la parte de arriba en la cual si el usuario
	presiona va a desplegar un pequeno messagebox de informacion sobre todo el programa
	para que el usuario pueda saber el nombre del programa, la version, la fecha de creacion 
	y el autor.
	Entradas: No recibe
	Salidas: El messagebox con la informacion correspondiente
	Restricciones: No tiene 
	"""
	messagebox.showinfo("INFORMACION DEL PROGRAMA", "NOMBRE: SUDOKU\nAUTOR:Carlos Calderon\nFECHA DE CREACION: 5/11/2019 \nVERSION:1.0.0")

#--------------------Interfaz Grafica Principal (root)--------------------
"""
Esta es la forma en la que creo mi ventana principal y la 
llamo de la forma root para futuras menciones, tiene un tamano
de 650x650 y es de color blanca
Entradas: No recibe
Salidas: Crea la ventana principal con el menu de arriba para que de ahi se elija que hacer
Restricciones: No recibe
"""
root=Tk()
root.title("SUDOKU")
root.iconbitmap("icono_sudoku.ico")
root.geometry("650x670")
root.config(bg="#9ACD32")

def top10Guardar():
	archivo=open("sudoku2019top10.dat", "wb")
	pickle.dump("1- Carlos Calderon          1:30:15", archivo)
	pickle.dump("2- Pedro Cabezas            1:40:25", archivo)
	pickle.dump("3- Rebeca Barquero          1:55:40", archivo)
	archivo.close()


#----------Menu desplegable tipo IDLE---------
"""
Todo esto son botones tipo menus que aparecen encima del juego
con diferentes opciones para que el usario pueda interactuar
Entradas: No recibe
Salidas: Esto crea el menu y lo coloca en la parte arriba del root
Restricciones: No tiene
"""
vinetas= Menu()
root.config(menu=vinetas)

BarraJugar=Menu(vinetas, tearoff=False)
vinetas.add_command(label="Jugar", command=jugarMenu)


BarraConfigurar=Menu(vinetas, tearoff=False)
vinetas.add_command(label="Configurar", command=configurarMenu)

BarraAyuda=Menu(vinetas, tearoff=False)
vinetas.add_cascade(label="Ayuda", command=ayudaMenu)

BarraAcerca=Menu(vinetas, tearoff=False)
vinetas.add_command(label="Acerca de", command=acercaDeMenu)

BarraSalir=Menu(vinetas, tearoff=False)
vinetas.add_command(label="Salir", command=salirMenu)


top10Guardar()
root.mainloop()