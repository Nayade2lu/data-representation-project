#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response
#from flask_cors import CORS
from zCountriesDAO import CountryDao


app = Flask(__name__,
            static_url_path='', 
            static_folder='../')

#SET FLASK_APP=serverCORS(app)


@app.route('/')
def hello_world():
    return 'Hello'

@app.route('/countries', methods=['GET'])
def get_countries():
    results = CountryDao.getAll()
    return jsonify(results)
# curl -i http://localhost:5000/countries

@app.route('/countries/<string:id>', methods =['GET'])
def get_country(id):
    foundcountries = CountryDao.findById(id)
    if not foundcountries:
        abort(404)
    return jsonify(foundcountries)
#curl -i http://localhost:5000/countries/1

@app.route('/countries', methods=['POST'])
def create_country():
    if not request.json:
        abort(400)
    if not 'id' in request.json:
        abort(400)
    country={
        "id":  request.json['id'],
        "countryname": request.json['countryname'],
        "continent":request.json['continent'],
        "equalityrate":request.json['equalityrate']
    }
    values = (country['countryname'], ['continent'], ['equalityrate'])
    newid = CountryDao.create(values)
    country['id'] = newid
    return jsonify(country)
# sample test
# curl -i -H "Content-Type:application/json" -X POST -d '{"id":"12 D 1234","country":"Fiat","continent":"Punto","equalityrate":3000}' http://localhost:5000/countries
# for windows use this one
# curl -i -H "Content-Type:application/json" -X POST -d "{\"id\":\"12 D 1234\",\"country\":\"Fiat\",\"continent\":\"Punto\",\"equalityrate\":3000}" http://localhost:5000/countries
@app.route('/countries/<string:id>', methods =['PUT'])
def update_country(id):
    foundCountries=list(filter(lambda t : t['id'] ==id, countries))
    if len(foundCountries) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'countryname' in request.json and type(request.json['countryname']) != str:
        abort(400)
    if 'continent' in request.json and type(request.json['continent']) is not str:
        abort(400)
    if 'equalityrate' in request.json and type(request.json['equalityrate']) is not int:
        abort(400)
    values = (foundCountries['countryname'], ['continent'], ['equalityrate'])
    CountryDao.update(values)
    return jsonify(foundCountries)
#curl -i -H "Content-Type:application/json" -X PUT -d '{"make":"Fiesta"}' http://localhost:5000/cars/181%20G%201234
# for windows use this one
#curl -i -H "Content-Type:application/json" -X PUT -d "{\"make\":\"Fiesta\"}" http://localhost:5000/cars/181%20G%201234


@app.route('/countries/<string:id>', methods =['DELETE'])
def delete_country(id):
    deletecountries = CountryDao.delete(id)
    
    return  jsonify({'done':True })

@app.errorhandler(404)
def not_found404(error):
    return make_response( jsonify( {'error':'Not found' }), 404)

@app.errorhandler(400)
def not_found400(error):
    return make_response( jsonify( {'error':'Bad Request' }), 400)


if __name__ == '__main__' :
    app.run(debug= True)