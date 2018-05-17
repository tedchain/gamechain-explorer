import pytest

import os
import json
import tempfile
import py.path

from db import testdb
import data
import Abe.Chain
from Abe.deserialize import opcodes

@pytest.fixture(scope="module")
def gen(testdb, request):
    gen = data.testnet14(testdb)
    chain = gen.chain
    blocks = gen.blocks

    # A - C* - D**
    #   \
    #     E  - B*
    #
    # * contains tx1
    # ** contains tx2

    tx1 = gen.tx(txIn=[gen.txin(prevout=blocks[1]['transactions'][0]['txOut'][0], scriptSig='XXX')],
                 txOut=[gen.txout(addr='n1pTUVnjZ6GHxujaoJ62P9NBMNjLr5N2EQ', value=50e8)])
    A = blocks[-1]
    C = gen.block(prev=A, transactions=[gen.coinbase(), tx1])
    E = gen.block(prev=A)
    B = gen.block(prev=E, transactions=[gen.coinbase(), tx1])

    tx2 = gen.tx(txIn=[gen.txin(prevout=C['transactions'][1]['txOut'][0], scriptSig='YYY')],
                 txOut=[gen.txout(addr='2NFTctsgcAmrgtiboLJUx9q8qu5H1qVpcAb', value=50e8)])

    D = gen.block(prev=C, transactions=[gen.coinbase(), tx2])

    blocks += [B, C, D, E]

    # XXX Lots of code duplicated in test_std_tx.py.
    datadir = py.path.local(tempfile.mkdtemp(prefix='abe-test-'))
    request.addfinalizer(datadir.remove)
    gen.save_blkfile(str(datadir.join('blk0001.dat')), blocks)

    gen.store = testdb.load('--datadir', json.dumps([{
                    'dirname': str(datadir),
                    'chain': chain.name,
                    'loader': 'blkfile'}]))
    gen.chain = gen.store.get_chain_by_name(chain.name)

    return gen

@pytest.fixture(scope="module")
def a2NFT(gen):
    return data.ah(gen, '2NFTctsgcAmrgtiboLJUx9q8qu5H1qVpcAb')

def test_a2NFT_balance(a2NFT, gen):
    assert a2NFT['balance'] == { gen.chain.id: 50e8 }
