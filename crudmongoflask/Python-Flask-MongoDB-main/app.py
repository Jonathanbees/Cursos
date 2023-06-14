from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase  
from Motivo import Motivo
from Usuarios import Usuarios
from hijueputa import hijueputa
from Mesas import Mesas
from Iluminacion import Iluminacion
from Salon import Salon
from Reserva import Reserva
from Ocupacion import Ocupacion

db = dbase.dbConnection()

app = Flask(__name__)

#Rutas de la aplicación

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/motivo')
def motivo():
    Motivos = db['Motivo']
    Motivosrecibidos = Motivos.find()
    return render_template('motivo.html', Motivos = Motivosrecibidos)

'''
@app.route('/')
def home():
    Motivos = db['Motivo']
    Motivosrecibidos = Motivos.find()
    return render_template('index.html', Motivos = Motivosrecibidos)
'''
#Method Post
@app.route('/Motivos', methods=['POST'])
def addMotivo():
    Motivos = db['Motivo']
    IdMotivo = request.form['IdMotivo']
    indicacion = request.form['indicacion']

    if IdMotivo and indicacion:
        motivo = Motivo(IdMotivo, indicacion)
        Motivos.insert_one(motivo.toDBCollection())
        response = jsonify({
            'IdMotivo' : IdMotivo,
            'indicacion' : indicacion
        })
        return redirect(url_for('motivo'))
    else:
        return notFound()

#Method delete
@app.route('/delete/<string:indicacion_name>')
def delete(indicacion_name):
    Motivos = db['Motivo']
    Motivos.delete_one({'indicacion' : indicacion_name})
    return redirect(url_for('motivo'))

#Method Put
@app.route('/edit/<string:indicacion_name>', methods=['POST'])
def edit(indicacion_name):
    Motivos = db['Motivo']
    IdMotivo = request.form['IdMotivo']
    indicacion = request.form['indicacion']

    if IdMotivo and indicacion:
        Motivos.update_one({'indicacion' : indicacion_name}, {'$set' : {'IdMotivo' : IdMotivo, 'indicacion' : indicacion}})
        response = jsonify({'message' : 'Producto ' + indicacion_name + ' actualizado correctamente'})
        return redirect(url_for('motivo'))
    else:
        return notFound()


''' USUARIOS'''
# Method Post

@app.route('/usuario')
def usuario():
    Usuarioss = db['Usuarios']
    UsuariosRecibidos = Usuarioss.find()
    return render_template('usuario.html', Usuarioss=UsuariosRecibidos)


@app.route('/Usuarios', methods=['POST'])
def addPersona():
    Usuarioss = db['Usuarios']
    idUsuarios = request.form['idUsuarios']
    Nombre = request.form['Nombre']
    Apellido = request.form['Apellido']
    Celular = request.form['Celular']
    Correo = request.form['Correo']
    Ocupacion_idOcupacion = request.form['Ocupacion_idOcupacion']
    Fecha_nacimiento = request.form['Fecha_nacimiento']

    if idUsuarios and Nombre and Apellido and Celular and Correo and Ocupacion_idOcupacion and Fecha_nacimiento:
        persona = Usuarios(idUsuarios, Nombre, Apellido, Celular, Correo, Ocupacion_idOcupacion, Fecha_nacimiento)
        Usuarioss.insert_one(persona.toDBCollection())
        response = jsonify({
            'idUsuarios': idUsuarios,
            'Nombre': Nombre,
            'Apellido': Apellido,
            'Celular': Celular,
            'Correo': Correo,
            'Ocupacion_idOcupacion': Ocupacion_idOcupacion,
            'Fecha_nacimiento': Fecha_nacimiento

        })
        return redirect(url_for('usuario'))
    else:
        return notFound()


##########################
# Method delete
@app.route('/deleteuser/<string:Usuarios_idUsuarios>')
def deleteuser(Usuarios_idUsuarios):
    Usuarioss = db['Usuarios']
    Usuarioss.delete_one({'idUsuarios': Usuarios_idUsuarios})
    return redirect(url_for('usuario'))


# Method Put
@app.route('/edituser/<string:Usuarios_idUsuarios>', methods=['POST'])
def edituser(Usuarios_idUsuarios):
    Usuarioss = db['Usuarios']
    idUsuarios = request.form['idUsuarios']
    Nombre = request.form['Nombre']
    Apellido = request.form['Apellido']
    Celular = request.form['Celular']
    Correo = request.form['Correo']
    Ocupacion_idOcupacion = request.form['Ocupacion_idOcupacion']
    Fecha_nacimiento = request.form['Fecha_nacimiento']

    if idUsuarios and Nombre and Apellido and Celular and Correo and Ocupacion_idOcupacion and Fecha_nacimiento:
        Usuarioss.update_one({'idUsuarios': Usuarios_idUsuarios}, {'$set': {'idUsuarios': idUsuarios,
                                                                           'Nombre': Nombre,
                                                                           'Apellido': Apellido,
                                                                           'Celular': Celular,
                                                                           'Correo': Correo,
                                                                           'Ocupacion_idOcupacion': Ocupacion_idOcupacion,
                                                                           'Fecha_nacimiento': Fecha_nacimiento}})
        response = jsonify({'message': 'Persona ' + Usuarios_idUsuarios + ' actualizado correctamente'})
        return redirect(url_for('usuario'))
    else:
        return notFound()


