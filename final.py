#Запрос информации от пользователя
username = input('Enter your name: ')
title = input('Enter the first note title: ')
title1 = input('Enter the second note title: ')
title2 = input('Enter the third note title: ')
titles = [title, title1, title2]
content = input('Enter description: ')
status = input ('Enter status of your note: ')
created_date = input ('Enter the date of creation in the format dd-mm-yy: ')
issue_date = input('Enter deadline in format dd-mm-yy: ')
#Формирование словаря
note = {
'username' : username,
'title' : title,
'title1' : title1,
'title2' : title2,
'titles' : [title, title1, title2],  #формирование списка заголовков
'content' : content,
'status' : status,
'created_date' : created_date[:-3], #Хранение дат в коротком формате
'issue_date' : issue_date[:-3]
}
#Вывод данных
print('Hello, ', note['username'])
print('Your note content this titles: ', note['titles'])
print('Description:', note['content'])
print('Status of your note: ', note['status'])
print('Creation date: ', note['created_date'])
print('Deadline: ', note['issue_date'])