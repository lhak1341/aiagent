# from functions.get_files_info import get_files_info


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

# -------------------------------------------------------

# from functions.get_file_content import get_file_content


# def test_get_files_contents(root_dir, file_path):
#     print(f"Result for '{file_path}' file:")
#     print(get_file_content(root_dir, file_path))

# test_get_files_contents("calculator", "lorem.txt")
# test_get_files_contents("calculator", "main.py")
# test_get_files_contents("calculator", "pkg/calculator.py")
# test_get_files_contents("calculator", "/bin/cat")
# test_get_files_contents("calculator", "pkg/does_not_exist.py")

# -------------------------------------------------------

# from functions.write_file import write_file


# def test_write_file(root_dir, file_path, content):
#     print(write_file(root_dir, file_path, content))

# test_write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
# test_write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
# test_write_file("calculator", "/tmp/temp.txt", "this should not be allowed")

# -------------------------------------------------------

from functions.run_python_file import run_python_file


def test_run_python_file(working_directory, file_path, args=[]):
    print(run_python_file(working_directory, file_path, args))

test_run_python_file("calculator", "main.py")
test_run_python_file("calculator", "main.py", ["3 + 5"])
test_run_python_file("calculator", "tests.py")
test_run_python_file("calculator", "../main.py")
test_run_python_file("calculator", "nonexistent.py")
test_run_python_file("calculator", "lorem.txt")

# -------------------------------------------------------
