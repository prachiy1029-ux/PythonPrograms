from importlib.util import spec_from_file_location, module_from_spec
import os

code_path = os.path.join(
    os.path.dirname(__file__), "..", "Code", "14_char_frequency.py"
)

spec = spec_from_file_location("char_frequency", code_path)
module = module_from_spec(spec)
spec.loader.exec_module(module)

assert module.character_frequency("hello") == {
    "h": 1,
    "e": 1,
    "l": 2,
    "o": 1
}

assert module.character_frequency("apple") == {
    "a": 1,
    "p": 2,
    "l": 1,
    "e": 1
}

assert module.character_frequency("aaa") == {
    "a": 3
}

assert module.character_frequency("") == {}

print("All test cases passed.")