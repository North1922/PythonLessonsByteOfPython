number = 23
guess = int(input('Введите целое число : '))

if guess == number:
    print('Поздравляю, вы угадали, ')#Начало нового блока
    print('(хотя и не выиграли не какого приза!)')# Конец нового блока
elif guess < number:
    print('Нет, загаданное число немного больше этого.')#Ещё один блок
    #Внутри этого блока вы можете выполнять всё, что угодно...
else:
    print('Нет, загаданное число немного меньше этого.')
    # что бы попасть сюда, guess должно быть больше, чем number 
print('Завершено')
    #Это последнее выражение выполняется всегда после выполнения оператора if       