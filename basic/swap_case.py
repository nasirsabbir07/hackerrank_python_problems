def swap_case(s):
    text = list(s)
    #print(text)
    char = []
    for i in text:
        if i.isupper():
            i = i.lower()
            char.append(i)
        elif i.islower():
            i = i.upper()
            char.append(i)
        else:
            char.append(i)
    sent = ''.join(char)    
    return sent

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)