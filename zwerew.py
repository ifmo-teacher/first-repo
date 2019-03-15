with open('text.txt', 'r') as file:
    lines = file.readlines()
    print(lines[0])
    ans = lines[1].split('&')
    x = 1
    for i in ans:
        print(f'{x}.' + i)
        x += 1
    a = int(input('Введите ответ от 1 до 3:'))
    if a == int(lines[2]):
        print('Верно!')
    else:
        print('Неверно(')
