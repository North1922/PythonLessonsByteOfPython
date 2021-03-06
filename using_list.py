#это мой список покупок
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']# Переменная shoplist – это список покупок человека, идущего на рынок. В
                                                    #shoplist мы храним только строки с названиями того, что нужно купить,
                                                    #однако в список можно добавлять любые объекты, включая числа или даже
                                                    #другие списки.
print('Я должен сделать', len(shoplist), 'покупки.')

print('Покупки:', end=' ')
for item in shoplist:                                #Мы также использовали цикл for..in для итерации по элементам списка.
    print(item, end=' ')                             #Вы уже, наверное, поняли, что список является также и последовательностью.
    
print('n\Также нужно купить риса.')                 #Обратите внимание на использование ключевого аргумента end в функции
shoplist.append('рис')                              # print, который показывает, что мы хотим закончить вывод пробелом вместо
                                                    #обычного перевода строки.
print('Теперь мой список покупок таков:', shoplist) 
#Далее мы добавляем элемент к списку при помощи append – метода объекта
#списка, который уже обсуждался ранее. Затем мы проверяем, действительно
#ли элемент был добавлен к списку, выводя содержимое списка на экран при
#помощи простой передачи этого списка функции print, которая аккуратно
#его печатает.
print('Отсортирую-ка я свой список')
shoplist.sort()
print('Отсортированный список покупок выглядит так:', shoplist)
#Затем мы сортируем список, используя метод sort объекта списка. Имейте в
#виду, что этот метод действует на сам список, а не возвращает изменённую его
#версию. В этом отличие от того, как происходит работа со строками. Именно
#это имеется в виду, когда мы говорим, что списки изменяемы, а строки – неиз-
#меняемы.
print('Первое, что нужно купить, это', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('Я купил:', olditem)
print('Теперь мой список покупок:',shoplist)
#Далее после совершения покупки мы хотим удалить её из списка. Это дости-
#гается применением оператора del. Мы указываем, какой элемент списка мы
#хотим удалить, и оператор del удаляет его. Мы указываем, что хотим удалить
#первый элемент списка, и поэтому пишем «del shoplist[0]» (помните, что
#Python начинает отсчёт с 0).