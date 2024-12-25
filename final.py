#Запрос информации от пользователя и формирование списка
note = [
username := input('Enter your name: '),
title := input('Enter the first note title: '),
title1 := input('Enter the second note title: '),
title2 := input('Enter the third note title: '),
titles := [title, title1, title2],  #формирование списка заголовков
content := input('Enter description: '),
status := input ('Enter status of your note: '),
created_date := input ('Enter the date of creation in the format dd-mm-yy: '),
issue_date := input('Enter deadline in format dd-mm-yy: ')
]
#Вывод данных
print('Hello, ', note[0])
print('Your note content this titles: ', note[4])
print('Description:', note[5])
print('Status of your note: ', note[6])
print('Creation date: ', note[7][:-3])   #Вывод дат в коротком формате
print('Deadline: ', note[8][:-3])