# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def select_sort(array):
    # Use a breakpoint in the code line below to debug your script.
    print("select sort: ")
    for i in range(len(array) - 1):
        minimum_position = i
        for j in range(minimum_position + 1, len(array)):
            if array[minimum_position] > array[j]:
                temp = array[minimum_position]
                array[minimum_position] = array[j]
                array[j] = temp
    return array


def insert_sort(array):
    print("Insert Sort: ")
    for i in range(1, len(array)):
        value_to_sort = array[i]

        while array[i - 1] > value_to_sort and i > 0:
            array[i], array[i - 1] = array[i - 1], array[i]
            i = i - 1
    return array


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(select_sort([10, 12, 1, 2, 0, 5]))
    print(insert_sort([10, 12, 1, 2, 0, 5]))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
