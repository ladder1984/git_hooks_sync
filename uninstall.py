# -*- coding: utf-8 -*-
import os

from git_hooks_sync import hooks_dir
from install import hook_types

try:
    for hook_type in hook_types:
        os.remove(os.path.join(hooks_dir, hook_type))
    print(u'卸载成功')
    os.system('pause')
except BaseException as e:
    print(e)
    print(u'卸载失败')
    os.system('pause')
