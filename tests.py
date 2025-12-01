from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def tests():
    #test_get_file_info()
    test_get_file_content()

def test_get_file_info():
    print(f"Testing get_files_info... .\n")

    print(f'\nRunning: get_files_info("calculator", ".")')
    files_info = get_files_info("calculator", ".")
    print(files_info)

    print(f'\nRunning: get_files_info("calculator", "pkg")')
    files_info = get_files_info("calculator", "pkg")
    print(files_info)

    print(f'\nRunning: get_files_info("calculator", "/bin")')
    files_info = get_files_info("calculator", "/bin")
    print(files_info)

    print(f'\nRunning: get_files_info("calculator", "../")')
    files_info = get_files_info("calculator", "../")
    print(files_info)

def test_get_file_content():
    print(f"Testing get_file_content... .\n")

    #print(f'get_file_content("calculator", "lorem.txt")')
    #file_content = get_file_content("calculator", "lorem.txt")
    #print(file_content)

    print(f'\nRunning: get_file_content("calculator", "main.py")')
    file_content = get_file_content("calculator", "main.py")
    print(file_content)

    print(f'\nRunning: get_file_content("calculator", "pkg/calculator.py")')
    file_content = get_file_content("calculator", "pkg/calculator.py")
    print(file_content)

    print(f'\nRunning: get_file_content("calculator", "/bin/cat")')
    file_content = get_file_content("calculator", "/bin/cat")
    print(file_content)

    print(f'\nRunning: get_file_content("calculator", "pkg/does_not_exist.py")')
    file_content = get_file_content("calculator", "pkg/does_not_exist.py")
    print(file_content)

tests()