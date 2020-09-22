def file(path):
    file_name = open(path, 'r')
    list = []
    for line in file_name:
        list.append(line)
    file_name.close()
    return list