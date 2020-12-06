import functools

with open("input.txt") as Lines:
    tree_map = [line.strip() for line in Lines]

slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]

current_position = (0, 0)
map_width = len(tree_map[0])
tree_counter = 0
results = []

for slope in slopes:
    while current_position[0] < len(tree_map):
        if tree_map[current_position[0]][current_position[1]] == '#':
            tree_counter += 1
        next_right_pos = (current_position[1] + slope[1]) % map_width
        next_bottom_pos = (current_position[0] + slope[0])
        current_position = (next_bottom_pos, next_right_pos)
    results.append(tree_counter)
    tree_counter = 0
    current_position = (0, 0)

final_result = functools.reduce(lambda a, b: a * b, results)

print(f"The final result is {str(final_result)}")
