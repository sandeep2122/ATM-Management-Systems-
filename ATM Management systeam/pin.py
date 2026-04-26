def check_pin():
    correct_pin = "1234"
    attempts = 3

    while attempts > 0:
        user_pin = input("Enter PIN: ")
        if user_pin == correct_pin:
            return True
        else:
            attempts -= 1
            print("Wrong PIN! Attempts left:", attempts)

    return False