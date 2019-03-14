def main():
    import string
    
    alphabet_l = string.ascii_lowercase
    alphabet_u = string.ascii_uppercase
    offset = 1
    # input_s = "ifm mpx psm ea"
    input_s = "hello world z"
    output_s = ""
    
    for char in input_s:
        if char is " ":
            output_s += '_'
        if char in alphabet_l:
            if char is not 'z':
                pos = alphabet_l.find(char)
                pos-=offset
                output_s += alphabet_l[pos]
            else:
                output_s += 'a'
                
        if char in alphabet_u:
            if char is not 'Z':
                pos = alphabet_l.find(char)
                pos-=offset
                output_s += alphabet_l[pos]
            else:
                output_s += 'a'
       
    print(output_s)
    
    
main()
