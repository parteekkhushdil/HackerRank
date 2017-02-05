n = int(input())
phonebook = {}
for i in range(n):
    name, number = input().strip().split(' ')
    phonebook[name] = int(number)

# print(phonebook)
while True:
    search = input()
    if search == ' ':
        break
    else:
        if search in phonebook:
            print(search + '=' + str(phonebook[search]))
        else:
            print('Not found')
