from importlib.util import spec_from_file_location, module_from_spec
import os

code_path = os.path.join(
    os.path.dirname(__file__), "..", "Code", "11_vowel_consonents.py"
)

spec = spec_from_file_location("vowel_consonents", code_path)
module = module_from_spec(spec)
spec.loader.exec_module(module)

assert module.check_vowel_consonant("a") == "Vowel"
assert module.check_vowel_consonant("E") == "Vowel"
assert module.check_vowel_consonant("b") == "Consonant"
assert module.check_vowel_consonant("Z") == "Consonant"
assert module.check_vowel_consonant("1") == "Invalid"

print("All test cases passed.")