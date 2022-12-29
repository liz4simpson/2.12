#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def benchmark(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end - start))
        return return_value

    return wrapper


@benchmark
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.text


if __name__ == "__main__":
    webpage = fetch_webpage('https://google.com')
    print(webpage)
