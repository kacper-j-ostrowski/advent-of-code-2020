file = open("input.txt", 'r')
Lines = file.readlines()

max_unique_id = 0
all_seats = []

for line in Lines:
    line = line.strip()
    number = line.replace('R', '1').replace('L', '0').replace('B', '1').replace('F', '0')
    unique_id = int(number, 2)
    max_unique_id = max(unique_id, max_unique_id)
    all_seats.append(unique_id)

print(f"Max unique id: {str(max_unique_id)}")

for i in range(256 * 8):
    if i not in all_seats and i + 1 in all_seats and i - 1 in all_seats:
        print(i)
