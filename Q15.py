def sum(*numbers):
    result = 0
    for n in numbers:
        result += n
    print(f"sum = {result}")


sum(1,2,3,4,5,6,7,8,8,7,6,5,4,3,2,1)