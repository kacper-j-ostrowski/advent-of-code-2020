from Passport import Passport

file = open("input.txt", 'r')
Lines = file.readlines()

valid_passports = 0
passport_string = ''

for line in Lines:
    if len(line.strip()) > 0:
        passport_string = passport_string + ' ' + line.strip()
    else:
        passport = Passport(passport_string)
        passport_string = ''
        if passport.is_valid():
            valid_passports += 1

print(f"Valid passports: {str(valid_passports)}")
