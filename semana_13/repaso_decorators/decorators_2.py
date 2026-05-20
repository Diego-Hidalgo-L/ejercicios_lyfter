
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        execution_time = end - start

        print(f"Execution time: {round(execution_time, 3)} seconds")
        return result

    return wrapper


@measure_time
def slow_function():
    return time.sleep(1)


print(slow_function())