'''TABLERO'''
#Method Post
@app.route('/tablero')
def tablero():
    Tablero = db['Tablero']
    TableroRecibido = Tablero.find()
    return render_template('tablero.html', Tablero = TableroRecibido)

@app.route('/tablero', methods=['POST'])
def addTablero():
    Tablero = db['Tablero']
    idTablero = request.form['idTablero']
    Tamano = request.form['Tamano']
    Tipo = request.form['Tipo']

    if idTablero and Tamano and Tipo:
        tableros = hijueputa(idTablero, Tamano, Tipo)
        
        Tablero.insert_one(tableros.toDBCollection())
        response = jsonify({
            'idTablero' : idTablero,
            'Tamano' : Tamano,
            'Tipo' : Tipo
        })
        return redirect(url_for('tablero'))
    else:
        return notFound()

#Method delete
@app.route('/deleteTablero/<string:Tablero_idTablero>')
def deleteTablero(Tablero_idTablero):
    Tablero = db['Tablero']
    Tablero.delete_one({'idTablero' : Tablero_idTablero})
    return redirect(url_for('tablero'))

#Method put
@app.route('/editTablero/<string:Tablero_idTablero>', methods=['POST'])
def editTablero(Tablero_idTablero):
    Tablero = db['Tablero']
    idTablero = request.form['idTablero']
    Tamano = request.form['Tamano']
    Tipo = request.form['Tipo']

    if idTablero and Tamano and Tipo:
        Tablero.update_one({'idTablero' : Tablero_idTablero}, {'$set' : {'idTablero' : idTablero, 'Tamano' : Tamano, 'Tipo' : Tipo}})
        response = jsonify({'message' : 'Producto ' + Tablero_idTablero + ' actualizado correctamente'})
        return redirect(url_for('tablero'))
    else:
        return notFound()

'''MESAS'''
@app.route('/mesa')
def mesa():
    Mesa = db['Mesas']
    Mesasrecibidas = Mesa.find()
    return render_template('mesa.html', Mesa = Mesasrecibidas)
#Method Post
@app.route('/addMesas', methods=['POST'])
def addMesas():
    Mesa = db['Mesas']
    idMesas = request.form['idMesas']
    Color = request.form['Color']
    Tamano = request.form['Tamano']

    if idMesas and Color and Tamano:
        mesas = Mesas(idMesas, Color, Tamano)
        Mesa.insert_one(mesas.toDBCollection())

        response = jsonify({
            'idMesas' : idMesas,
            'Color' : Color,
            'Tamano' : Tamano
        })
        return redirect(url_for('mesa'))
    else:
        return notFound()

#Method delete
@app.route('/deleteMesas/<string:Mesas_name>')
def deleteMesas(Mesas_name):
    Mesa = db['Mesas']
    Mesa.delete_one({'idMesas' : Mesas_name})
    return redirect(url_for('mesa'))

#Method put
@app.route('/editMesas/<string:Mesas_name>', methods=['POST'])
def editMesas(Mesas_name):
    Mesa = db['Mesas']
    idMesas = request.form['idMesas']
    Color = request.form['Color']
    Tamano = request.form['Tamano']

    if idMesas and Color and Tamano:
        Mesa.update_one({'idMesas' : Mesas_name}, {'$set' : {'idMesas' : idMesas, 'Color' : Color, 'Tamano' : Tamano}})
        response = jsonify({'message' : 'Producto ' + Mesas_name + ' actualizado correctamente'})
        return redirect(url_for('mesa'))
    else:
        return notFound()
'''ILUMINACION'''
@app.route('/iluminacion')
def iluminacion():
    Ilu = db['Iluminacion']
    Ilurecibidas = Ilu.find()
    return render_template('iluminacion.html', Ilu = Ilurecibidas)
