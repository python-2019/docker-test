#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import time

if __name__ == '__main__':
    for i in range(1000):
        time.sleep(1)
        if i ==10:
            i = 1/0
        print(datetime.datetime.now())