def monkeypatch_class(cls):
    """Decorator to add methods to a class.

    @monkeypatch_class(Vasp)
    def some_func(self):
        return "you got it."

    """
    def decorator(func):
        setattr(cls, func.__name__, func)
        s = ('\n\nMonkey-patch defined in '
             '{f.__code__.co_filename} '
             'at line {f.__code__.co_firstlineno}')
        if func.__doc__ is None:
            func.__doc__ = ''
        func.__doc__ += s.format(f=func)
        return func
    return decorator
