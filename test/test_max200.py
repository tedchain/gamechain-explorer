import pytest

from db import testdb
import os
import Abe.util
import Abe.Chain

@pytest.fixture(scope="module")
def max200(testdb):
    try:
        Abe.util.sha3_256('x')
    except Exception as e:
        pytest.skip('SHA3 not working: e')
    dirname = os.path.join(os.path.split(__file__)[0], 'max200')
    store = testdb.load('--datadir', dirname)
    return store

def test_block_number(max200):
    assert max200.get_block_number(max200.get_chain_by_name('Maxcoin').id) == 200
