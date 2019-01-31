#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from cx_Freeze import setup,Executable
import os
#
#把python打包成exe可执行文件
os.environ['TCL_LIBRARY'] = r"C:\Users\yp\Anaconda3\tcl\tcl8.6"
os.environ['TK_LIBRARY'] =  r"C:\Users\yp\Anaconda3\tcl\tk8.6"

include_files = [
    r"C:\Users\yp\Anaconda3\DLLs\tcl86t.dll",
    r"C:\Users\yp\Anaconda3\DLLs\tk86t.dll "
]

# 建立exe文件的选项
build_exe_options = {
    # 打包
    "packages":['os',"tkinter",'requests','idna'],
    #排除
    # "excludes":["tkinter"],
    # 包含文件
    "include_files":include_files
}
base = None
# platform 平台  系统平台
if sys.platform == "win32":
    base = "Win32GUI"
    #打完包后取的名字  版本 描述 选项  执行
setup(name = "translate_tool",version="0.1",description="fanyitools!",
      options={"build_exe":build_exe_options},
    executables={Executable("windows.py",base=base)})


