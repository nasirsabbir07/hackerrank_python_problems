def solve(s):
    text = s.split(' ')
    name = list()
    for i in text:
        item = i.capitalize()
        name.append(item)
    full_name = ' '.join(name)
    return full_name

s = input()
print(solve(s))