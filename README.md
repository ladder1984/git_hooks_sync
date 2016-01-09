# git_hooks_sync指南

用git管理git hooks。

# 安装与配置

## 添加git_hooks_sync

这一步是下载git_hooks_sync文件并添加到项目文件中，就可以像管理普通文件的方式管理git_hooks_sync和其中的hooks脚本。一个成员操作即可。

- subtree方式（推荐）
  
  切换到git项目根目录，执行：
  
  ``` 
  git remote add -f git_hooks_sync https://github.com/ladder1984/git_hooks_sync.git
  git subtree add --prefix=git_hooks_sync git_hooks_sync master --squash
  git subtree pull --prefix=git_hooks_sync git_hooks_sync master --squash
  ```
  
- 下载<https://github.com/ladder1984/git_hooks_sync/archive/master.zip>，解压后放到项目根目录

## 安装与卸载

运行`install.py`安装，运行`uninstall.py`卸载。每一个成员都需要执行安装才能在本地注册git_hooks_sync。

## 配置

* 脚本目录：git_hooks_sync会依次尝试`git_hoooks_sync/hooks_scripts`（git_hoooks_sync目录下）、`../hook_scripts`（项目根目录）、`../../hook_scripts`（与项目目录同级）作为脚本目录。对应的hooks类型脚本在<type>-scripts目录内，在config.ini选择启用相应脚本。
* 配置文件(config.ini)：控制是否启用git_hooks_sync与启用哪些脚本。详情见文件内注释。

# hooks概念

hooks是在git特定操作时触发的脚本，比如commit之前，merge之后，详见：<https://git-scm.com/book/uz/v2/Customizing-Git-Git-Hooks>

# git_hooks_sync原理

由git_hooks_sync接管触发git hooks后的操作。

# TODO

- 配置文件