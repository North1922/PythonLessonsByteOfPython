while True:
    s = input('Введите что нибудь : ')
    if s == 'выход':
        break
    print('Длина строки: ', len(s))#при помощи встроенной функции len() выводим длину указзанной строки
print('Завершение')
help(int)