#insertion sort
def insertion_sort(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i - 1
        while (j >= 0 and temp < list[j]):
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = temp
list = input('Enter the numbers of the list: ').split()
list = [int(x) for x in list]
insertion_sort(list)
print('Sorted list: ', end='')
print(list)