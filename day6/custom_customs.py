from functools import reduce

file = open('input.txt', 'r')
Lines = file.readlines()

# part one
results = []
group_answers = set()

for line in Lines:
    if len(line.strip()) > 0:
        group_answers.update(set(line.strip()))
    else:
        results.append(len(group_answers))
        group_answers = set()

res = reduce(lambda a, b: a + b, results)
print(res)

results = []
individual_answers = []

# part two
for line in Lines:
    if len(line.strip()) > 0:
        individual_answers.append(set(line.strip()))
    else:
        common_answers = individual_answers[0]
        for answer in individual_answers:
            common_answers = answer.intersection(common_answers)
        results.append(len(common_answers))
        individual_answers = []

res = reduce(lambda a, b: a + b, results)
print(res)
