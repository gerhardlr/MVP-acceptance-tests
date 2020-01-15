#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_calc
----------------------------------

Acceptance tests for MVP.
"""

import pytest
from assertpy import assert_that
from oet.domain import SKAMid, SubArray, ResourceAllocation, Dish

def test_halo_world():
    assert_that(1).is_equal_to(1)