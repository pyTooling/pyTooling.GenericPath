# EMACS settings: -*- tab-width: 2; indent-tabs-mode: t -*-
# vim: tabstop=2:shiftwidth=2:noexpandtab
# kate: tab-width 2; replace-tabs off; indent-width 2;
# =============================================================================
#               ____                      _      ____       _   _
#  _ __  _   _ / ___| ___ _ __   ___ _ __(_) ___|  _ \ __ _| |_| |__
# | '_ \| | | | |  _ / _ \ '_ \ / _ \ '__| |/ __| |_) / _` | __| '_ \
# | |_) | |_| | |_| |  __/ | | |  __/ |  | | (__|  __/ (_| | |_| | | |
# | .__/ \__, |\____|\___|_| |_|\___|_|  |_|\___|_|   \__,_|\__|_| |_|
# |_|    |___/
# =============================================================================
# Authors:						Patrick Lehmann
#
# Python package:	    A generic path to derive domain specific path libraries.
#
# Description:
# ------------------------------------
#		TODO
#
# License:
# ============================================================================
# Copyright 2017-2020 Patrick Lehmann - Bötzingen, Germany
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#		http://www.apache.org/licenses/LICENSE-2.0
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
from typing import List


class Base():
	"""Base-class for all pyGenericPath path elements"""

	DELIMITER = "/"

	_parent = None #

	def __init__(self, parent):
		self._parent = parent


class RootMixIn(Base):
	"""Mixin-class for root elements in a path system."""

	def __init__(self):
		super().__init__(None)


class ElementMixIn(Base):
	"""Mixin-class for elements in a path system."""

	_elementName: str = None

	def __init__(self, parent, elementName):
		super().__init__(parent)
		self._elementName = elementName

	def __str__(self):
		return self._elementName


class PathMixIn():
	"""Mixin-class for a path."""

	ELEMENT_DELIMITER = "/"
	ROOT_DELIMITER =    "/"

	_isAbsolute: bool = None
	_elements:   List = None

	def __init__(self, elements, isAbsolute):
		self._isAbsolute = isAbsolute
		self._elements =   elements

	def __len__(self):
		return len(self._elements)

	def __str__(self):
		result = self.ROOT_DELIMITER if self._isAbsolute else ""

		if (len(self._elements) > 0):
			result = result + str(self._elements[0])

			for element in self._elements[1:]:
				result = result + self.ELEMENT_DELIMITER + str(element)

		return result

	@classmethod
	def Parse(cls, path: str, root, pathCls, elementCls):
		"""Parses a string representation of a path and returns a path instance."""

		parent = root

		if path.startswith(cls.ROOT_DELIMITER):
			isAbsolute = True
			path = path[len(cls.ELEMENT_DELIMITER):]
		else:
			isAbsolute = False

		parts = path.split(cls.ELEMENT_DELIMITER)
		elements = []
		for part in parts:
			element = elementCls(parent, part)
			parent =  element
			elements.append(element)

		return pathCls(elements, isAbsolute)


class SystemMixIn():
	"""Mixin-class for a path system."""
