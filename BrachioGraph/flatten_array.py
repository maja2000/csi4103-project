def array_to_2d(original_array):
    array_2d = []
    for x in original_array:
        for y in x:
            array_2d.append(y)
    return array_2d

