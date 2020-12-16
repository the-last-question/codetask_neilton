
def caesar(data, realoc_pos, mode):
    alphabet = 'abcdefghijklmnopqrstuvwyzàáãâéêóôõíúçABCDEFGHIJKLMNOPQRSTUVWYZÀÁÃÂÉÊÓÕÍÚÇ'
    output = ''
    for c in data:
        pos = alphabet.find(c)
        if pos == -1:
            output += c
        else:
            new_pos = pos + realoc_pos if mode == 1 else pos - realoc_pos
            new_pos = new_pos % len(alphabet)
            output += alphabet[new_pos:new_pos+1]
    return output

realoc_pos = 3 #realoca a posição relativa do novo 'a'
original = 'Oi, tudo bem? Faremos um ataque ao norte!'
print('Original:  ', original)
ciphered = caesar(original, realoc_pos, 1)
print('Encriptada:', ciphered)
plain = caesar(ciphered, realoc_pos, 0)
print('Decriptada:', plain)