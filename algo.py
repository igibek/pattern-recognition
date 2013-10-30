import math
import sys

def euclidean_distance(list1, list2):
    '''(list of numbers, list of numbers) -> number

    Return the distance between two points in space
    
    Precondition: list1 and list2 length are equal

    >> give example
    
    '''
    sum = 0
    for index in range(len(list1)):
        sum = sum + math.pow((list1[index] - list2[index]), 2)

    return math.sqrt(sum)

def min_distance_between_center(centers, s_attr):
    '''(dictionary of centers, list of numbers) -> number

    Return the minimum distance between centers and object
    
    Precondition: list1 and list2 length are equal

    >> give example
    
    '''
    min = sys.maxsize

    for key in centers:
        tmp = euclidean_distance(centers[key], s_attr)
        if min > tmp:
            min = tmp
    
    return min

def max_distance(centers):
    '''(dictionary of centers) -> number

    Return the maximum distance between centers

    >> give example
    
    '''
    max = 0

    for key1 in centers:
        for key2 in centers:
            tmp = euclidean_distance(centers[key1], centers[key2])                
            if max < tmp:
                max = tmp
    
    return max

def is_center_exists(centers, objects, p):
    '''(dictionary of centers, dictionary of objects, number in range [1/2, 1] ) -> bool

    Return true if new center found

    >> give example
    
    '''
    max = 0
    nextCenterKey = ''
    for key in objects:
        tmp = min_distance_between_center(centers, objects[key])
        print(key + ":" + str(tmp))
        if max < tmp:
            max = tmp
            nextCenterKey = key
    
    if nextCenterKey != '' and max >= p*max_distance(centers):
        centers[nextCenterKey] = objects[nextCenterKey]
        return True
    
    return False

def read_from_file(path):
    '''(str path of file) -> dictionary of objects

    >> give example
    
    '''
    objects = {}
    f = open(path, 'r')
    for line in f:
        objects = eval(line)
    return objects

