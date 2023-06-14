import pymongo
from pymongo import MongoClient
from tkinter import*
from tkinter import ttk
from tkinter import messagebox

HOST="localhost"
PUERTO="27017"
URI = "mongodb://"+HOST+":"+PUERTO+"/"
BASEDATOS="reto3"
COLECCION="Reserva"
cliente = MongoClient(URI,serverSelectionTimeOutMS=1000)
baseDatos=cliente[BASEDATOS]
coleccion=baseDatos[COLECCION]

def mostrardatos():
    try:
        registros = tabla.get_children()
        for registro in registros:
            tabla.delete(registro)
        for documento in coleccion.find():
            tabla.insert('', 0, text=documento["idReserva"], values=(documento["Hora_inicio"], documento["Hora_fin"],documento["Motivo_idMotivo"], documento["Salones_idSalones"], documento["Usuarios_idUsuarios"]))
    except pymongo.errors.ConnectionFailure as error:
        print(error)

def crearReserva():
    if len(IdReserva.get())!=0 and len(Horainicio.get())!=0 and len(Horafin.get())!=0 and len(IdMotivo.get())!=0 and len(IdSalon.get())!=0 and len(IdUsuario.get())!=0:
        try:
            diccionario={"idReserva":IdReserva.get(),"Hora_fin":Horafin.get(), "Hora_inicio":Horainicio.get(), "Motivo_idMotivo":IdMotivo.get(),"Salones_idSalones":IdSalon.get(),"Usuarios_idUsuarios":IdUsuario.get()}
            coleccion.insert(diccionario)
        except pymongo.errors.ConnectionFailure as error:
            print(error)
    mostrardatos()

ventana=Tk()
tabla =ttk.Treeview(ventana,columns=('#0', '#1', '#2', '#3', '#4', '#5'))
tabla.grid(row=1, column=0, columnspan=2)
tabla.heading("#0", text="IdReserva")
tabla.heading("#1", text="Hora_inicio")
tabla.heading("#2", text="Hora_fin")
tabla.heading("#3", text="Motivo_idMotivo")
tabla.heading("#4", text="Salones_idSalones")
tabla.heading("#5", text="Usuarios_idUsuarios")

    #IdReserva
Label(ventana, text="IdReserva").grid(row=2, column=0)
IdReserva = Entry(ventana)
IdReserva.grid(row=2,column=1)
    #Hora_inicio
Label(ventana, text="Hora de inicio").grid(row=3, column=0)
Horainicio = Entry(ventana)
Horainicio.grid(row=3,column=1)
    #Hora_fin
Label(ventana, text="Hora de fin").grid(row=4, column=0)
Horafin = Entry(ventana)
Horafin.grid(row=4,column=1)
    #Idmotivo
Label(ventana, text="Idmotivo").grid(row=5, column=0)
IdMotivo = Entry(ventana)
IdMotivo.grid(row=5,column=1)
    #IdSalon
Label(ventana, text="IdSalon").grid(row=6, column=0)
IdSalon = Entry(ventana)
IdSalon.grid(row=6,column=1)
    #IdUsuario
Label(ventana, text="IdUsuario").grid(row=7, column=0)
IdUsuario = Entry(ventana)
IdUsuario.grid(row=7,column=1)
    #boton de submit
submit = Button(ventana, text="Hacer reserva", command=crearReserva(),bg="green", fg="white")
submit.grid(row=8, columnspan=6)
mostrardatos()

ventana.mainloop()
