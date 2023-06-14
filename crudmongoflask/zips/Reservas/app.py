from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase  
from reserva import Reserva

db = dbase.dbConnection()

app = Flask(__name__)

# Rutas de la aplicación
@app.route('/')
def home():
    Reservas = db['Reserva']
    Reservasrecibidas = Reservas.find()
    return render_template('index.html', Reservas=Reservasrecibidas)

# Method Post
@app.route('/Reservas', methods=['POST'])
def addMotivo():
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
        return redirect(url_for('home'))
    else:
        return notFound()

# Method delete
@app.route('/delete/<string:Reserva_idReserva>')
def delete(Reserva_idReserva):
    Reservas = db['Reserva']
    Reservas.delete_one({'idReserva': Reserva_idReserva})
    return redirect(url_for('home'))

# Method Put
@app.route('/edit/<string:Reserva_idReserva>', methods=['POST'])
def edit(Reserva_idReserva):
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
        return redirect(url_for('home'))
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