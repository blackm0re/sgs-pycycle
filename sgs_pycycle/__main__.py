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
    """stderr print wrapper"""
    print(*arg, file=sys.stderr, flush=True, **kwargs)


def main(args=None):
    """the main entry point"""
    parser = argparse.ArgumentParser(
        prog=__package__,
        epilog=(f'%(prog)s {sgs_pycycle.__version__} by Simeon Simeonov '
                '(sgs @ Freenode)'),
        description='The following options are available')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        '-l', '--list-all-stations',
        action='store_true',
        dest='list_all_stations',
        default=False,
        help=('Lists all active stations with id, name, '
              'number of docks available, number of bikes available'))
    parser.add_argument(
        '-k', '--sort-by-key',
        type=str,
        dest='sort_by_key',
        default='',
        help='Sorts the stations by the provided key')
    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'%(prog)s {sgs_pycycle.__version__}',
        help='display program-version and exit')
    args = parser.parse_args(args)
    if args.list_all_stations:
        client = sgs_pycycle.client.Client(
            'http://simeon.simeonov.no/bysykkel/gbfs.json')
        collection = client.get_station_collection()
        if args.sort_by_key:
            collection.sort_by_key(args.sort_by_key)
        for station in collection:
            print(station)


if __name__ == '__main__':
    main()
