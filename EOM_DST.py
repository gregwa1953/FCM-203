# DST2
#! /usr/bin/env python
#  -*- coding: utf-8 -*-
# ======================================================
#     US_DST.py
#  ------------------------------------------------------
# Created for Full Circle Magazine Issue #203
# Written by G.D. Walters
# Copyright © 2023, 2024 by G.D. Walters
# This source code is released under the MIT License
# ======================================================

import datetime
from dateutil.relativedelta import *


dstyears = [2024, 2025, 2026, 2027, 2028, 2029, 2030]
for cntr in dstyears:
    dstStart = datetime.date(cntr, 3, 1) + relativedelta(day=31, weekday=SU(-1))
    dstEnd = datetime.date(cntr, 10, 1) + relativedelta(day=31, weekday=SU(-1))

    print(
        f"Last Sunday of month countries - {cntr} DST Start {dstStart} - DST End {dstEnd}"
    )
