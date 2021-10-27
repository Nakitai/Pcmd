# Pcmd
#  前言
 >本人是 `PentestBox` 的忠实用户，使用了也有3年多了吧，毋庸置疑 `PentestBox` 是强大，的但是原作者已经不更新了，很多工具都没用也很老了，也太臃肿了，而且他也是用的`ConEmu`封装, 所以我想用`ConEmu`自己做一个，于是就通过`ConEmu` 二次编译成 `Pcmd`, 目前还有很多环境没有加入，后期慢慢加入。

#  使用
- 运行 `Pcmd.exe` 或 `Pcmd64.exe`, 基础操作命令同 `cmd` 相同，部分 `Linux` 命令如 `ls` 等。
- `ctrl + t` 新建一个窗口。
- `ctrl + w` 关闭当前窗口。
- `ctrl + tab` 或 `ctrl + 数字` 切换窗口。

#  添加工具
> 和 `Pentestbox` 一样我们可以添加一些自定义的工具。例：我们这里添加一个工具 `geek.exe` 一个轻量级卸载工具。
1. 在 `tools` 目录创建 `geek` 文件夹并把 `geek.exe` 复制到其中。
2. 打开 `config` 目录下 `doskey.config` 文件，此文件就是 `Clink` 注入的别名文件。
```config
geek = "%tools%/geek/geek.exe" $T
```
3. 这里 `=号` 前面 `geek` 是终端的运行命令，`=号` 后面是程序的路径 `%tools%` 就是 `tools` 目录路径。
4. 我们终端运行 `geek`，注：如果没有生效请 `ctrl + t` 新建一个窗口在运行。

# 更新日志
- 2021-08-19
  -  使用 `PortableGit` 代替 `coreutils`。
  -  添加 `burpsuite` 工具，使用 `burpsuite` 启动英文版，使用 `burpsuitezh` 启动汉化版。
- 2021-08-20
  - 添加 `hfs` 轻量级文件服务器工具，命令行使用  `hfs` 启动。
  - 添加 `winhex` 二进制查看修改工具，命令行使用 `winhex` 启动。
- 2021-08-21
  - 添加 `python27` 环境，命令行使用 `python27` 启动。
  - 添加 `sqlmap` SQL注入检测工具，使用 `sqlmap` 启动工具。
- 2021-10-28
  - 添加 `windwos` 自带的环境变量。
  - 添加 `Windows-Exploit` 漏洞扫描程序，使用 `exploit` 运行。
  - 修改了任务栏只显示一个Pcmd活动窗口，顶部cmd图标使用Pcmd图标，取消了关闭需要点击确认按钮。