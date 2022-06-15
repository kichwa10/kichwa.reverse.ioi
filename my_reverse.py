numbers = [1, 2, 3, 4, 7, 8 , 9, 10]


def my_reverse(numbers):
    length = len(numbers) - 1
    new_List = []
    while (length >= 0):
        new_List.append(numbers[length])
        length = length - 1
    return new_List


print(my_reverse(numbers))
