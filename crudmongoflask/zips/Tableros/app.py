from flask import Flask, render_template, request, Response, jsonify, redirect, url_for
import database as dbase  
from Motivo import Motivo
from Iluminacion import Iluminacion
from Mesas import Mesas
from Tablero import Tablero

db = dbase.dbConnection()

app = Flask(__name__)

'''
#------ ILUMINACION

#Rutas de la app
@app.route('/')
def home():
    Iluminacion = dbase['Iluminacion']
    IluminacionReceived = Iluminacion.find()
    return render_template('index.html', Iluminacion = IluminacionReceived)

#Method Post
@app.route('/Iluminacion', methods=['POST'])
def addIluminacion():
    Iluminacion = dbase['Iluminacion']
    idIluminacion = request.form['idIluminacion']
    Color = request.form['Color']
    Origen = request.form['Origen']
    Regulacion = request.form['Regulacion']
    Ubicacion = request.form['Ubicacion']

    if idIluminacion and Color and Origen and Regulacion and Ubicacion:
        Iluminacion = Iluminacion(idIluminacion,Color,Origen,Regulacion, Ubicacion)
        Iluminacion.insert_one(Iluminacion.toDBCollection())
        response = jsonify({
            'idiluminacion' : idIluminacion,
            'Color' : Color,
            'Origen' : Origen,
            'Regulacion' : Regulacion,
            'Ubicacion' : Ubicacion
        })
        return redirect(url_for('home'))
    else:
        return notFound()

#Method delete
@app.route('/deleteIlum/<string:Iluminacion_name>')
def deleteIlum(Iluminacion_name):
    Iluminacion = dbase['Iluminacion']
    Iluminacion.delete_one({'Iluminacion' : Iluminacion_name})
    return redirect(url_for('home'))

#Method put
@app.route('/editIlum/<string:Iluminacion_name>', methods=['POST'])
def editIlum(Iluminacion_name):
    Iluminacion = dbase['Iluminacion']
    idIluminacion = request.form['idIluminacion']
    Color = request.form['Color']
    Origen = request.form['Origen']
    Regulacion = request.form['Regulacion']
    Ubicacion = request.form['Ubicacion']

    if idIluminacion and Color and Origen and Regulacion and Ubicacion:
        Iluminacion.update_one({'idIluminacion' : idIluminacion}, {'$set' : {'idIluminacion' : idIluminacion, 'Color' : Color, 'Origen' : Origen, 'Regulacion' : Regulacion, 'Ubicacion' : Ubicacion}})
        response = jsonify({'message' : 'Producto ' + Iluminacion_name + ' actualizado correctamente'})
        return redirect(url_for('home'))
    else:
        return notFound()

#------ MESAS

#Rutas de la app
@app.route('/')
def home():
    Mesas = dbase['Mesas']
    MesasRecibido = Mesas.find()
    return render_template('index.html', Mesas = MesasRecibido)

#Method Post
@app.route('/Mesas', methods=['POST'])
def addMesas():
    Mesas = dbase['Mesas']
    idMesas = request.form['idMesas']
    Color = request.form['Color']
    Tamano = request.form['Tamano']

    if idMesas and Color and Tamano:
        Mesas = Mesas(idMesas,Color,Tamano)
        Mesas.insert_one(Mesas.toDBCollection())
        response = jsonify({
            'idMesas' : idMesas,
            'Color' : Color,
            'Tamano' : Tamano
        })
        return redirect(url_for('home'))
    else:
        return notFound()

#Method delete
@app.route('/deleteMesas/<string:Mesas_name>')
def deleteMesas(Mesas_name):
    Mesas = dbase['Mesas']
    Mesas.delete_one({'Mesas' : Mesas_name})
    return redirect(url_for('home'))

#Method put
@app.route('/editMesas/<string:Mesas_name>', methods=['POST'])
def editMesas(Mesas_name):
    Mesas = dbase['Mesas']
    idMesas = request.form['idMesas']
    Color = request.form['Color']
    Tamano = request.form['Tamano']

    if idMesas and Color and Tamano:
        Mesas.update_one({'idMesas' : idMesas}, {'$set' : {'idMesas' : idMesas, 'Color' : Color, 'Tamano' : Tamano}})
        response = jsonify({'message' : 'Producto ' + Mesas_name + ' actualizado correctamente'})
        return redirect(url_for('home'))
    else:
        return notFound()

'''
#------ TABLERO

#Rutas de la app
@app.route('/')
def home():
    Tablero = dbase['Tablero']
    TableroRecibido = Tablero.find()
    return render_template('index.html', Tablero = TableroRecibido)

#Method Post
@app.route('/Mesas', methods=['POST'])
def addTablero():
    Tablero = dbase['Tablero']
    idTablero = request.form['idTablero']
    Tamano = request.form['Tamano']
    Tipo = request.form['Tipo']

    if idTablero and Tamano and Tipo:
        Tablero = Tablero(idTablero,Tamano,Tipo)
        Tablero.insert_one(Tablero.toDBCollection())
        response = jsonify({
            'idTablero' : idTablero,
            'Tamano' : Tamano,
            'Tipo' : Tipo
        })
        return redirect(url_for('home'))
    else:
        return notFound()

#Method delete
@app.route('/deleteTablero/<string:Tablero_name>')
def deleteTablero(Tablero_name):
    Tablero = dbase['Tablero']
    Tablero.delete_one({'Tablero' : Tablero_name})
    return redirect(url_for('home'))

#Method put
@app.route('/editTablero/<string:Tablero_name>', methods=['POST'])
def editTablero(Tablero_name):
    Tablero = dbase['Tablero']
    idTablero = request.form['idTablero']
    Tamano = request.form['Tamano']
    Tipo = request.form['Tipo']

    if idTablero and Tamano and Tipo:
        Tablero.update_one({'idTablero' : idTablero}, {'$set' : {'idTablero' : idTablero, 'Tamano' : Tamano, 'Tipo' : Tipo}})
        response = jsonify({'message' : 'Producto ' + Tablero_name + ' actualizado correctamente'})
        return redirect(url_for('home'))
    else:
        return notFound()

'''
#------ MOTIVOS

#Rutas de la aplicación
@app.route('/')
def home():
    Motivos = db['Motivo']
    Motivosrecibidos = Motivos.find()
    return render_template('index.html', Motivos = Motivosrecibidos)

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
        return redirect(url_for('home'))
    else:
        return notFound()

#Method delete
@app.route('/delete/<string:indicacion_name>')
def delete(indicacion_name):
    Motivos = db['Motivo']
    Motivos.delete_one({'indicacion' : indicacion_name})
    return redirect(url_for('home'))

#Method Put
@app.route('/edit/<string:indicacion_name>', methods=['POST'])
def edit(indicacion_name):
    Motivos = db['Motivo']
    IdMotivo = request.form['IdMotivo']
    indicacion = request.form['indicacion']

    if IdMotivo and indicacion:
        Motivos.update_one({'indicacion' : indicacion_name}, {'$set' : {'IdMotivo' : IdMotivo, 'indicacion' : indicacion}})
        response = jsonify({'message' : 'Producto ' + indicacion_name + ' actualizado correctamente'})
        return redirect(url_for('home'))
    else:
        return notFound()

'''

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
