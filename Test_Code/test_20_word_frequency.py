from importlib.util import spec_from_file_location, module_from_spec
import os

code_path = os.path.join(
    os.path.dirname(__file__), "..", "Code", "20_word_frequency.py"
)

spec = spec_from_file_location("word_frequency", code_path)
module = module_from_spec(spec)
spec.loader.exec_module(module)

assert module.word_frequency("hello world hello") == {
    "hello": 2,
    "world": 1
}

assert module.word_frequency("Python is easy Python") == {
    "python": 2,
    "is": 1,
    "easy": 1
}

assert module.word_frequency("apple apple apple") == {
    "apple": 3
}

assert module.word_frequency("") == {}

print("All test cases passed.")