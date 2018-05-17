from .Sha256Chain import Sha256Chain

class Testnet(Sha256Chain):
    """
    The original bitcoin test blockchain.
    """
    def __init__(chain, **kwargs):
        chain.name = 'Testnet'
        chain.code3 = 'BC0'
        chain.address_version = '\x6f'
        chain.script_addr_vers = '\xc4'
        chain.magic = '\xfa\xbf\xb5\xda'
        Sha256Chain.__init__(chain, **kwargs)

    # XXX
    #datadir_conf_file_name = "bitcoin.conf"
    #datadir_rpcport = 8332
