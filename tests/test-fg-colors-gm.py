# encoding=UTF-8

# Copyright © 2010-2015 Jakub Wilk <jwilk@jwilk.net>
#
# This file is part of pdfdjvu.
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
    assert_equal,
    assert_in,
    case,
    count_ppm_colors,
)

class test(case):

    def test(self):
        # Bug: https://bitbucket.org/jwilk/pdf2djvu/issue/47
        # + fixed in 0.7.2 [3d0f55ae5a65]
        def t(i, n):
            self.require_feature('GraphicsMagick')
            self.pdf2djvu(
                '--dpi=72',
                '--fg-colors={0}'.format(i)
            ).assert_()
            r = self.decode()
            r.assert_(stdout=None)
            r = self.decode(mode='foreground')
            r.assert_(stdout=None)
            colors = count_ppm_colors(r.stdout)
            if isinstance(n, tuple):
                assert_in(len(colors), n)
            else:
                assert_equal(len(colors), n)
        yield t, 1, 2
        yield t, 2, 3
        yield t, 4, 5
        yield t, 255, 241
        yield t, 256, (245, 256)
        yield t, 652, (245, 325)

# vim:ts=4 sts=4 sw=4 et
