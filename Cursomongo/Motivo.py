import pymongo
from pymongo import MongoClient
from tkinter import*
from tkinter import ttk
from tkinter import messagebox

HOST="localhost"
PUERTO="27017"
URI = "mongodb://"+HOST+":"+PUERTO+"/"
BASEDATOS="reto3"
COLECCION="Motivo"
cliente = MongoClient(URI,serverSelectionTimeOutMS=1000)
baseDatos=cliente[BASEDATOS]
coleccion=baseDatos[COLECCION]

def mostrardatos():
    try:
        registros = tabla.get_children()
        for registro in registros:
            tabla.delete(registro)
        for documento in coleccion.find():
            tabla.insert('', 0, text=documento["_id"], values=(documento["indicacion"]))
    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
        print("Tiempo exedido "+str(errorTiempo))
    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Fallo al conectarse a mongodb "+errorConexion)
def crearMotivo():
    if len(IdMotivo.get())!=0 and len(indicacion.get())!=0:
        try:
            diccionario={"IdMotivo":IdMotivo.get(),"indicacion":indicacion.get()}
            coleccion.insert_one(diccionario)
            IdMotivo.delete(0, END)
            indicacion.delete(0, END)

        except pymongo.errors.ConnectionFailure as error:
            print(error)
    mostrardatos()

ventana=Tk()
tabla =ttk.Treeview(ventana,columns=('#0', '#1'))
tabla.grid(row=1, column=0, columnspan=2)
tabla.heading("#0", text="IdMotivo")
tabla.heading("#1", text="indicacion")


    #IdMotivo
Label(ventana, text="IdMotivo").grid(row=2, column=0)
IdMotivo = Entry(ventana)
IdMotivo.grid(row=2,column=1)
    #Hora_inicio
Label(ventana, text="indicacion").grid(row=3, column=0)
indicacion = Entry(ventana)
indicacion.grid(row=3,column=1)

    #boton de submit
submit = Button(ventana, text="coloca motivo", command=crearMotivo(),bg="green", fg="white")
submit.grid(row=4, columnspan=2)
mostrardatos()

ventana.mainloop()
