def drinking_age(age, country):
    if country=='Germany':
        if age<16:
            print('Not allowed to drink.')
            drinking_bool = False
        elif 16<=age<18:
            print('Can drink wine and beer.')
            drinking_bool = True
        else:
            print('Drink whatever you like.')
            drinking_bool = True
    elif country=='USA':
        if age<21:
            print('Not allowed to drink.')
            drinking_bool = False
        else:
            print('Drink whatever you like.')
            drinking_bool = True
    else:
        print('Country not in data base.')
        drinking_bool = False
    return drinking_bool
