'''функція алгоритму FizzBuzz'''

def FizzBuzz(numbers: list) -> list:

    '''

    :param numbers: enter numbers -> [1,2,3,4,5,6,7,8,9,15]
    :return: value_list
    '''

    value_list = []
    for num in numbers:
        if num % 3 == 0 and num % 5 == 0:
            value_list.append('FizzBuzz')
        elif num % 3 == 0:
            value_list.append('Fizz')
        elif num % 5 == 0:
            value_list.append('Buzz')
        else:
            value_list.append(num)
    return value_list

print(FizzBuzz([1,2,3,4,5,6,7,8,9,15]))