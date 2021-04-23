# Copyright (C) 2021 SUSE LLC
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, see <http://www.gnu.org/licenses/>.

from testapi import *


def run(self):
    assert_and_click('openqa-login')
    assert_screen('openqa-logged-in')

    assert_and_click('openqa-search')
    type_string('shutdown.pm')
    send_key('ret')
    assert_screen('openqa-search-results')


def post_fail_hook(self):
    send_key('ctrl-alt-f3') # switch to root console
    script_run('openqa-cli api --o3 experimental/search q=shutdown.pm')
    save_screenshot()


def test_flags(self):
    return dict([('fatal', 1)])
