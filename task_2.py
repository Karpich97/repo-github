user_list = []
n = int(input("Введите количество элементов: "))
for i in range(0, n):
    elements = input()
    user_list.append(elements)
print(user_list)

j = 0
for i in range(int(len(user_list) / 2)):
    user_list[j], user_list[j + 1] = user_list[j + 1], user_list[j]
    j += 2
print(user_list)



