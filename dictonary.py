capitals={'USA':'WASHINGTON DC',
          'india': 'new delhi',
          'china': 'beijing', 
          'russia': 'moscow'}
print(capitals["russia"])
print(capitals.get('germany'))
print(capitals.keys())
print(capitals.values())
print(capitals.items())
capitals.update({'gremany':'Berlin'})
capitals.update({'USA': 'Lasvegas'})
capitals.pop('china')
capitals.clear()
for key,Value in capitals.items():
    print

