def main(input_s):
    import string
    
    alphabet_l = string.ascii_lowercase
    alphabet_u = string.ascii_uppercase
    symbols = string.punctuation
    offset = 1 # 25
    # input_s = "ifmmp_xpsme_"
#     input_s = "hello,world!"
#     input_s = input('Введите строку: ')
    
    output_s = ""
    
    for char in input_s:
        if char in symbols:
            output_s += '_'
            
                
    
        if char in alphabet_l:
            pos = alphabet_l.find(char)
            
            if offset > len(alphabet_l):                
            if char is not 'z':
                pos = alphabet_l.find(char)
                pos+=offset
                output_s += alphabet_l[pos]
            else:
                output_s += 'a'
                
        if char in alphabet_u:
            if char is not 'Z':
                pos = alphabet_l.find(char)
                pos+=offset
                output_s += alphabet_l[pos]
            else:
                output_s += 'a'
       
    print(output_s)
    return output_s


assert main("hello,world!") == "ifmmp_xpsme_", 'Плохо работаю с обычными строками'
assert main("hello192") == "ifmmp192", "Ошибка при кодировании цифр"
