def stop_words(words: list):
    def stop_words_decorator(func):
        def func_wrapper(param):
            func_returns = func(param)
            for item in words:
                if item in func_returns:
                    func_returns = func_returns.replace(item, "*")
            return func_returns
        return func_wrapper
    return stop_words_decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
