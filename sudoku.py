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

	for i in range(0,9):
		for k in range(0,9):e
			BotonSudoku=Button(frameSudoku).grid(row=i, column=k, sticky="NSEW")



	#--------------------Botones de Juego-----------------
	"""
	Estos son los botones que el jugador va a tener para poder jugar al sudoku,]
	dependiendo del tipo de juego que el usuario seleccione, estos botones van a cambiar
	Entradas: No recibe
	Salidas: Los botones de juego
	Restricciones: No tiene
	"""
	boton1=Button(root).grid(row=1, column=22, rowspan=2, columnspan=4, sticky="NSEW")
	boton2=Button(root).grid(row=3, column=24, rowspan=2, columnspan=4, sticky="NSEW")
	boton3=Button(root).grid(row=5, column=22, rowspan=2, columnspan=4, sticky="NSEW")
	boton4=Button(root).grid(row=7, column=24, rowspan=2, columnspan=4, sticky="NSEW")
	boton5=Button(root).grid(row=9, column=22, rowspan=2, columnspan=4, sticky="NSEW")
	boton6=Button(root).grid(row=11, column=24, rowspan=2, columnspan=4, sticky="NSEW")
	boton7=Button(root).grid(row=13, column=22, rowspan=2, columnspan=4, sticky="NSEW")
	boton8=Button(root).grid(row=15, column=24, rowspan=2, columnspan=4, sticky="NSEW")
	boton9=Button(root).grid(row=17, column=22, rowspan=2, columnspan=4, sticky="NSEW")


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