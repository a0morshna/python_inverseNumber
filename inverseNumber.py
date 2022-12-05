def inverseNumber(param):

  numberInverse = ''

  if (int(param / 10) == 0):
        
    number = str(param % 10)
    numberInverse += number

  else:
        
    number = str(param % 10)
    numberInverse += number + inverseNumber(int(param / 10))

  return numberInverse

print(inverseNumber(473))