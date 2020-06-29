def mergeSort(num_list):
    """
    sorts a list via merge sorting algorithm
    :param num_list: num_list[0] = number of elements to be sorted
    :return: none, num_list is mutable
    """
    if len(num_list) > 1:
        middle = len(num_list) // 2  # integer divide to find middle
        left = num_list[:middle]  # slice list into right and left halves
        right = num_list[middle:]

        mergeSort(left)  # recursive call
        mergeSort(right)  # recursive call

        i = 0  # init variables
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                num_list[k] = left[i]
                i += 1
            else:
                num_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            num_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            num_list[k] = right[j]
            j += 1
            k += 1


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
        mergeSort(number_list)
        # add values to output string
        for i in range(0, len(number_list)):
            output += str(number_list[i])
            output += " "
        # start newline after each line
        output += "\n"

# write file
with open("merge.out", 'w') as outfile:
    # cast my_sum as string, write to file
    outfile.write(str(output))