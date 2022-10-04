def arg_rules(type_: type, max_length: int, contains: list):
    def func_decorator(func):
        def func_wrapper(param):

            if len(param) > max_length:
                print("Your name parameter is too long!")
                return False

            if not isinstance(param, type_):
                print("You name parameter doesn't have the mandatory type!")
                return False

            for char in contains:
                if char not in param:
                    print(f"Your name parameter doesn't contain {char}, but it should!")
                    return False

            return func(param)
        return func_wrapper
    return func_decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
