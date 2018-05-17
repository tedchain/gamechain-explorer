from .Sha256Chain import Sha256Chain

class Bitcoin(Sha256Chain):
    def __init__(chain, **kwargs):
        chain.name = 'Bitcoin'
        chain.code3 = 'BTC'
        chain.address_version = '\x00'
        chain.script_addr_vers = '\x05'
        chain.magic = '\xf9\xbe\xb4\xd9'
        Sha256Chain.__init__(chain, **kwargs)
