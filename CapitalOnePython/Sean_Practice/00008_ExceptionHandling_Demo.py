def division_task(k: int):
    """
    Demonstrates a function that raises an error for invalid input.
    """
    if k == 0:
        raise ValueError("k cannot be zero (invalid per problem constraints)")
    return 100 / k

def run_exception_demo():
    print("--- Exception Handling Demo ---")
    
    # Test Case 1: Valid Input
    try:
        k = 10
        print(f"Attempting with k={k}...")
        result = division_task(k)
        print(f"Success! Result: {result}")
    except ValueError as e:
        print(f"Caught an error: {e}")
    print("-" * 20)

    # Test Case 2: Invalid Input (Triggers Exception)
    try:
        k = 0
        print(f"Attempting with k={k}...")
        result = division_task(k)
        print(f"Success! Result: {result}") # This line will be skipped
    except ValueError as e:
        # This block runs when ValueError is raised
        print(f"⚠️ CAUGHT ERROR: {e}")
        # You can handle it here (e.g., set default value, log it, or exit gracefully)
    
    print("-" * 20)
    print("Program continued running after catching the error.")

if __name__ == "__main__":
    run_exception_demo()
