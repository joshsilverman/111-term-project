import os

#core global definitions
if (os.getcwd().find('\\') != -1): DS = '\\'
else: DS = '/'

ROOT = os.getcwd() + '%s..%ssrc' % (DS, DS)
VENDORS = ROOT + '%svendors' % DS
DATA = ROOT + "%sdata" % (DS)
TRANSCRIPT = ROOT + "%sdata%stranscript.db" % (DS, DS)