def corrector(func):
    def wrapper(*arg, **kwargs):
        try:
            func(*arg, **kwargs)
        except Exception as e:
            print('Error. Enter once again', e)
        return wrapper
