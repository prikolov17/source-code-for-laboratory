#1
user_text = input('Введите текст для записи:')
with open('user_input.txt','w',encoding='utf-8') as file:
    file.write(user_text + '\n')
print('Текст успещно записан')
#2
additional_text = input('Введите текст для добавлени в файл')
with open('user_input.txt','a',encoding='utf-8') as file:
    file.write(additional_text + '\n')
print('Текст успешно добавлен')
