def read_file(filename='example.tx', mode='all'):
    try:
        with open(filename,'r',encoding='utf-8') as file:
            if mode == 'all':
                content = file.read()
                print('---File Contents----')
                print(content)
            elif mode == 'lines':
                print('----Line-by-line reading----')
                for line in file:
                    print(line.strip())
            else:
                print('Некоретный режим чтения.')
    except FileNotFoundError:
        print(f'Файл "{filename}"не найдено. Проверьте путь и имя файла.')
read_file(mode='all')
read_file(mode='lines')