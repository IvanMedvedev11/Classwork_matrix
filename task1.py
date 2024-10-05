import random
list_01 = [random.randint(0, 9) for i in range(10)]
try:
    k = int(input("Введите число: "))
except ValueError:
    print("Ты что, совсем тупой?")
    quit()
list_01.sort()
size = len(list_01)
for i in range(1, size):
    if list_01[i-1] <= k <= list_01[i]:
        list_01.insert(i, k)
        break
else:
    if k <= list_01[0]:
        list_01.insert(0, k)
    else:
        list_01.append(k)
print(list_01)
