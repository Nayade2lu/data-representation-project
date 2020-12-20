from zCountriesDAO import CountryDao

country1 = {
    'id': 1234567,
    'equalityrate': 12,
    'continent': 'jk',
    'countryname': 'some fantasy country'

}
country2 = {
    'id': 1234567,
    'equalityrate': 999,
    'continent': 'mary',
    'countryname': 'had a little lamb'

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