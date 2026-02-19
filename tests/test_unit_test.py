import testpkg.test_function

def test_myfunction():
    return_value = testpkg.test_function.my_function()
    assert return_value == "Hello World"