#Method Post
@app.route('/addIluminacion', methods=['POST'])
def addIluminacion():
    Ilu = db['Iluminacion']
    idIluminacion = request.form['idIluminacion']
    Color = request.form['Color']
    Origen = request.form['Origen']
    Regulacion = request.form['Regulacion']
    Ubicacion = request.form['Ubicacion']

    if idIluminacion and Color and Origen and Regulacion and Ubicacion:
        iluminacion = Iluminacion(idIluminacion,Color,Origen,Regulacion, Ubicacion)
        Ilu.insert_one(iluminacion.toDBCollection())
        response = jsonify({
            'idiluminacion' : idIluminacion,
            'Color' : Color,
            'Origen' : Origen,
            'Regulacion' : Regulacion,
            'Ubicacion' : Ubicacion
        })
        return redirect(url_for('iluminacion'))
    else:
        return notFound()

#Method delete
@app.route('/deleteIlum/<string:Iluminacion_name>')
def deleteIlum(Iluminacion_name):
    Ilu = db['Iluminacion']
    Ilu.delete_one({'idIluminacion' : Iluminacion_name})
    return redirect(url_for('iluminacion'))

#Method put
@app.route('/editIlum/<string:Iluminacion_name>', methods=['POST'])
def editIlum(Iluminacion_name):
    Ilu = db['Iluminacion']
    idIluminacion = request.form['idIluminacion']
    Color = request.form['Color']
    Origen = request.form['Origen']
    Regulacion = request.form['Regulacion']
    Ubicacion = request.form['Ubicacion']

    if idIluminacion and Color and Origen and Regulacion and Ubicacion:
        Ilu.update_one({'idIluminacion' : Iluminacion_name}, {'$set' : {'idIluminacion' : idIluminacion, 'Color' : Color, 'Origen' : Origen, 'Regulacion' : Regulacion, 'Ubicacion' : Ubicacion}})
        response = jsonify({'message' : 'Producto ' + Iluminacion_name + ' actualizado correctamente'})
        return redirect(url_for('iluminacion'))
    else:
        return notFound()


'''SALONES'''
@app.route('/salones')
def salones():
    Salones = db['Salones']
    Salonesrecibidos = Salones.find()
    return render_template('salones.html', Salones = Salonesrecibidos)
# Method Post
@app.route('/addSalon', methods=['POST'])
def addSalon():
    Salones = db['Salones']
    idSalon = request.form['idSalones']
    numero = request.form['numero_salon']
    piso = request.form['Piso']
    capacidad = request.form['Capacidad_estudiantes']
    idIluminacion = request.form['Iluminacion_idIluminacion']
    idMesa = request.form['Mesas_idMesas']
    idTablero = request.form['tablero_idtablero']
    Tamano = request.form['Tamano']

    if idSalon and numero and piso and capacidad and idIluminacion and idMesa and idTablero and Tamano:
        salon = Salon(idSalon, numero, piso, capacidad, idIluminacion, idMesa, idTablero, Tamano)
        Salones.insert_one(salon.toDBCollection())
        response = jsonify({
            'idSalon': idSalon,
            'numero_salon': numero,
            'piso': piso,
            'capacidad': capacidad,
            'idIluminacion': idIluminacion,
            'idMesa': idMesa,
            'idTablero': idTablero,
            'Tamano': Tamano
        })
        return redirect(url_for('salones'))
    else:
        return notFound()


# Method delete
@app.route('/deletesalones/<string:Salones_idSalones>')
def deletesalones(Salones_idSalones):
    Salones = db['Salones']
    Salones.delete_one({'idSalones': Salones_idSalones})
    return redirect(url_for('salones'))


# Method Put
@app.route('/editsalones/<string:Salones_idSalones>', methods=['POST'])
def editsalones(Salones_idSalones):
    Salones = db['Salones']
    idSalon = request.form['idSalones']
    numero = request.form['numero_salon']
    piso = request.form['Piso']
    capacidad = request.form['Capacidad_estudiantes']
    idIluminacion = request.form['Iluminacion_idIluminacion']
    idMesa = request.form['Mesas_idMesas']
    idTablero = request.form['tablero_idtablero']
    Tamano = request.form['Tamano']

    if idSalon and numero and piso and capacidad and idIluminacion and idMesa and idTablero and Tamano:
        Salones.update_one({'idSalones': Salones_idSalones}, {'$set': {'idSalon': idSalon,
                                                                     'numero_salon': numero,
                                                                     'Piso': piso,
                                                                     'Capacidad_estudiantes': capacidad,
                                                                     'Iluminacion_idIluminacion': idIluminacion,
                                                                     'Mesas_idMesas': idMesa,
                                                                     'tablero_idtablero': idTablero,
                                                                     'Tamano': Tamano}})
        response = jsonify({'message': 'Producto ' + Salones_idSalones + ' actualizado correctamente'})
        return redirect(url_for('salones'))
    else:
        return notFound()
'''Reservas'''
@app.route('/reservas')
def reservas():
    Reserva = db['Reserva']
    ReservasRecibidas = Reserva.find()
    return render_template('reservas.html', Reserva = ReservasRecibidas)
