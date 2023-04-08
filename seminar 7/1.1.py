file = open('data.txt', mode='r', encoding='utf-8')

list_ = [el.strip().split('#') for el in file]
print(list_)

file.close()