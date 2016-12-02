# encoding=UTF-8

# Copyright © 2011-2015 Jakub Wilk <jwilk@jwilk.net>
#
# This file is part of pdf2djvu.
#
# pdf2djvu is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# pdf2djvu is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.

from tools import (
    case,
    re,
)

class test(case):
    # Bug: https://github.com/jwilk/pdf2djvu/issues/59
    # + fixed in 0.7.10 [6c155e7cc346]

    def test(self):
        self.pdf2djvu('--monochrome').assert_()
        r = self.djvudump()
        r.assert_(stdout=re(r'Sjbz \[[0-9]{4,}\]'))

# vim:ts=4 sts=4 sw=4 et
