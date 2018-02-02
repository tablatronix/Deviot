#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals

import sublime

quick_panel_active = False
quick_panel_id = 0


<<<<<<< HEAD:libs/QuickPanel.py
def quickPanel(items, callback, window=False, flags=0, index=0):
=======
def quick_panel(items, callback, window=False, flags=0, index=0):
>>>>>>> a409637fc6f72cbea323be5a2b6803b3115a5abd:libraries/quick_panel.py
    if(not flags):
        flags = sublime.KEEP_OPEN_ON_FOCUS_LOST
    window = sublime.active_window()
    window.show_quick_panel(items, callback, flags, index)
