file = open("input.txt")
Lines = file.readlines()

num_dict = dict()

for line in Lines:
    number = int(line)
    candidate = 2020 - number
    if candidate in num_dict:
        print(num_dict[candidate] * number)
        print("found")
        exit(0)
    else:
        num_dict[number] = number
