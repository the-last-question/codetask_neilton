def isGoodPass(myPass):
    points = 0
    if len(myPass) >= 8:
        points += 1
    if containsLower(myPass):
        points += 2
    if containsUpper(myPass):
        points += 4
    if points < 7:
        return False, points
    return True, points

def containsLower(myPass):
    for c in myPass:
        if c.islower():
            return True
    return False

def containsUpper(myPass):
    for c in myPass:
        if c.isupper():
            return True
    return False


while True:
    urPass = input('INSIRA UMA SENHA\n')
    isGood, myPoints = isGoodPass(urPass)
    print('senha: '+str(urPass), 'pontos: '+str(myPoints))
    if  isGood:
        print('senha boa')
        break
    else:
        if myPoints == 1:
            print('Falta caracteres com caixa alta e baixa')
        if myPoints == 2:
            print('Senha curta e faltando caixa alta')
        if myPoints == 3:
            print('Falta caracteres com caixa alta')
        if myPoints == 4:
            print('Senha curta e faltando caixa baixa')
        if myPoints == 5:
            print('Falta caixa baixa')
        if myPoints == 6:
            print(str(8 - len(urPass))+' restantes')
        continue



