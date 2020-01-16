#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_calc
----------------------------------

Acceptance tests for MVP.
"""
import sys
sys.path.append('/app')

import pytest
from time import sleep
from assertpy import assert_that
from oet.domaim import SKAMid, SubArray, ResourceAllocation, Dish
from tango import DeviceProxy

def pause():
    sleep(4)


def test_allocation():
    the_telescope = SKAMid()
    the_subarray = SubArray(1)
    the_resource_allocation = ResourceAllocation(dishes=[Dish(1), Dish(2)])

    print("Starting up telescope ...")
    the_telescope.start_up()

    print("Releasing any previously allocated resources... ")
    result = the_subarray.deallocate()
    pause()

    print("Allocating new resources... ")
    result = the_subarray.allocate(the_resource_allocation)
    pause()

    assert_that(result).is_equal_to(the_resource_allocation)

    # Confirm result via direct inspection of TMC
    subarray_proxy = DeviceProxy('ska_mid/tm_subarray_node/1')
    pause()
    receptor_list = subarray_proxy.receptorIDList
    pause()

    assert_that(receptor_list).is_equal_to("(1, 2)")

    print("Now deallocating resources ... ")
    subarray.deallocate()
    pause()

    # Confirm result via direct inspection of TMC - expecting None 
    receptor_list = subarray_proxy.receptorIDList
    pause()
    
    assert_that(receptor_list).is_equal_to(None)

    print("Subarry has no allocated resources")

    # put telescope to standby
    telescope.standby()
    print("Script Complete: All resources dealoccated, Telescope is in standby")
