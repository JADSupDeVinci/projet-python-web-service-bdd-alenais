from flask import jsonify, Flask

from database.model import Habitante

app = Flask(__name__)#donne le nom de notre controller et il faut faire importer et installer Flask

@app.route('/getAllDepartments', methods=['GET'])
def get_all_departments():
    results = Departments.getAll()#on recupere toutes les données de notre collection
    return jsonify(Departments.toDict() for department in Departments)#transforme notre collection en json

app.run(host = 'localhost', port=5000)#lance notre application sur le port 5000
