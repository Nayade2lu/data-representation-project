#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response
#from flask_cors import CORS

app = Flask(__name__,
            static_url_path='', 
            static_folder='../')

#CORS(app)

countries = [
    {
        "id":"1",
        "countryname":"Spain",
        "continent":"Europe",
        "equalityrate":3
    },
    {
        "id":"2",
        "countryname":"India",
        "continent":"Asia",
        "equalityrate":2
    }
]

@app.route('/countries', methods=['GET'])
def get_countries():
    return jsonify( {'countries':countries})
# curl -i http://localhost:5000/countries

@app.route('/countries/<string:id>', methods =['GET'])
def get_country(id):
    foundcountries = list(filter(lambda t : t['id'] == id , countries))
    if len(foundcountries) == 0:
        return jsonify( { 'country' : '' }),204
    return jsonify( { 'country' : foundcountries[0] })
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
    countries.append(country)
    return jsonify( {'country':country }),201
# sample test
# curl -i -H "Content-Type:application/json" -X POST -d '{"id":"12 D 1234","country":"Fiat","continent":"Punto","equalityrate":3000}' http://localhost:5000/countries
# for windows use this one
# curl -i -H "Content-Type:application/json" -X POST -d "{\"id\":\"12 D 1234\",\"country\":\"Fiat\",\"continent\":\"Punto\",\"equalityrate\":3000}" http://localhost:5000/countries
@app.route('/countries/<string:id>', methods =['PUT'])
def update_country(id):
    foundcountries=list(filter(lambda t : t['id'] ==id, countries))
    if len(foundcountries) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'country' in request.json and type(request.json['country']) != str:
        abort(400)
    if 'continent' in request.json and type(request.json['continent']) is not str:
        abort(400)
    if 'equalityrate' in request.json and type(request.json['equalityrate']) is not int:
        abort(400)
    foundcountries[0]['countryname']  = request.json.get('countryname', foundcountries[0]['countryname'])
    foundcountries[0]['continent'] =request.json.get('continent', foundcountries[0]['continent'])
    foundcountries[0]['equalityrate'] =request.json.get('equalityrate', foundcountries[0]['equalityrate'])
    return jsonify( {'country':foundcountries[0]})
#curl -i -H "Content-Type:application/json" -X PUT -d '{"country":"Fiesta"}' http://localhost:5000/countries/181%20G%201234
# for windows use this one
#curl -i -H "Content-Type:application/json" -X PUT -d "{\"country\":\"Fiesta\"}" http://localhost:5000/countries/181%20G%201234

@app.route('/countries/<string:id>', methods =['DELETE'])
def delete_country(id):
    foundcountries = list(filter (lambda t : t['id'] == id, countries))
    if len(foundcountries) == 0:
        abort(404)
    countries.remove(foundcountries[0])
    return  jsonify( { 'result':True })

#@app.errorhandler(404)
#def not_found404(error):
    #return make_response( jsonify( {'error':'Not found' }), 404)

#@app.errorhandler(400)
#def not_found400(error):
    #return make_response( jsonify( {'error':'Bad Request' }), 400)


if __name__ == '__main__' :
    app.run(debug= True)