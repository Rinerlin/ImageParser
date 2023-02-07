# при помощи декоратора и функции while, написать этот текст 5 раз подряд

def fiveTimes(input_func): # это уже готовый ответ, нужно просто правильно вызвать декоратор
    def output_func():
        n = 0
        while n < 5:
            input_func()
            n = n + 1

    return output_func



def test():
    print("Ура, мы закончили этот ужасный тест")


test()
