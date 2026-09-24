from importlib.util import spec_from_file_location, module_from_spec
import os

code_path = os.path.join(
    os.path.dirname(__file__), "..", "Code", "12_reverse_string.py"
)

spec = spec_from_file_location("reverse_string", code_path)
module = module_from_spec(spec)
spec.loader.exec_module(module)

assert module.reverse_string("hello") == "olleh"
assert module.reverse_string("Python") == "nohtyP"
assert module.reverse_string("abc") == "cba"
assert module.reverse_string("a") == "a"
assert module.reverse_string("") == ""

print("All test cases passed.")