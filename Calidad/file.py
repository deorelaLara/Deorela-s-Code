def countChar(file_name='c:/Users/deore/OneDrive/Escritorio/Python/Calidad/test.txt'):
    file = open(file_name, 'r')
    count = 0
    content = file.read()

    for x in content:
        count += 1

    file.close()
    #return print(count)
    return count

if __name__=="__main__":
    #countChar()
    print(countChar('c:/Users/deore/OneDrive/Escritorio/Python/Calidad/test.txt'))