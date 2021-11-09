# =============================================================================
#               ____                      _      ____       _   _
#  _ __  _   _ / ___| ___ _ __   ___ _ __(_) ___|  _ \ __ _| |_| |__
# | '_ \| | | | |  _ / _ \ '_ \ / _ \ '__| |/ __| |_) / _` | __| '_ \
# | |_) | |_| | |_| |  __/ | | |  __/ |  | | (__|  __/ (_| | |_| | | |
# | .__/ \__, |\____|\___|_| |_|\___|_|  |_|\___|_|   \__,_|\__|_| |_|
# |_|    |___/
# =============================================================================
# Authors:            Patrick Lehmann
#
# Python unittest:    Testing the pyGenericPath.URL module
#
# Description:
# ------------------------------------
#		TODO
#
# License:
# ============================================================================
# Copyright 2017-2021 Patrick Lehmann - Bötzingen, Germany
# Copyright 2007-2016 Patrick Lehmann - Dresden, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
# ============================================================================
#
"""
pyGenericPath
#############

:copyright: Copyright 2007-2021 Patrick Lehmann - Bötzingen, Germany
:license: Apache License, Version 2.0
"""
from unittest     import TestCase

from pyTooling.pyGenericPath.URL import URL, Protocols


if __name__ == "__main__":
	print("ERROR: you called a testcase declaration file as an executable module.")
	print("Use: 'python -m unitest <testcase module>'")
	exit(1)


class GenericPath(TestCase):
	url : URL = URL.Parse("https://paebbels.github.io:8080/path/to/endpoint?user=paebbels&token=1234567890")

	def test_Protocol(self):
		self.assertEqual(self.url.Scheme, Protocols.HTTPS)

	def test_Port(self):
		self.assertEqual(self.url.Host.Port, 8080)

	def test_Hostname(self):
		self.assertEqual(self.url.Host.Hostname, "paebbels.github.io")

	def test_str(self):
		self.assertEqual(str(self.url), "https://paebbels.github.io:8080/path/to/endpoint?user=paebbels&token=1234567890")
