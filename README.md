git_hooks_sync指南
-----------------------
用git管理git hooks。


## 安装与配置
### 使用方式
使用subtree或者复制文件的方式把git_hooks_sync目录放到项目的根目录下，就可以像管理普通文件的方式管理git_hooks_sync和其中的hooks脚本。需要注意的是，每一个启用git_hooks_sync的用户都需要自行安装和卸载。
运行`install.py`安装，运行`uninstall.py`卸载。

脚本目录为git_hooks_sync/scripts，对应的hooks类型脚本在<type>-scripts目录内，在config.ini选择启用相应脚本。

### 配置

配置在config.ini文件中，selected_scripts表示启用的脚本，以英文','分割。config中的选项及含义见注释，1表示开，0表示关。需要注意的是，update_config表示是否更新config.ini文件（“更新的含义见下文”），执行install会覆盖config.ini。如果你并不打算自己更改git hooks的运作，就无需关心config.ini文件。

需要注意的是commit-msg脚本用于给commit-msg自动添加信息，添加的顺序类似栈，写在后面的出现在前面。


### hooks概念

git的hooks就在.git/hooks/目录下，一个初始化的git仓库就会包含若干形如“pre-commit.sample”的文件，这个文件内容为hooks示例，只有把文件名改为pre-commit时才会启用。hooks是在git特定操作时触发的脚本，比如commit之前，merge之后，我们就可以用hooks做一些检出与修改操作

### git_hooks_sync原理

处罚hook时统一调用项目目录内的git_hooks_sync进行处理。

# TODO
- 配置文件
