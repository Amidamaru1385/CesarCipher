# put your python code here
def cesar_code(key, text, decipher):
    const_upper = []
    const_lower = []
    new_text = ''
    power = 0
    is_eng = True
    if text[0] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
        is_eng = True
    if is_eng:
        for i in range(ord('a'),ord('z') + 1):
            const_lower.append(chr(i))
        for i in range(ord('A'),ord('Z') + 1):
            const_upper.append(chr(i))
        power = 26
    else:
        for i in range(ord('а'),ord('я') + 1):
            const_lower.append(chr(i))
        for i in range(ord('А'),ord('Я') + 1):
            const_upper.append(chr(i))
        power = 32
    if decipher == 'y':
        key = power - key
    for symbol in text:
        if symbol.isupper():
            new_text += const_upper[(const_upper.index(symbol) + key) % power]
        elif symbol.islower():
            new_text += const_lower[(const_lower.index(symbol) + key) % power]
        else:
            new_text += symbol
    return new_text


text = input().split()
new_line = ''
counter = 0
for i in range(len(text)):          #Шифруем текст со сдвигом каждого слова на количество букв в слове
    for j in range(len(text[i])):
        if text[i][j].isalpha():
            counter += 1
    new_line += cesar_code(counter, text[i], 'n')
    new_line += ' '
    counter = 0
new_line = new_line[0: len(new_line) - 1] #Убирает пробел в конце строки
print(new_line)