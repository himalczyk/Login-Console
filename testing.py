choices = {
    'login': ['login', 'log in', 'sign in', 'logging in', 'log', 'logg'],
    'register': ['register', 'sign up', 'sign', 'registre', 'registr', 'register me']
}

askWhereToGo = input('what to do?')

if askWhereToGo in choices['login']:
    print('login')
elif askWhereToGo in choices['register']:
    print('register')