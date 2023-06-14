from flask import Flask, render_template, request, jsonify, redirect, url_for

import database as dbase
from salon import Salon

db = dbase.dbConnection()

app = Flask(__name__)


# Rutas de la aplicación
@app.route('/')
def home():
    Salones = db['Salones']
    Salonesrecibidos = Salones.find()
    return render_template('index.html', Salones=Salonesrecibidos)


# Method Post
@app.route('/Salon', methods=['POST'])
def addTablero():
    Salones = db['Salones']
    idSalon = request.form['idSalones']
    numero = request.form['numero_salon']
    piso = request.form['Piso']
    capacidad = request.form['Capacidad_estudiantes']
    idIluminacion = request.form['Iluminacion_idIluminacion']
    idMesa = request.form['Mesas_idMesas']
    idTablero = request.form['tablero_idtablero']
    Tamano3 = request.form['Tamano3']

    if idSalon and numero and piso and capacidad and idIluminacion and idMesa and idTablero and Tamano3:
        salon = Salon(idSalon, numero, piso, capacidad, idIluminacion, idMesa, idTablero, Tamano3)
        Salones.insert_one(salon.toDBCollection())
        response = jsonify({
            'idSalon': idSalon,
            'numero_salon': numero,
            'piso': piso,
            'capacidad': capacidad,
            'idIluminacion': idIluminacion,
            'idMesa': idMesa,
            'idTablero': idTablero,
            'Tamano3': Tamano3
        })
        return redirect(url_for('home'))
    else:
        return notFound()


# Method delete
@app.route('/delete/<string:Salones_idSalones>')
def delete(Salones_idSalones):
    Salones = db['Salones']
    Salones.delete_one({'idSalones': Salones_idSalones})
    return redirect(url_for('home'))


# Method Put
@app.route('/edit/<string:Salones_idSalones>', methods=['POST'])
def edit(Salones_idSalones):
    Salones = db['Salones']
    idSalon = request.form['idSalones']
    numero = request.form['numero_salon']
    piso = request.form['Piso']
    capacidad = request.form['Capacidad_estudiantes']
    idIluminacion = request.form['Iluminacion_idIluminacion']
    idMesa = request.form['Mesas_idMesas']
    idTablero = request.form['tablero_idtablero']
    Tamano3 = request.form['Tamano3']

    if idSalon and numero and piso and capacidad and idIluminacion and idMesa and idTablero and Tamano3:
        Salones.update_one({'idSalon': Salones_idSalones}, {'$set': {'idSalon': idSalon,
                                                                     'numero_salon': numero,
                                                                     'Piso': piso,
                                                                     'Capacidad_estudiantes': capacidad,
                                                                     'Iluminacion_idIluminacion': idIluminacion,
                                                                     'Mesas_idMesas': idMesa,
                                                                     'tablero_idtablero': idTablero,
                                                                     'Tamano3': Tamano3}})
        response = jsonify({'message': 'Producto ' + Salones_idSalones + ' actualizado correctamente'})
        return redirect(url_for('home'))
    else:
        return notFound()


@app.errorhandler(404)
def notFound(error=None):
    message = {
        'message': 'No encontrado ' + request.url,
        'status': '404 Not Found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response


if __name__ == '__main__':
    app.run(debug=True, port=4000)
