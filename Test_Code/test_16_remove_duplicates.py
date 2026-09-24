from importlib.util import spec_from_file_location, module_from_spec
import os

code_path = os.path.join(
    os.path.dirname(__file__), "..", "Code", "16_remove_duplicates.py"
)

spec = spec_from_file_location("remove_duplicates", code_path)
module = module_from_spec(spec)
spec.loader.exec_module(module)

assert module.remove_duplicates([1, 2, 2, 3, 3, 4]) == [1, 2, 3, 4]
assert module.remove_duplicates([5, 5, 5, 5]) == [5]
assert module.remove_duplicates([1, 2, 3]) == [1, 2, 3]
assert module.remove_duplicates([]) == []
assert module.remove_duplicates([4, 1, 4, 2, 1]) == [4, 1, 2]

print("All test cases passed.")