# Method Post
@app.route('/addReservas', methods=['POST'])
def addReservas():
    Reservas = db['Reserva']
    idReserva = request.form['idReserva']
    Hora_fin = request.form['Hora_fin']
    Hora_inicio = request.form['Hora_inicio']
    Motivo_idMotivo = request.form['Motivo_idMotivo']
    Salones_idSalones = request.form['Salones_idSalones']
    Usuarios_idUsuarios = request.form['Usuarios_idUsuarios']

    if idReserva and Hora_fin and Hora_inicio and Motivo_idMotivo and Salones_idSalones and Usuarios_idUsuarios:
        reserva = Reserva(idReserva, Hora_fin, Hora_inicio, Motivo_idMotivo, Salones_idSalones, Usuarios_idUsuarios)
        Reservas.insert_one(reserva.toDBCollection())
        response = jsonify({
            'idReserva': idReserva,
            'Hora_fin': Hora_fin,
            'Hora_inicio': Hora_inicio,
            'Motivo_idMotivo': Motivo_idMotivo,
            'Salones_idSalones': Salones_idSalones,
            'Usuarios_idUsuarios': Usuarios_idUsuarios
        })
        return redirect(url_for('reservas'))
    else:
        return notFound()

# Method delete
@app.route('/deletereservas/<string:Reserva_idReserva>')
def deletereservas(Reserva_idReserva):
    Reservas = db['Reserva']
    Reservas.delete_one({'idReserva': Reserva_idReserva})
    return redirect(url_for('reservas'))

# Method Put
@app.route('/editreservas/<string:Reserva_idReserva>', methods=['POST'])
def editreservas(Reserva_idReserva):
    Reservas = db['Reserva']
    idReserva = request.form['idReserva']
    Hora_fin = request.form['Hora_fin']
    Hora_inicio = request.form['Hora_inicio']
    Motivo_idMotivo = request.form['Motivo_idMotivo']
    Salones_idSalones = request.form['Salones_idSalones']
    Usuarios_idUsuarios = request.form['Usuarios_idUsuarios']

    if idReserva and Hora_fin and Hora_inicio and Motivo_idMotivo and Salones_idSalones and Usuarios_idUsuarios:
        Reservas.update_one({'idReserva': Reserva_idReserva}, {'$set': {'idReserva': idReserva,
                                                                        'hora_fin': Hora_fin,
                                                                        'hora_inicio': Hora_inicio,
                                                                        'Motivo_idMotivo': Motivo_idMotivo,
                                                                        'Salones_idSalones': Salones_idSalones,
                                                                        'Usuarios_idUsuarios': Usuarios_idUsuarios}})
        response = jsonify({'message': 'Reserva ' + Reserva_idReserva + ' actualizado correctamente'})
        return redirect(url_for('reservas'))
    else:
        return notFound()
'''Ocupacion'''
@app.route('/ocupacion')
def ocupacion():
    Ocu = db['Ocupacion']
    OcuRecibidas = Ocu.find()
    return render_template('ocupacion.html', Ocu = OcuRecibidas)
#Method Post
@app.route('/addOcupacion', methods=['POST'])
def addOcupacion():
    Ocu = db['Ocupacion']
    idOcupacion = request.form['idOcupacion']    
    Afiliacion = request.form['Afiliacion']

    if idOcupacion and Afiliacion :
        ocupacion = Ocupacion(idOcupacion,Afiliacion)
        Ocu.insert_one(ocupacion.toDBCollection())
        response = jsonify({
            'idOcupacion' : idOcupacion,
            'Afiliacion' : Afiliacion,
        })
        return redirect(url_for('ocupacion'))
    else:
        return notFound()

#Method delete
@app.route('/deleteOcu/<string:Ocupacion_name>')
def deleteOcu(Ocupacion_name):
    Ocu = db['Ocupacion']
    Ocu.delete_one({'idOcupacion' : Ocupacion_name})
    return redirect(url_for('ocupacion'))

#Method put
@app.route('/editOcu/<string:Ocupacion_name>', methods=['POST'])
def editOcu(Ocupacion_name):
    Ocu = db['Ocupacion']
    idOcupacion = request.form['idOcupacion']
    Afiliacion = request.form['Afiliacion']


    if idOcupacion and Afiliacion:
        Ocu.update_one({'idOcupacion' : Ocupacion_name}, {'$set' : {'idOcupacion' : idOcupacion, 'Afiliacion' : Afiliacion}})
        response = jsonify({'message' : 'Ocupacion ' + Ocupacion_name + ' actualizado correctamente'})
        return redirect(url_for('ocupacion'))
    else:
        return notFound()

@app.errorhandler(404)
def notFound(error=None):
    message ={
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run(debug=True, port=4000)