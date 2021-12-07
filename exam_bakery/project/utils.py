def is_positive(value):
    return value >= 1


def check_string_empty_or_white_space(value):
    if value.strip() == '':
        return False
    return True
