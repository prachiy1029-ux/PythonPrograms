from importlib.util import spec_from_file_location, module_from_spec
import os

code_path = os.path.join(
    os.path.dirname(__file__), "..", "Code", "10_sum_of_digits.py"
)

spec = spec_from_file_location("sum_of_digits", code_path)
module = module_from_spec(spec)
spec.loader.exec_module(module)

assert module.sum_of_digits(12345) == 15
assert module.sum_of_digits(100) == 1
assert module.sum_of_digits(0) == 0
assert module.sum_of_digits(9) == 9
assert module.sum_of_digits(-123) == 6

print("All test cases passed.")