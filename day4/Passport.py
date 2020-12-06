import re


class Passport:
    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    passport_info = dict()

    def __init__(self, passport):
        self.passport_info = dict()
        entries = passport.split()
        for entry in entries:
            key_value = entry.split(':')
            self.passport_info[key_value[0]] = key_value[1]

    def is_valid(self):
        for field in self.mandatory_fields:
            if field not in self.passport_info.keys():
                return False
        return self.validate_birth_year() and self.validate_issue_year() and self.validate_expiration_year() and \
               self.validate_height() and self.validate_eye_color() and self.validate_passport_number() and \
                self.validate_hair_color()

    def validate_birth_year(self):
        birth_year = int(self.passport_info['byr'])
        return 1920 <= birth_year <= 2002

    def validate_issue_year(self):
        issue_year = int(self.passport_info['iyr'])
        return 2010 <= issue_year <= 2020

    def validate_expiration_year(self):
        expiration_year = int(self.passport_info['eyr'])
        return 2020 <= expiration_year <= 2030

    def validate_height(self):
        height = str(self.passport_info['hgt'])
        if len(height) < 3:
            return False
        elif height[-2:] == 'cm':
            height = int(height[0:-2])
            return 150 <= height <= 193
        else:
            height = int(height[0:-2])
            return 59 <= height <= 76

    def validate_eye_color(self):
        eye_color = str(self.passport_info['ecl'])
        return eye_color in self.eye_colors

    def validate_passport_number(self):
        regex = re.compile('^[0-9]{9}$')
        passport_number = str(self.passport_info['pid'])
        return regex.match(passport_number)

    def validate_hair_color(self):
        regex = re.compile('^#([a-f0-9]{6})$')
        hair_color = str(self.passport_info['hcl'])
        return regex.match(hair_color)
