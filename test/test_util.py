import pytest

import Abe.util as util

def test_calculate_target_004c792d():
    assert util.calculate_target(0x004c792d) == 0

def test_calculate_target_1d00ffff():
    assert util.calculate_target(0x1d00ffff) == 0xffff0000000000000000000000000000000000000000000000000000

def test_calculate_target_1c00800e():
    assert util.calculate_target(0x1c00800e) == 0x800e00000000000000000000000000000000000000000000000000

def test_calculate_target_1b0e7256():
    assert util.calculate_target(0x1b0e7256) == 0xe7256000000000000000000000000000000000000000000000000

def test_calculate_target_1b0098fa():
    assert util.calculate_target(0x1b0098fa) == 0x98fa000000000000000000000000000000000000000000000000

def test_calculate_target_1a6a93b3():
    assert util.calculate_target(0x1a6a93b3) == 0x6a93b30000000000000000000000000000000000000000000000

def test_calculate_target_1a022fbe():
    assert util.calculate_target(0x1a022fbe) == 0x22fbe0000000000000000000000000000000000000000000000

def test_calculate_target_1900896c():
    assert util.calculate_target(0x1900896c) == 0x896c00000000000000000000000000000000000000000000

def test_calculate_target_1e0fffff():
    assert util.calculate_target(0x1e0fffff) == 0xfffff000000000000000000000000000000000000000000000000000000

def test_calculate_target_1f123456():
    assert util.calculate_target(0x1f123456) == 0x12345600000000000000000000000000000000000000000000000000000000

def test_calculate_target_80555555():
    assert util.calculate_target(0x80555555) == 0x5555550000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

def test_calculate_target_00777777():
    assert util.calculate_target(0x00777777) == 0x0

def test_calculate_target_01cccccc():
    assert util.calculate_target(0x01cccccc) == -0x4c

def test_calculate_target_02666666():
    assert util.calculate_target(0x02666666) == 0x6666

def test_calculate_target_03aaaaaa():
    assert util.calculate_target(0x03aaaaaa) == -0x2aaaaa
