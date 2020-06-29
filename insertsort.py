
def insertionSort(num_list):
    """
    sort a list of numbers via insertion sorting algorithm
    :param num_list: num_list[0] = how many numbers to sort
    :return: None, num_list is mutable
    """
    for ind in range(1, len(num_list)):
        current = num_list[ind]
        j = ind - 1
        while j >= 0 and current > num_list[j]:
            num_list[j + 1] = num_list[j]
            j -= 1
        num_list[j + 1] = current


# open file
with open('data.txt', 'r') as infile:
    # iterate through each line
    output = ""
    for line in infile:
        # populate list by values separated by spaces, strip newline characters
        number_list = line.strip().split(" ")
        # typecast strings to ints
        for i in range(0, len(number_list)):
            number_list[i] = int(number_list[i])
        # remove first value
        del number_list[0]
        # sort
        insertionSort(number_list)
        # add values to output string
        for i in range(0, len(number_list)):
            output += str(number_list[i])
            output += " "
        # start newline after each line
        output += "\n"

# write file
with open("insert.out", 'w') as outfile:
    # cast my_sum as string, write to file
    outfile.write(str(output))