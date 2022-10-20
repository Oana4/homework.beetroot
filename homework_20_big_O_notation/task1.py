from typing import List, Tuple


# Following will be some very short explanations:
# O(n) because we only have an interation through a list with length n
def question1(first_list: List[int], second_list: List[int]) -> List[int]:
    res: List[int] = []
    for el_first_list in first_list:
        if el_first_list in second_list:
            res.append(el_first_list)
    return res


# O(1) is constant because no matter what the integer n is, we will have every time
# the same number of executions (n to the power of 3 repeated 10 times), independent of n
def question2(n: int) -> int:
    for _ in range(10):
        n **= 3
    return n


# O(n^2) because we have nested loops of 2 arrays of the same length (n)
# I considered the worst scenario in the loops to determine the complexity
def question3(first_list: List[int], second_list: List[int]) -> List[int]:
    temp: List[int] = first_list[:]
    for el_second_list in second_list:
        flag = False
        for check in temp:
            if el_second_list == check:
                flag = True
                break
        if not flag:
            temp.append(el_second_list)
    return temp


# O(n) because it also iterates through the entire input array of size n
def question4(input_list: List[int]) -> int:
    res: int = 0
    for el in input_list:
        if el > res:
            res = el
    return res
