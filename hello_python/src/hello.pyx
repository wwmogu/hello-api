# Add the language level directive
# cython: language_level=3

def hello(name: str) -> str:
    return "Hello from Python, {}!".format(name)
