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
A pure Python object-mapper for the Oslo Bysykkel API

This module provides some classes that create a nice abstraction layer
from the JSON content presented by the API. Hence making it easier and more
intuitive to manipulate the data fetched from the API.
"""


class StationStatus:
    """
    Station status-class that represents a single station and its information
    as presented by the API.

    https://gbfs.urbansharing.com/oslobysykkel.no/station_status.json
    """


class StationInformation:
    """
    Station information-class that represents all stations as presented by
    the API.

    https://gbfs.urbansharing.com/oslobysykkel.no/station_information.json

    Instance(s) of this class serve as container object for the StationStatus
    objects.
    """
