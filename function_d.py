def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    highest_number = 0

    for number in numbers:
        if number > highest_number:
            highest_number = number
    
    return highest_number


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
