def read_file(filename='example.txt', mode='all'):
    with open(filename, 'r', encoding='utf-8') as file:
        if mode == 'all':
            content = file.read()
            print("----File Contents----")
            print(content)

        elif mode == 'lines':
            print("----Line-by-line reading----")
            for line in file:
                print(line.strip())
read_file(mode='all')
read_file(mode='lines')
