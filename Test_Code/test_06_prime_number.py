from importlib.util import spec_from_file_location, module_from_spec
import os

code_path = os.path.join(
    os.path.dirname(__file__), "..", "Code", "06_prime_number.py"
)

spec = spec_from_file_location("prime_number", code_path)
module = module_from_spec(spec)
spec.loader.exec_module(module)

assert module.is_prime(2) == True
assert module.is_prime(3) == True
assert module.is_prime(5) == True
assert module.is_prime(10) == False
assert module.is_prime(1) == False
assert module.is_prime(0) == False
assert module.is_prime(-7) == False

print("All test cases passed.")