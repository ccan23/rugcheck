#!/usr/bin/env python3

import sys
from .rugcheck import rugcheck

def rugcheck_cli():
    if len(sys.argv) != 2:
        print('rugcheck v1.0.0\nUsage: rugcheck <token_address>')
        sys.exit(1)

    token = sys.argv[1]
    rc = rugcheck(token)

    print(rc)