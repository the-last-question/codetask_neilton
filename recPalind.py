def ispalindrome(word):
    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    return ispalindrome(word[1:-1])


isPalin = ispalindrome(input('Digite a palavra que deseja verificar: '))

if isPalin:
    print('A palavra inserida é palindromo')
else:
    print('Não é palindromo')