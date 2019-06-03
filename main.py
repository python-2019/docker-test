#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import datetime
import time

if __name__ == '__main__':
    for i in range(1000):
        time.sleep(1)
        print(datetime.datetime.now())