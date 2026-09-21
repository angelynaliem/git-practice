def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    # branch testing hehe 
    max_number = numbers[0]

    for number in numbers:
        if number > max_number:
            max_number = number

    return max_number


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
