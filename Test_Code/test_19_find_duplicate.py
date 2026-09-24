from importlib.util import spec_from_file_location, module_from_spec
import os

code_path = os.path.join(
    os.path.dirname(__file__), "..", "Code", "19_find_duplicate.py"
)

spec = spec_from_file_location("find_duplicate", code_path)
module = module_from_spec(spec)
spec.loader.exec_module(module)

assert module.find_duplicates([1, 2, 2, 3, 4, 4]) == [2, 4]
assert module.find_duplicates([5, 5, 5, 5]) == [5]
assert module.find_duplicates([1, 2, 3, 4]) == []
assert module.find_duplicates([1, 1, 2, 2, 3, 3]) == [1, 2, 3]
assert module.find_duplicates([]) == []

print("All test cases passed.")