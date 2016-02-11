

def diff_files():
    first_file = input('Enter the name of the first file: ')
    second_file = input('Enter the name of the second file: ')

    # Open first file and read its contents
    open_file1 = open(first_file)
    contents1 = open_file1.read()
    open_file1.close()
    
    # Open second file and read its contents
    open_file2 = open(second_file)
    contents2 = open_file2.read()
    open_file2.close()
    
    print(contents1)
    print(contents2)

    
