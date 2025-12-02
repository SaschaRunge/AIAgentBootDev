from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

def tests():
    #test_get_file_info()
    #test_get_file_content()
    #test_write_file()
    return

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

def test_write_file():
    print(f'\nRunning: write_file("calculator", "lorem.txt", "wait, this isnt lorem ipsum")')
    return_string = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(return_string)

    print(f'\nRunning: write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")')
    return_string = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(return_string)

    print(f'\nRunning: write_file("calculator", "/tmp/temp.txt", "this should not be allowed")')
    return_string = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(return_string)

    print(f'\nRunning: write_file("calculator", "pkg/testfolder/nestedtestfolder/test.txt", "test successful")')
    return_string = write_file("calculator", "pkg/testfolder/nestedtestfolder/test.txt", "test successful")
    print(return_string)

    print(f'\nRunning: write_file("calculator", "test.txt", "test successful")')
    return_string = write_file("calculator", "test.txt", "test successful")
    print(return_string)

tests()