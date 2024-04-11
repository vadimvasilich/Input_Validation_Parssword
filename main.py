import hashlib

def password_is_good(pas):
    has_digit   = 0
    has_low_let = 0
    has_up_let  = 0
    for symb in pas:
        if symb.isdigit():
            has_digit = 1
        if symb.isalpha():
            if symb.islower():
                has_low_let = 1
            else:
                has_up_let = 1
    return len(pas) >= 8 and has_digit and has_low_let and has_up_let

pas = input('Enter Password to hash: ')

if password_is_good(pas):
    hash_object = hashlib.sha256(pas.encode())
    print(hash_object.hexdigest())
else:
    print('Пароль ненадежный!')


