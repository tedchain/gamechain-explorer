from .Sha256Chain import Sha256Chain

class GameChain(Sha256Chain):
    def __init__(chain, **kwargs):
        chain.name = 'GameChain'
        chain.dirname = ''
        chain.code3 = '???'
        # gamechain handshake is randomly created, so use Bitcoin compatible network settings as the default.
        chain.address_version = '\x00'
        chain.script_addr_vers = '\x05'
        chain.magic = '\xf9\xbe\xb4\xd9'
        chain.address_checksum = '\x00\x00\x00\x00'
        Sha256Chain.__init__(chain, **kwargs)

    # We don't set datadir_rpccport.
    # The port number is found in params.dat and should be set in gamechain.conf, e.g. rpcport=XXXX
    datadir_conf_file_name = "gamechain.conf"

