class StartMenu:
    print("Welcome in the text adventure Game!\n")
    print("*** Start menu ***\n")

    def menuChoice():

        moveInto = ''

        choices = {
            'login': ['login', 'log in', 'sign in', 'logging in', 'log', 'logg'],
            'register': ['register', 'sign up', 'sign', 'registre', 'registr', 'register me'],
            'exit' : ['exit', 'leave', 'escape']
        }
        print("[1] Log into the game\n")
        print("[2] No account. I want to register!\n")
        print("[3] Exit\n")

        askWhereToGo = input("""If you already have an account, you just need to login..otherwise you need to register\n\nChoose what would you like to do\n
        """)
        if askWhereToGo in choices['login']:
            moveInto = 'login'
        elif askWhereToGo in choices['register']:
            moveInto = 'register'
        elif askWhereToGo in choices['exit']:
            moveInto = 'exit'

        return moveInto
