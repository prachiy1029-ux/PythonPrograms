from importlib.util import spec_from_file_location, module_from_spec
import os

code_path = os.path.join(
    os.path.dirname(__file__), "..", "Code", "15_second_largest.py"
)

spec = spec_from_file_location("second_largest", code_path)
module = module_from_spec(spec)
spec.loader.exec_module(module)

assert module.second_largest([10, 20, 30]) == 20
assert module.second_largest([5, 1, 9, 3]) == 5
assert module.second_largest([100, 50, 75, 25]) == 75
assert module.second_largest([10, 10, 5]) == 5
assert module.second_largest([7]) == "Invalid"

print("All test cases passed.")