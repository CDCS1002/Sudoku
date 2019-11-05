#--------------------Imports del programa--------------------
"""
Aqui se realizan todos los imports que vaya a utilizar dentro del programa
Entradas: Los modulos a los que llamo
Salidas: Las funciones para los cuales los llame
Restricciones: Estan basados en la version python 3.7
"""
from tkinter import *
from tkinter import messagebox


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

	frameSudoku=Frame(root, bg="Grey").grid(row=1, column=1, rowspan=18, columnspan=18, sticky="NSEW")
	botonIniciar=Button(root, bg="#cc8e35", text="Iniciar\nJuego", font="Arial, 12").grid(row=20, column=1, rowspan=2, columnspan=4, sticky="NSEW")
	botonBorrarJugada=Button(root, bg="#ffda79", text="Borrar\nJugada", font="Arial, 12").grid(row=20, column=7, rowspan=2, columnspan=4, sticky="NSEW")
	botonTerminar=Button(root, bg="#ccae62", text="Terminar\nJuego", font="Arial, 12").grid(row=20, column=13, rowspan=2, columnspan=4, sticky="NSEW")
	botonBorrarJuego=Button(root, bg="#ffb142", text="Borrar\nJuego", font="Arial, 12").grid(row=20, column=19, rowspan=2, columnspan=4, sticky="NSEW")
	botonTOP10=Button(root, bg="#cd6133", text="TOP 10", font="Arial, 12").grid(row=20, column=25, rowspan=2, columnspan=4, sticky="NSEW")
	labelNombreJugador=Label(root, bg="#F8EFBA", text="Nombre del Jugador:", font="Arial, 12").grid(row=23, column=1, rowspan=2, columnspan=7, sticky="NSEW")
	EntryNombreJugador=Entry(root, bg="White", font="Arial, 12")
	EntryNombreJugador.grid(row=23, column=9, rowspan=2, columnspan=10, sticky="NSEW")
	labelHoras=Label(root, bg="#808e9b", text="Horas", font="Arial, 11").grid(row=23, column=20, rowspan=2, columnspan=3, sticky="NSEW")
	labelMinutos=Label(root, bg="#d2dae2", text="Minutos", font="Arial, 11").grid(row=23, column=23, rowspan=2, columnspan=3, sticky="NSEW")
	labelSegundos=Label(root, bg="#808e9b", text="Segundos", font="Arial, 11").grid(row=23, column=26, rowspan=2, columnspan=3, sticky="NSEW")

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
root.config(bg="#F8EFBA")

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