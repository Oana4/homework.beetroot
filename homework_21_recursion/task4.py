# Function returns reversed input string
def reverse(input_str: str) -> str:
    if len(input_str) == 0:
        return ''
    else:
        return input_str[-1] + reverse(input_str[:-1])


assert reverse("hello") == "olleh"
assert reverse("o") == "o"
print(reverse("oana"))
