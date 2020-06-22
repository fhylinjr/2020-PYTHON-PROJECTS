import time
from random import randint


def analyzer():
    listsize = int(input("What size list do you want to create? "))
    maxvalue = int(input("What is the max value of the range? "))
    numrun = int(input("How many times do you want to run? "))

    for i in range(1, numrun+1):
        arr = []

        for j in range(listsize):
            arr.append(randint(1, maxvalue))

        start = time.time()

        def quicksort(l1):
            if len(l1) < 2:
                return l1
            else:
                pivot = l1[-1]
                smaller, equal, larger = [], [], []
                for num in l1:
                    if num < pivot:
                        smaller.append(num)
                    elif num == pivot:
                        equal.append(num)
                    else:
                        larger.append(num)
                return quicksort(smaller) + equal + quicksort(larger)
        quicksort(arr)
        time1 = time.time() - start

        start2 = time.time()

        def mergesort(arr1, arr2):
            sorted_arr = []
            i = 0
            j = 0

            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    sorted_arr.append(arr1[i])
                    i += 1
                else:
                    sorted_arr.append(arr2[j])
                    j += 1

            if i == len(arr1):
                for num in arr2[j:]:
                    sorted_arr.append(num)
            elif j == len(arr2):
                for num in arr1[i:]:
                    sorted_arr.append(num)

            return sorted_arr

        def div_arr(l1):
            if len(l1) < 2:
                return l1[:]
            else:
                middle = len(l1) // 2
                arrlower = div_arr(l1[:middle])
                arrupper = div_arr(l1[middle:])
                return mergesort(arrlower, arrupper)
        div_arr(arr)
        time2 = time.time() - start2

        start3 = time.time()

        def bubsort(l1):
            swap = True
            while swap:
                count = 0
                for i in range(len(l1) - 1):
                    if l1[i] > l1[i + 1]:
                        l1[i], l1[i + 1] = l1[i + 1], l1[i]
                        swap = True
                        count += 1
                    if count == 0:
                        swap = False
        bubsort(arr)
        time3 = time.time() - start3

        start4 = time.time()

        def selsort(l1):
            marker = 0
            while marker < len(l1):
                for i in range(marker, len(l1)):
                    if l1[i] < l1[marker]:
                        l1[marker], l1[i] = l1[i], l1[marker]
                marker += 1
        selsort(arr)
        time4 = time.time() - start4

        start5 = time.time()

        def builtinsort(l1):
            l1.sort()

        builtinsort(arr)
        time5 = time.time() - start5

        start6 = time.time()

        def inssort(l1):
            key = 1
            marker = 1
            while marker < len(l1):
                for i in range(key):
                    if l1[key] < l1[key - 1]:
                        l1[key - 1], l1[key] = l1[key], l1[key - 1]
                        key -= 1

                marker += 1
                key = marker

        inssort(arr)
        time6 = time.time() - start6

        print("Run:", i, "\nQuicksort   ->   Elapsed time:", time1, "\nMergesort   ->   Elapsed time:", time2,
              "\nBubblesort   ->   Elapsed time:", time3, "\nSelectionsort   ->   Elapsed time:", time4,
              "\nBuilt-Insort   ->   Elapsed time:", time5, "\nInsertion Sort   ->   Elapsed time:", time6)

        print("----------------------------------------------------------------------------------")


analyzer()
