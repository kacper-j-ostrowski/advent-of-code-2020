from Policy import LetterCountPolicy
from Policy import LetterPositionPolicy

file = open("input.txt", 'r')
Lines = file.readlines()


def get_password_letter_count_policy(args):
    lines = args.split()
    ranges = lines[0].split('-')
    return LetterCountPolicy(int(ranges[0]), int(ranges[1]), lines[1])


def get_password_letter_position_policy(args):
    lines = args.split()
    ranges = lines[0].split('-')
    return LetterPositionPolicy(int(ranges[0]), int(ranges[1]), lines[1])


total_passwords = len(Lines)
wrong_passwords_one = 0
wrong_passwords_two = 0
for line in Lines:
    line = str(line).strip()
    args = line.split(':')
    letter_count_policy = get_password_letter_count_policy(args[0])
    letter_position_policy = get_password_letter_position_policy(args[0])
    password = args[1].strip()
    if letter_count_policy.is_password_not_compliant(password):
        wrong_passwords_one += 1
    if letter_position_policy.is_password_not_compliant(password):
        wrong_passwords_two += 1


print("Found " + str(total_passwords - wrong_passwords_one) + " valid passwords due to letter count policy")
print("Found " + str(total_passwords - wrong_passwords_two) + " valid passwords due to letter position policy")
