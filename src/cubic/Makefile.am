# Makefile.am for BEEBS cubic test
#
# Copyright (C) 2013 Embecosm Limited and University of Bristol
#
# Contributor Jeremy Bennett <jeremy.bennett@embecosm.com>
#
# This file is part of the Bristol/Embecosm Embedded Benchmark Suite.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bin_PROGRAMS = cubic
cubic_SOURCES = cubic.c \
	        basicmath_small.c \
		pi.h \
		snipmath.h \
		sniptype.h

include $(top_srcdir)/src/common.mk.am

AM_LDFLAGS += "-lm"

cubic_SOURCES += ${platform_src}
