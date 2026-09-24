from importlib.util import spec_from_file_location, module_from_spec
import os

code_path = os.path.join(
    os.path.dirname(__file__), "..", "Code", "02_largest_of_three.py"
)

spec = spec_from_file_location("largest_of_three", code_path)
module = module_from_spec(spec)
spec.loader.exec_module(module)

assert module.largest_of_three(10, 20, 30) == 30
assert module.largest_of_three(50, 20, 30) == 50
assert module.largest_of_three(10, 40, 20) == 40
assert module.largest_of_three(-5, -2, -10) == -2

print("All test cases passed.")