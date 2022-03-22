def array_to_2d(original_array):
    new_array = []
    for line in original_array:
        new_line = []
        for coordinate in line:
            new_line.append([coordinate[0]-512, coordinate[1]])
        new_array.append(new_line)
    return new_array

