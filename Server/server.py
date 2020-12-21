#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response
#from flask_cors import CORS
from newtestDAO import yCountryDAO


app = Flask(__name__,
            static_url_path='',     
            static_folder='../')

#SET FLASK_APP=serverCORS(app)


#@app.route('/')
#def hello_world():
    #return 'Hello'

@app.route('/countries', methods=['GET'])
def getAll():
    results = yCountryDAO.getAll()
    return jsonify(results)
# curl -i http://localhost:5000/countries

@app.route('/countries/<string:id>', methods =['GET'])
def findById(id):
    foundcountry = yCountryDAO.findById(id)
    if not foundcountry:
        abort(404)
    return jsonify(foundcountry)
#curl -i http://localhost:5000/countries/1

@app.route('/countries', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    if not 'id' in request.json:
        abort(400)
    country={
        "countryname": request.json['countryname'],
        "continent":request.json['continent'],
        "equalityrate":request.json['equalityrate']
    }
    values = (country['countryname'], ['continent'], ['equalityrate'])
    newid = yCountryDAO.create(values)
    country['id'] = newid
    return jsonify(country)
# sample test
# curl -i -H "Content-Type:application/json" -X POST -d '{"id":"12 D 1234","country":"Fiat","continent":"Punto","equalityrate":3000}' http://localhost:5000/countries
# for windows use this one
# curl -i -H "Content-Type:application/json" -X POST -d "{\"id\":\"12 D 1234\",\"country\":\"Fiat\",\"continent\":\"Punto\",\"equalityrate\":3000}" http://localhost:5000/countries
@app.route('/countries/<string:id>', methods =['PUT'])
#def update_country(id):
    #foundCountries=list(filter(lambda t : t['id'] ==id, countries))
    #if len(foundCountries) == 0:
        #abort(404)
    #if not request.json:
        #abort(400)
    #if 'countryname' in request.json and type(request.json['countryname']) != str:
        #abort(400)
    #if 'continent' in request.json and type(request.json['continent']) is not str:
        #abort(400)
    #if 'equalityrate' in request.json and type(request.json['equalityrate']) is not int:
        #abort(400)
    #values = (foundCountries['countryname'], ['continent'], ['equalityrate'])
    #yCountryDAO.update(values)
    #return jsonify(foundCountries)

def update(id):
    foundCountry = yCountryDAO.findByID(id)
    if not foundCountry:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'equalityrate' in reqJson and type(reqJson['equalityrate']) is not int:
        abort(400)

    if 'countryname' in reqJson:
        foundCountry['countryname'] = reqJson['countryname']
    if 'continent' in reqJson:
        foundCountry['continent'] = reqJson['continent']
    if 'equalityrate' in reqJson:
        foundCountry['equalityrate'] = reqJson['equalityrate']
    values = (foundCountry['countryname'],foundCountry['continent'],foundCountry['equalityrate'],foundBook['id'])
    yCountryDAO.update(values)
    return jsonify(foundCountry)
#curl -i -H "Content-Type:application/json" -X PUT -d '{"make":"Fiesta"}' http://localhost:5000/cars/181%20G%201234
# for windows use this one
#curl -i -H "Content-Type:application/json" -X PUT -d "{\"make\":\"Fiesta\"}" http://localhost:5000/cars/181%20G%201234


@app.route('/countries/<string:id>', methods =['DELETE'])
def delete(id):
    yCountryDAO.delete(id)
    return jsonify({"done":True})

#@app.errorhandler(404)
#def not_found404(error):
    #return make_response( jsonify( {'error':'Not found' }), 404)

#@app.errorhandler(400)
#def not_found400(error):
    #return make_response( jsonify( {'error':'Bad Request' }), 400)


if __name__ == '__main__' :
    app.run(debug= True)