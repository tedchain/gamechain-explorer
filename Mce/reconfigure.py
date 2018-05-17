#!/usr/bin/env python

"""Reconfigure an Abe instance."""

import sys
import logging

import util
import firstbits

def keep_scriptsig_reconfigure(store, args):
    have = store.keep_scriptsig
    want = args.keep_scriptsig
    if have == want:
        return
    if want:
        store.log.warn("Can not turn on keep-scriptsig: unimplemented")
        return
    lock = store.get_lock()
    try:
        # XXX Should use a temporary schema_version.
        store.drop_view_if_exists("txin_detail")

        store.drop_column_if_exists("txin", "txin_scriptSig")
        store.drop_column_if_exists("txin", "txin_sequence")
        store.config['keep_scriptsig'] = "false"

        store.keep_scriptsig = want
        store.refresh_ddl()
        store.ddl(store.get_ddl("txin_detail"))
        store.save_configvar("keep_scriptsig")
        store.commit()
    finally:
        store.release_lock(lock)

def main(argv):
    cmdline = util.CmdLine(argv)
    cmdline.usage = lambda: \
        """Usage: python -m Abe.reconfigure [-h] [--config=FILE] [--CONFIGVAR=VALUE]...

Apply configuration changes to an existing Abe database, if possible.

  --help                    Show this help message and exit.
  --config FILE             Read options from FILE.
  --use-firstbits {true|false}
                            Turn Firstbits support on or off.
  --keep-scriptsig false    Remove input validation scripts from the database.

All configuration variables may be given as command arguments."""

    store, argv = cmdline.init()
    if store is None:
        return 0

    firstbits.reconfigure(store, args)
    keep_scriptsig_reconfigure(store, args)
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
