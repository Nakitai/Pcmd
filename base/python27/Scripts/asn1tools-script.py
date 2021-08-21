#!C:\python27\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'asn1tools==0.155.3','console_scripts','asn1tools'
__requires__ = 'asn1tools==0.155.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('asn1tools==0.155.3', 'console_scripts', 'asn1tools')()
    )
