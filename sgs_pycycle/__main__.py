# -*- coding: utf-8 -*-
# SPDX-License-Identifier: BSD-2-Clause-FreeBSD
#
# Copyright (c) 2020, Simeon Simeonov
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE AUTHORS ``AS IS'' AND ANY EXPRESS OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
# NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
CLI entry point for the sgs_pycycle package

Examples:
python -m sgs_pycycle -h
"""
import argparse
import sys

import sgs_pycycle


def eprint(*arg, **kwargs):
    """stdderr print wrapper"""
    print(*arg, file=sys.stderr, flush=True, **kwargs)


def main(args=None):
    """the main entry point"""
    parser = argparse.ArgumentParser(
        prog=__package__,
        epilog=(f'%(prog)s {sgs_pycycle.__version__} by Simeon Simeonov '
                '(sgs @ Freenode)'),
        description='The following options are available')
    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'%(prog)s {sgs_pycycle.__version__}',
        help='display program-version and exit')
    args = parser.parse_args(args)


if __name__ == '__main__':
    main()
