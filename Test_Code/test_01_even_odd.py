from importlib.util import spec_from_file_location, module_from_spec
import os

code_path = os.path.join(os.path.dirname(__file__), "..", "Code", "01_even_odd.py")

spec = spec_from_file_location("even_odd", code_path)
module = module_from_spec(spec)
spec.loader.exec_module(module)

assert module.check_even_odd(2) == "Even"
assert module.check_even_odd(5) == "Odd"
assert module.check_even_odd(0) == "Even"
assert module.check_even_odd(-3) == "Odd"

print("All test cases passed.")