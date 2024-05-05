def validate_name(name):
    return name.isalpha()

def validate_last_name(last_name):
    return last_name.isalpha()

def validate_second_last_name(second_last_name):
    if second_last_name:
        return second_last_name.isalpha()
    return True
