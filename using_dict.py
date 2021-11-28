# 'ab' - сокращение от 'a'ddress'b'ook
ab = {  'Swaroop'   : 'swaroop@swaroopch.com',
        'Larry'     : 'larry@wall.org',
        'Matsumoto' : 'matz@ruby-lang.org',
        'Spammer'   : 'spammer@hotmail.com'
     }

print("Адрес Swaroop'а:", ab['Swaroop'])
# Удаление пары ключ-значение
del ab['Spammer']
#Удалять пары ключ-значение можно при помощи нашего старого доброго
#оператора del. Мы просто указываем имя словаря и оператор индексирования
#для удаляемого ключа, после чего передаём это оператору del. Для этой опе-
#рации нет необходимости знать, какое значение соответствует данному клю-
#чу.
print('\nВ адресной книге {0} контакта\n'.format(len(ab)))
for name, address in ab.items():
    print('Контакт {0} с адресом {1}'.format(name, address))
#Далее мы обращаемся ко всем парам ключ-значение нашего словаря, исполь-
#зуя метод items, который возвращает список кортежей, каждый из которых
#содержит пару элементов: ключ и значение. Мы получаем эту пару и при-
#сваиваем её значение переменным name и address соответственно в цикле
#for..in, а затем выводим эти значения на экран в блоке for.
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\nАдрес Guido:", ab['Guido'])