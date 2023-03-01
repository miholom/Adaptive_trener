# 4.3 Caesar cipher - Шифр Цезаря
import copy
# ввод данных, создание переменных,констант
ALPHABET = ' abcdefghijklmnopqrstuvwxyz' 
shift_input = int(input()) # int(27)
strings = input().lstrip(' ').rstrip(' ') # "abc"
string_on_exit = []
d = ""
ALPHABET_LEN = len(ALPHABET)

# Заменил повторяющийся код функцией, вспомнил как список передать в функцию с помощью *
def func(cezarPass, ALPHABET_LEN, *kwrg):
        if cezarPass == ALPHABET_LEN:
            string_on_exit.append(ALPHABET[cezarPass-ALPHABET_LEN])
        elif cezarPass > ALPHABET_LEN:
            string_on_exit.append(ALPHABET[cezarPass-ALPHABET_LEN])
        elif cezarPass < ALPHABET_LEN:
            string_on_exit.append(ALPHABET[cezarPass])

# Запускаем цикл через который каждый символ в алфавите
for i, string in enumerate(strings):
    a = ALPHABET.find(string)
    cezarPass = a+shift_input

# В первом блоке просматриваем вариант когда символ сдвигается в пределах алвафита    
    if 0 <= shift_input <= ALPHABET_LEN:
        func(cezarPass, ALPHABET_LEN, *string_on_exit)

# во втором блоке просматриваем вариант когда уходим в минус
    elif (0 > shift_input):
        while 0 > cezarPass:
            cezarPass += ALPHABET_LEN
        func(cezarPass, ALPHABET_LEN, *string_on_exit)

# в третьем блоке просматриваем вариант когда уходим в огромный плюс    
    elif (shift_input > ALPHABET_LEN):
        while cezarPass > ALPHABET_LEN:
            cezarPass -= ALPHABET_LEN
        func(cezarPass, ALPHABET_LEN, *string_on_exit)

# В конце через цикл for и формат выводим на печать получившееся решение
for i in string_on_exit:
    d += str(i)

print(f"""Result: \"{d}\"""")
