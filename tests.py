from functions.get_files_info import get_files_info

def tests():
    print(f"Testing get_files_info... .\n")

    print(f'Running: get_files_info("calculator", ".")')
    files_info = get_files_info("calculator", ".")
    print(files_info)

    print(f'Running: get_files_info("calculator", "pkg")')
    files_info = get_files_info("calculator", "pkg")
    print(files_info)

    print(f'Running: get_files_info("calculator", "/bin")')
    files_info = get_files_info("calculator", "/bin")
    print(files_info)

    print(f'Running: get_files_info("calculator", "../")')
    files_info = get_files_info("calculator", "../")
    print(files_info)

tests()