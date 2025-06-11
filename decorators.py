import time
import functools

def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🔍 Running '{func.__name__}'...")
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        duration = end_time - start_time
        print(f"✅ '{func.__name__}' completed in {duration:.4f} seconds\n")
        return result
    return wrapper
@log_execution_time
def simulate_task():
    time.sleep(2)
    return "Task finished"
output = simulate_task()
print(output)
