from zCountriesDAO import CountryDao

country1 = {
    'id': 3,
    'equalityrate': 12,
    'continent': 'Eur',
    'countryname': 'Germany'

}
country2 = {
    'id': 4,
    'equalityrate': 999,
    'continent': 'Asia',
    'countryname': 'Thailand'

}

#returnValue = countryDao.create(country)
returnValue = CountryDao.getAll()
#print(returnValue)
returnValue = CountryDao.findById(country2['id'])
#print("find By Id")
#print(returnValue)
returnValue = CountryDao.update(country2)
#print(returnValue)
returnValue = CountryDao.findById(country2['id'])
#print(returnValue)
returnValue = CountryDao.delete(country2['id'])
print(returnValue)
print("deleted")
returnValue = CountryDao.getAll()
print(returnValue)