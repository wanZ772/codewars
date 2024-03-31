def validate_pin(pin):
    try:
        if (len(pin) == 4 and int(pin) >= 0) or (len(pin) == 6 and int(pin) >= 0):
            return True
        else:
            return False
    except:
        return False
print(validate_pin("+111"))