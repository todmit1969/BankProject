from time import time

# Декоратор log
def log(filename=None):
    """
    Функция декоратор, которая записывает/показывает лог выполнения функции: время начала выполнения
    функции, время окончания и результат. В случае ошибки выдает тип ошибки
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time()
            try:
                result = func(*args, **kwargs)
                end_time = time()
                log_message = f"{func.__name__} started at {start_time:.6f} and finished at {end_time:.6f} with result: {result}"
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message + '\n')
                else:
                    print(log_message)
                return result
            except Exception as e:
                end_time = time()
                log_message = f"{func.__name__} error: {str(e)}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_message + '\n')
                else:
                    print(log_message)
                raise e
        return wrapper
    return decorator


@log(filename="")
def my_function(x, y):
    """ Функция суммирует два числа"""
    return x + y

my_function(1, 2)