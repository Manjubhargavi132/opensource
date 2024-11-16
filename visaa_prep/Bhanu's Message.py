import re
def validate_number(msg):
    if len(msg)==10 and msg.isdigit():
        if sum(int(digit) for digit in msg)>0:
            return "Correct"
    match=re.match(r'^\+(\d{2}) (\d{10})$',msg)
    if match:
        country_code,number=match.groups()
        if len(country_code) in [1,2] and number.isdigit() and sum(int(digit) for digit in number)>0:
            return "Correct"
    return "Incorrect"
msg=input()
print(validate_number(msg))
