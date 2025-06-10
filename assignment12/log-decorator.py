import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        pos_args = list(args) if args else "none"
        kw_args = dict(kwargs) if kwargs else "none"
        logger.info(f"function : {func.__name__}")
        logger.info(f"positional parameters: {pos_args}")
        logger.info(f"keyword parameters: {kw_args}")
        logger.info(f"return: {result}")
        logger.info("-" * 40)
        return result
    return wrapper

@logger_decorator
def hello_world():
    print("Hello, World!")

@logger_decorator
def check_numbers(*args):
    return True

@logger_decorator
def return_decorator(**kwargs):
    return logger_decorator

if __name__ == '__main__':
    hello_world()
    check_numbers(1,2,3,4)
    return_decorator(x = 5, y=15)