X = int(input("сколько строк?: ").strip())
присутствующие = 0
online = 0
for i in range(X):
    фамилия, имя, возраст, format = input().strip().split()
    возраст1 = int(возраст)
    present = format.lower() == "true"
    if present:
        присутствующие += 1
    else:
        online += 1
print(присутствующие, online)
