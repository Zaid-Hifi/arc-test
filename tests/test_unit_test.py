from src.testpkg import test_function

def test_myfunction():
    return_value = test_function.my_function()
    assert return_value == "Hello World"