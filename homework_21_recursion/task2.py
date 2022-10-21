def is_palindrome(looking_str: str) -> bool:
    if len(looking_str) == 1 or len(looking_str) == 0:  # I use 1 for an odd-length of string and 0 for an even one
        return True

    if looking_str[0] == looking_str[-1]:
        return is_palindrome(looking_str[1:-1])
    else:
        return False


assert is_palindrome('mom') is True
assert is_palindrome('sassas') is True
assert is_palindrome('o') is True
