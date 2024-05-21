def read_file(filename):
    file = open(filename)
    my_data = file.read()
    return my_data


def write_file(filename, data):
    file = open(filename, "w")
    file.write(data)