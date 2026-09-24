from importlib.util import spec_from_file_location, module_from_spec
import os

code_path = os.path.join(
    os.path.dirname(__file__), "..", "Code", "03_pos_neg_zero.py"
)

spec = spec_from_file_location("pos_neg_zero", code_path)
module = module_from_spec(spec)
spec.loader.exec_module(module)

assert module.check_number(10) == "Positive"
assert module.check_number(-5) == "Negative"
assert module.check_number(0) == "Zero"
assert module.check_number(100) == "Positive"
assert module.check_number(-100) == "Negative"

print("All test cases passed.")
