def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()

inner_function() # не вызывается вне функции test_function, т.к. находятся в разных пространствах.