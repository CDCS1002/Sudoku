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
from random import *

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
diccIntermedio={}
diccDIficiles={}


matrizActual=""
option=""
#--------------------Funcion de Jugar esto engomera toda la interfaz de jugar--------------------
def jugarMenu():
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
		frameAyuda = Frame(root, width=1, height=650, bg= "Blue")
		frameAyuda.grid(row= 0, column=k, rowspan=n, sticky= "NW")
		frameAyuda = Frame(root, width=650, height=1, bg= "Blue")
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
	def configuracionNumeros():
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

			x, y=widget.position
			widget.config(text=option)
			matrizActual[x][y]="option"
			
		def creaSudokuFaciles():#Crea la matriz si el usuario decide crear una partida facil
			global matrizActual
			partida=randint(1,3)
			matrizActual=diccFaciles[partida]

			i=0
			k=0
			for linea in diccFaciles[partida]:
				for elemento in linea:
					if elemento=="":
						botonSudoku=Button(frameSudoku)
						botonSudoku.config(command=lambda widget=botonSudoku: modificaMatrizNumeros(widget))
						botonSudoku.grid(row=i, column=k, sticky="NSEW")
						botonSudoku.position=(i, k)
						k+=1
					else:
						botonSudoku=Button(frameSudoku, text=diccFaciles[partida][i][k], state="disable").grid(row=i, column=k, sticky="NSEW")
						k+=1
				i+=1
				k=0

		def creaSudokuIntermedio():#Crea la matriz si el usuario decide crear una partida intermedia
			global matrizActual
			partida=randint(1,3)
			matrizActual=diccIntermedio[partida]
			
			i=0
			k=0
			for linea in diccIntermedio[partida]:
				for elemento in linea:
					if elemento=="":
						botonSudoku=Button(frameSudoku)
						botonSudoku.config(command=lambda widget=botonSudoku: modificaMatrizNumeros(widget))
						botonSudoku.grid(row=i, column=k, sticky="NSEW")
						botonSudoku.position=(i, k)
						k+=1
					else:
						botonSudoku=Button(frameSudoku, text=diccIntermedio[partida][i][k], state="disable").grid(row=i, column=k, sticky="NSEW")
						k+=1
				i+=1
				k=0

		def creaSudokuDificiles():#crea la matriz si el usuario decide crear una partida dificil
			global matrizActual
			partida=randint(1,3)
			matrizActual=diccDIficiles[partida]
			
			i=0
			k=0
			for linea in diccDIficiles[partida]:
				for elemento in linea:
					if elemento=="":
						botonSudoku=Button(frameSudoku)
						botonSudoku.config(command=lambda widget=botonSudoku: modificaMatrizNumeros(widget))
						botonSudoku.grid(row=i, column=k, sticky="NSEW")
						botonSudoku.position=(i, k)
						k+=1
					else:
						botonSudoku=Button(frameSudoku, text=diccDIficiles[partida][i][k], state="disable").grid(row=i, column=k, sticky="NSEW")
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
		def modificaMatrizLetras(widget):
			global matrizActual

			x, y=widget.position
			widget.config(text=option)
			matrizActual[x][y]="option"
			
		def creaSudokuFaciles():#Crea la matriz si el usuario decide crear una partida facil
			global matrizActual
			partida=randint(1,3)
			matrizActual=diccFaciles[partida]
			listaLetras=["","A","B","C","D","E","F","G","H","I"]

			i=0
			k=0
			for linea in diccFaciles[partida]:
				for elemento in linea:
					if elemento=="":
						botonSudoku=Button(frameSudoku)
						botonSudoku.config(command=lambda widget=botonSudoku: modificaMatrizLetras(widget))
						botonSudoku.grid(row=i, column=k, sticky="NSEW")
						botonSudoku.position=(i, k)
						k+=1
					else:
						botonSudoku=Button(frameSudoku, text=listaLetras[int(diccFaciles[partida][i][k])], state="disable").grid(row=i, column=k, sticky="NSEW")
						k+=1
				i+=1
				k=0

		def creaSudokuIntermedio():#Crea la matriz si el usuario decide crear una partida intermedio
			global matrizActual
			partida=randint(1,3)
			matrizActual=diccIntermedio[partida]
			listaLetras=["","A","B","C","D","E","F","G","H","I"]

			i=0
			k=0
			for linea in diccIntermedio[partida]:
				for elemento in linea:
					if elemento=="":
						botonSudoku=Button(frameSudoku)
						botonSudoku.config(command=lambda widget=botonSudoku: modificaMatrizLetras(widget))
						botonSudoku.grid(row=i, column=k, sticky="NSEW")
						botonSudoku.position=(i, k)
						k+=1
					else:
						botonSudoku=Button(frameSudoku, text=listaLetras[int(diccIntermedio[partida][i][k])], state="disable").grid(row=i, column=k, sticky="NSEW")
						k+=1
				i+=1
				k=0

		def creaSudokuDificiles():#Crea la matriz si el usuario decide crear una partida dificil
			global matrizActual
			partida=randint(1,3)
			matrizActual=diccDIficiles[partida]
			listaLetras=["","A","B","C","D","E","F","G","H","I"]

			i=0
			k=0
			for linea in diccDIficiles[partida]:
				for elemento in linea:
					if elemento=="":
						botonSudoku=Button(frameSudoku)
						botonSudoku.config(command=lambda widget=botonSudoku: modificaMatrizLetras(widget))
						botonSudoku.grid(row=i, column=k, sticky="NSEW")
						botonSudoku.position=(i, k)
						k+=1
					else:
						botonSudoku=Button(frameSudoku, text=listaLetras[int(diccDIficiles[partida][i][k])], state="disable").grid(row=i, column=k, sticky="NSEW")
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

			option=widget["text"]

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
		def modificaMatrizColores(widget):
			global matrizActual

			x, y=widget.position
			widget.config(bg=option)
			matrizActual[x][y]="option"
			
		def creaSudokuFaciles():#Crea la matriz si el usuario decide crear una partida facil
			global matrizActual
			partida=randint(1,3)
			matrizActual=diccFaciles[partida]
			listaColores=["","Blue","Light Grey","#ffa502","Light Green","Brown","Red","Yellow","Purple","Black"]

			i=0
			k=0
			for linea in diccFaciles[partida]:
				for elemento in linea:
					if elemento=="":
						botonSudoku=Button(frameSudoku)
						botonSudoku.config(command=lambda widget=botonSudoku: modificaMatrizColores(widget))
						botonSudoku.grid(row=i, column=k, sticky="NSEW")
						botonSudoku.position=(i, k)
						k+=1
					else:
						botonSudoku=Button(frameSudoku, bg=listaColores[int(diccFaciles[partida][i][k])], state="disable").grid(row=i, column=k, sticky="NSEW")
						k+=1
				i+=1
				k=0

		def creaSudokuIntermedio():#Crea la matriz si el usuario decide crear una partida intermedio
			global matrizActual
			partida=randint(1,3)
			matrizActual=diccIntermedio[partida]
			llistaColores=["","Blue","Light Grey","#ffa502","Light Green","Brown","Red","Yellow","Purple","Black"]

			i=0
			k=0
			for linea in diccIntermedio[partida]:
				for elemento in linea:
					if elemento=="":
						botonSudoku=Button(frameSudoku)
						botonSudoku.config(command=lambda widget=botonSudoku: modificaMatrizColores(widget))
						botonSudoku.grid(row=i, column=k, sticky="NSEW")
						botonSudoku.position=(i, k)
						k+=1
					else:
						botonSudoku=Button(frameSudoku, text=listaColores[int(diccIntermedio[partida][i][k])], state="disable").grid(row=i, column=k, sticky="NSEW")
						k+=1
				i+=1
				k=0

		def creaSudokuDificiles():#Crea la matriz si el usuario decide crear una partida dificil
			global matrizActual
			partida=randint(1,3)
			matrizActual=diccDIficiles[partida]
			listaColores=["","Blue","Light Grey","#ffa502","Light Green","Brown","Red","Yellow","Purple","Black"]

			i=0
			k=0
			for linea in diccDIficiles[partida]:
				for elemento in linea:
					if elemento=="":
						botonSudoku=Button(frameSudoku)
						botonSudoku.config(command=lambda widget=botonSudoku: modificaMatrizColores(widget))
						botonSudoku.grid(row=i, column=k, sticky="NSEW")
						botonSudoku.position=(i, k)
						k+=1
					else:
						botonSudoku=Button(frameSudoku, text=listaColores[int(diccDIficiles[partida][i][k])], state="disable").grid(row=i, column=k, sticky="NSEW")
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

			option=widget["bg"]

		def botonesColores():
			f=1
			k1=22
			k2=24
			n=1
			listaColores=["","Blue","Light Grey","#ffa502","Light Green","Brown","Red","Yellow","Purple","Black"]
			
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


	#----------Boton y funcion de Iniciar Partida---------
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
		pass

	botonIniciar=Button(root, bg="#008000", text="Iniciar\nJuego", font="Arial, 12", fg="White").grid(row=20, column=1, rowspan=2, columnspan=4, sticky="NSEW")
	
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
		pass

	botonBorrarJugada=Button(root, bg="#6B8E23", text="Borrar\nJugada", font="Arial, 12", fg="White").grid(row=20, column=7, rowspan=2, columnspan=4, sticky="NSEW")
	
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
		pass

	botonTerminar=Button(root, bg="#008000", text="Terminar\nJuego", font="Arial, 12", fg="White").grid(row=20, column=13, rowspan=2, columnspan=4, sticky="NSEW")
	
	#----------Boton y funcion de Borrar Juego---------
	"""
	Entradas: No recibe
	Salidas: Despliega el boton de borrar juego dentro del root
	Restricciones: No tiene
	"""
	def borrarJuego():
		pass

	botonBorrarJuego=Button(root, bg="#6B8E23", text="Borrar\nJuego", font="Arial, 12", fg="White").grid(row=20, column=19, rowspan=2, columnspan=4, sticky="NSEW")
	
	#----------Boton y funcion de Top 10---------
	"""
	Entradas: No recibe
	Salidas: Despliega el boton de top 10 dentro del root
	Restricciones: No tiene
	"""
	def top10():
		pass

	botonTOP10=Button(root, bg="#008000", text="TOP 10", font="Arial, 12", fg="White").grid(row=20, column=25, rowspan=2, columnspan=4, sticky="NSEW")
	
	#----------Boton y funcion de Guardar---------
	"""
	Entradas: No recibe
	Salidas: Despliega el boton de guardar dentro del root
	Restricciones: No tiene
	"""	
	def guardar():
		pass

	botonGuardar=Button(root, bg="#6B8E23", text="Guardar\nJuego", font="Arial, 12", fg="White").grid(row=26, column=3, rowspan=2, columnspan=4, sticky="NSEW")
	
	#----------Boton y funcion de Cargar---------
	"""
	Entradas: No recibe
	Salidas: Despliega el boton de cargar dentro del root
	Restricciones: No tiene
	"""
	def cargar():
		pass

	botonCargar=Button(root, bg="#008000", text="Cargar\nJuego", font="Arial, 12", fg="White").grid(row=26, column=10, rowspan=2, columnspan=4, sticky="NSEW")
	
	#----------Despliegue del Nombre y Entry del jugador---------
	"""
	Entradas: No recibe
	Salidas: Despliega el label y el entry de jugador dentro del root
	Restricciones: No tiene
	"""	
	labelNombreJugador=Label(root, bg="#9ACD32", text="Nombre del Jugador:", font="Arial, 12", fg="White").grid(row=23, column=1, rowspan=2, columnspan=7, sticky="NSEW")
	EntryNombreJugador=Entry(root, bg="White", font="Arial, 12")
	EntryNombreJugador.grid(row=23, column=9, rowspan=2, columnspan=10, sticky="NSEW")
	
	#----------Boton y funciones de Timer y Reloj---------
	"""
	Entradas: No recibe
	Salidas: Despliega el label que muestra el timer y el reloj dentro del root
	Restricciones: No tiene
	"""
	def timer():
		pass

	def reloj():
		pass

	labelHoras=Label(root, bg="#808e9b", text="Horas", font="Arial, 11").grid(row=23, column=20, rowspan=2, columnspan=3, sticky="NSEW")
	labelMinutos=Label(root, bg="#d2dae2", text="Minutos", font="Arial, 11").grid(row=23, column=23, rowspan=2, columnspan=3, sticky="NSEW")
	labelSegundos=Label(root, bg="#808e9b", text="Segundos", font="Arial, 11").grid(row=23, column=26, rowspan=2, columnspan=3, sticky="NSEW")
	time = Label(root, fg="Black", font=("","12"))
	time.grid(row=25, column=20, rowspan=2, columnspan=9, sticky="NSEW")

	LabelINDDificultad=Label(root, bg="#9ACD32", borderwidth=1, text="Dificultad:", font="Arial, 12", fg="White").grid(row=27, column=20, rowspan=2, columnspan=9, sticky="NSEW")



#--------------------Funciones del Menu desplegable (Basicas)--------------------
#---Funcion de Ayuda---
def ayudaMenu():
	"""
	Esta funcion es la que muestra el manual de usuario
	Entradas: No recibe
	Salidas: El manual de usuario
	Restricciones: No tiene
	"""
	#wb.open_new(r"")


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
vinetas.add_command(label="Configurar")

BarraAyuda=Menu(vinetas, tearoff=False)
vinetas.add_cascade(label="Ayuda", command=ayudaMenu)

BarraAcerca=Menu(vinetas, tearoff=False)
vinetas.add_command(label="Acerca de", command=acercaDeMenu)

BarraSalir=Menu(vinetas, tearoff=False)
vinetas.add_command(label="Salir", command=salirMenu)



root.mainloop()