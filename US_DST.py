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

# Set the years to get the dates in a list
dstyears = [2024, 2025, 2026, 2027, 2028, 2029, 2030]
# For each year in the list, get the start and end dates of Daylight Saving
for cntr in dstyears:
    dstStart = (
        datetime.date(cntr, 3, 1) + relativedelta(weekday=SU) + relativedelta(days=+7)
    )
    dstEnd = datetime.date(cntr, 11, 1) + relativedelta(weekday=SU)

    print(f"U.S. {cntr} DST Start {dstStart} - DST End {dstEnd}")
