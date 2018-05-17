from distutils.core import setup

execfile("Mce/version.py")

setup(
    name         = "GameChain Explorer",
    version      = __version__,
    requires     = ['Crypto.Hash'],
    packages     = ['Mce', 'Mce.Chain'],
    package_data = {'Mce': ['htdocs/*.*','htdocs/*/*.*']},
    author       = "Coin Sciences Ltd",
    author_email = "simon@coinsciences.com",
    url          = "https://github.com/tedchain/gamechain-explorer",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Database :: Front-Ends',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Office/Business :: Financial',
        'Topic :: Security :: Cryptography',
        #'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    description  = "GameChain Explorer: a free browser for GameChain blockchains.",
    long_description = """GameChain Explorer reads a GameChain block chain from disk, loads
it into a database, indexes it, and provides a web interface to search
and navigate it.  GameChain blockchains are similar to the Bitcoin blockchain with
the addition of native assets and permissions.
GameChain Explorer is a fork of Abe.""",
    )
