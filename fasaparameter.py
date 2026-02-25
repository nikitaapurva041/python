def greet(name):
    return f"Hello {name}"

def process(function):
    return function("Nikita")

call = process(greet)
print(call)