from functions.run_python_file import run_python_file

def test_run_python_file():
    print(f"Testing run_python_file... .\n")

    print(f'\nRunning: run_python_file("calculator", "main.py")')
    return_string = run_python_file("calculator", "main.py")
    print(return_string)

    print(f'\nrun_python_file("calculator", "main.py", ["3 + 5"])')
    return_string = run_python_file("calculator", "main.py", ["3 + 5"])
    print(return_string)

    print(f'\nrun_python_file("calculator", "tests.py")')
    return_string = run_python_file("calculator", "tests.py")
    print(return_string)

    print(f'\nrun_python_file("calculator", "../main.py")')
    return_string = run_python_file("calculator", "../main.py")
    print(return_string)

    print(f'\nrun_python_file("calculator", "nonexistent.py")')
    return_string = run_python_file("calculator", "nonexistent.py")
    print(return_string)

    print(f'\nrun_python_file("calculator", "lorem.txt")')
    return_string = run_python_file("calculator", "lorem.txt")
    print(return_string)


test_run_python_file()