from flask import Flask, jsonify, request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():                             #Funcion que no Recibe nada y Retorna Index
    return 'Index'

@app.route('/ping')
def ping():                              #si invoco '/ping' en la ruta base + '\ping' retorna 'pong'
    return jsonify({"message":"pong"})   #Funcion json clave mensaje

@app.route('/usuarios/<string:nombre>')  #Cuando Tenga la ruta Base + /usuarios/ y una cadena 'algun_nombre'
def usuario_by_name(nombre):             #la Funcion Recibe lo que esta a Continuacion de Usuarios
    return jsonify({"name" : nombre})    #y lo Retorna

@app.route('/usuarios/<int:id>')         #Cuando Tenemos la Ruta Base + /usuarios/ y un Entero la funcion
def usuario_by_id(id):                   #Recibe lo que esta a Continuacion de usuarios
    return jsonify({"id": id})

@app.route('/<path:nombre>')
def no_hacer(nombre):
    return escape(nombre)

#GET Consulta Todos los Recursos
@app.route('/recurso', methods = ['GET'])
def get_recursos():
    return jsonify({"data": "Lista de Todos los Items de Este Recurso"})

#POST nuevo Recursos
@app.route('/recurso', methods = ['POST'])
def post_recurso():
    print(request.get_json())
    body = request.get_json()
    name = body["name"]
    modelo = body["modelo"]
    #insertar en la BD
    return jsonify({"data": {
        "name": name,
        "modelo": modelo
    }})
    
@app.route('/recurso/<int:id>', methods = ['GET'])
def get_recurso_by_id(id):
    #Buscar en la BD un Registro con su id
    return jsonify({"recurso":{
        "name": "nombre correspondiente a ese id",
        "modelo": "modelo correspondiente a ese id"
    }})















if __name__ == '__main__':
    app.run(debug = True, port = 5000)