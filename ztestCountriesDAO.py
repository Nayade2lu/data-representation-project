from zCountriesDAO import CountriesDAO
#create
latestid = CountriesDAO.create(('Norway', 2))
# find by id
result = CountriesDAO.findByID(latestid)
print (result)
#update
#CountriesDAO.update (("Finland",2,latestid))
#result = CountriesDAO.findByID(latestid)
#print (result)
# get all
allStudents = CountriesDAO.getAll()
for student in allStudents:
    print(student)
# delete
#CountriesDAO.delete(latestid)