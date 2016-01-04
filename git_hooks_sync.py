# -*- coding: utf-8 -*-
import ConfigParser
import os
import re
import sys


def git_shell(git_command):
    try:
        return os.popen(git_command).read().strip()
    except:
        return None


# 基本目录信息
git_dir = os.path.abspath(git_shell('git rev-parse --git-dir'))
project_dir = os.path.dirname(git_dir)
self_dir = os.path.join(project_dir, 'git_hooks_sync')
config_path = os.path.join(self_dir, 'config.ini')
hooks_dir = os.path.join(git_dir, 'hooks')
if os.path.isdir(os.path.join(self_dir, 'hook_scripts')):
    scripts_dir = os.path.join(self_dir, 'hook_scripts')  # 脚本目录在git_hooks_sync下
elif os.path.isdir('../hook_scripts'):  # 脚本目录与git_hooks_sync平级
    scripts_dir = os.path.abspath('../hook_scripts')
elif os.path.isdir('../../hook_scripts'):  # 脚本目录与项目目录平级
    scripts_dir = os.path.abspath('../../hook_scripts')
else:
    scripts_dir = ''


# 清除Windows记事本自动添加的BOM
def __clean_bom(file_name):
    with open(file_name, 'r+') as f:
        content = f.read()
        content = re.sub(r"\xfe\xff", "", content)
        content = re.sub(r"\xff\xfe", "", content)
        content = re.sub(r"\xef\xbb\xbf", "", content)
        f.seek(0)
        f.write(content)


# 获得配置信息
def __get_config():
    __clean_bom(config_path)
    try:
        config = ConfigParser.ConfigParser()
        config.read(config_path)
        able = config.get('config', 'able').strip()
        return able
    except BaseException as e:
        return None, None, None


# 获得启用脚本
def __get_selected_scripts(script_type):
    try:
        config = ConfigParser.ConfigParser()
        config.read(config_path)
        scripts = config.get('selected_scripts', script_type)
        return scripts.split(',') if scripts else []
    except:
        return []


# 运行脚本
def __run_scripts(script_type, scripts):
    if not scripts_dir:
        return  # 不存在脚本目录则退出
    for script in scripts:
        execfile('%s/%s-hook_scripts/%s.py' % (scripts_dir, script_type, script))


# 主函数
def go(script_type):
    able = __get_config()
    if not able == '1':
        return
    scripts = __get_selected_scripts(script_type)
    __run_scripts(script_type, scripts)


if __name__ == "__main__":
    script_type = os.path.split(sys.argv[1])[1]
    go(script_type)
