import math

def euclidean_distance(list1, list2):
    '''(list of int, list of int) -> float
    Precondition: list1 and list2 length are equal
    '''
    sum = 0
    for index in range(len(list1)):
        sum = sum + math.pow((list1[index] - list2[index]), 2)

    return math.sqrt(sum)
