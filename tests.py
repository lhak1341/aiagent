from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info

# def test_get_files_info(root_dir, dir):
#     if dir == ".":
#         dir_str = "current"
#     else:
#         dir_str = f"'{dir}'"
#     print(f"Result for {dir_str} directory:")
#     print(get_files_info(root_dir, dir))

# test_get_files_info("calculator", ".")
# test_get_files_info("calculator", "pkg")
# test_get_files_info("calculator", "/bin")
# test_get_files_info("calculator", "../")

def test_get_files_contents(root_dir, file_path):
    print(f"Result for '{file_path}' file:")
    print(get_file_content(root_dir, file_path))

test_get_files_contents("calculator", "main.py")
test_get_files_contents("calculator", "pkg/calculator.py")
test_get_files_contents("calculator", "/bin/cat")
test_get_files_contents("calculator", "pkg/does_not_exist.py")
