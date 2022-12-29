#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def decorator(start):
    def wrapper(func):
        def inner(li):
            return func(li) + start
        return inner
    return wrapper


@decorator(start=5)
def s_el(li):
    return sum([int(x) for x in li.split(' ')])


if __name__ == "__main__":
    nums = input('Введите числа через пробел: ')
    print(s_el(nums))
