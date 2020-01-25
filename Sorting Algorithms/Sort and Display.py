from plot import plot
# creates the list
def getList():
	return [100, 5, 63, 29, 69, 74, 96, 80, 82, 12]
#	return [82, 65, 93, 0, 60, 31, 99, 90, 31, 70]
#	return [63, 16, 78, 69, 36, 36, 3, 66, 75, 100]
#	return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#	return [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#	return [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]


# the bubble sort function
def bubbleSort(inputList):
        # input: a list of integers
        comparisons=0
        swaps=0
        n = len(inputList)
        for i in range(n):
                for j in range(0, n-i-1):
                        comparisons+=1
                        if inputList[j] > inputList[j+1] :
                                swaps+=1
                                inputList[j], inputList[j+1] = inputList[j+1], inputList[j]
        return comparisons,swaps
        # output: a number of comparisons and swaps


# the optimized bubble sort function
def optimizedBubbleSort(inputList):
        # input: a list of integers
        comparisons=0
        swaps=0
        n = len(inputList)
        for i in range(n):
                swap=False
                for j in range(0, n-i-1):
                        comparisons+=1
                        if inputList[j] > inputList[j+1] :
                                swap=True
                                swaps+=1
                                inputList[j], inputList[j+1] = inputList[j+1], inputList[j]
                if(not swap):
                        break
        return comparisons,swaps
        # output: a number of comparisons and swaps


# the selection sort function
def selectionSort(inputList):
# input: a list of integers
        comparisons=0
        swaps=-1
        n=len(inputList)
        for i in range(n):
                minSorted = i
                swaps+=1
                for j in range(i+1, len(inputList)):
                        comparisons+=1
                        if inputList[minSorted] > inputList[j]:
                                minSorted = j
                temp = inputList[i]
                inputList[i] = inputList[minSorted]
                inputList[minSorted] = temp
        return comparisons, swaps
# output: a number of comparisons and swaps


# the insertion sort function
def insertionSort_mod(inputList):
        # input: a list of integers
        comp = 0
        swap = 0
        for j in range(len(inputList)):
                key = inputList[j]
                temp = j
                comp+=1
                while temp>0 and inputList[temp-1]>key:
                        if inputList[temp-1]>key:
                                comp+=1
                        inputList[temp]=inputList[temp-1]
                        temp = temp-1
                        swap+=1
                inputList[temp]=key
        return comp,swap
# output: a number of comparisons and swaps

listToSort=getList()
listToSort=listToSort.sort()

# the main part of the program
bubble = bubbleSort(getList())
#print("The list: {}".format(getList()))
#print("After bubble sort: {}".format(listToSort))
#print("{} comparisons; {} swaps".format(comparisons,swaps))

#print("")

optimized = optimizedBubbleSort(getList())
#print("The list: {}".format(getList()))
#print("After optimized bubble sort: {}".format(listToSort))
#print("{} comparisons; {} swaps".format(comparisons,swaps))



#print("")

selection = selectionSort(getList())
#print("The list: {}".format(getList()))
#print("After selection sort: {}".format(listToSort))
#print("{} comparisons; {} swaps".format(comparisons,swaps))

#print("")

insertion = insertionSort_mod(getList())
#print("The list: {}".format(getList()))
#print("After insertion sort: {}".format(listToSort))
#print("{} comparisons; {} swaps".format(comparisons,swaps))
plot(bubble, optimized, selection, insertion)
