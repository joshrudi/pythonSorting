def ascending(dataToSort):

    dataSorted = ""
    dataSorted += dataToSort[0]

    # loop through dataSort and put in dataSorted ascending (Using Insertion Sort Algo)
    for i in range(1, len(dataToSort)):

        if dataToSort[i] < dataSorted[i - 1]:

            # if the next index is less than the previous, swap them
            dataSorted += dataSorted[i - 1]
            dataSorted = dataSorted[:i - 1] + dataToSort[i] + dataSorted[i:]

            # two nested for loops to arrange everything in ascending order
            for g in range(1, len(dataSorted)):
                for j in range(1, len(dataSorted)):
                    if dataSorted[j] < dataSorted[j - 1]:
                        dataSorted = dataSorted[:j - 1] + dataSorted[j] + dataSorted[j - 1] + dataSorted[j + 1:]

        else:

            # else then just add it to the end
            dataSorted += dataToSort[i]

    print(dataSorted)
    return dataSorted


dataToSort = "75982784"
ascending(dataToSort)

