from importlib.util import spec_from_file_location, module_from_spec
import os

code_path = os.path.join(
    os.path.dirname(__file__), "..", "Code", "13_palindrome_string.py"
)

spec = spec_from_file_location("palindrome_string", code_path)
module = module_from_spec(spec)
spec.loader.exec_module(module)

assert module.is_palindrome_string("madam") == True
assert module.is_palindrome_string("level") == True
assert module.is_palindrome_string("racecar") == True
assert module.is_palindrome_string("hello") == False
assert module.is_palindrome_string("Python") == False

print("All test cases passed.")