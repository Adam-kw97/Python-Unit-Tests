import os
import shutil
import pytest

abc = [1, 8, 3, 4, 5, 6, 7]
efg = [9, 9, 4, 3, 24, 6, 12, 13]
coin_flips = [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# 1: Task didn't specify order of vectors so I am looking at first vector and check elements in loop if they appear in second vector.
# If yes, loop is broken and we have repeated value
def find_repeated_number(vector1, vector2):
    first_repeated = None
    for obj in vector1:
        for obj2 in vector2:
            if obj == obj2:
                first_repeated = obj
                return first_repeated

    return first_repeated


# 2: I did it on Windows -> linux check if owner is admin looks diff
def find_file(path):
    path_to_file = ""
    byte_size = 14 * (2 ** 20)
    arr = os.listdir(path)
    for file in arr:
        user_id = os.stat(path + file).st_uid
        if user_id == 0:
            is_exe = shutil.which(file, path=path)
            if is_exe is not None:
                size = os.path.getsize(path + file)
                if size < byte_size:
                    path_to_file = path + file
                    print("File: " + path_to_file)
                    return path_to_file

    return path_to_file


# 3: there are 2 possible results of final sequence: 1010... or 0101..
# function should check 2 ways and return faster way
def min_permutations(sequence):
    flip_sequence = sequence
    flip_sequence2 = []
    counter0 = 0
    counter2 = 0
    length = len(flip_sequence)
    for n in flip_sequence:
        flip_sequence2.append(n)
    for i in range(length - 1):
        if flip_sequence[i] == flip_sequence[i + 1]:
            if flip_sequence[i + 1] == 0:
                flip_sequence[i + 1] = 1
            else:
                flip_sequence[i + 1] = 0
            counter0 += 1
    # 2nd way
    if flip_sequence2[0] == 0:
        flip_sequence2[0] = 1
    else:
        flip_sequence2[0] = 0
    counter2 += 1
    for i in range(length - 1):
        if flip_sequence2[i] == flip_sequence2[i + 1]:
            if flip_sequence2[i + 1] == 0:
                flip_sequence2[i + 1] = 1
            else:
                flip_sequence2[i + 1] = 0
            counter2 += 1

    return min(counter0, counter2)


def test1_task1():
    assert find_repeated_number([1, 8, 3, 4, 5, 6, 7], [9, 9, 4, 3, 24, 6, 12, 13]) == 3


def test2_task1():
    assert find_repeated_number([11, 30, 33, 4, 5, 6, 7], [12, 91, 6, 3, 24, 6, 12, 13]) == 6


def test1_task2():
    assert find_file("C:\Riot Games\League of Legends\\")  == "C:\Riot Games\League of Legends\LeagueClientUx.exe"




def test1_task3():
    assert min_permutations([1,0,1,0,0,1,0,1,0,1,0,1,1,0,1,0,1,0,0,0,1,1,1,0,0,0]) == 11


def test2_task3():
    assert min_permutations([1,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1]) == 6



