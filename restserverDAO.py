
from flask import Flask, url_for, request, redirect, abort, jsonify
from zCountriesDAO import CountryDao

app = Flask(__name__, static_url_path='', static_folder='staticpages')


@app.route('/')
def index():
    return "hello"
#get all


@app.route('/countries')
def getAll():
    return jsonify(CountryDAO.getAll())
# find By id


@app.route('/countries/<int:id>')
def findById(id):
    return jsonify(CountryDAO.findById(id))

# create
# curl -X POST -d "{\"countryname\":\"test\", \"continent\":\"some guy\", \"equalityrate\":123}" http://127.0.0.1:5000/countries


@app.route('/countries', methods=['POST'])
def create():
   
    if not request.json:
        abort(400)

    book = {
        "id": request.json["id"],
        "countryname": request.json["countryname"],
        "continent": request.json["continent"],
        "equalityrate": request.json["equalityrate"]
    }
    return jsonify(CountryDAO.create(book))

    return "served by Create"

#update
# curl -X PUT -d "{\"countryname\":\"new countryname\", \"equalityrate\":999}" -H "content-type:application/json" http://127.0.0.1:5000/countries/1


@app.route('/countries/<int:id>', methods=['PUT'])
def update(id):
    foundBook=CountryDAO.findById(id)
    print (foundBook)
    if foundBook == {}:
        return jsonify({}), 404
    currentBook = foundBook
    if 'countryname' in request.json:
        currentBook['countryname'] = request.json['countryname']
    if 'continent' in request.json:
        currentBook['continent'] = request.json['continent']
    if 'equalityrate' in request.json:
        currentBook['equalityrate'] = request.json['equalityrate']
    CountryDAO.update(currentBook)

    return jsonify(currentBook)

#delete
# curl -X DELETE http://127.0.0.1:5000/countries/1


@app.route('/countries/<int:id>', methods=['DELETE'])
def delete(id):
    CountryDAO.delete(id)

    return jsonify({"done": True})


if __name__ == "__main__":
    app.run(debug=True)