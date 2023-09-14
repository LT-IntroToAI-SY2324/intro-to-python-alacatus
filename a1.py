"""Assignment 1

Fill in the following function skeletons - descriptions are provided in 
the docstring (the triple quote thing at the top of each function)

Some assert statements have been provided - write more of them to test your code!

The `raise NotImplementedError(...)`s are placeholders to help you not skip implementing
a function. They should be removed and replaced with your solution.

This portion of the assignment will not be graded, but this gives you some problems to 
check, if you do not complete the generative AI portion of the assignment.
"""

from typing import List, TypeVar

import random

def absolute(n: int) -> int:
    if n < 0:
        return n * -1
    elif n > 0:
        return n
    elif n == 0:
        return 0
    

def factorial(n: int) -> int:
    result = 1 
    for x in range(1, n+1):
        result *= x
    
    return result
    



T = TypeVar("T")


def every_other(lst: List[T]) -> List[T]:
    listt = []
    for x in range(0,len(lst),2):
        listt.append(lst[x])
    return listt



def sum_list(lst: List[int]) -> int:
    summ = 0
    for x in range(len(lst)):
        summ += lst[x]
    return summ

    


def mean(lst: List[int]) -> float:
    mean = 0
    for x in range(len(lst)):
        mean += lst[x]
    mean /= len(lst)
    return mean
    


def median(lst: List[int]) -> float:
    r = len(lst)
    if r % 2 == 0:
        median1 = lst[r//2]
        median2 = lst[r//2 - 1]
        median = (median1 + median2)/2
    else:
        median = lst[r//2]
    return median
    


def duck_duck_goose(lst: List[str]) -> List[str]:
    i = 0
    while len(lst) > 2:
        i += 2
        if i >= len(lst):
             i -= len(lst)
        lst.pop(i)
    return lst








"""Given an list of names (strings), play 'duck duck goose' with it, knocking out
every third name (wrapping around) until only two names are left.

In other words, when you hit the end of the list, wrap around and keep counting from
where you were.

For example, if given this list ['Nathan', 'Sasha', 'Sara', 'Jennie'], you'd first
knock out Sara. Then first 'duck' on Jennie, wrap around to 'duck' on Nathan and
'goose' on Sasha - knocking him out and leaving only Nathan and Jennie.

You may assume the list has 3+ names to start

Args:
    lst - a list of names (strings)

Returns:
    the resulting list after playing duck duck goose
"""


# this line causes the nested code to be skipped if the file is imported instead of run

if __name__ == "__main__":
    assert absolute(-1) == 1, "absolute of -1 failed"
    assert factorial(3) == 6, "factorial of 3 failed"
    assert every_other([1, 2, 3, 4, 5]) == [
        1,
        3,
        5,
    ], "every_other of [1,2,3,4,5] failed"
    assert sum_list([1, 2, 3]) == 6, "sum_list of [1,2,3] failed"
    assert mean([1, 2, 3, 4, 5]) == 3, "mean of [1,2,3,4,5] failed"
    assert median([1, 2, 3, 4, 5]) == 3, "median of [1,2,3,4,5] failed"

    names = ["roscoe", "kim", "woz", "solin", "law", "remess"]
    assert duck_duck_goose(names) == ["roscoe", "law"]

    print("All tests passed!")