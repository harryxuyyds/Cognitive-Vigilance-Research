# -*- coding: utf-8 -*-
# Time          : 2024-05-16
# Author        : Harry Xu.
# File          : data_analysis_app.py
# Description   : 认知性警戒作业模拟及绩效测试系统 - 数据分析系统
# Release       : V1.0


import tkinter
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk
import ttkbootstrap


def da_tab_I_content_display():
    tkinter.Label(da_tab_I_root, text='认知性警戒作业模拟及绩效测试系统 - 数据分析系统', font=('HarmonyOS Sans SC', 22, 'bold')).place(x=120, y=80)
    tkinter.Label(da_tab_I_root, text='Copyright 2023 - 2024\n\nPowered by PbiD :)', font=('Consolas', 10)).place(x=900, y=80)
    tkinter.Label(da_tab_I_root, text='主页', font=('HarmonyOS Sans SC', 14, 'bold')).place(x=20, y=220)
    tkinter.Label(da_tab_I_root, text='这是心理特征对认知性警戒作业疲劳的影响研究项目的数据分析系统，隶属于认知性警戒作业模拟及绩效测试系统', font=('HarmonyOS Sans SC', 12)).place(x=20, y=260)
    tkinter.Label(da_tab_I_root, text='此系统的创作目的在于为项目管理者提供更便捷的数据分析解决方案，打通一站式处理全项目周期流程的最后一环', font=('HarmonyOS Sans SC', 12)).place(x=20, y=300)
    tkinter.Label(da_tab_I_root, text='我们希望你可以通过此软件系统完成除实时生理监测（需要硬件仪器配合）外的所有内容', font=('HarmonyOS Sans SC', 12)).place(x=20, y=340)
    tkinter.Label(da_tab_I_root, text='本系统具体的功能介绍可见于各标签页的说明文字或此项目的软件文档', font=('HarmonyOS Sans SC', 12)).place(x=20, y=380)
    tkinter.Label(da_tab_I_root, text='在开始之前，请确保 WebDAV 云端或本地程序目录下的 <data> 数据文件夹的完整性', font=('HarmonyOS Sans SC', 12)).place(x=20, y=420)
    tkinter.Label(da_tab_I_root, text='注：本数据分析系统的 <警戒作业分析> 基于认知性警戒作业模拟及绩效测试系统导出，<生理指标分析> 基于 Biofeedback Xpert 软件导出', font=('HarmonyOS Sans SC', 12)).place(x=20, y=460)


def da_tab_II_content_display():
    tkinter.Label(da_tab_II_root, text='被试信息预览与自动化', font=('HarmonyOS Sans SC', 14, 'bold')).place(x=20, y=20)


def da_tab_III_content_display():
    pass


def da_tab_IV_content_display():
    pass


def da_tab_V_content_display():
    pass


def main(root):
    global data_analyze_root, da_tab_I_root, da_tab_II_root, da_tab_III_root, da_tab_IV_root, da_tab_V_root
    data_analyze_root = tkinter.Toplevel(root)
    data_analyze_root.title('认知性警戒作业模拟及绩效测试系统 - 数据分析系统')
    data_analyze_root.geometry('1200x720')
    data_analyze_root.minsize(1200, 720)
    data_analyze_root.maxsize(1200, 720)
    data_analyze_root.resizable(False, False)
    data_analyze_root.tk.call('wm', 'iconphoto', data_analyze_root._w, tkinter.PhotoImage(file='.\\icons\\ic_public_connection_filled.png'))
    da_tab_bar = tkinter.ttk.Notebook(data_analyze_root)
    da_tab_I_root = tkinter.ttk.Frame(da_tab_bar)
    da_tab_II_root = tkinter.ttk.Frame(da_tab_bar)
    da_tab_III_root = tkinter.ttk.Frame(da_tab_bar)
    da_tab_IV_root = tkinter.ttk.Frame(da_tab_bar)
    da_tab_V_root = tkinter.ttk.Frame(da_tab_bar)
    da_tab_VI_root = tkinter.ttk.Frame(da_tab_bar)
    da_tab_VII_root = tkinter.ttk.Frame(da_tab_bar)
    da_tab_VIII_root = tkinter.ttk.Frame(da_tab_bar)
    da_tab_bar.add(da_tab_I_root, text='    数据分析系统主页    ')
    da_tab_bar.add(da_tab_II_root, text='    被试信息预览与自动化    ')
    da_tab_bar.add(da_tab_III_root, text='    数据标签定位    ')
    da_tab_bar.add(da_tab_IV_root, text='    警戒作业分析    ')
    da_tab_bar.add(da_tab_V_root, text='    生理指标分析    ')
    da_tab_bar.add(da_tab_VI_root, text='    相关性因素分析    ')
    da_tab_bar.add(da_tab_VII_root, text='    分析报告预览与导出    ')
    da_tab_bar.add(da_tab_VIII_root, text='    程序设置与高级组件    ')
    da_tab_bar.pack(padx=0, pady=0, fill=tkinter.BOTH, expand=True)
    da_tab_I_content_display()
    da_tab_II_content_display()
    da_tab_III_content_display()
    da_tab_IV_content_display()
    da_tab_V_content_display()
    data_analyze_root.mainloop()
