# -*- coding: utf-8 -*-
import os
from git_hooks_sync import hooks_dir

hook_types = ('pre-commit',
              'prepare-commit-msg',
              'commit-msg',
              'post-commit',
              'post-checkout',
              'pre-rebase',
              'post-merge',
              'post-rewrite'
              )

hook_content = """#!/bin/sh
python ./git_hooks_sync/git_hooks_sync.py $0
"""


if __name__ == "main":
    try:
        if not os.path.isdir(hooks_dir):
            os.mkdir(hooks_dir)
        for hook_type in hook_types:
            with open(os.path.join(hooks_dir, hook_type), 'w') as f:
                f.write(hook_content)
        print(u'安装成功')
        os.system('pause')
    except BaseException as e:
        print(e)
        print(u'安装失败')
        os.system('pause')


