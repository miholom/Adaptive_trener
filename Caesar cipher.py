# 4.3 Caesar cipher - Шифр Цезаря
import copy
# ввод данных, создание переменных,констант
ALPHABET = ' abcdefghijklmnopqrstuvwxyz' 
shift_input = int(input()) # int(27)
strings = input().lstrip(' ').rstrip(' ') # "abc"
string_on_exit = []
d = ""

# Запускаем цикл через который каждый символ в алфавите
for i, string in enumerate(strings):
    a = ALPHABET.find(string)

# В первом блоке просматриваем вариант когда символ сдвигается в пределах алвафита    
    cezarPass = a+shift_input
    if 0 <= shift_input <= len(ALPHABET):
        if cezarPass == len(ALPHABET):
            string_on_exit.append(ALPHABET[cezarPass-len(ALPHABET)])
        elif cezarPass > len(ALPHABET):
            string_on_exit.append(ALPHABET[cezarPass-len(ALPHABET)])
        elif cezarPass < len(ALPHABET):
            string_on_exit.append(ALPHABET[cezarPass])

# во втором блоке просматриваем вариант когда уходим в минус
    elif (0 > shift_input):
        count = copy.deepcopy(shift_input)
        while 0 > count:
            count += len(ALPHABET)
        cezarPass_copy = a + count
        if cezarPass_copy == len(ALPHABET):
            string_on_exit.append(ALPHABET[cezarPass_copy-len(ALPHABET)])
        elif cezarPass_copy > len(ALPHABET):
            string_on_exit.append(ALPHABET[cezarPass_copy-len(ALPHABET)])
        elif cezarPass_copy < len(ALPHABET):
            string_on_exit.append(ALPHABET[cezarPass_copy])

# в третьем блоке просматриваем вариант когда уходим в огромный плюс    
    elif (shift_input > len(ALPHABET)):
        count = copy.deepcopy(shift_input)
        while count > len(ALPHABET):
            count -= len(ALPHABET)
        cezarPass_copy = a + count
        if cezarPass_copy == len(ALPHABET):
            string_on_exit.append(ALPHABET[cezarPass_copy-len(ALPHABET)])
        elif cezarPass_copy > len(ALPHABET):
            string_on_exit.append(ALPHABET[cezarPass_copy-len(ALPHABET)])
        elif cezarPass_copy < len(ALPHABET):
            string_on_exit.append(ALPHABET[cezarPass_copy])

# В конце через цикл for и формат выводим на печать получившееся решение
for i in string_on_exit:
    d += str(i)

print(f"""Result: \"{d}\"""")
