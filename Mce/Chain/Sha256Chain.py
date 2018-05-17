from . import BaseChain
from .. import util

class Sha256Chain(BaseChain):
    """
    A blockchain that hashes its block headers using double SHA2-256 as Bitcoin does.
    """
    def block_header_hash(chain, header):
        return util.double_sha256(header)
