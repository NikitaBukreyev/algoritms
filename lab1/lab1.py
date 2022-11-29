import time, random, sys, glob, os, copy
import datetime as dt

sys.setrecursionlimit(5000)



#<----------------------------RANDROM NUMBER GENERATOR------------------------->
def number_generator(size):
    # Open a file
    file = open(str(size)+".txt", "w")

    # Generating random numbers
    for i in range(size):
        no = random.randrange(1,200000,1)
        # Writing random numbers in the file
        file.write(str(no)+" ");

    # Close opend file
    file.close()


#<---------------------------- OUTPUT LIST ------------------------>
def writeList(list,type):

    # Checking Sort type
    if type == "m":
        name = "_MergeSort.txt"
      # Open a file
    file = open("Sorted/"+str(len(list))+name, "w")

    # Generating random numbers
    for i in list:
        # Writing the number in sorted list
        file.write(str(i)+" ")

    # Close opend file
    file.close()

#<------------------------------------ MERGE SORT --------------------------------->
def merge(S1, S2, S):
    """Merge two sorted Python lists S1 and S2 into properly sized list S."""
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i+j] = S1[i]      # copy ith element of S1 as next item of S
            i += 1
        else:
            S[i+j] = S2[j]      # copy jth element of S2 as next item of S
            j += 1

def merge_sort(S):
    """Sort the elements of Python list S using the merge-sort algorithm."""
    n = len(S)
    if n < 2:
        return                # list is already sorted
    # divide
    mid = n // 2
    S1 = S[0:mid]           # copy of first half
    S2 = S[mid:n]           # copy of second half
    # conquer (with recursion)
    merge_sort(S1)          # sort copy of first half
    merge_sort(S2)          # sort copy of second half
    # merge results
    merge(S1, S2, S)        # merge sorted halves back into S
    #print(S)

# <----------------- METHOD TO MAKE LIST FROM FILE ----------------->

def read_filenum(file):
    alist=[]
    for line in file:
        line = line.strip()
        blist = line.split()
        blist = [int(i) for i in blist]
        alist.extend(blist)
    return alist

#<---------------------------------- GENERATING NUMBERS ------------------------------------------>
number_generator(100)
number_generator(2000000)

#<---------------------------------- OPENING FILES ----------------------------------------------->
file2 = open('100.txt','r')
file5 = open('2000000.txt','r')

#<---------------------------------- CREATING LIST FROM FILE -------------------------------------->


list2 = read_filenum(file2)
list5 = read_filenum(file5)

list7 = copy.deepcopy(list2)
list10 = copy.deepcopy(list5)


list12 = copy.deepcopy(list2)
list15 = copy.deepcopy(list5)


# <------------------------------------ MERGE-SORT -------------------------------------------------->


t0 = dt.datetime.now()
merge_sort(list2)
merge_time2 = (dt.datetime.now()-t0).microseconds



t0 = dt.datetime.now()
merge_sort(list5)
merge_time5 = (dt.datetime.now()-t0).microseconds



writeList(list2,"m")


writeList(list5,"m")


# <-------------------------------------- PRINTING OUTPUT --------------------------------------------------->

# <------------------------------------ MERGE SORT ---------------------------------------->
print("MergeSort")
print("Input size (N): (# of numbers) \t\t Time cost:")
print("100 \t\t\t\t\t", merge_time2, "microseconds")
print("2000000 \t\t\t\t\t", merge_time5, "microseconds")

print("===================================================================================================================")
print()


