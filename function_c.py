def merge_lists(list_a, list_b):
    """ Returns a new list which is
        a combination of list_a and list_b
        without any duplicate elements.
    """
    merged = []

    for item in list_a:
        if item not in merged:
            merged.append(item)

    for item in list_b:
        if item not in merged:
            merged.append(item)

    return merged

if __name__ == "__main__":
    print(merge_lists([1, 1, 2, 3], [3, 4, 5]))
