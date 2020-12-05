file = open("input.txt")
Lines = file.readlines()

partial_results = []
final_results = []

for line in Lines:
    x = int(line)
    rest = 2020 - x
    partial_results.append((x, rest))

for line in Lines:
    y = int(line)
    for res in partial_results:
        if y != res[0] and y < res[1]:
            final_results.append((res[0], y, 2020 - res[0] - y))

for line in Lines:
    z = int(line)
    for res in final_results:
        if z == res[2]:
            print("Found: " + str(res))
            print("Product: " + str(res[0] * res[1] * res[2]))
            exit(0)
