import random
import time
from time_inputs.generate import document_sizes 


def sortAndCountInv(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        mid = len(arr) // 2
        left_half, left_inversions = sortAndCountInv(arr[:mid])
        right_half, right_inversions = sortAndCountInv(arr[mid:])
        merged_arr, split_inversions = mergeAndCountSplitInv(
            left_half, right_half)
        inversions = left_inversions + right_inversions + split_inversions
        return merged_arr, inversions


def mergeAndCountSplitInv(left, right):
    merged = []
    split_inversions = 0
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            split_inversions += len(left) - i
            j += 1
    merged += left[i:]
    merged += right[j:]
    return merged, split_inversions


def countInversions(arr):
    _, inversions = sortAndCountInv(arr)
    return inversions


def sortAccording(arr: list, accordingTo: list) -> dict:
    dic = sorted(dict(zip(accordingTo, arr)).items())
    returnable = {k: v for k, v in dic}
    return returnable


def calculateRanking(matrix, compareTo):
    compareTo += -1
    rankings = []
    accordingTo = matrix[compareTo][1:]
    for i in range(len(matrix)):
        if (i == compareTo):
            continue
        person_preferences = list(sortAccording(
            matrix[i][1:], accordingTo).values())
        inversions = countInversions(person_preferences)
        rankings.append((i+1, inversions))
    rankings.sort(key=lambda x: x[1])
    return rankings


# Дані
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# matrix = [
#     [1, 1, 10, 8, 5, 9, 4, 3, 6, 2, 7],
#     [2, 9, 8, 7, 6, 4, 10, 2, 5, 1, 3],
#     [3, 9, 8, 2, 5, 3, 4, 10, 6, 1, 7],
#     [4, 9, 1, 2, 8, 5, 3, 7, 6, 4, 10],
#     [5, 10, 7, 6, 3, 5, 1, 4, 2, 8, 9]
# ]

def fileRead(fileName: str) -> list:
    returnable = []
    with open(f"./{fileName}", "r") as filey:
        filey = filey.readlines()
        returnable.append(filey[0].split())
        returnable.append([])
        for line in filey[1:]:
            returnable[1].append(line.split())
    return returnable


def fileWrite(fileName: str, matrix: list, customer: int) -> None:
    with open(fileName, "w") as filey:
        filey.write(f"{customer}\n")
        for line in matrix:
            line = map(str, line)
            filey.write(" ".join(line)+"\n")
        filey.write(str(customer))


matrix = [
    [1, 5, 2, 1, 3, 4],
    [2, 3, 2, 4, 1, 5],
    [3, 4, 5, 3, 2, 1],
    [4, 5, 1, 4, 3, 2],
    [5, 1, 2, 5, 4, 3],
    [6, 2, 5, 4, 1, 3],
    [7, 2, 4, 5, 3, 1],
    [8, 5, 3, 1, 4, 2],
    [9, 4, 5, 2, 3, 1],
    [10, 3, 1, 2, 4, 5]
]


def full_cycle(fileName: str, prefferedUser: int = 'all', resultDir: str = "") -> None:
    st_time = time.time_ns()

    resultDir = resultDir + "/"
    filey = fileRead(fileName)
    customers = filey[0][0]
    movies = filey[0][1]
    filey = filey[1]

    path = fileName.replace('.txt', '_result')

    if prefferedUser == 'all':
        for customer in range(1, int(customers)+1):
            rankings = calculateRanking(filey, customer)
            fileWrite(f"./{resultDir}{path}_{customer}.txt",
                      rankings, customer)
    else:
        rankings = calculateRanking(filey, prefferedUser)
        fileWrite(f"./{resultDir}{path}_{prefferedUser}.txt",
                  rankings, prefferedUser)

    end_time = time.time_ns()
    full_time = end_time - st_time

    print(f"{fileName.replace('.txt', '')} user {prefferedUser} took time: {full_time} nanoseconds")


if __name__ == "__main__":
    # for i, (rows, columns) in enumerate(document_sizes, start=1):
    #     fileName = f"time_{rows}_{columns}.txt"
    #     full_cycle(f'time_inputs/{fileName}', 'all', 'actual_outputs') #random.randrange(1, rows)
    full_cycle('example_inputs/input_2_1000.txt', 1, 'actual_outputs')
    full_cycle('example_inputs/input_2_1000.txt', 2, 'actual_outputs')

    full_cycle('example_inputs/input_3_5.txt', resultDir='actual_outputs')

    full_cycle('example_inputs/input_5_5.txt', 4, 'actual_outputs')
    full_cycle('example_inputs/input_5_5.txt', 5, 'actual_outputs')

    full_cycle('example_inputs/input_5_10.txt', 3, 'actual_outputs')
    full_cycle('example_inputs/input_5_10.txt', 4, 'actual_outputs')

    full_cycle('example_inputs/input_10_5.txt', 6, 'actual_outputs')
    full_cycle('example_inputs/input_10_5.txt', 9, 'actual_outputs')
    full_cycle('example_inputs/input_10_5.txt', 10, 'actual_outputs')

    full_cycle('example_inputs/input_22_7.txt', 1, 'actual_outputs')
    full_cycle('example_inputs/input_22_7.txt', 10, 'actual_outputs')

    full_cycle('example_inputs/input_240_5.txt', 1, 'actual_outputs')
    full_cycle('example_inputs/input_240_5.txt', 100, 'actual_outputs')

    full_cycle('example_inputs/input_720_6.txt', 1, 'actual_outputs')
    full_cycle('example_inputs/input_720_6.txt', 100, 'actual_outputs')

    full_cycle('example_inputs/input_1000_5.txt', 289, 'actual_outputs')
    full_cycle('example_inputs/input_1000_5.txt', 356, 'actual_outputs')
    full_cycle('example_inputs/input_1000_5.txt', 674, 'actual_outputs')

    full_cycle('example_inputs/input_1000_100.txt', 95, 'actual_outputs')
    full_cycle('example_inputs/input_1000_100.txt', 206, 'actual_outputs')
    full_cycle('example_inputs/input_1000_100.txt', 210, 'actual_outputs')
    full_cycle('example_inputs/input_1000_100.txt', 231, 'actual_outputs')
    full_cycle('example_inputs/input_1000_100.txt', 306, 'actual_outputs')
    full_cycle('example_inputs/input_1000_100.txt', 430, 'actual_outputs')
    full_cycle('example_inputs/input_1000_100.txt', 552, 'actual_outputs')
    full_cycle('example_inputs/input_1000_100.txt', 572, 'actual_outputs')
    full_cycle('example_inputs/input_1000_100.txt', 719, 'actual_outputs')
    full_cycle('example_inputs/input_1000_100.txt', 847, 'actual_outputs')
