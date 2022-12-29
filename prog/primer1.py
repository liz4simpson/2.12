#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def wrapper_function():
    def hello_world():
        print('Hello world!')
    hello_world()


if __name__ == "__main__":
    wrapper_function()
