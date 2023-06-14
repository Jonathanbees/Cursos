from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase
from usuarios import Usuarios

db = dbase.dbConnection()

app = Flask(__name__)


# Rutas de la aplicación
@app.route('/')
def home():
    Usuarioss = db['Usuarios']
    UsuariosRecibidos = Usuarioss.find()
    return render_template('index.html', Usuarioss=UsuariosRecibidos)


# Method Post
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
        return redirect(url_for('home'))
    else:
        return notFound()


##########################
# Method delete
@app.route('/delete/<string:Usuarios_idUsuarios>')
def delete(Usuarios_idUsuarios):
    Usuarioss = db['Usuarios']
    Usuarioss.delete_one({'idUsuarios': Usuarios_idUsuarios})
    return redirect(url_for('home'))


# Method Put
@app.route('/edit/<string:Usuarios_idUsuarios>', methods=['POST'])
def edit(Usuarios_idUsuarios):
    Usuarioss = db['Usuarios']
    idUsuarios = request.form['idUsuarios']
    Nombre = request.form['Nombre']
    Apellido = request.form['Apellido']
    Celular = request.form['Celular']
    Correo = request.form['Correo']
    Ocupacion_idOcupacion = request.form['Ocupacion_idOcupacion']
    Fecha_nacimiento = request.form['Fecha_nacimiento']

    if idUsuarios and Nombre and Apellido and Celular and Correo and Ocupacion_idOcupacion and Fecha_nacimiento:
        Usuarioss.update_one({'IdPersona': Usuarios_idUsuarios}, {'$set': {'idUsuarios': idUsuarios,
                                                                           'Nombre': Nombre,
                                                                           'Apellido': Apellido,
                                                                           'Celular': Celular,
                                                                           'Correo': Correo,
                                                                           'Ocupacion_idOcupacion': Ocupacion_idOcupacion,
                                                                           'Fecha_nacimiento': Fecha_nacimiento}})
        response = jsonify({'message': 'Persona ' + Usuarios_idUsuarios + ' actualizado correctamente'})
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
