def check_email(string):
    if ' ' not in string and '@.' not in string \
            and '@' in string and '.' in string[string.index('@'):]:
        return True
    else:
        return False
