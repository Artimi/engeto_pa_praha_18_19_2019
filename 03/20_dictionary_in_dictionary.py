database = {'id123': {},'id124': {},'id125': {}}

FirstDict = {'name': 'Thomas', 'age': 45, 'Country': 'Czechia', 'City': 'Brno'}
SecondDict = {'name': 'Daniel', 'age': 34, 'Country': 'Czechia', 'City': 'Prague'}
ThirdDict = {'name': 'Eva', 'age': 43, 'Country': 'Czechia', 'City': 'Olomouc'}

database['id123'] = FirstDict
database['id124'] = SecondDict
database['id125'] = ThirdDict

print(database)
