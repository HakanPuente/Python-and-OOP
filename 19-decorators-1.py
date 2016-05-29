#!/usr/bin/env python

# Decorators, as simple as it gets :)

# Reference: Decorators 101 - A Gentle Introduction to Functional Programming.
# By Jillian Munson - PyGotham 2014.
# https://www.youtube.com/watch?v=yW0cK3IxlHc

def my_decorator(my_function):
    def inner_decorator():
        print("This happened before!")
        my_function()
        print("This happens after ")
        print("This happened at the end!")
    return inner_decorator


@my_decorator
def decorated():
    print("This happened!")

if __name__ == '__main__':
    decorated()
