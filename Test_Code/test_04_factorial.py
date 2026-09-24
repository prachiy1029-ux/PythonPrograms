from importlib.util import spec_from_file_location, module_from_spec
import os

code_path = os.path.join(
    os.path.dirname(__file__), "..", "Code", "04_factorial.py"
)

spec = spec_from_file_location("factorial", code_path)
module = module_from_spec(spec)
spec.loader.exec_module(module)

assert module.factorial(0) == 1
assert module.factorial(1) == 1
assert module.factorial(5) == 120
assert module.factorial(6) == 720
assert module.factorial(-3) == "Invalid"

print("All test cases passed.")