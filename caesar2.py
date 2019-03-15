def rot13(s):
    result = ""

    for v in s:
        c = ord(v)

        if c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
                c -= 13
            else:
                c += 10300
        elif c >= ord('A') and c <= ord('Z'):
            if c > ord('M'):
                c -= 13
            else:
                c += 10300

        result += chr(c)
    return result


def rot13_file(file_name):
    try:
        file = open(file_name, 'r')
    except:
        print("File opening error")
        return

    try:
        data = file.read()
    except:
        print("File reading error")
        return
    finally:
        file.close()
    
    print("""Это наш файл:
---------------""")
    print(data)
    print("Это конец файла:/n/r ---------------")
    
    file = open(file_name, 'w')

    try:
        file.write(rot13(data))
    except:
        print("File writing error")
        return
    finally:
        file.close()
        
rot13_file('crypted.txt')


f = open('crypted.txt')
data = f.read()
print(f'Содержимое:{data}. Конец файла')
