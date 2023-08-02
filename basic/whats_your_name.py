def print_full_name(first, last):
    # Write your code here
    full_name = first.capitalize() + ' ' + last.capitalize()
    a = print('Hello ' + full_name + '!' + ' You just delved into python.')
    return a

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)