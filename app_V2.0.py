import pandas as pd

import data_analysis_app

import hashlib
import io
import logging
import matplotlib.font_manager
import matplotlib.pyplot as plt
import os
from numpy import average, nan
import pandas
import PIL
from pprint import pprint
import random
import shutil
import sqlite3
import subprocess
import threading
import time
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk
import ttkbootstrap
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from webdav4.client import Client
import winsound
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
VERSION = 'V2.0'
BOOT_TIME = time.strftime('%Y%m%d-%H%M%S', time.localtime())
FONTS_INCLUDED = {'HarmonyOS Sans SC', 'HarmonyOS Sans'}
FONTS_INSTALL_PATH = '.\\fonts\\FontsInstaller.vbs'
DATABASE = ['storage.db']
def database_initial():
    storage_db_cursor.execute('''CREATE TABLE "options" (
                                "serial"	INTEGER NOT NULL UNIQUE,
                                "key"	TEXT NOT NULL,
                                "setting"	TEXT,
                                PRIMARY KEY("serial" AUTOINCREMENT)
                            );''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('captcha_encrypted', '6e4d97fcf372625b900dbef16915d429')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('dashboard_num', '4')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('display_time', '3')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('vacant_time', '1')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('period_time', '10')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('period_num', '5')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('rest_time', '2')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('interval_length', '4')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('interval_change_cycle', '8')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('event_num_per_min_high', '4.0')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('event_num_per_min_low', '2.0')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('rate_handover_status', '0')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('emergency_num_per_ten_min', '2')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('top_window_status', '0')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('del_window_status', '0')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('tip_enhanced_status', '0')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('force_dark_mode_status', '0')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('webdav_status', '0')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('webdav_account', 'null')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('webdav_password', 'null')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('local_filepath', 'null')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('keyboard_preference_I', 'Q')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('keyboard_preference_II', 'W')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('keyboard_preference_III', 'A')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('keyboard_preference_IV', 'S')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('keyboard_preference_opt_I', 'q')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('keyboard_preference_opt_II', 'w')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('keyboard_preference_opt_III', 'a')''')
    storage_db_cursor.execute(
        '''INSERT INTO options (key, setting) VALUES ('keyboard_preference_opt_IV', 's')''')
    storage_db_connect.commit()
def delete_root():
    if del_window_status:
        logging.warning('The exit operation is aborted')
        tkinter.messagebox.showwarning(
            title='系统端提示', message='此功能已被限制，若已完成测试，请示意项目组人员。')
    elif tkinter.messagebox.askquestion(title='退出程序', message='感谢使用，是否确定退出程序？') == 'yes':
        logging.info('Exiting the root window')
        root.destroy()
        try:
            watchdog_root.destroy()
        except NameError:
            pass
        else:
            logging.info('Exiting the watchdog_root window')
            watchdog_root.destroy()
        try:
            upload_root.destroy()
        except NameError:
            pass
        else:
            logging.info('Exiting the upload_root window')
            upload_root.destroy()
        try:
            keyboard_root.destroy()
        except NameError:
            pass
        else:
            logging.info('Exiting the keyboard_root window')
            keyboard_root.destroy()
        try:
            data_analyze_root.destroy()
        except NameError:
            pass
        else:
            logging.info('Exiting the data_analyze_root window')
            data_analyze_root.destroy()
def tab_I_content_display():
    def account_submit_display():
        if tkinter.messagebox.askyesno(
                title='系统端提示', message='已输入：%s - %s - %s - %s - %s\n请确认填写的信息是否正确！' %
                (tester_entry.get(), id_entry.get(), name_entry.get(), gender_combobox.get(), period_combobox.get())):
            global TESTER_CODE, ID, NAME, GENDER, PERIOD, START_TIME
            TESTER_CODE = tester_entry.get()
            ID = id_entry.get()
            NAME = name_entry.get()
            GENDER = gender_combobox.get()
            PERIOD = period_combobox.get()
            START_TIME = time.strftime("%m%d-%H%M%S", time.localtime())
            logging.info('Getting tester information: %s - %s - %s - %s - %s -%s' %
                (TESTER_CODE, ID, NAME, GENDER, START_TIME, PERIOD))
            status_check = '被试者：%s - %s - %s - %s，登陆时间：%s，%s阶段，欢迎使用 认知性警戒作业模拟及绩效测试系统' % (
                TESTER_CODE, ID, NAME, GENDER, START_TIME, PERIOD)
            bottom_status_bar.configure(text=status_check)
            account_submit.configure(state='disabled')
            tester_entry.configure(state='disabled')
            id_entry.configure(state='disabled')
            name_entry.configure(state='disabled')
            gender_combobox.configure(state='disabled')
            period_combobox.configure(state='disabled')
            account_reset.configure(state='normal')
    def account_reset_display():
        if tkinter.messagebox.askyesno(title='系统端提示', message='是否确定重置填写的信息？'):
            logging.info('The user resets the information')
            account_submit.configure(state='normal')
            tester_entry.configure(state='normal')
            id_entry.configure(state='normal')
            name_entry.configure(state='normal')
            gender_combobox.configure(state='normal')
            period_combobox.configure(state='normal')
            account_reset.configure(state='disabled')
    tkinter.Label(
        tab_I_root,
        text='认知性警戒作业模拟及绩效测试系统',
        font=('HarmonyOS Sans SC',24,'bold')).place(x=120,y=80)
    tkinter.Label(
        tab_I_root,
        text='Copyright 2023 - 2024\n\nPowered by PbiD :)',
        font=('Consolas', 10)).place(x=900, y=80)
    tkinter.Label(
        tab_I_root,
        text='主页',
        font=('HarmonyOS Sans SC',14,'bold')).place(x=20,y=260)
    tkinter.Label(
        tab_I_root,
        text='感谢你愿意参与此次模拟研究项目，我们将会量化你的心理特征与认知性警戒作业的测试情况。',
        font=('HarmonyOS Sans SC',12)).place(x=20,y=300)
    tkinter.Label(
        tab_I_root,
        text='*必填项* 请先在右侧填写相关信息，填写完成后请点击 <信息提交> 键。',
        font=('HarmonyOS Sans SC',12)).place(x=20,y=340)
    tkinter.Label(
        tab_I_root,
        text='在正式测试开始前，你可以在 <模拟作业教程> 选项卡页面下进行适应模拟。',
        font=('HarmonyOS Sans SC',12)).place(x=20,y=380)
    tkinter.Label(
        tab_I_root,
        text='在我们给出下一步提示前，请不要打开 <警戒作业测试> 和 <程序设置与高级组件> 选项卡页面。',
        font=('HarmonyOS Sans SC',12)).place(x=20,y=420)
    tkinter.Label(
        tab_I_root,
        text='*重要声明* 在测试过程中，请不要自行切换标签页！',
        font=('HarmonyOS Sans SC',12)).place(x=20,y=460)
    for index in range(16):
        tkinter.Label(
            tab_I_root,
            text='|',
            font=('HarmonyOS Sans',10,'bold')).place(x=900,y=300 +20 *index)
    tkinter.Label(
        tab_I_root,
        text='* 系统端 相关信息收集',
        font=('HarmonyOS Sans SC',12,'bold')).place(x=920,y=300)
    tkinter.Label(
        tab_I_root,
        text='声明：所有数据仅用于数据分析统计',
        font=('HarmonyOS Sans SC',10)).place(x=920,y=340)
    tkinter.Label(
        tab_I_root,
        text='请输入编号：',
        font=('HarmonyOS Sans SC',12)).place(x=920,y=380)
    tester_entry = tkinter.Entry(
        tab_I_root, width=12, font=('HarmonyOS Sans', 12))
    tester_entry.place(x=1030, y=380)
    tkinter.Label(
        tab_I_root,
        text='请输入学号：',
        font=('HarmonyOS Sans SC',12)).place(x=920,y=420)
    id_entry = tkinter.Entry(tab_I_root, width=12, font=('HarmonyOS Sans', 12))
    id_entry.place(x=1030, y=420)
    tkinter.Label(
        tab_I_root,
        text='请输入姓名：',
        font=('HarmonyOS Sans SC',12)).place(x=920,y=460)
    name_entry = tkinter.Entry(
        tab_I_root, width=12, font=('HarmonyOS Sans SC', 12))
    name_entry.place(x=1030, y=460)
    tkinter.Label(
        tab_I_root,
        text='请选择性别：',
        font=('HarmonyOS Sans SC',12)).place(x=920,y=500)
    gender_combobox = tkinter.ttk.Combobox(
        tab_I_root, width=10, font=(
            'HarmonyOS Sans SC', 12), values=('男', '女'))
    gender_combobox.place(x=1030, y=500)
    tkinter.Label(
        tab_I_root,
        text='请选择阶段：',
        font=('HarmonyOS Sans SC',12)).place(x=920,y=540)
    period_combobox = tkinter.ttk.Combobox(
        tab_I_root, width=10, font=(
            'HarmonyOS Sans SC', 12), values=('预测试', '第一轮测试', '第二轮测试'))
    period_combobox.place(x=1030, y=540)
    account_submit = tkinter.Button(tab_I_root, width=10, text='信息提交', font=(
        'HarmonyOS Sans SC', 10, 'bold'), command=account_submit_display)
    account_submit.place(x=920, y=590)
    account_reset = tkinter.Button(tab_I_root, width=10, text='信息重置', font=(
        'HarmonyOS Sans SC', 10, 'bold'), command=account_reset_display, state='disabled')
    account_reset.place(x=1030, y=590)
def tab_II_content_display():
    tkinter.Label(
        tab_II_root,
        text='心理特征测试',
        font=('HarmonyOS Sans SC',14,'bold')).place(x=20,y=20)
    tkinter.Label(
        tab_II_root,
        text='此功能已透过其他方式测试实现……',
        font=('HarmonyOS Sans SC',12)).place(x=20,y=60)
def tab_III_content_display():
    def simulation_display():
        try:
            ID, NAME, GENDER
        except NameError:
            logging.warning('The tester did not fill in the information')
            tkinter.messagebox.showwarning(
                title='系统端提示', message='请先在程序主页提交个人信息！')
            return
        time.sleep(2)
        status_check = 'InfoCheck-%s-Tab_III-Work-T-%s-%s-%s-%s-%s-%s' % (
            VERSION, TESTER_CODE, ID, NAME, GENDER, PERIOD, START_TIME)
        logging.info(status_check)
        bottom_status_bar.configure(text=status_check)
        next_submit.configure(state='normal')
        tkinter.Label(
            tab_III_root,
            text='当浏览完当前提示后，可点击<继续模拟>进行下一步提示。',
            font=('HarmonyOS Sans SC',10,'bold')).place(x=660,y=230)
        start_submit.configure(state='disabled')
        key_press = tkinter.Label(
            tab_III_root,
            text='Tips：当前，<%s%s%s%s> 键位分别对应 DashBoard_I ~ IV。'%(keyboard_preference_I,keyboard_preference_II,keyboard_preference_III,keyboard_preference_IV),
            font=('HarmonyOS Sans SC',10,'bold'))
        key_press.focus_set()
        key_press.place(x=660, y=300)
        key_press.bind("<Key>", key_feedback)
        simulation_next()
    def simulation_next():
        global status
        if status == 0:
            tkinter.Label(
                tab_III_root,
                text='               ',
                font=('HarmonyOS Sans SC',100)).place(x=50,y=140)
            tkinter.Label(
                tab_III_root,
                text='               ',
                font=('HarmonyOS Sans SC',100)).place(x=50,y=390)
            tkinter.Label(
                tab_III_root,
                text='12 —— 16',
                font=('HarmonyOS Sans SC',16,'bold')).place(x=50,y=160)
            tkinter.Label(
                tab_III_root,
                text='4          6',
                font=('HarmonyOS Sans SC',20,'bold')).place(x=50,y=230)
            tkinter.Label(
                tab_III_root,
                text='<- tips 目标区间',
                font=('HarmonyOS Sans SC',10)).place(x=170,y=165)
            tkinter.Label(
                tab_III_root,
                text='<- tips 操作数字对',
                font=('HarmonyOS Sans SC',10)).place(x=170,y=235)
            tkinter.Label(
                tab_III_root,
                text='tips 请你计算<操作数字对>之和 判断是否落在<目标区间>内\n此时 4+6=10 < 12，因此不需要按下键盘',
                font=('HarmonyOS Sans SC',10)).place(x=120,y=280)
            status += 1
        elif status == 1:
            tkinter.Label(
                tab_III_root,
                text='               ',
                font=('HarmonyOS Sans SC',100)).place(x=50,y=140)
            tkinter.Label(
                tab_III_root,
                text='               ',
                font=('HarmonyOS Sans SC',100)).place(x=50,y=390)
            tkinter.Label(
                tab_III_root,
                text='12 —— 16',
                font=('HarmonyOS Sans SC',16,'bold')).place(x=350,y=410)
            tkinter.Label(
                tab_III_root,
                text='8          7',
                font=('HarmonyOS Sans SC',20,'bold')).place(x=350,y=480)
            tkinter.Label(
                tab_III_root,
                text='tips 此时 12 < 8+7=15 < 16，因此需要按下键盘（此区块对应<%s>键）\n来试试看吧！'%keyboard_preference_IV,
                font=('HarmonyOS Sans SC',10)).place(x=200,y=530)
            status += 1
        elif status == 2:
            tkinter.Label(
                tab_III_root,
                text='               ',
                font=('HarmonyOS Sans SC',100)).place(x=50,y=140)
            tkinter.Label(
                tab_III_root,
                text='               ',
                font=('HarmonyOS Sans SC',100)).place(x=50,y=390)
            tkinter.Label(
                tab_III_root,
                text='8 —— 12',
                font=('HarmonyOS Sans SC',16,'bold')).place(x=50,y=160)
            tkinter.Label(
                tab_III_root,
                text='2          5',
                font=('HarmonyOS Sans SC',20,'bold')).place(x=50,y=230)
            tkinter.Label(
                tab_III_root,
                text='15 —— 19',
                font=('HarmonyOS Sans SC',16,'bold')).place(x=350,y=160)
            tkinter.Label(
                tab_III_root,
                text='7          6',
                font=('HarmonyOS Sans SC',20,'bold')).place(x=350,y=230)
            tkinter.Label(
                tab_III_root,
                text='2 —— 6',
                font=('HarmonyOS Sans SC',16,'bold')).place(x=50,y=410)
            tkinter.Label(
                tab_III_root,
                text='4          4',
                font=('HarmonyOS Sans SC',20,'bold')).place(x=50,y=480)
            tkinter.Label(
                tab_III_root,
                text='14 —— 18',
                font=('HarmonyOS Sans SC',16,'bold')).place(x=350,y=410)
            tkinter.Label(
                tab_III_root,
                text='4          6',
                font=('HarmonyOS Sans SC',20,'bold')).place(x=350,y=480)
            tkinter.Label(
                tab_III_root,
                text='tips 现在，快速判断一下上面这四个区块的情况吧，有异常就按下相应的键盘按键。',
                font=('HarmonyOS Sans SC',10)).place(x=50,y=540)
            status += 1
        elif status == 3:
            tkinter.Label(
                tab_III_root,
                text='               ',
                font=('HarmonyOS Sans SC',100)).place(x=50,y=140)
            tkinter.Label(
                tab_III_root,
                text='               ',
                font=('HarmonyOS Sans SC',100)).place(x=50,y=390)
            tkinter.Label(
                tab_III_root,
                text='8 —— 12',
                font=('HarmonyOS Sans SC',16,'bold')).place(x=50,y=160)
            tkinter.Label(
                tab_III_root,
                text='6          7',
                font=('HarmonyOS Sans SC',20,'bold')).place(x=50,y=230)
            tkinter.Label(
                tab_III_root,
                text='15 —— 19',
                font=('HarmonyOS Sans SC',16,'bold')).place(x=350,y=160)
            tkinter.Label(
                tab_III_root,
                text='9          9',
                font=('HarmonyOS Sans SC',20,'bold')).place(x=350,y=230)
            tkinter.Label(
                tab_III_root,
                text='6 —— 10',
                font=('HarmonyOS Sans SC',16,'bold')).place(x=50,y=410)
            tkinter.Label(
                tab_III_root,
                text='5          8',
                font=('HarmonyOS Sans SC',20,'bold')).place(x=50,y=480)
            tkinter.Label(
                tab_III_root,
                text='11 —— 15',
                font=('HarmonyOS Sans SC',16,'bold')).place(x=350,y=410)
            tkinter.Label(
                tab_III_root,
                text='4          6',
                font=('HarmonyOS Sans SC',20,'bold')).place(x=350,y=480)
            tkinter.Label(
                tab_III_root,
                text='tips 现在，快速判断一下上面这四个区块的情况吧，有异常就按下相应的键盘按键。',
                font=('HarmonyOS Sans SC',10)).place(x=50,y=540)
            status += 1
        elif status == 4:
            tkinter.Label(
                tab_III_root,
                text='               ',
                font=('HarmonyOS Sans SC',100)).place(x=50,y=140)
            tkinter.Label(
                tab_III_root,
                text='               ',
                font=('HarmonyOS Sans SC',100)).place(x=50,y=390)
            tkinter.Label(
                tab_III_root,
                text='基本的操作流程就是这些，不过在正式测试中还需要有更快的反应速度和持续的专注力哦 ~',
                font=('HarmonyOS Sans SC',10)).place(x=50,y=180)
            status = 0
            start_submit.configure(state='normal')
            next_submit.configure(state='disabled')
            feedback_submit.configure(state='disabled')
    def key_feedback(event):
        logging.info('The tester clicks the keyboard: %s' % str(event.keysym))
        if event.keysym in keyboard_preference_I or event.keysym in keyboard_preference_opt_I:
            index = -4
            key_warn.configure(text='键盘输入检查：你当前输入状态正常，请继续测试 ~')
        elif event.keysym in keyboard_preference_II or event.keysym in keyboard_preference_opt_II:
            index = -3
            key_warn.configure(text='键盘输入检查：你当前输入状态正常，请继续测试 ~')
        elif event.keysym in keyboard_preference_III or event.keysym in keyboard_preference_opt_III:
            index = -2
            key_warn.configure(text='键盘输入检查：你当前输入状态正常，请继续测试 ~')
        elif event.keysym in keyboard_preference_IV or event.keysym in keyboard_preference_opt_IV:
            index = -1
            key_warn.configure(text='键盘输入检查：你当前输入状态正常，请继续测试 ~')
        elif event.keysym in '??':
            key_warn.configure(text='键盘输入检查：你当前处于中文输入状态，请检查！')
            return
        else:
            key_warn.configure(text='键盘输入检查：除切换输入状态外，请不要按下其他按键！')
            return
        tips_IV = tkinter.Label(
            tab_III_root, text='', font=('HarmonyOS Sans SC', 10, 'bold'))
        tips_IV.place(x=670, y=630)
        if status == 1 or status == 3:
            tips_IV.configure(text='Nonono，不对哦！     ')
        elif status == 2 and index == -1 or status == 4 and index == -3:
            tips_IV.configure(text='Bingo，正确啦！     ')
        else:
            tips_IV.configure(text='Nonono，不对哦！     ')
    def simulation_feedback():
        tips_IV = tkinter.Label(
            tab_III_root, text='', font=('HarmonyOS Sans SC', 10, 'bold'))
        tips_IV.place(x=670, y=630)
        if status == 1 or status == 3:
            tips_IV.configure(text='Nonono，不对哦！     ')
        else:
            tips_IV.configure(text='Bingo，正确啦！     ')
    global status
    status = 0
    tkinter.Label(
        tab_III_root,
        text='模拟作业教程 —— 非正式测试',
        font=('HarmonyOS Sans SC',14,'bold')).place(x=20,y=20)
    tkinter.Label(
        tab_III_root,
        text='此页面将会通过测试样例来为你介绍警戒作业模拟的流程和细节。',
        font=('HarmonyOS Sans SC',12)).place(x=20,y=60)
    for index in range(40):
        tkinter.Label(
            tab_III_root,
            text='|',
            font=('HarmonyOS Sans',10,'bold')).place(x=650,y=20 * index)
    for index in range(40):
        tkinter.Label(
            tab_III_root,
            text='|',
            font=('HarmonyOS Sans',10,'bold')).place(x=1025,y=20 * index)
    tkinter.Label(
        tab_III_root,
        text='---------- Info_Area  信息区域 ----------',
        font=('HarmonyOS Sans SC',14,'bold')).place(x=660,y=0)
    tkinter.Label(
        tab_III_root,
        text='-------- Submit_Area  提交区域 --------',
        font=('HarmonyOS Sans SC',14,'bold')).place(x=660,y=500)
    tkinter.Label(
        tab_III_root,
        text='---------- 量表区域 ----------',
        font=('HarmonyOS Sans SC',14,'bold')).place(x=1030,y=0)
    tkinter.Label(
        tab_III_root,
        text='即将呈现量表内容，请做好准备！',
        font=('HarmonyOS Sans SC',10,'bold')).place(x=1040,y=50)
    tkinter.Label(
        tab_III_root,
        text='请尽快选择出最符合你当前状态的选项。',
        font=('HarmonyOS Sans SC',10,'bold')).place(x=1040,y=80)
    choose_I = tkinter.Button(
        tab_III_root, width=28, text='完全警觉，完全清醒', font=('HarmonyOS Sans SC', 11, 'bold'))
    choose_I.place(x=1035, y=150)
    choose_II = tkinter.Button(
        tab_III_root,
        width=28,
        text='很有活力，反应灵敏，但非最好状态',
        font=('HarmonyOS Sans SC',11,'bold'))
    choose_II.place(x=1035, y=200)
    choose_III = tkinter.Button(
        tab_III_root, width=28, text='情况一般，稍微清醒', font=('HarmonyOS Sans SC', 11, 'bold'))
    choose_III.place(x=1035, y=250)
    choose_IV = tkinter.Button(
        tab_III_root, width=28, text='有点累，不怎么清醒', font=('HarmonyOS Sans SC', 11, 'bold'))
    choose_IV.place(x=1035, y=300)
    choose_V = tkinter.Button(
        tab_III_root, width=28, text='挺累的，无精打采', font=('HarmonyOS Sans SC', 11, 'bold'))
    choose_V.place(x=1035, y=350)
    choose_VI = tkinter.Button(
        tab_III_root, width=28, text='非常疲惫，难以集中精神', font=('HarmonyOS Sans SC', 11, 'bold'))
    choose_VI.place(x=1035, y=400)
    choose_VII = tkinter.Button(
        tab_III_root, width=28, text='精疲力尽，无法有效地工作', font=('HarmonyOS Sans SC', 11, 'bold'))
    choose_VII.place(x=1035, y=450)
    tkinter.Label(
        tab_III_root,
        text='此页面呈现的量表仅作模拟样例使用！',
        font=('HarmonyOS Sans SC',10)).place(x=1040,y=520)
    tkinter.Label(
        tab_III_root,
        text='此页面的点击操作将不会被记录。',
        font=('HarmonyOS Sans SC',10)).place(x=1040,y=550)
    tkinter.Label(
        tab_III_root,
        text='如果你已做好准备，请点按下方按钮以开始模拟适应。',
        font=('HarmonyOS Sans SC',10)).place(x=660,y=50)
    tkinter.Label(
        tab_III_root,
        text='Please press the button below to continue.',
        font=('HarmonyOS Sans',10)).place(x=660,y=80)
    tkinter.Label(
        tab_III_root,
        text='当点按后，将有 2 秒的准备时间，随后模拟流程即刻开始。',
        font=('HarmonyOS Sans SC',10)).place(x=660,y=110)
    tkinter.Label(
        tab_III_root,
        text='当观察到任一模拟面板出现异常，请立刻点按相应键盘按键。',
        font=('HarmonyOS Sans SC',10)).place(x=660,y=550)
    tkinter.Label(
        tab_III_root,
        text='请你尽快熟悉右侧的量表选项信息，以便在测试中快速反应。',
        font=('HarmonyOS Sans SC',10)).place(x=660,y=400)
    key_warn = tkinter.Label(
        tab_III_root,
        text='键盘输入检查：请确认已处于英文输入状态或大写锁定状态。',
        font=('HarmonyOS Sans SC',10,'bold'))
    key_warn.place(x=660, y=460)
    start_submit = tkinter.Button(
        tab_III_root,
        width=42,
        text='开始模拟  START SIMULATION',
        font=('HarmonyOS Sans SC',10,'bold'),
        command=simulation_display)
    start_submit.place(x=670, y=150)
    next_submit = tkinter.Button(
        tab_III_root,
        width=42,
        text='继续模拟  CONTINUE SIMULATION',
        font=('HarmonyOS Sans SC',10,'bold'),
        state='disabled',
        command=simulation_next)
    next_submit.place(x=670, y=190)
    feedback_submit = tkinter.Button(
        tab_III_root,
        width=42,
        text='(此环节已禁用) 预警提交  SUBMIT FEEDBACK',
        font=('HarmonyOS Sans SC',10,'bold'),
        state='disabled',
        command=simulation_feedback)
    feedback_submit.place(x=670, y=600)
    tkinter.Label(
        tab_III_root,
        text='DashBoard_I',
        font=('HarmonyOS Sans',12,'italic')).place(x=50,y=100)
    tkinter.Label(
        tab_III_root,
        text='DashBoard_II',
        font=('HarmonyOS Sans',12,'italic')).place(x=350,y=100)
    tkinter.Label(
        tab_III_root,
        text='DashBoard_III',
        font=('HarmonyOS Sans',12,'italic')).place(x=50,y=350)
    tkinter.Label(
        tab_III_root,
        text='DashBoard_IV',
        font=('HarmonyOS Sans',12,'italic')).place(x=350,y=350)
def tab_IV_content_display():
    def time_display():
        while True:
            clock.configure(
                text='----------- ' +time.strftime('%Y-%m-%d %H:%M:%S') +' -----------')
            time.sleep(1)
    def test_display():
        def countdown_display(total_seconds):
            while total_seconds != 0:
                total_seconds -= 1
                countdown.configure(text='倒计时：%02dmin %02ds' %(total_seconds //60,total_seconds %60))
                time.sleep(1)
            if total_seconds == 0:
                logging.info('The countdown is over')
                display_status = False
                data_upload()
        def rest_countdown_display(total_seconds):
            countdown_round = period_num * 2 - 1
            total_seconds = [period_time * 60,rest_time * (display_time + vacant_time)]
            seconds_countdown = total_seconds[(countdown_round + 1) % 2]
            while countdown_round != 0:
                seconds_countdown -= 1
                rest_countdown.configure(text='距离下一阶段还有：%02dmin %02ds' %
                    (seconds_countdown //60,seconds_countdown %60))
                time.sleep(1)
                if seconds_countdown == 0:
                    countdown_round -= 1
                    seconds_countdown = total_seconds[(countdown_round + 1) % 2]
        def interval_countdown_display():
            interval_seconds = interval_change_time
            while True:
                interval_seconds -= 1
                interval_countdown.configure(
                    text='距离数字对目标区间变更还有： %02ds' %(interval_seconds))
                time.sleep(1)
                if interval_seconds == 0:
                    interval_seconds = interval_change_time
                    interval_start.append([random.randint(2, 10)
                                          for i in range(dashboard_num)])
                    logging.info('The number pair interval changed to %s' %
                                 str(interval_start[-1]))
        def dashboard_display():
            def choose_confirm(index):
                situation_end = time.time()
                situation_record.append(
                    [display_round_count, index, situation_end - situation_start])
                logging.info('The self-test of psychological scale completed %s' %str(index))
                choose_I.configure(state='disabled')
                choose_II.configure(state='disabled')
                choose_III.configure(state='disabled')
                choose_IV.configure(state='disabled')
                choose_V.configure(state='disabled')
                choose_VI.configure(state='disabled')
                choose_VII.configure(state='disabled')
            while display_status:
                global start_time, display_round_count, rest_round_count, rest_status
                if rest_round_count == 0:
                    dashboard_emergency.configure(image=img_scale)
                    rest_status = True
                    logging.info('Start of transition period')
                    key_warn.configure(text='键盘输入检查：当前处于过渡时间段内，请不要操作键盘！')
                    tkinter.Label(
                        tab_IV_root, text='    ', font=(
                            'HarmonyOS Sans SC', 360, 'bold')).place(x=1040, y=50)
                    rest_round_countdown.configure(
                        text='目前处于过渡时间段内，请完成右侧呈现的自评表！')
                    tkinter.Label(
                        tab_IV_root, text='即将呈现量表内容，请做好准备！', font=(
                            'HarmonyOS Sans SC', 10, 'bold')).place(x=1040, y=50)
                    tkinter.Label(
                        tab_IV_root, text='请尽快选择出最符合你当前状态的选项。', font=(
                            'HarmonyOS Sans SC', 10, 'bold')).place(x=1040, y=80)
                    situation_start = time.time()
                    choose_I = tkinter.Button(tab_IV_root, width=28, text='完全警觉，完全清醒', font=(
                        'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(0))
                    choose_I.place(x=1035, y=150)
                    choose_II = tkinter.Button(
                        tab_IV_root, width=28, text='很有活力，反应灵敏，但非最好状态', font=(
                            'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(1))
                    choose_II.place(x=1035, y=200)
                    choose_III = tkinter.Button(tab_IV_root, width=28, text='情况一般，稍微清醒', font=(
                        'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(2))
                    choose_III.place(x=1035, y=250)
                    choose_IV = tkinter.Button(tab_IV_root, width=28, text='有点累，不怎么清醒', font=(
                        'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(3))
                    choose_IV.place(x=1035, y=300)
                    choose_V = tkinter.Button(tab_IV_root, width=28, text='挺累的，无精打采', font=(
                        'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(4))
                    choose_V.place(x=1035, y=350)
                    choose_VI = tkinter.Button(tab_IV_root, width=28, text='非常疲惫，难以集中精神', font=(
                        'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(5))
                    choose_VI.place(x=1035, y=400)
                    choose_VII = tkinter.Button(tab_IV_root, width=28, text='精疲力尽，无法有效地工作', font=(
                            'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(6))
                    choose_VII.place(x=1035, y=450)
                if rest_round_count == 0:
                    time.sleep(rest_time * (display_time + vacant_time))
                    rest_status = False
                    dashboard_emergency.configure(image='')
                    logging.info('End of transition period')
                    key_warn.configure(text='键盘输入检查：请确认已处于英文输入状态或大写锁定状态。')
                    rest_round_count = display_round_per_min * period_time
                    tkinter.Label(tab_IV_root, text='    ', font=(
                            'HarmonyOS Sans SC', 360, 'bold')).place(x=1035, y=50)
                rest_status = False
                key_press.focus_set()
                data_item.append([[random.randint(2, 8) for i in range(2)]
                                 for j in range(dashboard_num)])
                for index in range(dashboard_num):
                    data_item[-1][index][1] = data_item[-1][index][0] + random.randint(-1,1)
                current_interval = interval_start[-1]
                for index in range(dashboard_num):
                    pair_sum = data_item[-1][index][0] + data_item[-1][index][1]
                    while interval_start[-1][index] <= pair_sum <= interval_start[-1][index] + interval_length:
                        data_item[-1][index] = [random.randint(2, 8) for i in range(2)]
                        data_item[-1][index][1] = data_item[-1][index][0] + random.randint(-1,1)
                        pair_sum = data_item[-1][index][0] + data_item[-1][index][1]
                random_prob = random.random()
                if random_prob < RATE_CALL:
                    display_area = random.randint(1, dashboard_num)
                    pair_sum = data_item[-1][display_area - 1][0] + data_item[-1][display_area - 1][1]
                    while not interval_start[-1][display_area - 1] <= pair_sum <= interval_start[-1][display_area - 1] + interval_length:
                        data_item[-1][display_area - 1] = [random.randint(2, 8) for i in range(2)]
                        data_item[-1][display_area - 1][1] = data_item[-1][display_area - 1][0] + random.randint(-1,1)
                        pair_sum = data_item[-1][display_area - 1][0] + data_item[-1][display_area - 1][1]
                display_round_count += 1
                rest_round_count -= 1
                rest_round_countdown.configure(
                    text='距离下次过渡时间段还有： %d 轮' %(rest_round_count))
                judge = interval_start[-1][0] <= sum(
                    data_item[-1][0]) <= interval_start[-1][0] + interval_length
                data_record.append([display_round_count,
                                    'DashBoard_I',
                                    interval_start[-1][0],
                                    interval_start[-1][0] + interval_length,
                                    data_item[-1][0][0],
                                    data_item[-1][0][1],
                                    judge,
                                    'Missed' if judge else 'Accepted'])
                judge = interval_start[-1][1] <= sum(
                    data_item[-1][1]) <= interval_start[-1][1] + interval_length
                data_record.append([display_round_count,
                                    'DashBoard_II',
                                    interval_start[-1][1],
                                    interval_start[-1][1] + interval_length,
                                    data_item[-1][1][0],
                                    data_item[-1][1][1],
                                    judge,
                                    'Missed' if judge else 'Accepted'])
                judge = interval_start[-1][2] <= sum(
                    data_item[-1][2]) <= interval_start[-1][2] + interval_length
                data_record.append([display_round_count,
                                    'DashBoard_III',
                                    interval_start[-1][2],
                                    interval_start[-1][2] + interval_length,
                                    data_item[-1][2][0],
                                    data_item[-1][2][1],
                                    judge,
                                    'Missed' if judge else 'Accepted'])
                judge = interval_start[-1][3] <= sum(
                    data_item[-1][3]) <= interval_start[-1][3] + interval_length
                data_record.append([display_round_count,
                                    'DashBoard_IV',
                                    interval_start[-1][3],
                                    interval_start[-1][3] + interval_length,
                                    data_item[-1][3][0],
                                    data_item[-1][3][1],
                                    judge,
                                    'Missed' if judge else 'Accepted'])
                dashboard_I_interval.configure(
                    text='%-2s —— %-2s' % (interval_start[-1][0], interval_start[-1][0] + interval_length))
                dashboard_II_interval.configure(
                    text='%-2s —— %-2s' % (interval_start[-1][1], interval_start[-1][1] + interval_length))
                dashboard_III_interval.configure(
                    text='%-2s —— %-2s' % (interval_start[-1][2], interval_start[-1][2] + interval_length))
                dashboard_IV_interval.configure(
                    text='%-2s —— %-2s' % (interval_start[-1][3], interval_start[-1][3] + interval_length))
                dashboard_I_data.configure(text='%s          %s' % (
                    data_item[-1][0][0], data_item[-1][0][1]))
                dashboard_II_data.configure(text='%s          %s' % (
                    data_item[-1][1][0], data_item[-1][1][1]))
                dashboard_III_data.configure(text='%s          %s' % (
                    data_item[-1][2][0], data_item[-1][2][1]))
                dashboard_IV_data.configure(text='%s          %s' % (
                    data_item[-1][3][0], data_item[-1][3][1]))
                start_time = time.time()
                time.sleep(display_time)
                if interval_start[-1] != current_interval:
                    dashboard_I_interval.configure(text='')
                    dashboard_II_interval.configure(text='')
                    dashboard_III_interval.configure(text='')
                    dashboard_IV_interval.configure(text='')
                dashboard_I_data.configure(text='')
                dashboard_II_data.configure(text='')
                dashboard_III_data.configure(text='')
                dashboard_IV_data.configure(text='')
                time.sleep(vacant_time)
        try:
            ID, NAME, GENDER
        except NameError:
            tkinter.messagebox.showwarning(
                title='系统端提示', message='请先在程序主页提交个人信息！')
            return
        time.sleep(2)
        global interval_start, data_item, data_record, display_round_count, rest_round_count, situation_record, display_status
        display_status = True
        interval_start = []
        data_item = []
        data_record = []
        situation_record = []
        display_round_count = 0
        rest_round_count = display_round_per_min * period_time
        start_submit.configure(state='disabled')
        status_check = 'InfoCheck-%s-Tab_IV-Work-O-MS-%s-%s-%s-%s-%s-%s' % (
            VERSION, TESTER_CODE, ID, NAME, GENDER, PERIOD, START_TIME)
        logging.info(status_check)
        bottom_status_bar.configure(text=status_check)
        interval_start.append([random.randint(2, 10)for i in range(dashboard_num)])
        logging.info('The number pair interval changed to %s' %
                     str(interval_start[-1]))
        tkinter.Label(
            tab_IV_root,
            text='请不要在一轮中连续点按键盘，否则只会记录首次数据。',
            font=('HarmonyOS Sans SC',10)).place(x=660,y=210)
        minute = period_time * period_num + rest_time * \
            (display_time + vacant_time) * (period_num - 1) / 60
        tkinter.Label(
            tab_IV_root, 
            text='本次测试共历时 %d 分钟，将分为 %d 个阶段。' %(minute, period_num), 
            font=('HarmonyOS Sans SC', 10)).place(x=660, y=240)
        tkinter.Label(tab_IV_root,
                      text='每阶段测试 %d 分钟，两段之间另含过渡时间 %d 秒。' % (period_time,
                                                             rest_time * (display_time + vacant_time)),
                      font=('HarmonyOS Sans SC',10)).place(x=660,y=270)
        key_press = tkinter.Label(
            tab_IV_root,
            text='Tips：当前，<%s%s%s%s> 键位分别对应 DashBoard_I ~ IV。'%(keyboard_preference_I,keyboard_preference_II,keyboard_preference_III,keyboard_preference_IV),
            font=('HarmonyOS Sans SC',10,'bold'))
        key_press.focus_set()
        key_press.place(x=660, y=300)
        key_press.bind("<Key>", key_feedback)
        countdown = tkinter.Label(
            tab_IV_root, 
            text='倒计时： %02dmin 00s' %(minute), 
            font=('HarmonyOS Sans SC', 10, 'bold'))
        countdown.place(x=660, y=330)
        rest_round_countdown = tkinter.Label(
            tab_IV_root, 
            text='距离下次过渡时间段还有： %d 轮' %(rest_round_count), 
            font=('HarmonyOS Sans SC', 10, 'bold'))
        rest_round_countdown.place(x=660, y=360)
        rest_countdown = tkinter.Label(
            tab_IV_root, 
            text='距离下一阶段还有： %02dmin 00s' %(period_time), 
            font=('HarmonyOS Sans SC', 10, 'bold'))
        rest_countdown.place(x=660, y=390)
        countdown_thread = threading.Thread(
            target=lambda: countdown_display(total_seconds=minute * 60))
        countdown_thread.daemon = True
        countdown_thread.start()
        rest_countdown_thread = threading.Thread(
            target=lambda: rest_countdown_display(total_seconds=period_time * 60))
        rest_countdown_thread.daemon = True
        rest_countdown_thread.start()
        interval_countdown = tkinter.Label(
            tab_IV_root, 
            text='距离数字对目标区间变更还有： %02ds' %(interval_change_time), 
            font=('HarmonyOS Sans SC', 10, 'bold'))
        interval_countdown.place(x=660, y=420)
        interval_change_thread = threading.Thread(target=lambda: interval_countdown_display())
        interval_change_thread.daemon = True
        interval_change_thread.start()
        dashboard_thread = threading.Thread(target=dashboard_display)
        dashboard_thread.daemon = True
        dashboard_thread.start()
    def key_feedback(event):
        end_time = time.time()
        logging.info('The tester clicks the keyboard: %s' % str(event.keysym))
        if rest_status:
            key_warn.configure(text='键盘输入检查：当前处于休息时间段内，请不要操作键盘！')
            return
        if event.keysym in keyboard_preference_I or event.keysym in keyboard_preference_opt_I:
            index = -4
            key_warn.configure(text='键盘输入检查：你当前输入状态正常，请继续测试 ~')
        elif event.keysym in keyboard_preference_II or event.keysym in keyboard_preference_opt_II:
            index = -3
            key_warn.configure(text='键盘输入检查：你当前输入状态正常，请继续测试 ~')
        elif event.keysym in keyboard_preference_III or event.keysym in keyboard_preference_opt_III:
            index = -2
            key_warn.configure(text='键盘输入检查：你当前输入状态正常，请继续测试 ~')
        elif event.keysym in keyboard_preference_IV or event.keysym in keyboard_preference_opt_IV:
            index = -1
            key_warn.configure(text='键盘输入检查：你当前输入状态正常，请继续测试 ~')
        elif event.keysym in '??':
            key_warn.configure(text='键盘输入检查：你当前处于中文输入状态，请检查！')
            return
        else:
            key_warn.configure(text='键盘输入检查：除切换输入状态外，请不要按下其他按键！')
            return
        if data_record[index][6]:
            if data_record[index][-2] != 'Hit':
                data_record[index][-1] = 'Hit'
                data_record[index].append(end_time - start_time)
        elif not data_record[index][6] and data_record[index][-2] != 'Wrong':
            data_record[index][-1] = 'Wrong'
            data_record[index].append(end_time - start_time)
    def test_feedback():
        end_time = time.time()
        count = 0
        for index in range(-dashboard_num, 0):
            if data_record[index][6]:
                if data_record[index][-2] != 'Hit':
                    data_record[index][-1] = 'Hit'
                    data_record[index].append(end_time - start_time)
                count += 1
        if count == 0:
            for index in range(-dashboard_num, 0):
                if not data_record[index][6] and data_record[index][-2] != 'Wrong':
                    data_record[index][-1] = 'Wrong'
                    data_record[index].append(end_time - start_time)
    def data_upload():
        key_warn.configure(text='Congratulations！测试结束，此界面即将关闭 ~')
        time.sleep(6)
        for widget in tab_IV_root.winfo_children():
            widget.destroy()
        if not os.path.exists(r'.\\data\\%s-%s-%s-%s' %(TESTER_CODE, ID, NAME, GENDER)):
            os.makedirs(r'.\\data\\%s-%s-%s-%s' %(TESTER_CODE, ID, NAME, GENDER))
        upload_time = time.strftime('%H%M%S', time.localtime())
        data_filename = 'Tab_IV-Work_O_MS-Test_Data-%s-%s-%s-%s-%s-%s-%s.csv' % (
            TESTER_CODE, ID, NAME, GENDER, PERIOD, START_TIME, upload_time)
        data_record_df = pandas.DataFrame(
            data_record,
            columns=[
                'display_round_count',
                'area_index',
                'interval_start',
                'interval_end',
                'data_I',
                'data_II',
                'system_judge',
                'user_judge',
                'response_time'])
        data_record_df.to_csv(r'data\\%s-%s-%s-%s\\%s' %
            (TESTER_CODE, ID, NAME, GENDER, data_filename), index=False)
        situation_filename = 'Tab_IV-Work_O_MS-Mental_Data-%s-%s-%s-%s-%s-%s-%s.csv' % (
            TESTER_CODE, ID, NAME, GENDER, PERIOD, START_TIME, upload_time)
        situation_record_df = pandas.DataFrame(
            situation_record,
            columns=[
                'display_round_count',
                'situation_selected',
                'response_time'])
        situation_record_df.to_csv(r'data\\%s-%s-%s-%s\\%s' %
            (TESTER_CODE, ID, NAME, GENDER, situation_filename), index=False)
        if webdav_status:
            client = Client(
                base_url='https://dav.jianguoyun.com/dav/',
                auth=(webdav_account,webdav_password))
            client.mkdir('/appdata_upload')
            client.mkdir('/appdata_upload/%s-%s-%s-%s/' %
                (TESTER_CODE, ID, NAME, GENDER))
            client.upload_file(
                from_path='data\\%s-%s-%s-%s\\%s' %
                (TESTER_CODE,ID,NAME,GENDER,data_filename),
                to_path='/appdata_upload/%s-%s-%s-%s/%s' %
                (TESTER_CODE,ID,NAME,GENDER,data_filename),
                overwrite=True)
            client.upload_file(
                from_path='data\\%s-%s-%s-%s\\%s' %
                (TESTER_CODE,ID,NAME,GENDER,situation_filename),
                to_path='/appdata_upload/%s-%s-%s-%s/%s' %
                (TESTER_CODE,ID,NAME,GENDER,situation_filename),
                overwrite=True)
        else:
            os.startfile(r'.\\data\\%s-%s-%s-%s\\%s' %
                         (TESTER_CODE, ID, NAME, GENDER, data_filename))
            os.startfile(r'.\\data\\%s-%s-%s-%s\\%s' %
                         (TESTER_CODE, ID, NAME, GENDER, situation_filename))
        tab_IV_content_display()
    tkinter.Label(
        tab_IV_root,
        text='警戒作业测试 -O-MS',
        font=('HarmonyOS Sans SC',14,'bold')).place(x=20,y=20)
    clock = tkinter.Label(
        tab_IV_root, text='', font=('HarmonyOS Sans', 12, 'bold'))
    clock.place(x=660, y=650)
    clock_thread = threading.Thread(target=time_display)
    clock_thread.daemon = True
    clock_thread.start()
    for index in range(40):
        tkinter.Label(
            tab_IV_root,
            text='|',
            font=('HarmonyOS Sans',10,'bold')).place(x=650,y=20 *index)
    for index in range(40):
        tkinter.Label(
            tab_IV_root,
            text='|',
            font=('HarmonyOS Sans',10,'bold')).place(x=1025,y=20 *index)
    tkinter.Label(
        tab_IV_root,
        text='---------- Info_Area  信息区域 ----------',
        font=('HarmonyOS Sans SC',14,'bold')).place(x=660,y=0)
    tkinter.Label(
        tab_IV_root,
        text='-------- Submit_Area  提交区域 --------',
        font=('HarmonyOS Sans SC',14,'bold')).place(x=660,y=500)
    tkinter.Label(
        tab_IV_root,
        text='---------- 量表区域 ----------',
        font=('HarmonyOS Sans SC',14,'bold')).place(x=1030,y=0)
    tkinter.Label(
        tab_IV_root,
        text='如果你已做好准备，请点按下方按钮以开始测试。',
        font=('HarmonyOS Sans SC',10)).place(x=660,y=50)
    tkinter.Label(
        tab_IV_root,
        text='Please press the button below to continue.',
        font=('HarmonyOS Sans',10)).place(x=660,y=80)
    tkinter.Label(
        tab_IV_root,
        text='当点按后，将有 2 秒的准备时间，随后测试即刻开始。',
        font=('HarmonyOS Sans SC',10)).place(x=660,y=110)
    tkinter.Label(
        tab_IV_root,
        text='当观察到任一面板出现异常事件，请立刻点按相应键盘按键。',
        font=('HarmonyOS Sans SC',10)).place(x=660,y=550)
    key_warn = tkinter.Label(
        tab_IV_root,
        text='键盘输入检查：请确认已处于英文输入状态或大写锁定状态。',
        font=('HarmonyOS Sans SC',10,'bold'))
    key_warn.place(x=660, y=460)
    start_submit = tkinter.Button(
        tab_IV_root,
        width=42,
        text='开始测试  START TEST',
        font=('HarmonyOS Sans SC',10,'bold'),
        command=test_display)
    start_submit.place(x=670, y=150)
    feedback_submit = tkinter.Button(
        tab_IV_root,
        width=42,
        text='(此环节已禁用) 预警提交  SUBMIT FEEDBACK',
        font=('HarmonyOS Sans SC',10,'bold'),
        state='disabled',
        command=test_feedback)
    feedback_submit.place(x=670, y=600)
    tkinter.Label(
        tab_IV_root,
        text='DashBoard_I',
        font=('HarmonyOS Sans',12,'italic')).place(x=50,y=100)
    dashboard_I_interval = tkinter.Label(
        tab_IV_root, text='', font=('HarmonyOS Sans SC', 18, 'bold'))
    dashboard_I_interval.place(x=50, y=160)
    dashboard_I_data = tkinter.Label(
        tab_IV_root, text='', font=('HarmonyOS Sans SC', 20, 'bold'))
    dashboard_I_data.place(x=50, y=230)
    tkinter.Label(
        tab_IV_root,
        text='DashBoard_II',
        font=('HarmonyOS Sans',12,'italic')).place(x=350,y=100)
    dashboard_II_interval = tkinter.Label(
        tab_IV_root, text='', font=('HarmonyOS Sans SC', 18, 'bold'))
    dashboard_II_interval.place(x=350, y=160)
    dashboard_II_data = tkinter.Label(
        tab_IV_root, text='', font=('HarmonyOS Sans SC', 20, 'bold'))
    dashboard_II_data.place(x=350, y=230)
    tkinter.Label(
        tab_IV_root,
        text='DashBoard_III',
        font=('HarmonyOS Sans',12,'italic')).place(x=50,y=350)
    dashboard_III_interval = tkinter.Label(
        tab_IV_root, text='', font=('HarmonyOS Sans SC', 18, 'bold'))
    dashboard_III_interval.place(x=50, y=410)
    dashboard_III_data = tkinter.Label(
        tab_IV_root, text='', font=('HarmonyOS Sans SC', 20, 'bold'))
    dashboard_III_data.place(x=50, y=480)
    tkinter.Label(
        tab_IV_root,
        text='DashBoard_IV',
        font=('HarmonyOS Sans',12,'italic')).place(x=350,y=350)
    dashboard_IV_interval = tkinter.Label(
        tab_IV_root, text='', font=('HarmonyOS Sans SC', 18, 'bold'))
    dashboard_IV_interval.place(x=350, y=410)
    dashboard_IV_data = tkinter.Label(
        tab_IV_root, text='', font=('HarmonyOS Sans SC', 20, 'bold'))
    dashboard_IV_data.place(x=350, y=480)
    dashboard_emergency = tkinter.Label(
        tab_IV_root, image='', font=('HarmonyOS Sans SC', 14, 'italic'))
    dashboard_emergency.place(x=50, y=300)

def tab_V_content_display():
    def time_display():
        while True:
            clock.configure(text='----------- ' +time.strftime('%Y-%m-%d %H:%M:%S') +' -----------')
            time.sleep(1)
    def test_display():
        def countdown_display(total_seconds):
            while total_seconds != 0:
                total_seconds -= 1
                countdown.configure(
                    text='倒计时：%02dmin %02ds' %(total_seconds //60,total_seconds %60))
                time.sleep(1)
            if total_seconds == 0:
                logging.info('The countdown is over')
                display_status = False
                data_upload()
        def rest_countdown_display(total_seconds):
            countdown_round = period_num * 2 - 1
            total_seconds = [period_time * 60,rest_time * (display_time + vacant_time)]
            seconds_countdown = total_seconds[(countdown_round + 1) % 2]
            while countdown_round != 0:
                seconds_countdown -= 1
                rest_countdown.configure(
                    text='距离下一阶段还有：%02dmin %02ds' %
                    (seconds_countdown //60,seconds_countdown %60))
                time.sleep(1)
                if seconds_countdown == 0:
                    countdown_round -= 1
                    seconds_countdown = total_seconds[(countdown_round + 1) % 2]
        def interval_countdown_display():
            interval_seconds = interval_change_time
            while True:
                interval_seconds -= 1
                interval_countdown.configure(
                    text='距离数字对目标区间变更还有： %02ds' %(interval_seconds))
                time.sleep(1)
                if interval_seconds == 0:
                    interval_seconds = interval_change_time
                    interval_start.append([random.randint(2, 10)for i in range(dashboard_num)])
        def dashboard_display():
            def choose_confirm(index):
                situation_end = time.time()
                situation_record_plus.append(
                    [display_round_count, index, situation_end - situation_start])
                choose_I.configure(state='disabled')
                choose_II.configure(state='disabled')
                choose_III.configure(state='disabled')
                choose_IV.configure(state='disabled')
                choose_V.configure(state='disabled')
                choose_VI.configure(state='disabled')
                choose_VII.configure(state='disabled')
            while display_status:
                global start_time, display_round_count, rest_round_count, rest_status
                if rest_round_count == 0:
                    dashboard_emergency.configure(image=img_scale)
                    rest_status = True
                    key_warn.configure(text='键盘输入检查：当前处于过渡时间段内，请不要操作键盘！')
                    tkinter.Label(
                        tab_V_root, text='    ', font=(
                            'HarmonyOS Sans SC', 360, 'bold')).place(x=1040, y=50)
                    rest_round_countdown.configure(
                        text='目前处于过渡时间段内，请完成右侧呈现的自评表！')
                    tkinter.Label(
                        tab_V_root, text='即将呈现量表内容，请做好准备！', font=(
                            'HarmonyOS Sans SC', 10, 'bold')).place(x=1040, y=50)
                    tkinter.Label(
                        tab_V_root, text='请尽快选择出最符合你当前状态的选项。', font=(
                            'HarmonyOS Sans SC', 10, 'bold')).place(x=1040, y=80)
                    situation_start = time.time()
                    choose_I = tkinter.Button(tab_V_root, width=28, text='完全警觉，完全清醒', font=(
                        'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(0))
                    choose_I.place(x=1035, y=150)
                    choose_II = tkinter.Button(
                        tab_V_root, width=28, text='很有活力，反应灵敏，但非最好状态', font=(
                            'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(1))
                    choose_II.place(x=1035, y=200)
                    choose_III = tkinter.Button(tab_V_root, width=28, text='情况一般，稍微清醒', font=(
                        'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(2))
                    choose_III.place(x=1035, y=250)
                    choose_IV = tkinter.Button(tab_V_root, width=28, text='有点累，不怎么清醒', font=(
                        'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(3))
                    choose_IV.place(x=1035, y=300)
                    choose_V = tkinter.Button(tab_V_root, width=28, text='挺累的，无精打采', font=(
                        'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(4))
                    choose_V.place(x=1035, y=350)
                    choose_VI = tkinter.Button(tab_V_root, width=28, text='非常疲惫，难以集中精神', font=(
                        'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(5))
                    choose_VI.place(x=1035, y=400)
                    choose_VII = tkinter.Button(tab_V_root, width=28, text='精疲力尽，无法有效地工作', font=(
                        'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(6))
                    choose_VII.place(x=1035, y=450)
                if rest_round_count == 0:
                    time.sleep(rest_time * (display_time + vacant_time))
                    rest_status = False
                    dashboard_emergency.configure(image='')
                    key_warn.configure(text='键盘输入检查：请确认已处于英文输入状态或大写锁定状态。')
                    rest_round_count = display_round_per_min * period_time
                    tkinter.Label(
                        tab_V_root, text='    ', font=(
                            'HarmonyOS Sans SC', 360, 'bold')).place(x=1035, y=50)
                rest_status = False
                key_press.focus_set()
                data_item.append([[random.randint(2, 8) for i in range(2)]
                                 for j in range(dashboard_num)])
                for index in range(dashboard_num):
                    data_item[-1][index][1] = data_item[-1][index][0] + random.randint(-1,1)
                current_interval = interval_start[-1]
                for index in range(dashboard_num):
                    pair_sum = data_item[-1][index][0] + data_item[-1][index][1]
                    while interval_start[-1][index] <= pair_sum <= interval_start[-1][index] + interval_length:
                        data_item[-1][index] = [random.randint(2, 8)for i in range(2)]
                        data_item[-1][index][1] = data_item[-1][index][0] + random.randint(-1,1)
                        pair_sum = data_item[-1][index][0] + data_item[-1][index][1]
                random_prob = random.random()
                random_emergency_prob = random.random()
                if random_prob < RATE_CALL:
                    display_area = random.randint(1, dashboard_num)
                    pair_sum = data_item[-1][display_area - 1][0] + data_item[-1][display_area - 1][1]
                    while not interval_start[-1][display_area - 1] <= pair_sum <= interval_start[-1][display_area - 1] + interval_length:
                        data_item[-1][display_area - 1] = [random.randint(2, 8) for i in range(2)]
                        data_item[-1][display_area - 1][1] = data_item[-1][display_area - 1][0] + random.randint(-1,1)
                        pair_sum = data_item[-1][display_area - 1][0] + data_item[-1][display_area - 1][1]
                if random_emergency_prob < emergency_rate:
                    winsound.Beep(2000, 500)
                    data_record_plus.append(
                        [-1, 'DashBoard_Emergency', -1, -1, -1, -1, True, 'Missed'])
                    dashboard_emergency.configure(image=img_attention)
                else:
                    data_record_plus.append(
                        [-1, 'DashBoard_Emergency', -1, -1, -1, -1, False, 'Accepted'])
                display_round_count += 1
                rest_round_count -= 1
                rest_round_countdown.configure(
                    text='距离下次过渡时间段还有： %d 轮' %(rest_round_count))
                judge = interval_start[-1][0] <= sum(
                    data_item[-1][0]) <= interval_start[-1][0] + interval_length
                data_record_plus.append([display_round_count,
                                         'DashBoard_I',
                                         interval_start[-1][0],
                                         interval_start[-1][0] + interval_length,
                                         data_item[-1][0][0],
                                         data_item[-1][0][1],
                                         judge,
                                         'Missed' if judge else 'Accepted'])
                judge = interval_start[-1][1] <= sum(
                    data_item[-1][1]) <= interval_start[-1][1] + interval_length
                data_record_plus.append([display_round_count,
                                         'DashBoard_II',
                                         interval_start[-1][1],
                                         interval_start[-1][1] + interval_length,
                                         data_item[-1][1][0],
                                         data_item[-1][1][1],
                                         judge,
                                         'Missed' if judge else 'Accepted'])
                judge = interval_start[-1][2] <= sum(
                    data_item[-1][2]) <= interval_start[-1][2] + interval_length
                data_record_plus.append([display_round_count,
                                         'DashBoard_III',
                                         interval_start[-1][2],
                                         interval_start[-1][2] + interval_length,
                                         data_item[-1][2][0],
                                         data_item[-1][2][1],
                                         judge,
                                         'Missed' if judge else 'Accepted'])
                judge = interval_start[-1][3] <= sum(
                    data_item[-1][3]) <= interval_start[-1][3] + interval_length
                data_record_plus.append([display_round_count,
                                         'DashBoard_IV',
                                         interval_start[-1][3],
                                         interval_start[-1][3] + interval_length,
                                         data_item[-1][3][0],
                                         data_item[-1][3][1],
                                         judge,
                                         'Missed' if judge else 'Accepted'])
                dashboard_I_interval.configure(
                    text='%-2s —— %-2s' % (interval_start[-1][0], interval_start[-1][0] + interval_length))
                dashboard_II_interval.configure(
                    text='%-2s —— %-2s' % (interval_start[-1][1], interval_start[-1][1] + interval_length))
                dashboard_III_interval.configure(
                    text='%-2s —— %-2s' % (interval_start[-1][2], interval_start[-1][2] + interval_length))
                dashboard_IV_interval.configure(
                    text='%-2s —— %-2s' % (interval_start[-1][3], interval_start[-1][3] + interval_length))
                dashboard_I_data.configure(text='%s          %s' % (
                    data_item[-1][0][0], data_item[-1][0][1]))
                dashboard_II_data.configure(text='%s          %s' % (
                    data_item[-1][1][0], data_item[-1][1][1]))
                dashboard_III_data.configure(text='%s          %s' % (
                    data_item[-1][2][0], data_item[-1][2][1]))
                dashboard_IV_data.configure(text='%s          %s' % (
                    data_item[-1][3][0], data_item[-1][3][1]))
                start_time = time.time()
                time.sleep(display_time)
                if interval_start[-1] != current_interval:
                    dashboard_I_interval.configure(text='')
                    dashboard_II_interval.configure(text='')
                    dashboard_III_interval.configure(text='')
                    dashboard_IV_interval.configure(text='')
                dashboard_I_data.configure(text='')
                dashboard_II_data.configure(text='')
                dashboard_III_data.configure(text='')
                dashboard_IV_data.configure(text='')
                dashboard_emergency.configure(image='')
                time.sleep(vacant_time)
        try:
            ID, NAME, GENDER
        except NameError:
            tkinter.messagebox.showwarning(
                title='系统端提示', message='请先在程序主页提交个人信息！')
            return
        if tip_enhanced_status:
            tkinter.messagebox.showinfo(
                title='系统端提示', message='对于突发事件的定义：请留意每轮中区域内的突显文字。')
        time.sleep(2)
        global interval_start, data_item, data_record_plus, display_round_count, rest_round_count, situation_record_plus, display_status
        display_status = True
        interval_start = []
        data_item = []
        data_record_plus = []
        situation_record_plus = []
        display_round_count = 0
        rest_round_count = display_round_per_min * period_time
        start_submit.configure(state='disabled')
        feedback_submit.configure(state='normal')
        status_check = 'InfoCheck-%s-Tab_V-Work-E-MS-%s-%s-%s-%s-%s-%s' % (
            VERSION, TESTER_CODE, ID, NAME, GENDER, PERIOD, START_TIME)
        bottom_status_bar.configure(text=status_check)
        interval_start.append([random.randint(2, 10)for i in range(dashboard_num)])
        tkinter.Label(
            tab_V_root,
            text='请不要在一轮中连续点按键盘，否则只会记录首次数据。',
            font=('HarmonyOS Sans SC',10)).place(x=660,y=210)
        minute = period_time * period_num + rest_time * \
            (display_time + vacant_time) * (period_num - 1) / 60
        tkinter.Label(
            tab_V_root, 
            text='本次测试共历时 %d 分钟，将分为 %d 个阶段。' %(minute, period_num), 
            font=('HarmonyOS Sans SC', 10)).place(x=660, y=240)
        tkinter.Label(tab_V_root,
                      text='每阶段测试 %d 分钟，两段之间另含过渡时间 %d 秒。' % (period_time,
                                                             rest_time * (display_time + vacant_time)),
                      font=('HarmonyOS Sans SC',10)).place(x=660,y=270)
        key_press = tkinter.Label(
            tab_V_root, text='Tips：当前，<%s%s%s%s> 键位分别对应 DashBoard_I ~ IV。'%(keyboard_preference_I, keyboard_preference_II, keyboard_preference_III, keyboard_preference_IV), font=(
                'HarmonyOS Sans SC', 10, 'bold'))
        key_press.focus_set()
        key_press.place(x=660, y=300)
        key_press.bind("<Key>", key_feedback)
        countdown = tkinter.Label(
            tab_V_root, 
            text='倒计时： %02dmin 00s' %(minute), 
            font=('HarmonyOS Sans SC', 10, 'bold'))
        countdown.place(x=660, y=330)
        rest_round_countdown = tkinter.Label(
            tab_V_root, 
            text='距离下次过渡时间段还有： %d 轮' %(rest_round_count), 
            font=('HarmonyOS Sans SC', 10, 'bold'))
        rest_round_countdown.place(x=660, y=360)
        rest_countdown = tkinter.Label(
            tab_V_root, 
            text='距离下一阶段还有： %02dmin 00s' %(period_time), 
            font=('HarmonyOS Sans SC', 10, 'bold'))
        rest_countdown.place(x=660, y=390)
        countdown_thread = threading.Thread(
            target=lambda: countdown_display(total_seconds=minute * 60))
        countdown_thread.daemon = True
        countdown_thread.start()
        rest_countdown_thread = threading.Thread(
            target=lambda: rest_countdown_display(total_seconds=period_time * 60))
        rest_countdown_thread.daemon = True
        rest_countdown_thread.start()
        interval_countdown = tkinter.Label(
            tab_V_root, 
            text='距离数字对目标区间变更还有： %02ds' %(interval_change_time), 
            font=('HarmonyOS Sans SC', 10, 'bold'))
        interval_countdown.place(x=660, y=420)
        interval_change_thread = threading.Thread(target=lambda: interval_countdown_display())
        interval_change_thread.daemon = True
        interval_change_thread.start()
        dashboard_thread = threading.Thread(target=dashboard_display)
        dashboard_thread.daemon = True
        dashboard_thread.start()
    def key_feedback(event):
        end_time = time.time()
        logging.info('The tester clicks the keyboard: %s' % str(event.keysym))
        if rest_status:
            key_warn.configure(text='键盘输入检查：当前处于休息时间段内，请不要操作键盘！')
            return
        if event.keysym in keyboard_preference_I or event.keysym in keyboard_preference_opt_I:
            index = -4
            key_warn.configure(text='键盘输入检查：你当前输入状态正常，请继续测试 ~')
        elif event.keysym in keyboard_preference_II or event.keysym in keyboard_preference_opt_II:
            index = -3
            key_warn.configure(text='键盘输入检查：你当前输入状态正常，请继续测试 ~')
        elif event.keysym in keyboard_preference_III or event.keysym in keyboard_preference_opt_III:
            index = -2
            key_warn.configure(text='键盘输入检查：你当前输入状态正常，请继续测试 ~')
        elif event.keysym in keyboard_preference_IV or event.keysym in keyboard_preference_opt_IV:
            index = -1
            key_warn.configure(text='键盘输入检查：你当前输入状态正常，请继续测试 ~')
        elif event.keysym in '??':
            key_warn.configure(text='键盘输入检查：你当前处于中文输入状态，请检查！')
            return
        else:
            key_warn.configure(text='键盘输入检查：除切换输入状态外，请不要按下其他按键！')
            return
        if data_record_plus[index][6]:
            if data_record_plus[index][-2] != 'Hit':
                data_record_plus[index][-1] = 'Hit'
                data_record_plus[index].append(end_time - start_time)
        elif not data_record_plus[index][6] and data_record_plus[index][-2] != 'Wrong':
            data_record_plus[index][-1] = 'Wrong'
            data_record_plus[index].append(end_time - start_time)
    def emergency_feedback():
        end_time = time.time()
        if data_record_plus[-dashboard_num - 1][0] == -1:
            if data_record_plus[-dashboard_num - 1][6]:
                if data_record_plus[-dashboard_num - 1][-2] != 'Hit':
                    data_record_plus[-dashboard_num - 1][-1] = 'Hit'
                    data_record_plus[-dashboard_num -1].append(end_time - start_time)
            else:
                if data_record_plus[-dashboard_num - 1][-2] != 'Wrong':
                    data_record_plus[-dashboard_num - 1][-1] = 'Wrong'
                    data_record_plus[-dashboard_num -1].append(end_time - start_time)
    def data_upload():
        key_warn.configure(text='Congratulations！测试结束，此界面即将关闭 ~')
        time.sleep(6)
        for widget in tab_V_root.winfo_children():
            widget.destroy()
        if not os.path.exists(r'.\\data\\%s-%s-%s-%s' %(TESTER_CODE, ID, NAME, GENDER)):
            os.makedirs(r'.\\data\\%s-%s-%s-%s' %(TESTER_CODE, ID, NAME, GENDER))
        upload_time = time.strftime('%H%M%S', time.localtime())
        data_filename = 'Tab_V-Work_E_MS-Test_Data-%s-%s-%s-%s-%s-%s-%s.csv' % (
            TESTER_CODE, ID, NAME, GENDER, PERIOD, START_TIME, upload_time)
        data_record_df = pandas.DataFrame(
            data_record_plus,
            columns=[
                'display_round_count',
                'area_index',
                'interval_start',
                'interval_end',
                'data_I',
                'data_II',
                'system_judge',
                'user_judge',
                'response_time'])
        data_record_df.to_csv(r'data\\%s-%s-%s-%s\\%s' %
            (TESTER_CODE, ID, NAME, GENDER, data_filename), index=False)
        situation_filename = 'Tab_V-Work_E_MS-Mental_Data-%s-%s-%s-%s-%s-%s-%s.csv' % (
            TESTER_CODE, ID, NAME, GENDER, PERIOD, START_TIME, upload_time)
        situation_record_df = pandas.DataFrame(
            situation_record_plus,
            columns=[
                'display_round_count',
                'situation_selected',
                'response_time'])
        situation_record_df.to_csv(r'data\\%s-%s-%s-%s\\%s' %
            (TESTER_CODE, ID, NAME, GENDER, situation_filename), index=False)
        if webdav_status:
            client = Client(
                base_url='https://dav.jianguoyun.com/dav/',
                auth=(webdav_account,webdav_password))
            client.mkdir('/appdata_upload')
            client.mkdir('/appdata_upload/%s-%s-%s-%s/' %
                (TESTER_CODE, ID, NAME, GENDER))
            client.upload_file(
                from_path='data\\%s-%s-%s-%s\\%s' %
                (TESTER_CODE,ID,NAME,GENDER,data_filename),
                to_path='/appdata_upload/%s-%s-%s-%s/%s' %
                (TESTER_CODE,ID,NAME,GENDER,data_filename),
                overwrite=True)
            client.upload_file(
                from_path='data\\%s-%s-%s-%s\\%s' %
                (TESTER_CODE,ID,NAME,GENDER,situation_filename),
                to_path='/appdata_upload/%s-%s-%s-%s/%s' %
                (TESTER_CODE,ID,NAME,GENDER,situation_filename),
                overwrite=True)
        else:
            os.startfile(r'.\\data\\%s-%s-%s-%s\\%s' %
                         (TESTER_CODE, ID, NAME, GENDER, data_filename))
            os.startfile(r'.\\data\\%s-%s-%s-%s\\%s' %
                         (TESTER_CODE, ID, NAME, GENDER, situation_filename))
        tab_V_content_display()
    tkinter.Label(
        tab_V_root,
        text='警戒作业测试 -E-MS',
        font=('HarmonyOS Sans SC',14,'bold')).place(x=20,y=20)
    clock = tkinter.Label(
        tab_V_root, text='', font=('HarmonyOS Sans', 12, 'bold'))
    clock.place(x=660, y=650)
    clock_thread = threading.Thread(target=time_display)
    clock_thread.daemon = True
    clock_thread.start()
    for index in range(40):
        tkinter.Label(
            tab_V_root,
            text='|',
            font=('HarmonyOS Sans',10,'bold')).place(x=650,y=20 *index)
    for index in range(40):
        tkinter.Label(
            tab_V_root,
            text='|',
            font=('HarmonyOS Sans',10,'bold')).place(x=1025,y=20 *index)
    tkinter.Label(
        tab_V_root,
        text='---------- Info_Area  信息区域 ----------',
        font=('HarmonyOS Sans SC',14,'bold')).place(x=660,y=0)
    tkinter.Label(
        tab_V_root,
        text='-------- Submit_Area  提交区域 --------',
        font=('HarmonyOS Sans SC',14,'bold')).place(x=660,y=500)
    tkinter.Label(
        tab_V_root,
        text='---------- 量表区域 ----------',
        font=('HarmonyOS Sans SC',14,'bold')).place(x=1030,y=0)
    tkinter.Label(
        tab_V_root,
        text='如果你已做好准备，请点按下方按钮以开始测试。',
        font=('HarmonyOS Sans SC',10)).place(x=660,y=50)
    tkinter.Label(
        tab_V_root,
        text='Please press the button below to continue.',
        font=('HarmonyOS Sans',10)).place(x=660,y=80)
    tkinter.Label(
        tab_V_root,
        text='当点按后，将有 2 秒的准备时间，随后测试即刻开始。',
        font=('HarmonyOS Sans SC',10)).place(x=660,y=110)
    tkinter.Label(
        tab_V_root,
        text='当观察到任一面板出现异常事件，请立刻点按相应键盘按键。',
        font=('HarmonyOS Sans SC',10)).place(x=660,y=540)
    if tip_enhanced_status:
        tkinter.Label(
            tab_V_root,
            text='当观察到任一面板出现突发事件，请立刻点按下方提交按钮。',
            font=('HarmonyOS Sans SC',10)).place(x=660,y=570)
    key_warn = tkinter.Label(
        tab_V_root, text='键盘输入检查：请确认已处于英文输入状态或大写锁定状态。', font=(
            'HarmonyOS Sans SC', 10, 'bold'))
    key_warn.place(x=660, y=460)
    start_submit = tkinter.Button(
        tab_V_root,
        width=42,
        text='开始测试  START TEST',
        font=('HarmonyOS Sans SC',10,'bold'),
        command=test_display)
    start_submit.place(x=670, y=150)
    feedback_submit = tkinter.Button(
        tab_V_root,
        width=42,
        text='预警提交  SUBMIT FEEDBACK',
        font=('HarmonyOS Sans SC',10,'bold'),
        state='disabled',
        command=emergency_feedback)
    feedback_submit.place(x=670, y=600)
    tkinter.Label(
        tab_V_root,
        text='DashBoard_I',
        font=('HarmonyOS Sans',12,'italic')).place(x=50,y=100)
    dashboard_I_interval = tkinter.Label(
        tab_V_root, text='', font=('HarmonyOS Sans SC', 18, 'bold'))
    dashboard_I_interval.place(x=50, y=160)
    dashboard_I_data = tkinter.Label(
        tab_V_root, text='', font=('HarmonyOS Sans SC', 20, 'bold'))
    dashboard_I_data.place(x=50, y=230)
    tkinter.Label(
        tab_V_root,
        text='DashBoard_II',
        font=('HarmonyOS Sans',12,'italic')).place(x=350,y=100)
    dashboard_II_interval = tkinter.Label(
        tab_V_root, text='', font=('HarmonyOS Sans SC', 18, 'bold'))
    dashboard_II_interval.place(x=350, y=160)
    dashboard_II_data = tkinter.Label(
        tab_V_root, text='', font=('HarmonyOS Sans SC', 20, 'bold'))
    dashboard_II_data.place(x=350, y=230)
    tkinter.Label(
        tab_V_root,
        text='DashBoard_III',
        font=('HarmonyOS Sans',12,'italic')).place(x=50,y=350)
    dashboard_III_interval = tkinter.Label(
        tab_V_root, text='', font=('HarmonyOS Sans SC', 18, 'bold'))
    dashboard_III_interval.place(x=50, y=410)
    dashboard_III_data = tkinter.Label(
        tab_V_root, text='', font=('HarmonyOS Sans SC', 20, 'bold'))
    dashboard_III_data.place(x=50, y=480)
    tkinter.Label(
        tab_V_root,
        text='DashBoard_IV',
        font=('HarmonyOS Sans',12,'italic')).place(x=350,y=350)
    dashboard_IV_interval = tkinter.Label(
        tab_V_root, text='', font=('HarmonyOS Sans SC', 18, 'bold'))
    dashboard_IV_interval.place(x=350, y=410)
    dashboard_IV_data = tkinter.Label(
        tab_V_root, text='', font=('HarmonyOS Sans SC', 20, 'bold'))
    dashboard_IV_data.place(x=350, y=480)
    dashboard_emergency = tkinter.Label(
        tab_V_root, image='', font=('HarmonyOS Sans SC', 14, 'italic'))
    dashboard_emergency.place(x=50, y=300)
def tab_VI_content_display():
    def time_display():
        while True:
            clock.configure(text='----------- ' +time.strftime('%Y-%m-%d %H:%M:%S') +' -----------')
            time.sleep(1)
    def test_display():
        def countdown_display(total_seconds):
            while total_seconds != 0:
                total_seconds -= 1
                countdown.configure(
                    text='倒计时：%02dmin %02ds' %(total_seconds //60,total_seconds %60))
                time.sleep(1)
            if total_seconds == 0:
                display_status = False
                data_upload()
        def interval_countdown_display():
            interval_seconds = interval_change_time
            while True:
                interval_seconds -= 1
                interval_countdown.configure(
                    text='距离数字对目标区间变更还有： %02ds' %(interval_seconds))
                time.sleep(1)
                if interval_seconds == 0:
                    interval_seconds = interval_change_time
                    interval_start.append([random.randint(2, 10)for i in range(dashboard_num)])
        def dashboard_display():
            while display_status:
                global start_time, display_round_count, rest_round_count, rest_status
                rest_status = False
                key_press.focus_set()
                data_item.append([[random.randint(2, 8) for i in range(2)]for j in range(dashboard_num)])
                for index in range(dashboard_num):
                    data_item[-1][index][1] = data_item[-1][index][0] + random.randint(-1,1)
                current_interval = interval_start[-1]
                for index in range(dashboard_num):
                    pair_sum = data_item[-1][index][0] + data_item[-1][index][1]
                    while interval_start[-1][index] <= pair_sum <= interval_start[-1][index] + interval_length:
                        data_item[-1][index] = [random.randint(2, 8)for i in range(2)]
                        data_item[-1][index][1] = data_item[-1][index][0] + random.randint(-1,1)
                        pair_sum = data_item[-1][index][0] + data_item[-1][index][1]
                random_prob = random.random()
                if random_prob < RATE_CALL:
                    display_area = random.randint(1, dashboard_num)
                    pair_sum = data_item[-1][display_area - 1][0] + data_item[-1][display_area - 1][1]
                    while not interval_start[-1][display_area - 1] <= pair_sum <= interval_start[-1][display_area - 1] + interval_length:
                        data_item[-1][display_area - 1] = [random.randint(2, 8) for i in range(2)]
                        data_item[-1][display_area - 1][1] = data_item[-1][display_area - 1][0] + random.randint(-1,1)
                        pair_sum = data_item[-1][display_area - 1][0] + data_item[-1][display_area - 1][1]
                display_round_count += 1
                judge = interval_start[-1][0] <= sum(
                    data_item[-1][0]) <= interval_start[-1][0] + interval_length
                data_record_III.append([display_round_count,
                                        'DashBoard_I',
                                        interval_start[-1][0],
                                        interval_start[-1][0] + interval_length,
                                        data_item[-1][0][0],
                                        data_item[-1][0][1],
                                        judge,
                                        'Missed' if judge else 'Accepted'])
                judge = interval_start[-1][1] <= sum(
                    data_item[-1][1]) <= interval_start[-1][1] + interval_length
                data_record_III.append([display_round_count,
                                        'DashBoard_II',
                                        interval_start[-1][1],
                                        interval_start[-1][1] + interval_length,
                                        data_item[-1][1][0],
                                        data_item[-1][1][1],
                                        judge,
                                        'Missed' if judge else 'Accepted'])
                judge = interval_start[-1][2] <= sum(
                    data_item[-1][2]) <= interval_start[-1][2] + interval_length
                data_record_III.append([display_round_count,
                                        'DashBoard_III',
                                        interval_start[-1][2],
                                        interval_start[-1][2] + interval_length,
                                        data_item[-1][2][0],
                                        data_item[-1][2][1],
                                        judge,
                                        'Missed' if judge else 'Accepted'])
                judge = interval_start[-1][3] <= sum(
                    data_item[-1][3]) <= interval_start[-1][3] + interval_length
                data_record_III.append([display_round_count,
                                        'DashBoard_IV',
                                        interval_start[-1][3],
                                        interval_start[-1][3] + interval_length,
                                        data_item[-1][3][0],
                                        data_item[-1][3][1],
                                        judge,
                                        'Missed' if judge else 'Accepted'])
                dashboard_I_interval.configure(
                    text='%-2s —— %-2s' % (interval_start[-1][0], interval_start[-1][0] + interval_length))
                dashboard_II_interval.configure(
                    text='%-2s —— %-2s' % (interval_start[-1][1], interval_start[-1][1] + interval_length))
                dashboard_III_interval.configure(
                    text='%-2s —— %-2s' % (interval_start[-1][2], interval_start[-1][2] + interval_length))
                dashboard_IV_interval.configure(
                    text='%-2s —— %-2s' % (interval_start[-1][3], interval_start[-1][3] + interval_length))
                dashboard_I_data.configure(text='%s          %s' % (
                    data_item[-1][0][0], data_item[-1][0][1]))
                dashboard_II_data.configure(text='%s          %s' % (
                    data_item[-1][1][0], data_item[-1][1][1]))
                dashboard_III_data.configure(text='%s          %s' % (
                    data_item[-1][2][0], data_item[-1][2][1]))
                dashboard_IV_data.configure(text='%s          %s' % (
                    data_item[-1][3][0], data_item[-1][3][1]))
                start_time = time.time()
                time.sleep(display_time)
                if interval_start[-1] != current_interval:
                    dashboard_I_interval.configure(text='')
                    dashboard_II_interval.configure(text='')
                    dashboard_III_interval.configure(text='')
                    dashboard_IV_interval.configure(text='')
                dashboard_I_data.configure(text='')
                dashboard_II_data.configure(text='')
                dashboard_III_data.configure(text='')
                dashboard_IV_data.configure(text='')
                time.sleep(vacant_time)
        try:
            ID, NAME, GENDER
        except NameError:
            tkinter.messagebox.showwarning(
                title='系统端提示', message='请先在程序主页提交个人信息！')
            return
        time.sleep(2)
        global interval_start, data_item, data_record_III, situation_record_III, display_round_count, display_status
        display_status = True
        interval_start = []
        data_item = []
        data_record_III = []
        situation_record_III = []
        display_round_count = 0
        start_submit.configure(state='disabled')
        status_check = 'InfoCheck-%s-Tab_VI-Work-O-SS-%s-%s-%s-%s-%s-%s' % (
            VERSION, TESTER_CODE, ID, NAME, GENDER, PERIOD, START_TIME)
        bottom_status_bar.configure(text=status_check)
        interval_start.append([random.randint(2, 10)for i in range(dashboard_num)])
        tkinter.Label(
            tab_VI_root,
            text='请不要在一轮中连续点按键盘，否则只会记录首次数据。',
            font=('HarmonyOS Sans SC',10)).place(x=660,y=210)
        minute = period_time * period_num
        tkinter.Label(
            tab_VI_root,
            text='本次测试共历时 %d 分钟。' %(minute),
            font=('HarmonyOS Sans SC',10)).place(x=660,y=240)
        key_press = tkinter.Label(
            tab_VI_root,
            text='Tips：当前，<%s%s%s%s> 键位分别对应 DashBoard_I ~ IV。'%(keyboard_preference_I, keyboard_preference_II, keyboard_preference_III, keyboard_preference_IV),
            font=('HarmonyOS Sans SC',10,'bold'))
        key_press.focus_set()
        key_press.place(x=660, y=300)
        key_press.bind("<Key>", key_feedback)
        countdown = tkinter.Label(
            tab_VI_root, 
            text='倒计时： %02dmin 00s' %(minute), 
            font=('HarmonyOS Sans SC', 10, 'bold'))
        countdown.place(x=660, y=330)
        countdown_thread = threading.Thread(target=lambda: countdown_display(total_seconds=minute * 60))
        countdown_thread.daemon = True
        countdown_thread.start()
        interval_countdown = tkinter.Label(
            tab_VI_root, 
            text='距离数字对目标区间变更还有： %02ds' %(interval_change_time), 
            font=('HarmonyOS Sans SC', 10, 'bold'))
        interval_countdown.place(x=660, y=420)
        interval_change_thread = threading.Thread(target=lambda: interval_countdown_display())
        interval_change_thread.daemon = True
        interval_change_thread.start()
        dashboard_thread = threading.Thread(target=dashboard_display)
        dashboard_thread.daemon = True
        dashboard_thread.start()
    def key_feedback(event):
        end_time = time.time()
        logging.info('The tester clicks the keyboard: %s' % str(event.keysym))
        if event.keysym in keyboard_preference_I or event.keysym in keyboard_preference_opt_I:
            index = -4
            key_warn.configure(text='键盘输入检查：你当前输入状态正常，请继续测试 ~')
        elif event.keysym in keyboard_preference_II or event.keysym in keyboard_preference_opt_II:
            index = -3
            key_warn.configure(text='键盘输入检查：你当前输入状态正常，请继续测试 ~')
        elif event.keysym in keyboard_preference_III or event.keysym in keyboard_preference_opt_III:
            index = -2
            key_warn.configure(text='键盘输入检查：你当前输入状态正常，请继续测试 ~')
        elif event.keysym in keyboard_preference_IV or event.keysym in keyboard_preference_opt_IV:
            index = -1
            key_warn.configure(text='键盘输入检查：你当前输入状态正常，请继续测试 ~')
        elif event.keysym in '??':
            key_warn.configure(text='键盘输入检查：你当前处于中文输入状态，请检查！')
            return
        else:
            key_warn.configure(text='键盘输入检查：除切换输入状态外，请不要按下其他按键！')
            return
        if data_record_III[index][6]:
            if data_record_III[index][-2] != 'Hit':
                data_record_III[index][-1] = 'Hit'
                data_record_III[index].append(end_time - start_time)
        elif not data_record_III[index][6] and data_record_III[index][-2] != 'Wrong':
            data_record_III[index][-1] = 'Wrong'
            data_record_III[index].append(end_time - start_time)
    def data_upload():
        def choose_confirm(index):
            situation_end = time.time()
            situation_record_III.append(
                [display_round_count, index, situation_end - situation_start])
            choose_I.configure(state='disabled')
            choose_II.configure(state='disabled')
            choose_III.configure(state='disabled')
            choose_IV.configure(state='disabled')
            choose_V.configure(state='disabled')
            choose_VI.configure(state='disabled')
            choose_VII.configure(state='disabled')
        dashboard_emergency.configure(image=img_scale)  # TODO
        tkinter.Label(
            tab_VI_root, text='即将呈现量表内容，请做好准备！', font=(
                'HarmonyOS Sans SC', 10, 'bold')).place(x=1040, y=50)
        tkinter.Label(
            tab_VI_root, text='请尽快选择出最符合你当前状态的选项。', font=(
                'HarmonyOS Sans SC', 10, 'bold')).place(x=1040, y=80)
        situation_start = time.time()
        choose_I = tkinter.Button(tab_VI_root, width=28, text='完全警觉，完全清醒', font=(
            'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(0))
        choose_I.place(x=1035, y=150)
        choose_II = tkinter.Button(
            tab_VI_root, width=28, text='很有活力，反应灵敏，但非最好状态', font=(
                'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(1))
        choose_II.place(x=1035, y=200)
        choose_III = tkinter.Button(tab_VI_root, width=28, text='情况一般，稍微清醒', font=(
            'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(2))
        choose_III.place(x=1035, y=250)
        choose_IV = tkinter.Button(tab_VI_root, width=28, text='有点累，不怎么清醒', font=(
            'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(3))
        choose_IV.place(x=1035, y=300)
        choose_V = tkinter.Button(tab_VI_root, width=28, text='挺累的，无精打采', font=(
            'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(4))
        choose_V.place(x=1035, y=350)
        choose_VI = tkinter.Button(tab_VI_root, width=28, text='非常疲惫，难以集中精神', font=(
            'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(5))
        choose_VI.place(x=1035, y=400)
        choose_VII = tkinter.Button(tab_VI_root, width=28, text='精疲力尽，无法有效地工作', font=(
            'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(6))
        choose_VII.place(x=1035, y=450)
        key_warn.configure(text='Congratulations！测试结束，此界面即将关闭 ~')
        time.sleep(6)
        for widget in tab_VI_root.winfo_children():
            widget.destroy()
        if not os.path.exists(r'.\\data\\%s-%s-%s-%s' %(TESTER_CODE, ID, NAME, GENDER)):
            os.makedirs(r'.\\data\\%s-%s-%s-%s' %(TESTER_CODE, ID, NAME, GENDER))
        upload_time = time.strftime('%H%M%S', time.localtime())
        data_filename = 'Tab_VI-Work_O_SS-Test_Data-%s-%s-%s-%s-%s-%s-%s.csv' % (
            TESTER_CODE, ID, NAME, GENDER, PERIOD, START_TIME, upload_time)
        data_record_df = pandas.DataFrame(
            data_record_III,
            columns=[
                'display_round_count',
                'area_index',
                'interval_start',
                'interval_end',
                'data_I',
                'data_II',
                'system_judge',
                'user_judge',
                'response_time'])
        data_record_df.to_csv(r'data\\%s-%s-%s-%s\\%s' %
            (TESTER_CODE, ID, NAME, GENDER, data_filename), index=False)
        situation_filename = 'Tab_VI-Work_O_SS-Mental_Data-%s-%s-%s-%s-%s-%s-%s.csv' % (
            TESTER_CODE, ID, NAME, GENDER, PERIOD, START_TIME, upload_time)
        situation_record_df = pandas.DataFrame(
            situation_record_III,
            columns=[
                'display_round_count',
                'situation_selected',
                'response_time'])
        situation_record_df.to_csv(r'data\\%s-%s-%s-%s\\%s' %
            (TESTER_CODE, ID, NAME, GENDER, situation_filename), index=False)
        if webdav_status:
            client = Client(
                base_url='https://dav.jianguoyun.com/dav/',
                auth=(webdav_account,webdav_password))
            client.mkdir('/appdata_upload')
            client.mkdir('/appdata_upload/%s-%s-%s-%s/' %(TESTER_CODE, ID, NAME, GENDER))
            client.upload_file(
                from_path='data\\%s-%s-%s-%s\\%s' %
                (TESTER_CODE,ID,NAME,GENDER,data_filename),
                to_path='/appdata_upload/%s-%s-%s-%s/%s' %
                (TESTER_CODE,ID,NAME,GENDER,data_filename),
                overwrite=True)
            client.upload_file(
                from_path='data\\%s-%s-%s-%s\\%s' %
                (TESTER_CODE,ID,NAME,GENDER,situation_filename),
                to_path='/appdata_upload/%s-%s-%s-%s/%s' %
                (TESTER_CODE,ID,NAME,GENDER,situation_filename),
                overwrite=True)
        else:
            os.startfile(r'.\\data\\%s-%s-%s-%s\\%s' %
                         (TESTER_CODE, ID, NAME, GENDER, data_filename))
        tab_VI_content_display()
    tkinter.Label(
        tab_VI_root,
        text='警戒作业测试 -O-SS',
        font=('HarmonyOS Sans SC',14,'bold')).place(x=20,y=20)
    clock = tkinter.Label(
        tab_VI_root, text='', font=('HarmonyOS Sans', 12, 'bold'))
    clock.place(x=660, y=650)
    clock_thread = threading.Thread(target=time_display)
    clock_thread.daemon = True
    clock_thread.start()
    for index in range(40):
        tkinter.Label(
            tab_VI_root,
            text='|',
            font=('HarmonyOS Sans',10,'bold')).place(x=650,y=20 *index)
    for index in range(40):
        tkinter.Label(
            tab_VI_root,
            text='|',
            font=('HarmonyOS Sans',10,'bold')).place(x=1025,y=20 *index)
    tkinter.Label(
        tab_VI_root,
        text='---------- Info_Area  信息区域 ----------',
        font=('HarmonyOS Sans SC',14,'bold')).place(x=660,y=0)
    tkinter.Label(
        tab_VI_root,
        text='-------- Submit_Area  提交区域 --------',
        font=('HarmonyOS Sans SC',14,'bold')).place(x=660,y=500)
    tkinter.Label(
        tab_VI_root,
        text='---------- 量表区域 ----------',
        font=('HarmonyOS Sans SC',14,'bold')).place(x=1030,y=0)
    '''
    tkinter.Label(
        tab_VI_root,
        text='此\n环\n节\n已\n禁\n用',
        font=('HarmonyOS Sans SC',12,'bold')).place(x=1150,y=280)
    '''
    tkinter.Label(
        tab_VI_root,
        text='如果你已做好准备，请点按下方按钮以开始测试。',
        font=('HarmonyOS Sans SC',10)).place(x=660,y=50)
    tkinter.Label(
        tab_VI_root,
        text='Please press the button below to continue.',
        font=('HarmonyOS Sans',10)).place(x=660,y=80)
    tkinter.Label(
        tab_VI_root,
        text='当点按后，将有 2 秒的准备时间，随后测试即刻开始。',
        font=('HarmonyOS Sans SC',10)).place(x=660,y=110)
    tkinter.Label(
        tab_VI_root,
        text='当观察到任一面板出现异常事件，请立刻点按相应键盘按键。',
        font=('HarmonyOS Sans SC',10)).place(x=660,y=550)
    key_warn = tkinter.Label(
        tab_VI_root,
        text='键盘输入检查：请确认已处于英文输入状态或大写锁定状态。',
        font=('HarmonyOS Sans SC',10,'bold'))
    key_warn.place(x=660, y=460)
    start_submit = tkinter.Button(
        tab_VI_root,
        width=42,
        text='开始测试  START TEST',
        font=('HarmonyOS Sans SC',10,'bold'),
        command=test_display)
    start_submit.place(x=670, y=150)
    feedback_submit = tkinter.Button(
        tab_VI_root,
        width=42,
        text='(此环节已禁用) 预警提交  SUBMIT FEEDBACK',
        font=('HarmonyOS Sans SC',10,'bold'),
        state='disabled')
    feedback_submit.place(x=670, y=600)
    tkinter.Label(
        tab_VI_root,
        text='DashBoard_I',
        font=('HarmonyOS Sans',12,'italic')).place(x=50,y=100)
    dashboard_I_interval = tkinter.Label(
        tab_VI_root, text='', font=('HarmonyOS Sans SC', 18, 'bold'))
    dashboard_I_interval.place(x=50, y=160)
    dashboard_I_data = tkinter.Label(
        tab_VI_root, text='', font=('HarmonyOS Sans SC', 20, 'bold'))
    dashboard_I_data.place(x=50, y=230)
    tkinter.Label(
        tab_VI_root,
        text='DashBoard_II',
        font=('HarmonyOS Sans',12,'italic')).place(x=350,y=100)
    dashboard_II_interval = tkinter.Label(
        tab_VI_root, text='', font=('HarmonyOS Sans SC', 18, 'bold'))
    dashboard_II_interval.place(x=350, y=160)
    dashboard_II_data = tkinter.Label(
        tab_VI_root, text='', font=('HarmonyOS Sans SC', 20, 'bold'))
    dashboard_II_data.place(x=350, y=230)
    tkinter.Label(
        tab_VI_root,
        text='DashBoard_III',
        font=('HarmonyOS Sans',12,'italic')).place(x=50,y=350)
    dashboard_III_interval = tkinter.Label(
        tab_VI_root, text='', font=('HarmonyOS Sans SC', 18, 'bold'))
    dashboard_III_interval.place(x=50, y=410)
    dashboard_III_data = tkinter.Label(
        tab_VI_root, text='', font=('HarmonyOS Sans SC', 20, 'bold'))
    dashboard_III_data.place(x=50, y=480)
    tkinter.Label(
        tab_VI_root,
        text='DashBoard_IV',
        font=('HarmonyOS Sans',12,'italic')).place(x=350,y=350)
    dashboard_IV_interval = tkinter.Label(
        tab_VI_root, text='', font=('HarmonyOS Sans SC', 18, 'bold'))
    dashboard_IV_interval.place(x=350, y=410)
    dashboard_IV_data = tkinter.Label(
        tab_VI_root, text='', font=('HarmonyOS Sans SC', 20, 'bold'))
    dashboard_IV_data.place(x=350, y=480)
    dashboard_emergency = tkinter.Label(
        tab_VI_root, image='', font=('HarmonyOS Sans SC', 14, 'italic'))
    dashboard_emergency.place(x=50, y=300)
def tab_VII_content_display():
    def time_display():
        while True:
            clock.configure(text='----------- ' +time.strftime('%Y-%m-%d %H:%M:%S') +' -----------')
            time.sleep(1)
    def test_display():
        def countdown_display(total_seconds):
            while total_seconds != 0:
                total_seconds -= 1
                countdown.configure(
                    text='倒计时：%02dmin %02ds' %(total_seconds //60,total_seconds %60))
                time.sleep(1)
            if total_seconds == 0:
                display_status = False
                data_upload()
        def interval_countdown_display():
            interval_seconds = interval_change_time
            while True:
                interval_seconds -= 1
                interval_countdown.configure(
                    text='距离数字对目标区间变更还有： %02ds' %(interval_seconds))
                time.sleep(1)
                if interval_seconds == 0:
                    interval_seconds = interval_change_time
                    interval_start.append([random.randint(2, 10)
                                          for i in range(dashboard_num)])
        def dashboard_display():
            while display_status:
                global start_time, display_round_count, rest_round_count, rest_status, emer_status
                rest_status = False
                key_press.focus_set()
                data_item.append([[random.randint(2, 8) for i in range(2)]
                                 for j in range(dashboard_num)])
                for index in range(dashboard_num):
                    data_item[-1][index][1] = data_item[-1][index][0] + random.randint(-1,1)
                current_interval = interval_start[-1]
                for index in range(dashboard_num):
                    pair_sum = data_item[-1][index][0] + data_item[-1][index][1]
                    while interval_start[-1][index] <= pair_sum <= interval_start[-1][index] + interval_length:
                        data_item[-1][index] = [random.randint(2, 8)for i in range(2)]
                        data_item[-1][index][1] = data_item[-1][index][0] + random.randint(-1,1)
                        pair_sum = data_item[-1][index][0] + data_item[-1][index][1]
                random_prob = random.random()
                random_emergency_prob = random.random()
                if random_prob < RATE_CALL:
                    display_area = random.randint(1, dashboard_num)
                    pair_sum = data_item[-1][display_area - 1][0] + data_item[-1][display_area - 1][1]
                    while not interval_start[-1][display_area - 1] <= pair_sum <= interval_start[-1][display_area - 1] + interval_length:
                        data_item[-1][display_area - 1] = [random.randint(2, 8) for i in range(2)]
                        data_item[-1][display_area - 1][1] = data_item[-1][display_area - 1][0] + random.randint(-1,1)
                        pair_sum = data_item[-1][display_area - 1][0] + data_item[-1][display_area - 1][1]
                emer_status = display_round_all * 0.5 < display_round_count < display_round_all * 0.7
                if random_emergency_prob < emergency_rate and emer_status:
                    winsound.Beep(2000, 500)
                    data_record_IV.append(
                        [-1, 'DashBoard_Emergency', -1, -1, -1, -1, True, 'Missed'])
                    dashboard_emergency.configure(image=img_attention)
                else:
                    data_record_IV.append(
                        [-1, 'DashBoard_Emergency', -1, -1, -1, -1, False, 'Accepted'])
                display_round_count += 1
                judge = interval_start[-1][0] <= sum(
                    data_item[-1][0]) <= interval_start[-1][0] + interval_length
                data_record_IV.append([display_round_count,
                                       'DashBoard_I',
                                       interval_start[-1][0],
                                       interval_start[-1][0] + interval_length,
                                       data_item[-1][0][0],
                                       data_item[-1][0][1],
                                       judge,
                                       'Missed' if judge else 'Accepted'])
                judge = interval_start[-1][1] <= sum(
                    data_item[-1][1]) <= interval_start[-1][1] + interval_length
                data_record_IV.append([display_round_count,
                                       'DashBoard_II',
                                       interval_start[-1][1],
                                       interval_start[-1][1] + interval_length,
                                       data_item[-1][1][0],
                                       data_item[-1][1][1],
                                       judge,
                                       'Missed' if judge else 'Accepted'])
                judge = interval_start[-1][2] <= sum(
                    data_item[-1][2]) <= interval_start[-1][2] + interval_length
                data_record_IV.append([display_round_count,
                                       'DashBoard_III',
                                       interval_start[-1][2],
                                       interval_start[-1][2] + interval_length,
                                       data_item[-1][2][0],
                                       data_item[-1][2][1],
                                       judge,
                                       'Missed' if judge else 'Accepted'])
                judge = interval_start[-1][3] <= sum(
                    data_item[-1][3]) <= interval_start[-1][3] + interval_length
                data_record_IV.append([display_round_count,
                                       'DashBoard_IV',
                                       interval_start[-1][3],
                                       interval_start[-1][3] + interval_length,
                                       data_item[-1][3][0],
                                       data_item[-1][3][1],
                                       judge,
                                       'Missed' if judge else 'Accepted'])
                dashboard_I_interval.configure(
                    text='%-2s —— %-2s' % (interval_start[-1][0], interval_start[-1][0] + interval_length))
                dashboard_II_interval.configure(
                    text='%-2s —— %-2s' % (interval_start[-1][1], interval_start[-1][1] + interval_length))
                dashboard_III_interval.configure(
                    text='%-2s —— %-2s' % (interval_start[-1][2], interval_start[-1][2] + interval_length))
                dashboard_IV_interval.configure(
                    text='%-2s —— %-2s' % (interval_start[-1][3], interval_start[-1][3] + interval_length))
                dashboard_I_data.configure(text='%s          %s' % (
                    data_item[-1][0][0], data_item[-1][0][1]))
                dashboard_II_data.configure(text='%s          %s' % (
                    data_item[-1][1][0], data_item[-1][1][1]))
                dashboard_III_data.configure(text='%s          %s' % (
                    data_item[-1][2][0], data_item[-1][2][1]))
                dashboard_IV_data.configure(text='%s          %s' % (
                    data_item[-1][3][0], data_item[-1][3][1]))
                start_time = time.time()
                time.sleep(display_time)
                if interval_start[-1] != current_interval:
                    dashboard_I_interval.configure(text='')
                    dashboard_II_interval.configure(text='')
                    dashboard_III_interval.configure(text='')
                    dashboard_IV_interval.configure(text='')
                dashboard_I_data.configure(text='')
                dashboard_II_data.configure(text='')
                dashboard_III_data.configure(text='')
                dashboard_IV_data.configure(text='')
                dashboard_emergency.configure(image='')
                time.sleep(vacant_time)
        try:
            ID, NAME, GENDER
        except NameError:
            tkinter.messagebox.showwarning(
                title='系统端提示', message='请先在程序主页提交个人信息！')
            return
        if tip_enhanced_status:
            tkinter.messagebox.showinfo(
                title='系统端提示', message='对于突发事件的定义：请留意每轮中区域内的突显文字。')
        time.sleep(2)
        global interval_start, data_item, data_record_IV, situation_record_IV, display_round_count, display_status, emer_status
        minute = period_time * period_num
        emer_status = False
        display_status = True
        interval_start = []
        data_item = []
        data_record_IV = []
        situation_record_IV = []
        display_round_count = 0
        display_round_all = display_round_per_min * minute
        start_submit.configure(state='disabled')
        feedback_submit.configure(state='normal')
        status_check = 'InfoCheck-%s-Tab_VII-Work-E-SS-%s-%s-%s-%s-%s-%s' % (
            VERSION, TESTER_CODE, ID, NAME, GENDER, PERIOD, START_TIME)
        bottom_status_bar.configure(text=status_check)
        interval_start.append([random.randint(2, 10)for i in range(dashboard_num)])
        tkinter.Label(
            tab_VII_root,
            text='请不要在一轮中连续点按键盘，否则只会记录首次数据。',
            font=('HarmonyOS Sans SC',10)).place(x=660,y=210)
        tkinter.Label(
            tab_VII_root,
            text='本次测试共历时 %d 分钟。' %(minute),
            font=('HarmonyOS Sans SC',10)).place(x=660,y=240)
        key_press = tkinter.Label(
            tab_VII_root,
            text='Tips：当前，<%s%s%s%s> 键位分别对应 DashBoard_I ~ IV。'%(keyboard_preference_I, keyboard_preference_II, keyboard_preference_III, keyboard_preference_IV),
            font=('HarmonyOS Sans SC',10,'bold'))
        key_press.focus_set()
        key_press.place(x=660, y=300)
        key_press.bind("<Key>", key_feedback)
        countdown = tkinter.Label(
            tab_VII_root, 
            text='倒计时： %02dmin 00s' %(minute), 
            font=('HarmonyOS Sans SC', 10, 'bold'))
        countdown.place(x=660, y=330)
        countdown_thread = threading.Thread(target=lambda: countdown_display(total_seconds=minute * 60))
        countdown_thread.daemon = True
        countdown_thread.start()
        interval_countdown = tkinter.Label(
            tab_VII_root, 
            text='距离数字对目标区间变更还有： %02ds' %(interval_change_time), 
            font=('HarmonyOS Sans SC', 10, 'bold'))
        interval_countdown.place(x=660, y=420)
        interval_change_thread = threading.Thread(target=lambda: interval_countdown_display())
        interval_change_thread.daemon = True
        interval_change_thread.start()
        dashboard_thread = threading.Thread(target=dashboard_display)
        dashboard_thread.daemon = True
        dashboard_thread.start()
    def key_feedback(event):
        end_time = time.time()
        logging.info('The tester clicks the keyboard: %s' % str(event.keysym))
        if event.keysym in keyboard_preference_I or event.keysym in keyboard_preference_opt_I:
            index = -4
            key_warn.configure(text='键盘输入检查：你当前输入状态正常，请继续测试 ~')
        elif event.keysym in keyboard_preference_II or event.keysym in keyboard_preference_opt_II:
            index = -3
            key_warn.configure(text='键盘输入检查：你当前输入状态正常，请继续测试 ~')
        elif event.keysym in keyboard_preference_III or event.keysym in keyboard_preference_opt_III:
            index = -2
            key_warn.configure(text='键盘输入检查：你当前输入状态正常，请继续测试 ~')
        elif event.keysym in keyboard_preference_IV or event.keysym in keyboard_preference_opt_IV:
            index = -1
            key_warn.configure(text='键盘输入检查：你当前输入状态正常，请继续测试 ~')
        elif event.keysym in '??':
            key_warn.configure(text='键盘输入检查：你当前处于中文输入状态，请检查！')
            return
        else:
            key_warn.configure(text='键盘输入检查：除切换输入状态外，请不要按下其他按键！')
            return
        if data_record_IV[index][6]:
            if data_record_IV[index][-2] != 'Hit':
                data_record_IV[index][-1] = 'Hit'
                data_record_IV[index].append(end_time - start_time)
        elif not data_record_IV[index][6] and data_record_IV[index][-2] != 'Wrong':
            data_record_IV[index][-1] = 'Wrong'
            data_record_IV[index].append(end_time - start_time)
    def emergency_feedback():
        end_time = time.time()
        if data_record_IV[-dashboard_num - 1][0] == -1:
            if data_record_IV[-dashboard_num - 1][6]:
                if data_record_IV[-dashboard_num - 1][-2] != 'Hit':
                    data_record_IV[-dashboard_num - 1][-1] = 'Hit'
                    data_record_IV[-dashboard_num -1].append(end_time - start_time)
            else:
                if data_record_IV[-dashboard_num - 1][-2] != 'Wrong':
                    data_record_IV[-dashboard_num - 1][-1] = 'Wrong'
                    data_record_IV[-dashboard_num -1].append(end_time - start_time)
    def data_upload():
        def choose_confirm(index):
            situation_end = time.time()
            situation_record_IV.append(
                [display_round_count, index, situation_end - situation_start])
            choose_I.configure(state='disabled')
            choose_II.configure(state='disabled')
            choose_III.configure(state='disabled')
            choose_IV.configure(state='disabled')
            choose_V.configure(state='disabled')
            choose_VI.configure(state='disabled')
            choose_VII.configure(state='disabled')
        dashboard_emergency.configure(image=img_scale)  # TODO
        tkinter.Label(
            tab_VII_root, text='即将呈现量表内容，请做好准备！', font=(
                'HarmonyOS Sans SC', 10, 'bold')).place(x=1040, y=50)
        tkinter.Label(
            tab_VII_root, text='请尽快选择出最符合你当前状态的选项。', font=(
                'HarmonyOS Sans SC', 10, 'bold')).place(x=1040, y=80)
        situation_start = time.time()
        choose_I = tkinter.Button(tab_VII_root, width=28, text='完全警觉，完全清醒', font=(
            'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(0))
        choose_I.place(x=1035, y=150)
        choose_II = tkinter.Button(
            tab_VII_root, width=28, text='很有活力，反应灵敏，但非最好状态', font=(
                'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(1))
        choose_II.place(x=1035, y=200)
        choose_III = tkinter.Button(tab_VII_root, width=28, text='情况一般，稍微清醒', font=(
            'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(2))
        choose_III.place(x=1035, y=250)
        choose_IV = tkinter.Button(tab_VII_root, width=28, text='有点累，不怎么清醒', font=(
            'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(3))
        choose_IV.place(x=1035, y=300)
        choose_V = tkinter.Button(tab_VII_root, width=28, text='挺累的，无精打采', font=(
            'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(4))
        choose_V.place(x=1035, y=350)
        choose_VI = tkinter.Button(tab_VII_root, width=28, text='非常疲惫，难以集中精神', font=(
            'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(5))
        choose_VI.place(x=1035, y=400)
        choose_VII = tkinter.Button(tab_VII_root, width=28, text='精疲力尽，无法有效地工作', font=(
            'HarmonyOS Sans SC', 11, 'bold'), command=lambda: choose_confirm(6))
        choose_VII.place(x=1035, y=450)
        key_warn.configure(text='Congratulations！测试结束，此界面即将关闭 ~')
        time.sleep(6)
        for widget in tab_VII_root.winfo_children():
            widget.destroy()
        if not os.path.exists(r'.\\data\\%s-%s-%s-%s' %(TESTER_CODE, ID, NAME, GENDER)):
            os.makedirs(r'.\\data\\%s-%s-%s-%s' %(TESTER_CODE, ID, NAME, GENDER))
        upload_time = time.strftime('%H%M%S', time.localtime())
        data_filename = 'Tab_VII-Work_E_SS-Test_Data-%s-%s-%s-%s-%s-%s-%s.csv' % (
            TESTER_CODE, ID, NAME, GENDER, PERIOD, START_TIME, upload_time)
        data_record_df = pandas.DataFrame(
            data_record_IV,
            columns=[
                'display_round_count',
                'area_index',
                'interval_start',
                'interval_end',
                'data_I',
                'data_II',
                'system_judge',
                'user_judge',
                'response_time'])
        data_record_df.to_csv(r'data\\%s-%s-%s-%s\\%s' %
            (TESTER_CODE, ID, NAME, GENDER, data_filename), index=False)
        situation_filename = 'Tab_VII-Work_E_SS-Mental_Data-%s-%s-%s-%s-%s-%s-%s.csv' % (
            TESTER_CODE, ID, NAME, GENDER, PERIOD, START_TIME, upload_time)
        situation_record_df = pandas.DataFrame(
            situation_record_IV,
            columns=[
                'display_round_count',
                'situation_selected',
                'response_time'])
        situation_record_df.to_csv(r'data\\%s-%s-%s-%s\\%s' %
            (TESTER_CODE, ID, NAME, GENDER, situation_filename), index=False)
        if webdav_status:
            client = Client(
                base_url='https://dav.jianguoyun.com/dav/',
                auth=(webdav_account,webdav_password))
            client.mkdir('/appdata_upload')
            client.mkdir('/appdata_upload/%s-%s-%s-%s/' %(TESTER_CODE, ID, NAME, GENDER))
            client.upload_file(
                from_path='data\\%s-%s-%s-%s\\%s' %
                (TESTER_CODE,ID,NAME,GENDER,data_filename),
                to_path='/appdata_upload/%s-%s-%s-%s/%s' %
                (TESTER_CODE,ID,NAME,GENDER,data_filename),
                overwrite=True)
            client.upload_file(
                from_path='data\\%s-%s-%s-%s\\%s' %
                (TESTER_CODE,ID,NAME,GENDER,situation_filename),
                to_path='/appdata_upload/%s-%s-%s-%s/%s' %
                (TESTER_CODE,ID,NAME,GENDER,situation_filename),
                overwrite=True)
        else:
            os.startfile(r'.\\data\\%s-%s-%s-%s\\%s' %
                         (TESTER_CODE, ID, NAME, GENDER, data_filename))
        tab_VII_content_display()
    tkinter.Label(
        tab_VII_root,
        text='警戒作业测试 -E-SS',
        font=('HarmonyOS Sans SC',14,'bold')).place(x=20,y=20)
    clock = tkinter.Label(
        tab_VII_root, text='', font=('HarmonyOS Sans', 12, 'bold'))
    clock.place(x=660, y=650)
    clock_thread = threading.Thread(target=time_display)
    clock_thread.daemon = True
    clock_thread.start()
    for index in range(40):
        tkinter.Label(
            tab_VII_root,
            text='|',
            font=('HarmonyOS Sans',10,'bold')).place(x=650,y=20 *index)
    for index in range(40):
        tkinter.Label(
            tab_VII_root,
            text='|',
            font=('HarmonyOS Sans',10,'bold')).place(x=1025,y=20 *index)
    tkinter.Label(
        tab_VII_root,
        text='---------- Info_Area  信息区域 ----------',
        font=('HarmonyOS Sans SC',14,'bold')).place(x=660,y=0)
    tkinter.Label(
        tab_VII_root,
        text='-------- Submit_Area  提交区域 --------',
        font=('HarmonyOS Sans SC',14,'bold')).place(x=660,y=500)
    tkinter.Label(
        tab_VII_root,
        text='---------- 量表区域 ----------',
        font=('HarmonyOS Sans SC',14,'bold')).place(x=1030,y=0)
    '''
    tkinter.Label(
        tab_VII_root,
        text='此\n环\n节\n已\n禁\n用',
        font=('HarmonyOS Sans SC',12,'bold')).place(x=1150,y=280)
    '''
    tkinter.Label(
        tab_VII_root,
        text='如果你已做好准备，请点按下方按钮以开始测试。',
        font=('HarmonyOS Sans SC',10)).place(x=660,y=50)
    tkinter.Label(
        tab_VII_root,
        text='Please press the button below to continue.',
        font=('HarmonyOS Sans',10)).place(x=660,y=80)
    tkinter.Label(
        tab_VII_root,
        text='当点按后，将有 2 秒的准备时间，随后测试即刻开始。',
        font=('HarmonyOS Sans SC',10)).place(x=660,y=110)
    tkinter.Label(
        tab_VII_root,
        text='当观察到任一面板出现异常事件，请立刻点按相应键盘按键。',
        font=('HarmonyOS Sans SC',10)).place(x=660,y=540)
    if tip_enhanced_status:
        tkinter.Label(
            tab_VII_root,
            text='当观察到任一面板出现突发事件，请立刻点按下方提交按钮。',
            font=('HarmonyOS Sans SC',10)).place(x=660,y=570)
    key_warn = tkinter.Label(
        tab_VII_root,
        text='键盘输入检查：请确认已处于英文输入状态或大写锁定状态。',
        font=('HarmonyOS Sans SC',10,'bold'))
    key_warn.place(x=660, y=460)
    start_submit = tkinter.Button(
        tab_VII_root,
        width=42,
        text='开始测试  START TEST',
        font=('HarmonyOS Sans SC',10,'bold'),
        command=test_display)
    start_submit.place(x=670, y=150)
    feedback_submit = tkinter.Button(
        tab_VII_root,
        width=42,
        text='预警提交  SUBMIT FEEDBACK',
        font=('HarmonyOS Sans SC',10,'bold'),
        state='disabled',
        command=emergency_feedback)
    feedback_submit.place(x=670, y=600)
    tkinter.Label(
        tab_VII_root,
        text='DashBoard_I',
        font=('HarmonyOS Sans',12,'italic')).place(x=50,y=100)
    dashboard_I_interval = tkinter.Label(
        tab_VII_root, text='', font=('HarmonyOS Sans SC', 18, 'bold'))
    dashboard_I_interval.place(x=50, y=160)
    dashboard_I_data = tkinter.Label(
        tab_VII_root, text='', font=('HarmonyOS Sans SC', 20, 'bold'))
    dashboard_I_data.place(x=50, y=230)
    tkinter.Label(
        tab_VII_root,
        text='DashBoard_II',
        font=('HarmonyOS Sans',12,'italic')).place(x=350,y=100)
    dashboard_II_interval = tkinter.Label(
        tab_VII_root, text='', font=('HarmonyOS Sans SC', 18, 'bold'))
    dashboard_II_interval.place(x=350, y=160)
    dashboard_II_data = tkinter.Label(
        tab_VII_root, text='', font=('HarmonyOS Sans SC', 20, 'bold'))
    dashboard_II_data.place(x=350, y=230)
    tkinter.Label(
        tab_VII_root,
        text='DashBoard_III',
        font=('HarmonyOS Sans',12,'italic')).place(x=50,y=350)
    dashboard_III_interval = tkinter.Label(
        tab_VII_root, text='', font=('HarmonyOS Sans SC', 18, 'bold'))
    dashboard_III_interval.place(x=50, y=410)
    dashboard_III_data = tkinter.Label(
        tab_VII_root, text='', font=('HarmonyOS Sans SC', 20, 'bold'))
    dashboard_III_data.place(x=50, y=480)
    tkinter.Label(
        tab_VII_root,
        text='DashBoard_IV',
        font=('HarmonyOS Sans',12,'italic')).place(x=350,y=350)
    dashboard_IV_interval = tkinter.Label(
        tab_VII_root, text='', font=('HarmonyOS Sans SC', 18, 'bold'))
    dashboard_IV_interval.place(x=350, y=410)
    dashboard_IV_data = tkinter.Label(
        tab_VII_root, text='', font=('HarmonyOS Sans SC', 20, 'bold'))
    dashboard_IV_data.place(x=350, y=480)
    dashboard_emergency = tkinter.Label(
        tab_VII_root, image='', font=('HarmonyOS Sans SC', 14, 'italic'))
    dashboard_emergency.place(x=50, y=300)
def tab_VIII_content_display():
    def password_confirm():
        password_md5 = hashlib.md5()
        password_md5.update(str.encode(password_entry.get()))
        if password_md5.hexdigest() == storage_db_cursor.execute(
                '''SELECT setting FROM options WHERE key == "captcha_encrypted"''').fetchall()[0][0]:
            logging.info('Developer password validates successfully')
            bottom_status_bar.configure(
                text='口令验证成功！当前正处于 开发者状态，请在设置完成后注意登出账号')
            password_entry.configure(state='disabled')
            password_submit.configure(state='disabled')
            display_time_entry.configure(state='normal')
            vacant_time_entry.configure(state='normal')
            period_time_entry.configure(state='normal')
            period_num_entry.configure(state='normal')
            high_rate_entry.configure(state='normal')
            low_rate_entry.configure(state='normal')
            rate_handover_combobox.configure(state='normal')
            length_entry.configure(state='normal')
            interval_change_cycle_entry.configure(state='normal')
            rest_time_entry.configure(state='normal')
            emergency_rate_entry.configure(state='normal')
            top_window_status_combobox.configure(state='normal')
            del_window_status_combobox.configure(state='normal')
            tip_enhanced_status_combobox.configure(state='normal')
            force_dark_mode_status_combobox.configure(state='normal')
            webdav_status_combobox.configure(state='normal')
            webdav_account_entry.configure(state='normal')
            webdav_password_entry.configure(state='normal')
            local_filepath_entry.configure(state='normal')
            local_filepath_submit.configure(state='normal')
            setting_submit.configure(state='normal')
            setting_submit_exit.configure(state='normal')
            dev_exit_submit.configure(state='normal')
            data_upload_submit.configure(state='normal')
            watchdog_submit.configure(state='normal')
            log_filepath_submit.configure(state='normal')
            data_analyze_submit.configure(state='normal')
            keyboard_submit.configure(state='normal')
    def setting_confirm():
        display_time = int(display_time_entry.get())
        vacant_time = int(vacant_time_entry.get())
        period_time = int(period_time_entry.get())
        period_num = int(period_num_entry.get())
        event_num_per_min_high = float(high_rate_entry.get())
        event_num_per_min_low = float(low_rate_entry.get())
        rate_handover_status = 0 if rate_handover_combobox.get() == '低' else 1
        emergency_num_per_ten_min = float(emergency_rate_entry.get())
        interval_length = int(length_entry.get())
        interval_change_cycle = int(interval_change_cycle_entry.get())
        rest_time = int(rest_time_entry.get())
        top_window_status = 0 if top_window_status_combobox.get() == '禁用' else 1
        del_window_status = 0 if del_window_status_combobox.get() == '禁用' else 1
        tip_enhanced_status = 0 if tip_enhanced_status_combobox.get() == '禁用' else 1
        force_dark_mode_status = 0 if force_dark_mode_status_combobox.get() == '禁用' else 1
        webdav_status = 0 if webdav_status_combobox.get() == '禁用' else 1
        webdav_account = webdav_account_entry.get()
        webdav_password = webdav_password_entry.get()
        local_filepath = local_filepath_entry.get()
        if webdav_status:
            storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
                (webdav_status, 'webdav_status'))
            storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
                (webdav_account, 'webdav_account'))
            storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
                (webdav_password, 'webdav_password'))
            if local_filepath == '' or local_filepath == 'null':
                storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
                    ('null', 'local_filepath'))
            else:
                storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
                    (local_filepath, 'local_filepath'))
        else:
            storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
                (webdav_status, 'webdav_status'))
            storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
                ('null', 'webdav_account'))
            storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
                ('null', 'webdav_password'))
            storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
                ('null', 'local_filepath'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (display_time, 'display_time'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (vacant_time, 'vacant_time'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (period_time, 'period_time'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (period_num, 'period_num'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (event_num_per_min_high, 'event_num_per_min_high'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (event_num_per_min_low, 'event_num_per_min_low'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (rate_handover_status, 'rate_handover_status'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (emergency_num_per_ten_min, 'emergency_num_per_ten_min'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (interval_length, 'interval_length'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (interval_change_cycle, 'interval_change_cycle'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (rest_time, 'rest_time'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (top_window_status, 'top_window_status'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (del_window_status, 'del_window_status'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (tip_enhanced_status, 'tip_enhanced_status'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (force_dark_mode_status, 'force_dark_mode_status'))
        storage_db_connect.commit()
        logging.info('Configuration Update display_time: %s' % display_time)
        logging.info('Configuration Update vacant_time: %s' % vacant_time)
        logging.info('Configuration Update period_time: %s' % period_time)
        logging.info('Configuration Update period_num: %s' % period_num)
        logging.info('Configuration Update rest_time: %s' % rest_time)
        logging.info('Configuration Update interval_length: %s' %interval_length)
        logging.info('Configuration Update interval_change_cycle: %s' %interval_change_cycle)
        logging.info('Configuration Update event_num_per_min_high: %s' %event_num_per_min_high)
        logging.info('Configuration Update event_num_per_min_low: %s' %event_num_per_min_low)
        logging.info('Configuration Update rate_handover_status: %s' %rate_handover_status)
        logging.info('Configuration Update emergency_num_per_ten_min: %s' %emergency_num_per_ten_min)
        logging.info('Configuration Update top_window_status: %s' %top_window_status)
        logging.info('Configuration Update del_window_status: %s' %del_window_status)
        logging.info('Configuration Update tip_enhanced_status: %s' %tip_enhanced_status)
        logging.info('Configuration Update force_dark_mode_status: %s' %force_dark_mode_status)
        logging.info('Configuration Update webdav_status: %s' % webdav_status)
        logging.info('Configuration Update webdav_account: %s' %webdav_account)
        logging.info('Configuration Update webdav_password: %s' %webdav_password)
        logging.info('Configuration Update local_filepath: %s' %local_filepath)
        tkinter.messagebox.showinfo(title='系统端提示', message='设置更改完成，将在下次启动时生效。')
        for widget in tab_VIII_root.winfo_children():
            widget.destroy()
        try:
            ID, NAME, GENDER, START_TIME
        except NameError:
            bottom_status_bar.configure(text='欢迎使用 认知性警戒作业模拟及绩效测试系统')
        else:
            status_check = '被试者：%s - %s - %s，登陆时间：%s，%s阶段，欢迎使用 认知性警戒作业模拟及绩效测试系统' % (
                ID, NAME, GENDER, START_TIME, PERIOD)
            bottom_status_bar.configure(text=status_check)
        tab_VIII_content_display()
    def setting_confirm_exit():
        display_time = int(display_time_entry.get())
        vacant_time = int(vacant_time_entry.get())
        period_time = int(period_time_entry.get())
        period_num = int(period_num_entry.get())
        event_num_per_min_high = float(high_rate_entry.get())
        event_num_per_min_low = float(low_rate_entry.get())
        rate_handover_status = 0 if rate_handover_combobox.get() == '低' else 1
        emergency_num_per_ten_min = float(emergency_rate_entry.get())
        interval_length = int(length_entry.get())
        interval_change_cycle = int(interval_change_cycle_entry.get())
        rest_time = int(rest_time_entry.get())
        top_window_status = 0 if top_window_status_combobox.get() == '禁用' else 1
        del_window_status = 0 if del_window_status_combobox.get() == '禁用' else 1
        tip_enhanced_status = 0 if tip_enhanced_status_combobox.get() == '禁用' else 1
        force_dark_mode_status = 0 if force_dark_mode_status_combobox.get() == '禁用' else 1
        webdav_status = 0 if webdav_status_combobox.get() == '禁用' else 1
        webdav_account = webdav_account_entry.get()
        webdav_password = webdav_password_entry.get()
        local_filepath = local_filepath_entry.get()
        if webdav_status:
            storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
                (webdav_status, 'webdav_status'))
            storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
                (webdav_account, 'webdav_account'))
            storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
                (webdav_password, 'webdav_password'))
            if local_filepath == '' or local_filepath == 'null':
                storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
                    ('null', 'local_filepath'))
            else:
                storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
                    (local_filepath, 'local_filepath'))
        else:
            storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
                (webdav_status, 'webdav_status'))
            storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
                ('null', 'webdav_account'))
            storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
                ('null', 'webdav_password'))
            storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
                ('null', 'local_filepath'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (display_time, 'display_time'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (vacant_time, 'vacant_time'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (period_time, 'period_time'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (period_num, 'period_num'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (event_num_per_min_high, 'event_num_per_min_high'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (event_num_per_min_low, 'event_num_per_min_low'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (rate_handover_status, 'rate_handover_status'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (emergency_num_per_ten_min, 'emergency_num_per_ten_min'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (interval_length, 'interval_length'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (interval_change_cycle, 'interval_change_cycle'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (rest_time, 'rest_time'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (top_window_status, 'top_window_status'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (del_window_status, 'del_window_status'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (tip_enhanced_status, 'tip_enhanced_status'))
        storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
            (force_dark_mode_status, 'force_dark_mode_status'))
        storage_db_connect.commit()
        logging.info('Configuration Update display_time: %s' % display_time)
        logging.info('Configuration Update vacant_time: %s' % vacant_time)
        logging.info('Configuration Update period_time: %s' % period_time)
        logging.info('Configuration Update period_num: %s' % period_num)
        logging.info('Configuration Update rest_time: %s' % rest_time)
        logging.info('Configuration Update interval_length: %s' %interval_length)
        logging.info('Configuration Update interval_change_cycle: %s' %interval_change_cycle)
        logging.info('Configuration Update event_num_per_min_high: %s' %event_num_per_min_high)
        logging.info('Configuration Update event_num_per_min_low: %s' %event_num_per_min_low)
        logging.info('Configuration Update rate_handover_status: %s' %rate_handover_status)
        logging.info('Configuration Update emergency_num_per_ten_min: %s' %emergency_num_per_ten_min)
        logging.info('Configuration Update top_window_status: %s' %top_window_status)
        logging.info('Configuration Update del_window_status: %s' %del_window_status)
        logging.info('Configuration Update tip_enhanced_status: %s' %tip_enhanced_status)
        logging.info('Configuration Update force_dark_mode_status: %s' %force_dark_mode_status)
        logging.info('Configuration Update webdav_status: %s' % webdav_status)
        logging.info('Configuration Update webdav_account: %s' %webdav_account)
        logging.info('Configuration Update webdav_password: %s' %webdav_password)
        logging.info('Configuration Update local_filepath: %s' %local_filepath)
        tkinter.messagebox.showinfo(title='系统端提示', message='设置更改完成，程序即将退出。')
        logging.info('Exiting the root window')
        root.destroy()
        try:
            watchdog_root.destroy()
        except NameError:
            pass
        else:
            logging.info('Exiting the watchdog_root window')
            watchdog_root.destroy()
        try:
            upload_root.destroy()
        except NameError:
            pass
        else:
            logging.info('Exiting the upload_root window')
            upload_root.destroy()
        try:
            keyboard_root.destroy()
        except NameError:
            pass
        else:
            logging.info('Exiting the keyboard_root window')
            keyboard_root.destroy()
        try:
            data_analyze_root.destroy()
        except NameError:
            pass
        else:
            logging.info('Exiting the data_analyze_root window')
            data_analyze_root.destroy()
    def overall_upload_display():
        def data_upload_overall():
            upload_time = time.strftime('%H%M%S', time.localtime())
            if not os.path.exists(r'.\\data\\%s-%s-%s-%s' %(TESTER_CODE, ID, NAME, GENDER)):
                os.makedirs(r'.\\data\\%s-%s-%s-%s' %(TESTER_CODE, ID, NAME, GENDER))
            if test_list[0] != -1:
                data_filename = 'Tab_IV-Work_O_S-Test_Data-%s-%s-%s-%s-%s-%s-%s.csv' % (
                    TESTER_CODE, ID, NAME, GENDER, PERIOD, START_TIME, upload_time)
                data_record_df_I = pandas.DataFrame(
                    data_record,
                    columns=[
                        'display_round_count',
                        'area_index',
                        'interval_start',
                        'interval_end',
                        'data_I',
                        'data_II',
                        'system_judge',
                        'user_judge',
                        'response_time'])
                data_record_df_I.to_csv(r'.\\data\\%s-%s-%s-%s\\%s' %
                    (TESTER_CODE, ID, NAME, GENDER, data_filename), index=False)
                if webdav_status:
                    client = Client(
                        base_url='https://dav.jianguoyun.com/dav/',
                        auth=(webdav_account,webdav_password))
                    client.mkdir('/appdata_upload')
                    client.mkdir('/appdata_upload/%s-%s-%s-%s/' %(TESTER_CODE, ID, NAME, GENDER))
                    client.upload_file(
                        from_path='data\\%s-%s-%s-%s\\%s' %
                        (TESTER_CODE,ID,NAME,GENDER,data_filename),
                        to_path='/appdata_upload/%s-%s-%s-%s/%s' %
                        (TESTER_CODE,ID,NAME,GENDER,data_filename),
                        overwrite=True)
                else:
                    os.startfile(r'.\\data\\%s-%s-%s-%s\\%s' %
                        (TESTER_CODE, ID, NAME, GENDER, data_filename))
            if test_list[1] != -1:
                data_filename = 'Tab_V-Work_E_S-Test_Data-%s-%s-%s-%s-%s-%s-%s.csv' % (
                    TESTER_CODE, ID, NAME, GENDER, PERIOD, START_TIME, upload_time)
                data_record_df_II = pandas.DataFrame(
                    data_record_plus,
                    columns=[
                        'display_round_count',
                        'area_index',
                        'interval_start',
                        'interval_end',
                        'data_I',
                        'data_II',
                        'system_judge',
                        'user_judge',
                        'response_time'])
                data_record_df_II.to_csv(r'data\\%s-%s-%s-%s\\%s' %
                    (TESTER_CODE, ID, NAME, GENDER, data_filename), index=False)
                if webdav_status:
                    client = Client(
                        base_url='https://dav.jianguoyun.com/dav/',
                        auth=(webdav_account,webdav_password))
                    client.mkdir('/appdata_upload')
                    client.mkdir('/appdata_upload/%s-%s-%s-%s/' %(TESTER_CODE, ID, NAME, GENDER))
                    client.upload_file(
                        from_path='data\\%s-%s-%s-%s\\%s' %
                        (TESTER_CODE,ID,NAME,GENDER,data_filename),
                        to_path='/appdata_upload/%s-%s-%s-%s/%s' %
                        (TESTER_CODE,ID,NAME,GENDER,data_filename),
                        overwrite=True)
                else:
                    os.startfile(r'.\\data\\%s-%s-%s-%s\\%s' %
                        (TESTER_CODE, ID, NAME, GENDER, data_filename))
            if test_list[2] != -1:
                data_filename = 'Tab_VI-Work_O_NaS-Test_Data-%s-%s-%s-%s-%s-%s-%s.csv' % (
                    TESTER_CODE, ID, NAME, GENDER, PERIOD, START_TIME, upload_time)
                data_record_df_III = pandas.DataFrame(
                    data_record_III,
                    columns=[
                        'display_round_count',
                        'area_index',
                        'interval_start',
                        'interval_end',
                        'data_I',
                        'data_II',
                        'system_judge',
                        'user_judge',
                        'response_time'])
                data_record_df_III.to_csv(r'data\\%s-%s-%s-%s\\%s' %
                    (TESTER_CODE, ID, NAME, GENDER, data_filename), index=False)
                if webdav_status:
                    client = Client(
                        base_url='https://dav.jianguoyun.com/dav/',
                        auth=(webdav_account,webdav_password))
                    client.mkdir('/appdata_upload')
                    client.mkdir('/appdata_upload/%s-%s-%s-%s/' %(TESTER_CODE, ID, NAME, GENDER))
                    client.upload_file(
                        from_path='data\\%s-%s-%s-%s\\%s' %
                        (TESTER_CODE,ID,NAME,GENDER,data_filename),
                        to_path='/appdata_upload/%s-%s-%s-%s/%s' %
                        (TESTER_CODE,ID,NAME,GENDER,data_filename),
                        overwrite=True)
                else:
                    os.startfile(r'.\\data\\%s-%s-%s-%s\\%s' %
                        (TESTER_CODE, ID, NAME, GENDER, data_filename))
            if test_list[3] != -1:
                data_filename = 'Tab_VII-Work_E_NaS-Test_Data-%s-%s-%s-%s-%s-%s-%s.csv' % (
                    TESTER_CODE, ID, NAME, GENDER, PERIOD, START_TIME, upload_time)
                data_record_df_IV = pandas.DataFrame(
                    data_record_IV,
                    columns=[
                        'display_round_count',
                        'area_index',
                        'interval_start',
                        'interval_end',
                        'data_I',
                        'data_II',
                        'system_judge',
                        'user_judge',
                        'response_time'])
                data_record_df_IV.to_csv(r'data\\%s-%s-%s-%s\\%s' %
                    (TESTER_CODE, ID, NAME, GENDER, data_filename), index=False)
                if webdav_status:
                    client = Client(
                        base_url='https://dav.jianguoyun.com/dav/',
                        auth=(webdav_account,webdav_password))
                    client.mkdir('/appdata_upload')
                    client.mkdir('/appdata_upload/%s-%s-%s-%s/' %(TESTER_CODE, ID, NAME, GENDER))
                    client.upload_file(
                        from_path='data\\%s-%s-%s-%s\\%s' %
                        (TESTER_CODE,ID,NAME,GENDER,data_filename),
                        to_path='/appdata_upload/%s-%s-%s-%s/%s' %
                        (TESTER_CODE,ID,NAME,GENDER,data_filename),
                        overwrite=True)
                else:
                    os.startfile(r'.\\data\\%s-%s-%s-%s\\%s' %
                        (TESTER_CODE, ID, NAME, GENDER, data_filename))
            if mental_list[0] != -1:
                mental_filename = 'Tab_IV-Work_O_MS-Mental_Data-%s-%s-%s-%s-%s-%s-%s.csv' % (
                    TESTER_CODE, ID, NAME, GENDER, PERIOD, START_TIME, upload_time)
                mental_record_df = pandas.DataFrame(
                    situation_record,
                    columns=[
                        'display_round_count',
                        'situation_selected',
                        'response_time'])
                mental_record_df.to_csv(r'data\\%s-%s-%s-%s\\%s' %
                    (TESTER_CODE, ID, NAME, GENDER, mental_filename), index=False)
                if webdav_status:
                    client = Client(
                        base_url='https://dav.jianguoyun.com/dav/',
                        auth=(webdav_account,webdav_password))
                    client.mkdir('/appdata_upload')
                    client.mkdir('/appdata_upload/%s-%s-%s-%s/' %(TESTER_CODE, ID, NAME, GENDER))
                    client.upload_file(
                        from_path='data\\%s-%s-%s-%s\\%s' %
                        (TESTER_CODE,ID,NAME,GENDER,mental_filename),
                        to_path='/appdata_upload/%s-%s-%s-%s/%s' %
                        (TESTER_CODE,ID,NAME,GENDER,mental_filename),
                        overwrite=True)
                else:
                    os.startfile(r'.\\data\\%s-%s-%s-%s\\%s' %
                        (TESTER_CODE, ID, NAME, GENDER, mental_filename))
            if mental_list[1] != -1:
                mental_filename = 'Tab_V-Work_E_MS-Mental_Data-%s-%s-%s-%s-%s-%s-%s.csv' % (
                    TESTER_CODE, ID, NAME, GENDER, PERIOD, START_TIME, upload_time)
                mental_record_df = pandas.DataFrame(
                    situation_record_plus,
                    columns=[
                        'display_round_count',
                        'situation_selected',
                        'response_time'])
                mental_record_df.to_csv(r'data\\%s-%s-%s-%s\\%s' %
                    (TESTER_CODE, ID, NAME, GENDER, mental_filename), index=False)
                if webdav_status:
                    client = Client(
                        base_url='https://dav.jianguoyun.com/dav/',
                        auth=(webdav_account,webdav_password))
                    client.mkdir('/appdata_upload')
                    client.mkdir('/appdata_upload/%s-%s-%s-%s/' %(TESTER_CODE, ID, NAME, GENDER))
                    client.upload_file(
                        from_path='data\\%s-%s-%s-%s\\%s' %
                        (TESTER_CODE,ID,NAME,GENDER,mental_filename),
                        to_path='/appdata_upload/%s-%s-%s-%s/%s' %
                        (TESTER_CODE,ID,NAME,GENDER,mental_filename),
                        overwrite=True)
                else:
                    os.startfile(r'.\\data\\%s-%s-%s-%s\\%s' %
                        (TESTER_CODE, ID, NAME, GENDER, mental_filename))
            if mental_list[2] != -1:
                mental_filename = 'Tab_VI-Work_O_SS-Mental_Data-%s-%s-%s-%s-%s-%s-%s.csv' % (
                    TESTER_CODE, ID, NAME, GENDER, PERIOD, START_TIME, upload_time)
                mental_record_df = pandas.DataFrame(
                    situation_record_III,
                    columns=[
                        'display_round_count',
                        'situation_selected',
                        'response_time'])
                mental_record_df.to_csv(r'data\\%s-%s-%s-%s\\%s' %
                    (TESTER_CODE, ID, NAME, GENDER, mental_filename), index=False)
                if webdav_status:
                    client = Client(
                        base_url='https://dav.jianguoyun.com/dav/',
                        auth=(webdav_account,webdav_password))
                    client.mkdir('/appdata_upload')
                    client.mkdir('/appdata_upload/%s-%s-%s-%s/' %(TESTER_CODE, ID, NAME, GENDER))
                    client.upload_file(
                        from_path='data\\%s-%s-%s-%s\\%s' %
                        (TESTER_CODE,ID,NAME,GENDER,mental_filename),
                        to_path='/appdata_upload/%s-%s-%s-%s/%s' %
                        (TESTER_CODE,ID,NAME,GENDER,mental_filename),
                        overwrite=True)
                else:
                    os.startfile(r'.\\data\\%s-%s-%s-%s\\%s' %
                        (TESTER_CODE, ID, NAME, GENDER, mental_filename))
            if mental_list[3] != -1:
                mental_filename = 'Tab_VII-Work_E_SS-Mental_Data-%s-%s-%s-%s-%s-%s-%s.csv' % (
                    TESTER_CODE, ID, NAME, GENDER, PERIOD, START_TIME, upload_time)
                mental_record_df = pandas.DataFrame(
                    situation_record_IV,
                    columns=[
                        'display_round_count',
                        'situation_selected',
                        'response_time'])
                mental_record_df.to_csv(r'data\\%s-%s-%s-%s\\%s' %
                    (TESTER_CODE, ID, NAME, GENDER, mental_filename), index=False)
                if webdav_status:
                    client = Client(
                        base_url='https://dav.jianguoyun.com/dav/',
                        auth=(webdav_account,webdav_password))
                    client.mkdir('/appdata_upload')
                    client.mkdir('/appdata_upload/%s-%s-%s-%s/' %(TESTER_CODE, ID, NAME, GENDER))
                    client.upload_file(
                        from_path='data\\%s-%s-%s-%s\\%s' %
                        (TESTER_CODE,ID,NAME,GENDER,mental_filename),
                        to_path='/appdata_upload/%s-%s-%s-%s/%s' %
                        (TESTER_CODE,ID,NAME,GENDER,mental_filename),
                        overwrite=True)
                else:
                    os.startfile(r'.\\data\\%s-%s-%s-%s\\%s' %
                        (TESTER_CODE, ID, NAME, GENDER, mental_filename))
        info_text = '''程序端 管理组件 - 全程数据管理实现说明：
1. 模拟作业及自测量表抽测数据将先以数字形式呈现其维度，数字顺序等效于选项卡顺序，显示 -1 则表示未检测到此选项卡测试数据。\n
点击 <确定> 键后将在弹出窗口中呈现被试数据。'''
        tkinter.messagebox.showinfo(title='系统端提示', message=info_text)
        global upload_root
        logging.info('Creating app upload_root window')
        upload_root = tkinter.Toplevel(root)
        upload_root.title('被试端 全程数据管理系统')
        upload_root.geometry('600x400')
        upload_root.minsize(600, 400)
        upload_root.maxsize(600, 400)
        upload_root.resizable(False, False)
        if top_window_status:
            upload_root.wm_attributes('-topmost', 1)
        upload_root.tk.call(
            'wm', 'iconphoto', upload_root._w, tkinter.PhotoImage(
                file='.\\icons\\ic_public_storage.png'))
        tkinter.Label(
            upload_root,
            text='呈现数据仅在统计时间 %s 前有效，与实际导出数据会存在些许偏差' %
            time.strftime('%Y%m%d-%H%M%S',time.localtime()),
            font=('HarmonyOS Sans SC',8)).place(x=160,y=50)
        try:
            TESTER_CODE, ID, NAME, GENDER
        except NameError:
            tkinter.Label(
                upload_root,
                text='未检测到被试者信息！',
                font=('HarmonyOS Sans SC',12,'bold')).place(x=20,y=20)
        else:
            tkinter.Label(
                upload_root, text='被试者：%s - %s - %s - %s - %s -  %s' %
                (TESTER_CODE, ID, NAME, GENDER, PERIOD, START_TIME), font=(
                    'HarmonyOS Sans SC', 11, 'bold')).place(x=20, y=20)
            tkinter.Label(
                upload_root,
                text='-O-MS               -E-MS               -O-SS               -E-SS',
                font=('HarmonyOS Sans SC',8)).place(x=180,y=90)
            tkinter.Label(
                upload_root,
                text='警戒测试过程记录：',
                font=('HarmonyOS Sans SC',10)).place(x=40,y=120)
            tkinter.Label(
                upload_root,
                text='心理特征量表抽测：',
                font=('HarmonyOS Sans SC',10)).place(x=40,y=160)
            tkinter.Label(
                upload_root,
                text='程序日志文件备份：',
                font=('HarmonyOS Sans SC',10)).place(x=40,y=200)
            test_data_I = tkinter.Label(upload_root, text='', font=('HarmonyOS Sans SC', 10))
            test_data_I.place(x=180, y=120)
            test_data_II = tkinter.Label(upload_root, text='', font=('HarmonyOS Sans SC', 10))
            test_data_II.place(x=260, y=120)
            test_data_III = tkinter.Label(upload_root, text='', font=('HarmonyOS Sans SC', 10))
            test_data_III.place(x=340, y=120)
            test_data_IV = tkinter.Label(upload_root, text='', font=('HarmonyOS Sans SC', 10))
            test_data_IV.place(x=420, y=120)
            mental_data_I = tkinter.Label(upload_root, text='', font=('HarmonyOS Sans SC', 10))
            mental_data_I.place(x=180, y=160)
            mental_data_II = tkinter.Label(upload_root, text='', font=('HarmonyOS Sans SC', 10))
            mental_data_II.place(x=260, y=160)
            mental_data_III = tkinter.Label(upload_root, text='', font=('HarmonyOS Sans SC', 10))
            mental_data_III.place(x=340, y=160)
            mental_data_IV = tkinter.Label(upload_root, text='', font=('HarmonyOS Sans SC', 10))
            mental_data_IV.place(x=420, y=160)
            log_data = tkinter.Label(upload_root, text='', font=('HarmonyOS Sans SC', 10))
            log_data.place(x=180, y=200)
            test_list = []
            mental_list = []
            try:
                data_record
            except NameError:
                test_list.append(-1)
            else:
                test_list.append(len(data_record))
            try:
                data_record_plus
            except NameError:
                test_list.append(-1)
            else:
                test_list.append(len(data_record_plus))
            try:
                data_record_III
            except NameError:
                test_list.append(-1)
            else:
                test_list.append(len(data_record_III))
            try:
                data_record_IV
            except NameError:
                test_list.append(-1)
            else:
                test_list.append(len(data_record_IV))
            try:
                situation_record
            except NameError:
                mental_list.append(-1)
            else:
                mental_list.append(len(situation_record))
            try:
                situation_record_plus
            except NameError:
                mental_list.append(-1)
            else:
                mental_list.append(len(situation_record_plus))
            try:
                situation_record_III
            except NameError:
                mental_list.append(-1)
            else:
                mental_list.append(len(situation_record_III))
            try:
                situation_record_IV
            except NameError:
                mental_list.append(-1)
            else:
                mental_list.append(len(situation_record_IV))
            test_data_I.configure(text=str(test_list[0]))
            test_data_II.configure(text=str(test_list[1]))
            test_data_III.configure(text=str(test_list[2]))
            test_data_IV.configure(text=str(test_list[3]))
            mental_data_I.configure(text=str(mental_list[0]))
            mental_data_II.configure(text=str(mental_list[1]))
            mental_data_III.configure(text=str(mental_list[2]))
            mental_data_IV.configure(text=str(mental_list[3]))
            log_data.configure(text=log_file_name)
            data_file_submit = tkinter.Button(upload_root, width=14, text='打开数据文件夹', font=(
                'HarmonyOS Sans SC', 10), command=lambda: os.system('start %s'%local_filepath))
            data_file_submit.place(x=40, y=250)
            log_file_submit = tkinter.Button(upload_root, width=14, text='打开日志文件夹', font=(
                'HarmonyOS Sans SC', 10), command=lambda: os.system('start .\\logs'))
            log_file_submit.place(x=180, y=250)
            data_upload_plus_submit = tkinter.Button(
                upload_root, width=14, text='数据上传', font=(
                    'HarmonyOS Sans SC', 10), command=data_upload_overall)
            data_upload_plus_submit.place(x=320, y=250)
            tkinter.Label(
                upload_root,
                text='实现说明：',
                font=('HarmonyOS Sans SC',10)).place(x=20,y=300)
            tkinter.Label(
                upload_root,
                text='1. 为获得最佳显示效果，数据及日志文件夹下的文件建议使用 Notepad3 等软件打开。',
                font=('HarmonyOS Sans SC',8)).place(x=40,y=330)
            tkinter.Label(
                upload_root,
                text='2. <数据上传> 将会在 WebDAV 端生成以 <被试标识码> 为名字的文件夹并覆盖上传所有数据文件。',
                font=('HarmonyOS Sans SC',8)).place(x=40,y=360)
        upload_root.mainloop()
    def filepath_display():
        info_text = '''程序端 管理组件 - 本地同步路径实现说明：
1. 在 Windows 系统下，使用坚果云软件环境下的 <本地同步路径> 一般位于 C:\\Users\\<你的用户名>\\Nutstore\\1\\ 路径下。
2. 请注意，进入此路径需打开 <显示隐藏的项目> 选项。\n
点击 <确定> 键后将弹出文件夹选择窗口。'''
        tkinter.messagebox.showinfo(title='系统端提示', message=info_text)
        path = tkinter.filedialog.askdirectory()
        if path == "":
            file_path_string.get()
        else:
            path_ = path.replace("/", "\\")
            file_path_string.set(path)
    def watchdog_display():
        class ConsoleWindow:
            def __init__(self, master):
                self.master = master
                self.text = tkinter.Text(
                    master,
                    font=('HarmonyOS Sans SC',10),
                    height=21,
                    width=126,
                    wrap="none")
                self.text.pack(anchor='center')
            def write(self, message):
                self.text.insert(tkinter.END, message)
            def flush(self):
                pass
        class MyHandler(FileSystemEventHandler):
            def on_modified(self, event):
                if event.is_directory:
                    return
                logging.info(f'File {event.src_path} has been modified')
                print(f'文件 {event.src_path} 被修改\n')
        def watchdog_start():
            logging.info('Starting the WatchDog monitor')
            observer = Observer()
            observer.schedule(event_handler, local_filepath, recursive=True)
            observer.start()
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                observer.stop()
            observer.join()
        info_text = '''程序端 管理组件 - 数据上传监控实现说明：
1. 在程序未设置 WebDAV <组件状态>或 WebDAV <本地同步路径>时，将监控程序源代码下的数据文件夹。
2. 在程序已设置 WebDAV <组件状态>时，将监控 WebDAV <本地同步路径>的文件变化，此时可等效于云端数据变化。\n
点击 <确定> 键后将开始数据监控。'''
        tkinter.messagebox.showinfo(title='系统端提示', message=info_text)
        global watchdog_root
        logging.info('Creating app watchdog_root window')
        watchdog_root = tkinter.Toplevel(root)
        watchdog_root.title('程序端 管理组件 - 数据上传监控系统')
        watchdog_root.geometry('900x400')
        watchdog_root.minsize(900, 400)
        watchdog_root.maxsize(900, 400)
        watchdog_root.resizable(False, False)
        if top_window_status:
            watchdog_root.wm_attributes('-topmost', 1)
        watchdog_root.tk.call(
            'wm', 'iconphoto', watchdog_root._w, tkinter.PhotoImage(
                file='.\\icons\\ic_gallery_cloud_synchronization.png'))
        console = ConsoleWindow(watchdog_root)
        print = console.write
        event_handler = MyHandler()
        logging.info('WatchDog monitor path: %s' % local_filepath)
        print('系统端提示 - 当前监控路径为：%s\n\n' % local_filepath)
        watchdog_thread = threading.Thread(target=watchdog_start)
        watchdog_thread.daemon = True
        watchdog_thread.start()
        watchdog_root.mainloop()
    def root_destroy_dev():
        info_text = '''程序端 管理组件 - 强制退出程序实现说明：
1. 使用此控件将会结束程序主窗口及所有附属功能窗口。
2. 请注意，此功能实现时将不会主动保存数据文件。\n\n 点击 <是> 键后将退出程序。'''
        resp = tkinter.messagebox.askyesno(title='系统端提示', message=info_text)
        if resp:
            logging.info('Exiting the root window')
            root.destroy()
            try:
                watchdog_root.destroy()
            except NameError:
                pass
            else:
                logging.info('Exiting the watchdog_root window')
                watchdog_root.destroy()
            try:
                upload_root.destroy()
            except NameError:
                pass
            else:
                logging.info('Exiting the upload_root window')
                upload_root.destroy()
            try:
                keyboard_root.destroy()
            except NameError:
                pass
            else:
                logging.info('Exiting the keyboard_root window')
                keyboard_root.destroy()
            try:
                data_analyze_root.destroy()
            except NameError:
                pass
            else:
                logging.info('Exiting the data_analyze_root window')
                data_analyze_root.destroy()
    def log_filepath_display():
        info_text = '''程序端 管理组件 - 打开程序日志文件夹实现说明：
1. 使用此控件将会通过文件资源管理器打开程序路径下的日志文件夹。
2. 为确保显示效果，建议使用 Notepad3 等软件打开日志文件。\n\n 点击 <确定> 键后将打开日志文件夹。'''
        tkinter.messagebox.showinfo(title='系统端提示', message=info_text)
        logging.info('Opening the app logs folder')
        os.system('start .\\logs')
    def keyboard_display():
        def keyboard_commit_I(index, name):
            def key_feedback(event):
                global keyname
                keyname = event.keysym
                if event.keysym == '??':
                    keyboard_check.configure(text='键盘输入检查：你当前输入键位为 [ 未知键位 ] ，请检查中英文切换状态或重新输入。')
                else:
                    keyboard_check.configure(text='键盘输入反馈：你当前输入键位为 [ %s ] ，如果正确请按下确认键。'%event.keysym)
            def next_display():
                if keyname == '' or keyname == '??':
                    tkinter.messagebox.showerror(title='系统端提示', message='请先输入键位并确认后再进行下一步操作。')
                else:
                    winsound.Beep(3000, 300)
                    if index <= 3:
                        keyboard_list.append(keyname)
                    else:
                        if keyname == 'Escape':
                            keyboard_list_opt.append('null')
                        else:
                            keyboard_list_opt.append(keyname)
                    if index == 7:
                        keyboard_submit.configure(state='normal')
                        keyboard_next.configure(state='disabled')
                        keyboard_check.configure(text='键盘输入检查：你已完成全部键位设置，请点击 [ 提交全部键位更改 ] 键进行确认。')
                        keyboard_feedback.configure(text='键位设置反馈：当前设置如下，主选键位设置，%s'%keyboard_list)
                        keyboard_feedback_opt.configure(text='键位设置反馈：当前设置如下，可选键位设置，%s'%keyboard_list_opt)
                    else:
                        keyboard_commit_I(index+1, next_list[index+1])
            def keyboard_submit_all():
                keyboard_preference_I = keyboard_list[0]
                keyboard_preference_II = keyboard_list[1]
                keyboard_preference_III = keyboard_list[2]
                keyboard_preference_IV = keyboard_list[3]
                keyboard_preference_opt_I = keyboard_list_opt[0]
                keyboard_preference_opt_II = keyboard_list_opt[1]
                keyboard_preference_opt_III = keyboard_list_opt[2]
                keyboard_preference_opt_IV = keyboard_list_opt[3]
                storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
                    (keyboard_preference_I, 'keyboard_preference_I'))
                storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
                    (keyboard_preference_II, 'keyboard_preference_II'))
                storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
                    (keyboard_preference_III, 'keyboard_preference_III'))
                storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
                    (keyboard_preference_IV, 'keyboard_preference_IV'))
                storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
                    (keyboard_preference_opt_I, 'keyboard_preference_opt_I'))
                storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
                    (keyboard_preference_opt_II, 'keyboard_preference_opt_II'))
                storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
                    (keyboard_preference_opt_III, 'keyboard_preference_opt_III'))
                storage_db_cursor.execute('''UPDATE options SET setting = "%s" WHERE key = "%s"''' %
                    (keyboard_preference_opt_IV, 'keyboard_preference_opt_IV'))
                storage_db_connect.commit()
                logging.info('Configuration Update keyboard_preference_I: %s' % keyboard_preference_I)
                logging.info('Configuration Update keyboard_preference_II: %s' % keyboard_preference_II)
                logging.info('Configuration Update keyboard_preference_III: %s' % keyboard_preference_III)
                logging.info('Configuration Update keyboard_preference_IV: %s' % keyboard_preference_IV)
                logging.info('Configuration Update keyboard_preference_opt_I: %s' % keyboard_preference_opt_I)
                logging.info('Configuration Update keyboard_preference_opt_II: %s' % keyboard_preference_opt_II)
                logging.info('Configuration Update keyboard_preference_opt_III: %s' % keyboard_preference_opt_III)
                logging.info('Configuration Update keyboard_preference_opt_IV: %s' % keyboard_preference_opt_IV)
                tkinter.messagebox.showinfo(title='系统端提示', message='键位设置更改完成，将在下次启动时完全生效。')
                logging.info('Exiting the keyboard_root window')
                keyboard_root.destroy()
            dashboard_item.configure(text='请提交 [ %s ] 的 [ %s ] 键位：'%(name, next_status[index]))
            if next_status[index] == '可选':
                dashboard_tip.configure(text='Tips：当处于 [ 可选 ] 状态时，按下 [ Esc 键 ] 可以跳过此项设置。')
            key_press = tkinter.Label(keyboard_root, text='', font=('HarmonyOS Sans SC',10))
            key_press.focus_set()
            key_press.place(x=200, y=300)
            key_press.bind("<Key>", key_feedback)
            keyboard_next.configure(command=next_display)
            keyboard_submit.configure(command=keyboard_submit_all)
        info_text = '''程序端 管理组件 - 键盘交互设置实现说明：
1. 为确保在长时间测试过程中被试人员有更好的使用体验，我们设计了这个功能来调整相关键位设置。
2. 此页面的相关设置将会在下次启动时生效并作用于所有模拟测试标签页面。
3. 主选键位与可选键位的存在是为了调节大小写模式下获得一致的键位输入效果，请根据提示进行设置。
4. 请注意，不建议在没有相关使用经验的情况下随意调整此项目设置。\n\n 点击 <确定> 键后将打开键盘交互设置页面。'''
        tkinter.messagebox.showinfo(title='系统端提示', message=info_text)
        next_list = ['DashBoard_I 左上', 'DashBoard_II - 右上', 'DashBoard_III - 左下', 'DashBoard_IV - 右下', 'DashBoard_I 左上', 'DashBoard_II - 右上', 'DashBoard_III - 左下', 'DashBoard_IV - 右下']
        next_status = ['主选', '主选', '主选', '主选', '可选', '可选', '可选', '可选']
        keyboard_list = []
        keyboard_list_opt = []
        global keyboard_root
        logging.info('Creating app keyboard_root window')
        keyboard_root = tkinter.Toplevel(root)
        keyboard_root.title('程序端 键盘交互设置')
        keyboard_root.geometry('600x400')
        keyboard_root.minsize(600, 400)
        keyboard_root.maxsize(600, 400)
        keyboard_root.resizable(False, False)
        if top_window_status:
            keyboard_root.wm_attributes('-topmost', 1)
        keyboard_root.tk.call(
            'wm', 'iconphoto', keyboard_root._w, tkinter.PhotoImage(
                file='.\\icons\\ic_public_settings_filled.png'))
        tkinter.Label(keyboard_root, text='当前键位设置', font=('HarmonyOS Sans SC',12,'bold')).place(x=20,y=20)
        tkinter.Label(keyboard_root, text='（显示格式：主选键位 | 可选键位）', font=('HarmonyOS Sans SC',8)).place(x=140,y=25)
        tkinter.Label(keyboard_root, text='DashBoard_I - 左上：%s | %s'%(keyboard_preference_I, keyboard_preference_opt_I), font=('HarmonyOS Sans SC',10)).place(x=20,y=60)
        tkinter.Label(keyboard_root, text='DashBoard_II - 右上：%s | %s'%(keyboard_preference_II, keyboard_preference_opt_II), font=('HarmonyOS Sans SC',10)).place(x=280,y=60)
        tkinter.Label(keyboard_root, text='DashBoard_III - 左下：%s | %s'%(keyboard_preference_III, keyboard_preference_opt_III), font=('HarmonyOS Sans SC',10)).place(x=20,y=90)
        tkinter.Label(keyboard_root, text='DashBoard_IV - 右下：%s | %s'%(keyboard_preference_IV, keyboard_preference_opt_IV), font=('HarmonyOS Sans SC',10)).place(x=280,y=90)
        tkinter.Label(keyboard_root, text='更改键位设置', font=('HarmonyOS Sans SC',12,'bold')).place(x=20,y=130)
        tkinter.Label(keyboard_root, text='（根据对应显示的面板编号，提供新的键位名称，以最后一次提交的为准）', font=('HarmonyOS Sans SC',8)).place(x=140,y=135)
        dashboard_item = tkinter.Label(keyboard_root, text='', font=('HarmonyOS Sans SC',10))
        dashboard_item.place(x=20,y=170)
        dashboard_tip = tkinter.Label(keyboard_root, text='', font=('HarmonyOS Sans SC',10))
        dashboard_tip.place(x=20,y=200)
        keyboard_check = tkinter.Label(keyboard_root, text='', font=('HarmonyOS Sans SC',10,'bold'))
        keyboard_check.place(x=20,y=260)
        keyboard_feedback = tkinter.Label(keyboard_root, text='', font=('HarmonyOS Sans SC',10))
        keyboard_feedback.place(x=20,y=290)
        keyboard_feedback_opt = tkinter.Label(keyboard_root, text='', font=('HarmonyOS Sans SC',10))
        keyboard_feedback_opt.place(x=20,y=320)
        keyboard_next = tkinter.Button(keyboard_root, width=18, text='确认此项键位更改', font=('HarmonyOS Sans SC',8))
        keyboard_next.place(x=20,y=360)
        keyboard_submit = tkinter.Button(keyboard_root, width=18, text='提交全部键位更改', font=('HarmonyOS Sans SC',8), state='disabled')
        keyboard_submit.place(x=150,y=360)
        keyboard_commit_I(0, next_list[0])
        keyboard_root.mainloop()
    def data_analyze_display():
        def tester_confirm():
            selected_tester_file = tester_combobox.get()
            data_list = []
            data_filepath = os.path.join(local_filepath, selected_tester_file)
            for item in os.scandir(data_filepath):
                if item.is_file():
                    if 'Test_Data' in item.name:
                        data_list.append(item.name)
            data_combobox.configure(values=data_list)
            data_combobox.set('请选择具体测试项目信息')
            data_submit.configure(state='normal')
        def data_analyze():
            def data_export_display():
                data_template = pd.read_csv(r'./data/data_template.csv')
                data_template.set_index('序号', inplace=True)
                #pprint(data_template)
                #if record_line[0] == '第一轮测试':
                    #data_template.at[]
            data_export_submit.configure(state='normal', command=data_export_display)
            mental_dict = {0:'完全警觉，完全清醒', 1:'很有活力，反应灵敏，但非最好状态', 2:'情况一般，稍微清醒', 3:'有点累，不怎么清醒', 4:'挺累的，无精打采', 5:'非常疲惫，难以集中精神', 6:'精疲力尽，无法有效地工作'}
            selected_tester_file = tester_combobox.get()
            selected_data_file = data_combobox.get()
            data_filepath = os.path.join(local_filepath, selected_tester_file)
            test_data_file = os.path.join(data_filepath, selected_data_file)
            test_data_df = pandas.read_csv(test_data_file)
            test_data_df = test_data_df.fillna('null')
            try:
                mental_data_file = os.path.join(data_filepath, selected_data_file.replace('Test_Data', 'Mental_Data'))
                mental_data_df = pandas.read_csv(mental_data_file)
            except FileNotFoundError:
                mental_status = False
            else:
                mental_status = True
                mental_data_file = os.path.join(data_filepath, selected_data_file.replace('Test_Data', 'Mental_Data'))
                mental_data_df = pandas.read_csv(mental_data_file)
                mental_data_df = mental_data_df.fillna('null')
            test_data_table = tkinter.ttk.Treeview(data_analyze_root, show='headings')
            test_data_table['columns'] = ('显示轮次', '区域编码', '区间起点', '区间终点', '数字对_A', '数字对_B', '系统判定', '被试判定', '反应时间')
            test_data_table.column('显示轮次', width=60, minwidth=60)
            test_data_table.column('区域编码', width=120, minwidth=120)
            test_data_table.column('区间起点', width=65, minwidth=65)
            test_data_table.column('区间终点', width=65, minwidth=65)
            test_data_table.column('数字对_A', width=65, minwidth=65)
            test_data_table.column('数字对_B', width=65, minwidth=65)
            test_data_table.column('系统判定', width=65, minwidth=65)
            test_data_table.column('被试判定', width=80, minwidth=80)
            test_data_table.column('反应时间', width=60, minwidth=60)
            test_data_table.heading('显示轮次', text='显示轮次')
            test_data_table.heading('区域编码', text='区域编码')
            test_data_table.heading('区间起点', text='区间起点')
            test_data_table.heading('区间终点', text='区间终点')
            test_data_table.heading('数字对_A', text='数字对_A')
            test_data_table.heading('数字对_B', text='数字对_B')
            test_data_table.heading('系统判定', text='系统判定')
            test_data_table.heading('被试判定', text='被试判定')
            test_data_table.heading('反应时间', text='反应时间')
            for index in range(len(test_data_df)):
                test_data_table.insert('', tkinter.END, values=(test_data_df.at[index, 'display_round_count'], test_data_df.at[index, 'area_index'], test_data_df.at[index, 'interval_start'], test_data_df.at[index, 'interval_end'], test_data_df.at[index, 'data_I'], test_data_df.at[index, 'data_II'], test_data_df.at[index, 'system_judge'], test_data_df.at[index, 'user_judge'], test_data_df.at[index, 'response_time']))
            vertical_scrollbar = tkinter.ttk.Scrollbar(data_analyze_root, orient=tkinter.VERTICAL, command=test_data_table.yview)
            test_data_table.configure(yscrollcommand=vertical_scrollbar.set)
            test_data_table.place(x=20, y=180, height=140, width=650)
            vertical_scrollbar.place(x=670, y=180, height=140, width=10)
            if mental_status:
                mental_data_table = tkinter.ttk.Treeview(data_analyze_root, show='headings')
                mental_data_table['columns'] = ('显示轮次', '被试状态', '反应时间')
                mental_data_table.column('显示轮次', width=55, minwidth=55)
                mental_data_table.column('被试状态', width=150, minwidth=150)
                mental_data_table.column('反应时间', width=55, minwidth=55)
                mental_data_table.heading('显示轮次', text='显示轮次')
                mental_data_table.heading('被试状态', text='被试状态')
                mental_data_table.heading('反应时间', text='反应时间')
                for index in range(len(mental_data_df)):
                    mental_data_table.insert('', tkinter.END, values=(mental_data_df.at[index, 'display_round_count'], mental_dict[mental_data_df.at[index, 'situation_selected']], mental_data_df.at[index, 'response_time']))
                vertical_scrollbar = tkinter.ttk.Scrollbar(data_analyze_root, orient=tkinter.VERTICAL, command=mental_data_table.yview)
                mental_data_table.configure(yscrollcommand=vertical_scrollbar.set)
                mental_data_table.place(x=700, y=180, height=140, width=300)
                vertical_scrollbar.place(x=1000, y=180, height=140, width=10)
            name_spilt = selected_data_file.split('-')
            emer_status = 'E' in name_spilt[1] and test_data_df[(test_data_df['area_index'] == 'DashBoard_Emergency') & (test_data_df['system_judge'] == True)].count()[0] != 0
            mental_category = 'Multi' if 'MS' in name_spilt[1] else 'Single'
            tkinter.Label(data_analyze_root, text='测试项目编码：%s        '%(name_spilt[0]+'-'+name_spilt[1]), font=('HarmonyOS Sans SC',10)).place(x=20,y=380)
            tkinter.Label(data_analyze_root, text='包含状态量表：%s        '%(str(mental_status)+'-'+mental_category), font=('HarmonyOS Sans SC',10)).place(x=20,y=410)
            tkinter.Label(data_analyze_root, text='包含突发事件：%s        '%emer_status, font=('HarmonyOS Sans SC',10)).place(x=20,y=440)
            tkinter.Label(data_analyze_root, text='被试人员序列：%s        '%name_spilt[3], font=('HarmonyOS Sans SC',10)).place(x=20,y=470)
            tkinter.Label(data_analyze_root, text='被试人员工号：%s        '%name_spilt[4], font=('HarmonyOS Sans SC',10)).place(x=20,y=500)
            tkinter.Label(data_analyze_root, text='被试人员姓名：%s        '%name_spilt[5], font=('HarmonyOS Sans SC',10)).place(x=20,y=530)
            tkinter.Label(data_analyze_root, text='被试人员性别：%s        '%name_spilt[6], font=('HarmonyOS Sans SC',10)).place(x=20,y=560)
            tkinter.Label(data_analyze_root, text='测试阶段性质：%s        '%name_spilt[7], font=('HarmonyOS Sans SC',10)).place(x=20,y=590)
            tkinter.Label(data_analyze_root, text='测试开始时间：%s        '%(name_spilt[8]+'-'+name_spilt[9]), font=('HarmonyOS Sans SC',10)).place(x=20,y=620)
            tkinter.Label(data_analyze_root, text='数据上传时间：%s        '%name_spilt[10][:-4], font=('HarmonyOS Sans SC',10)).place(x=20,y=650)
            tkinter.Label(data_analyze_root, text='总事件数：%s        '%test_data_df.shape[0], font=('HarmonyOS Sans SC',10)).place(x=250,y=380)
            tkinter.Label(data_analyze_root, text='总事件回合数：%s        '%test_data_df['display_round_count'].max(), font=('HarmonyOS Sans SC',10)).place(x=250,y=410)
            tkinter.Label(data_analyze_root, text='总异常事件数：%s / %.2f%%        '%(test_data_df[(test_data_df['system_judge'] == True) & (test_data_df['area_index'] != 'DashBoard_Emergency')].count()[0], test_data_df[(test_data_df['system_judge'] == True) & (test_data_df['area_index'] != 'DashBoard_Emergency')].count()[0]/test_data_df.shape[0]*100), font=('HarmonyOS Sans SC',10)).place(x=250,y=440)
            tkinter.Label(data_analyze_root, text='总正常事件数：%s / %.2f%%        '%(test_data_df['system_judge'][test_data_df['system_judge'] == False].count(), test_data_df['system_judge'][test_data_df['system_judge'] == False].count()/test_data_df.shape[0]*100), font=('HarmonyOS Sans SC',10)).place(x=250,y=470)
            tkinter.Label(data_analyze_root, text='总突发事件数：%s / %.2f%%        '%(test_data_df[(test_data_df['area_index'] == 'DashBoard_Emergency') & (test_data_df['system_judge'] == True)].count()[0], test_data_df[(test_data_df['area_index'] == 'DashBoard_Emergency') & (test_data_df['system_judge'] == True)].count()[0]/test_data_df.shape[0]*100), font=('HarmonyOS Sans SC',10)).place(x=250,y=500)
            tkinter.Label(data_analyze_root, text='被试反应总数：%s        '%test_data_df['response_time'][test_data_df['response_time'] != 'null'].count(), font=('HarmonyOS Sans SC',10)).place(x=250,y=530)
            tkinter.Label(data_analyze_root, text='被试正确捕捉异常总数：%s / %.2f%%        '%(test_data_df[(test_data_df['user_judge'] == 'Hit') & (test_data_df['area_index'] != 'DashBoard_Emergency')].count()[0], test_data_df[(test_data_df['user_judge'] == 'Hit') & (test_data_df['area_index'] != 'DashBoard_Emergency')].count()[0]/test_data_df[(test_data_df['system_judge'] == True) & (test_data_df['area_index'] != 'DashBoard_Emergency')].count()[0]*100), font=('HarmonyOS Sans SC',10)).place(x=250,y=560)
            tkinter.Label(data_analyze_root, text='被试正确捕捉突发总数：%s / %.2f%%        '%(test_data_df[(test_data_df['user_judge'] == 'Hit') & (test_data_df['area_index'] == 'DashBoard_Emergency')].count()[0], test_data_df[(test_data_df['user_judge'] == 'Hit') & (test_data_df['area_index'] == 'DashBoard_Emergency')].count()[0]/test_data_df[(test_data_df['area_index'] == 'DashBoard_Emergency') & (test_data_df['system_judge'] == True)].count()[0]*100), font=('HarmonyOS Sans SC',10)).place(x=250,y=590)
            tkinter.Label(data_analyze_root, text='被试错误捕捉异常总数：%s / %.2f%%        '%(test_data_df[(test_data_df['user_judge'] == 'Wrong') & (test_data_df['area_index'] != 'DashBoard_Emergency')].count()[0], test_data_df[(test_data_df['user_judge'] == 'Wrong') & (test_data_df['area_index'] != 'DashBoard_Emergency')].count()[0]/(test_data_df[(test_data_df['user_judge'] == 'Wrong') & (test_data_df['area_index'] != 'DashBoard_Emergency')].count()[0]+test_data_df[(test_data_df['user_judge'] == 'Hit') & (test_data_df['area_index'] != 'DashBoard_Emergency')].count()[0])*100), font=('HarmonyOS Sans SC',10)).place(x=250,y=620)
            tkinter.Label(data_analyze_root, text='被试错误捕捉突发总数：%s / %.2f%%        '%(test_data_df[(test_data_df['user_judge'] == 'Wrong') & (test_data_df['area_index'] == 'DashBoard_Emergency')].count()[0], test_data_df[(test_data_df['user_judge'] == 'Wrong') & (test_data_df['area_index'] == 'DashBoard_Emergency')].count()[0]/(test_data_df[(test_data_df['user_judge'] == 'Wrong') & (test_data_df['area_index'] == 'DashBoard_Emergency')].count()[0]+test_data_df[(test_data_df['user_judge'] == 'Hit') & (test_data_df['area_index'] == 'DashBoard_Emergency')].count()[0])*100), font=('HarmonyOS Sans SC',10)).place(x=250,y=650)
            tkinter.Label(data_analyze_root, text='被试遗漏捕捉异常总数：%s / %.2f%%        '%(test_data_df[(test_data_df['user_judge'] == 'Missed') & (test_data_df['area_index'] != 'DashBoard_Emergency')].count()[0], test_data_df[(test_data_df['user_judge'] == 'Missed') & (test_data_df['area_index'] != 'DashBoard_Emergency')].count()[0]/test_data_df[(test_data_df['system_judge'] == True) & (test_data_df['area_index'] != 'DashBoard_Emergency')].count()[0]*100), font=('HarmonyOS Sans SC',10)).place(x=250,y=680)
            tkinter.Label(data_analyze_root, text='被试遗漏捕捉突发总数：%s / %.2f%%        '%(test_data_df[(test_data_df['user_judge'] == 'Missed') & (test_data_df['area_index'] == 'DashBoard_Emergency')].count()[0], test_data_df[(test_data_df['user_judge'] == 'Missed') & (test_data_df['area_index'] == 'DashBoard_Emergency')].count()[0]/test_data_df[(test_data_df['area_index'] == 'DashBoard_Emergency') & (test_data_df['system_judge'] == True)].count()[0]*100), font=('HarmonyOS Sans SC',10)).place(x=250,y=710)
            catch_exce_rate = []
            catch_exce_time = []
            catch_emer_rate = []
            catch_emer_time = []
            forg_exce_rate = []
            forg_emer_rate = []
            miss_exce_rate = []
            miss_emer_rate = []
            record_1007 = '%s,'%(name_spilt[3]+'-'+name_spilt[5]+'-'+name_spilt[7])
            #PERIOD_ANA_NUM = 10
            PERIOD_ANA_NUM = test_data_df['display_round_count'].max() * 4 // 60 // 5
            catch_exce_time_mean = test_data_df[(test_data_df['user_judge'] == 'Hit') & (test_data_df['area_index'] != 'DashBoard_Emergency')]['response_time'].mean()
            catch_emer_time_mean = test_data_df[(test_data_df['user_judge'] == 'Hit') & (test_data_df['area_index'] == 'DashBoard_Emergency')]['response_time'].mean()
            round_length = test_data_df.shape[0] // PERIOD_ANA_NUM + 1
            for i in range(PERIOD_ANA_NUM):
                data_round = test_data_df[(test_data_df.index>=round_length*i) & (test_data_df.index<round_length*(i+1))]
                catch_exce_rate.append(data_round[(data_round['user_judge'] == 'Hit') & (data_round['area_index'] != 'DashBoard_Emergency')].count()[0]/data_round[(data_round['system_judge'] == True) & (data_round['area_index'] != 'DashBoard_Emergency')].count()[0]*100)
                #record_1007 += '%d/%d,'%(data_round[(data_round['user_judge'] == 'Hit') & (data_round['area_index'] != 'DashBoard_Emergency')].count()[0], data_round[(data_round['system_judge'] == True) & (data_round['area_index'] != 'DashBoard_Emergency')].count()[0])
                catch_exce_time.append(data_round[(data_round['user_judge'] == 'Hit') & (data_round['area_index'] != 'DashBoard_Emergency')]['response_time'].mean())
                catch_emer_rate.append(data_round[(data_round['user_judge'] == 'Hit') & (data_round['area_index'] == 'DashBoard_Emergency')].count()[0]/data_round[(data_round['system_judge'] == True) & (data_round['area_index'] == 'DashBoard_Emergency')].count()[0]*100)
                catch_emer_time.append(data_round[(data_round['user_judge'] == 'Hit') & (data_round['area_index'] == 'DashBoard_Emergency')]['response_time'].mean())
                forg_exce_rate.append(data_round[(data_round['user_judge'] == 'Wrong') & (data_round['area_index'] != 'DashBoard_Emergency')].count()[0]/(data_round[(data_round['user_judge'] == 'Wrong') & (data_round['area_index'] != 'DashBoard_Emergency')].count()[0]+data_round[(data_round['user_judge'] == 'Hit') & (data_round['area_index'] != 'DashBoard_Emergency')].count()[0])*100)
                forg_emer_rate.append(data_round[(data_round['user_judge'] == 'Wrong') & (data_round['area_index'] == 'DashBoard_Emergency')].count()[0]/(data_round[(data_round['user_judge'] == 'Wrong') & (data_round['area_index'] == 'DashBoard_Emergency')].count()[0]+data_round[(data_round['user_judge'] == 'Hit') & (data_round['area_index'] == 'DashBoard_Emergency')].count()[0])*100)
                miss_exce_rate.append(data_round[(data_round['user_judge'] == 'Missed') & (data_round['area_index'] != 'DashBoard_Emergency')].count()[0]/data_round[(data_round['system_judge'] == True) & (data_round['area_index'] != 'DashBoard_Emergency')].count()[0]*100)
                miss_emer_rate.append(data_round[(data_round['user_judge'] == 'Missed') & (data_round['area_index'] == 'DashBoard_Emergency')].count()[0]/data_round[(data_round['system_judge'] == True) & (data_round['area_index'] == 'DashBoard_Emergency')].count()[0]*100)
                FA_ij = data_round[(data_round['user_judge'] == 'Wrong') & (data_round['area_index'] != 'DashBoard_Emergency')].count()[0]
                M_ij = data_round[(data_round['user_judge'] == 'Missed') & (data_round['area_index'] != 'DashBoard_Emergency')].count()[0]
                S_ij = data_round[(data_round['system_judge'] == True) & (data_round['area_index'] != 'DashBoard_Emergency')].count()[0]
                P_ij = (1 - (FA_ij + M_ij) / S_ij)
                record_1007 += '%s,%s,%s,%s,'%(FA_ij, M_ij, S_ij, round(P_ij, 5))
            record_1007 = record_1007[:-1]
            record_1007 += '\n'
            with open(r'./Analyse_test/record.csv', 'a', encoding='utf-8') as record:
                record.writelines(record_1007)
            tkinter.Label(data_analyze_root, text='时间段划分总数：%s        '%PERIOD_ANA_NUM, font=('HarmonyOS Sans SC',10)).place(x=520,y=380)
            tkinter.Label(data_analyze_root, text='每段事件数：%s        '%round_length, font=('HarmonyOS Sans SC',10)).place(x=520,y=410)
            tkinter.Label(data_analyze_root, text='每段异常事件捕捉率：%s        '%[str(round(item, 2))+'%' for item in catch_exce_rate], font=('HarmonyOS Sans SC',10)).place(x=520,y=440)
            tkinter.Label(data_analyze_root, text='每段异常事件捕捉反应时间：%s        '%[str(round(item, 2))+'s' for item in catch_exce_time], font=('HarmonyOS Sans SC',10)).place(x=520,y=470)
            tkinter.Label(data_analyze_root, text='每段突发事件捕捉率：%s        '%[str(round(item, 2))+'%' for item in catch_emer_rate], font=('HarmonyOS Sans SC',10)).place(x=520,y=500)
            tkinter.Label(data_analyze_root, text='每段突发事件捕捉反应时间：%s        '%[str(round(item, 2))+'s' for item in catch_emer_time], font=('HarmonyOS Sans SC',10)).place(x=520,y=530)
            tkinter.Label(data_analyze_root, text='每段异常事件错误捕捉率：%s        '%[str(round(item, 2))+'%' for item in forg_exce_rate], font=('HarmonyOS Sans SC',10)).place(x=520,y=560)
            tkinter.Label(data_analyze_root, text='每段突发事件错误捕捉率：%s        '%[str(round(item, 2))+'%' for item in forg_emer_rate], font=('HarmonyOS Sans SC',10)).place(x=520,y=590)
            tkinter.Label(data_analyze_root, text='每段异常事件遗漏捕捉率：%s        '%[str(round(item, 2))+'%' for item in miss_exce_rate], font=('HarmonyOS Sans SC',10)).place(x=520,y=620)
            tkinter.Label(data_analyze_root, text='每段突发事件遗漏捕捉率：%s        '%[str(round(item, 2))+'%' for item in miss_emer_rate], font=('HarmonyOS Sans SC',10)).place(x=520,y=650)
            global record_line
            record_line = [name_spilt[7],
                           int(name_spilt[3]),
                           test_data_df[(test_data_df['user_judge'] == 'Hit') & (test_data_df['area_index'] != 'DashBoard_Emergency')].count()[0]/test_data_df[(test_data_df['system_judge'] == True) & (test_data_df['area_index'] != 'DashBoard_Emergency')].count()[0]*100,
                           test_data_df[(test_data_df['user_judge'] == 'Wrong') & (test_data_df['area_index'] != 'DashBoard_Emergency')].count()[0]/(test_data_df[(test_data_df['user_judge'] == 'Wrong') & (test_data_df['area_index'] != 'DashBoard_Emergency')].count()[0]+test_data_df[(test_data_df['user_judge'] == 'Hit') & (test_data_df['area_index'] != 'DashBoard_Emergency')].count()[0])*100,
                           test_data_df[(test_data_df['user_judge'] == 'Missed') & (test_data_df['area_index'] != 'DashBoard_Emergency')].count()[0]/test_data_df[(test_data_df['system_judge'] == True) & (test_data_df['area_index'] != 'DashBoard_Emergency')].count()[0]*100]
            print(record_line)
            x_ax = [str(index) for index in range(1, PERIOD_ANA_NUM+1)]
            for index in range(PERIOD_ANA_NUM):
                if catch_emer_rate[index] == nan:
                    catch_emer_rate[index] = 0
                if forg_emer_rate[index] == nan:
                    forg_emer_rate[index] = 0
                if miss_emer_rate[index] == nan:
                    miss_emer_rate[index] = 0
            plt.figure(figsize=(10, 4), dpi=100)
            plt.subplot(1, 3, 1)
            plt.ylim(0, display_time+vacant_time)
            plt.title('事件捕捉反应时间相关')
            plt.plot(x_ax, catch_exce_time, color='orange', label='异常事件反应')
            plt.plot(x_ax, [catch_exce_time_mean for i in range(PERIOD_ANA_NUM)], color='orange', linestyle='--')
            if emer_status:
                plt.scatter(x_ax, catch_emer_time, color='purple', label='突发事件反应')
                plt.plot(x_ax, [catch_emer_time_mean for i in range(PERIOD_ANA_NUM)], color='purple', linestyle='--')
            plt.legend()
            plt.subplot(1, 3, 2)
            plt.title('异常事件率相关')
            plt.ylim(0, 100)
            plt.plot(x_ax, catch_exce_rate, color='red', label='正确捕捉异常')
            plt.plot(x_ax, [average(catch_exce_rate) for i in range(PERIOD_ANA_NUM)], color='red', linestyle='--')
            plt.plot(x_ax, forg_exce_rate, color='blue', label='错误捕捉异常')
            plt.plot(x_ax, [average(forg_exce_rate) for i in range(PERIOD_ANA_NUM)], color='blue', linestyle='--')
            plt.plot(x_ax, miss_exce_rate, color='green', label='遗漏捕捉异常')
            plt.plot(x_ax, [average(miss_exce_rate) for i in range(PERIOD_ANA_NUM)], color='green', linestyle='--')
            plt.legend()

            if emer_status:
                plt.subplot(1, 3, 3)
                plt.title('突发事件率相关')
                plt.ylim(0, 100)
                plt.scatter(x_ax, catch_emer_rate, color='red', label='正确捕捉突发')
                plt.scatter(x_ax, forg_emer_rate, color='blue', label='错误捕捉突发')
                plt.scatter(x_ax, miss_emer_rate, color='green', label='遗漏捕捉突发')
                plt.legend()

            plt.suptitle('测试数据逐轮可视化分析')
            #buffer_ = io.BytesIO()
            #plt.savefig(buffer_, format = "png")
            #image = PIL.Image.open(buffer_)
            #image = PIL.ImageTk.PhotoImage(image)
            #tkinter.Label(data_analyze_root, image=image).place(x=500, y=340)
            plt.show()
            #buffer_.close()
            plt.close()
        info_text = '''程序端 管理组件 - 数据分析系统实现说明：
1. 使用此控件将会分析程序数据同步路径下的文件，选择被试者信息后将呈现数据分析结果。
2. 请注意，此功能仅在程序数据同步路径下存在数据文件时才能正常使用。\n\n 点击 <确定> 键后将打开数据分析系统。'''
        tkinter.messagebox.showinfo(title='系统端提示', message=info_text)
        global data_analyze_root
        logging.info('Creating app data_analyze_root window')
        #data_analysis_app.main(root)

        data_analyze_root = tkinter.Toplevel(root)
        data_analyze_root.title('程序端 数据分析系统')
        data_analyze_root.geometry('1024x768')
        data_analyze_root.minsize(1024, 768)
        data_analyze_root.maxsize(1024, 768)
        data_analyze_root.resizable(False, False)
        if top_window_status:
            data_analyze_root.wm_attributes('-topmost', 1)
        data_analyze_root.tk.call(
            'wm', 'iconphoto', data_analyze_root._w, tkinter.PhotoImage(
                file='.\\icons\\ic_gallery_search_things.png'))
        tester_list = []
        for item in os.scandir(local_filepath):
            if item.is_dir():
                tester_list.append(item.name)
        tkinter.Label(
            data_analyze_root,
            text='呈现数据分析结果仅在统计时间 %s 前有效' %
            time.strftime('%Y%m%d-%H%M%S',time.localtime()),
            font=('HarmonyOS Sans SC',8)).place(x=640,y=25)
        tkinter.Label(
            data_analyze_root,
            text='请选择需观测的被试信息：',
            font=('HarmonyOS Sans SC',12,'bold')).place(x=20,y=20)
        tester_combobox = tkinter.ttk.Combobox(
            data_analyze_root, width=28, font=(
            'HarmonyOS Sans SC', 10), values=(tester_list))
        tester_combobox.place(x=250, y=20)
        tester_combobox.set('请选择被试者信息')
        tester_submit = tkinter.Button(
            data_analyze_root, width=10, text='确认选择', 
            font=('HarmonyOS Sans SC', 8), command=tester_confirm)
        tester_submit.place(x=480, y=25)
        tkinter.Label(
            data_analyze_root,
            text='请选择具体测试项目信息：',
            font=('HarmonyOS Sans SC',12)).place(x=20,y=60)
        data_combobox = tkinter.ttk.Combobox(
            data_analyze_root, width=85, font=(
            'HarmonyOS Sans SC', 10))
        data_combobox.place(x=250, y=60)
        data_combobox.set('请先在上方选择被试者信息')
        data_submit = tkinter.Button(
            data_analyze_root, width=10, text='开始分析',
            font=('HarmonyOS Sans SC', 8), state='disabled', command=data_analyze)
        data_submit.place(x=880, y=65)
        tkinter.Label(
            data_analyze_root,
            text='注：选择具体测试项目时，系统会自动包含此项目的量表测试结果（若存在），无需手动选择。  若无法输出可视化结果请尝试重启软件。',
            font=('HarmonyOS Sans SC',8)).place(x=40,y=100)
        tkinter.Label(
            data_analyze_root,
            text='* 项目测试数据预览：',
            font=('HarmonyOS Sans SC',10, 'bold')).place(x=20,y=140)
        tkinter.Label(
            data_analyze_root,
            text='* 被试相关信息：',
            font=('HarmonyOS Sans SC',10, 'bold')).place(x=20,y=340)
        tkinter.Label(
            data_analyze_root,
            text='* 相关数据指标统计：',
            font=('HarmonyOS Sans SC',10, 'bold')).place(x=250,y=340)
        data_export_submit = tkinter.Button(
            data_analyze_root, width=10, text='导出数据',
            font=('HarmonyOS Sans SC', 8), state='disabled')
        data_export_submit.place(x=880, y=340)
        data_analyze_root.mainloop()
    tkinter.Label(
        tab_VIII_root,
        text='程序设置与高级组件',
        font=('HarmonyOS Sans SC',14,'bold')).place(x=20,y=20)
    for index in range(26):
        tkinter.Label(
            tab_VIII_root,
            text='|',
            font=('HarmonyOS Sans',10,'bold')).place(x=1020,y=120 +20 *index)
    tkinter.Label(
        tab_VIII_root,
        text='此页面下的相关设置将影响部分选项卡以及程序界面呈现方式，修改设置需要先验证口令，修改完成后请重启程序。',
        font=('HarmonyOS Sans SC',12)).place(x=20,y=60)
    tkinter.Label(
        tab_VIII_root,
        text='About this program',
        font=('HarmonyOS Sans',12,'bold italic')).place(x=1040,y=120)
    tkinter.Label(
        tab_VIII_root,
        text='      认知性警戒作业模拟及绩效测试系统',
        font=('HarmonyOS Sans SC',10,'bold')).place(x=1040,y=160)
    tkinter.Label(
        tab_VIII_root,
        text='%s' %VERSION,
        font=('HarmonyOS Sans',12,'italic')).place(x=1100,y=200)
    tkinter.Label(
        tab_VIII_root,
        text='Copyright 2023 - 2024\n\nPowered by PbiD :)',
        font=('Consolas', 10)).place(x=1060, y=580)
    tkinter.Label(
        tab_VIII_root,
        text='输入系统口令以继续：',
        font=('HarmonyOS Sans SC',11,'bold')).place(x=20,y=120)
    password_entry = tkinter.Entry(
        tab_VIII_root, width=12, font=('HarmonyOS Sans', 10), show='*')
    password_entry.place(x=185, y=120)
    password_entry.insert(0, '0217')
    password_submit = tkinter.Button(
        tab_VIII_root, width=8, text='提交验证', font=(
            'HarmonyOS Sans SC', 8, 'bold'), command=password_confirm)
    password_submit.place(x=280, y=120)
    tkinter.Label(
        tab_VIII_root,
        text='* 测试端 组件设置',
        font=('HarmonyOS Sans SC',10,'bold')).place(x=80,y=180)
    tkinter.Label(
        tab_VIII_root,
        text='数字显示时间：                          秒',
        font=('HarmonyOS Sans SC',10)).place(x=80,y=220)
    display_time_entry = tkinter.Entry(
        tab_VIII_root, width=12, font=('HarmonyOS Sans', 10))
    display_time_entry.place(x=185, y=220)
    display_time_entry.insert(0, str(display_time))
    display_time_entry.configure(state='disabled')
    tkinter.Label(
        tab_VIII_root,
        text='数字空置时间：                          秒',
        font=('HarmonyOS Sans SC',10)).place(x=80,y=260)
    vacant_time_entry = tkinter.Entry(
        tab_VIII_root, width=12, font=('HarmonyOS Sans', 10))
    vacant_time_entry.place(x=185, y=260)
    vacant_time_entry.insert(0, str(vacant_time))
    vacant_time_entry.configure(state='disabled')
    tkinter.Label(
        tab_VIII_root,
        text='测试阶段时间：                          分钟每阶段',
        font=('HarmonyOS Sans SC',10)).place(x=80,y=300)
    period_time_entry = tkinter.Entry(
        tab_VIII_root, width=12, font=('HarmonyOS Sans', 10))
    period_time_entry.place(x=185, y=300)
    period_time_entry.insert(0, str(period_time))
    period_time_entry.configure(state='disabled')
    tkinter.Label(
        tab_VIII_root,
        text='测试阶段总量：                          阶段',
        font=('HarmonyOS Sans SC',10)).place(x=80,y=340)
    period_num_entry = tkinter.Entry(
        tab_VIII_root, width=12, font=('HarmonyOS Sans', 10))
    period_num_entry.place(x=185, y=340)
    period_num_entry.insert(0, str(period_num))
    period_num_entry.configure(state='disabled')
    tkinter.Label(
        tab_VIII_root,
        text='间隔过渡时间：                          轮',
        font=('HarmonyOS Sans SC',10)).place(x=80,y=380)
    rest_time_entry = tkinter.Entry(
        tab_VIII_root, width=12, font=('HarmonyOS Sans', 10))
    rest_time_entry.place(x=185, y=380)
    rest_time_entry.insert(0, str(rest_time))
    rest_time_entry.configure(state='disabled')
    tkinter.Label(
        tab_VIII_root,
        text='数字区间长度：                          位',
        font=('HarmonyOS Sans SC',10)).place(x=80,y=420)
    length_entry = tkinter.Entry(
        tab_VIII_root, width=12, font=('HarmonyOS Sans', 10))
    length_entry.place(x=185, y=420)
    length_entry.insert(0, str(interval_length))
    length_entry.configure(state='disabled')
    tkinter.Label(
        tab_VIII_root,
        text='区间变化周期：                          轮',
        font=('HarmonyOS Sans SC',10)).place(x=80,y=460)
    interval_change_cycle_entry = tkinter.Entry(
        tab_VIII_root, width=12, font=('HarmonyOS Sans', 10))
    interval_change_cycle_entry.place(x=185, y=460)
    interval_change_cycle_entry.insert(0, str(interval_change_cycle))
    interval_change_cycle_entry.configure(state='disabled')
    tkinter.Label(
        tab_VIII_root,
        text='较高事件比率：                          件每分钟',
        font=('HarmonyOS Sans SC',10)).place(x=80,y=500)
    high_rate_entry = tkinter.Entry(
        tab_VIII_root, width=12, font=('HarmonyOS Sans', 10))
    high_rate_entry.place(x=185, y=500)
    high_rate_entry.insert(0, str(event_num_per_min_high))
    high_rate_entry.configure(state='disabled')
    tkinter.Label(
        tab_VIII_root,
        text='较低事件比率：                          件每分钟',
        font=('HarmonyOS Sans SC',10)).place(x=80,y=540)
    low_rate_entry = tkinter.Entry(
        tab_VIII_root, width=12, font=('HarmonyOS Sans', 10))
    low_rate_entry.place(x=185, y=540)
    low_rate_entry.insert(0, str(event_num_per_min_low))
    low_rate_entry.configure(state='disabled')
    tkinter.Label(
        tab_VIII_root,
        text='事件比率调用：                          事件率',
        font=('HarmonyOS Sans SC',10)).place(x=80,y=580)
    rate_handover_combobox = tkinter.ttk.Combobox(
        tab_VIII_root, width=9, font=('HarmonyOS Sans SC', 10), values=(
            '低', '高'), state='disabled')
    rate_handover_combobox.place(x=185, y=580)
    rate_handover_combobox.current(rate_handover_status)
    tkinter.Label(
        tab_VIII_root,
        text='突发事件比率：                          件每十分钟',
        font=('HarmonyOS Sans SC',10)).place(x=80,y=620)
    emergency_rate_entry = tkinter.Entry(
        tab_VIII_root, width=12, font=('HarmonyOS Sans', 10))
    emergency_rate_entry.place(x=185, y=620)
    emergency_rate_entry.insert(0, str(emergency_num_per_ten_min))
    emergency_rate_entry.configure(state='disabled')
    tkinter.Label(
        tab_VIII_root,
        text='* 程序端 组件设置',
        font=('HarmonyOS Sans SC',10,'bold')).place(x=430,y=180)
    tkinter.Label(
        tab_VIII_root,
        text='全屏置顶接管：',
        font=('HarmonyOS Sans SC',10)).place(x=430,y=220)
    top_window_status_combobox = tkinter.ttk.Combobox(
        tab_VIII_root, width=13, font=('HarmonyOS Sans SC', 10), values=(
            '禁用', '启用'), state='disabled')
    top_window_status_combobox.place(x=535, y=220)
    top_window_status_combobox.current(top_window_status)
    tkinter.Label(
        tab_VIII_root,
        text='退出事件接管：',
        font=('HarmonyOS Sans SC',10)).place(x=430,y=260)
    del_window_status_combobox = tkinter.ttk.Combobox(
        tab_VIII_root, width=13, font=('HarmonyOS Sans SC', 10), values=(
            '禁用', '启用'), state='disabled')
    del_window_status_combobox.place(x=535, y=260)
    del_window_status_combobox.current(del_window_status)
    tkinter.Label(
        tab_VIII_root,
        text='增强型提示框：',
        font=('HarmonyOS Sans SC',10)).place(x=700,y=220)
    tip_enhanced_status_combobox = tkinter.ttk.Combobox(
        tab_VIII_root, width=13, font=('HarmonyOS Sans SC', 10), values=(
            '禁用', '启用'), state='disabled')
    tip_enhanced_status_combobox.place(x=805, y=220)
    tip_enhanced_status_combobox.current(tip_enhanced_status)
    tkinter.Label(
        tab_VIII_root,
        text='强制深色模式：',
        font=('HarmonyOS Sans SC',10)).place(x=700,y=260)
    force_dark_mode_status_combobox = tkinter.ttk.Combobox(
        tab_VIII_root, width=13, font=('HarmonyOS Sans SC', 10), values=(
            '禁用', '启用'), state='disabled')
    force_dark_mode_status_combobox.place(x=805, y=260)
    force_dark_mode_status_combobox.current(force_dark_mode_status)
    tkinter.Label(
        tab_VIII_root,
        text='* WebDAV 组件设置 - 基于坚果云实现',
        font=('HarmonyOS Sans SC',10,'bold')).place(x=430,y=340)
    tkinter.Label(
        tab_VIII_root,
        text='WebDAV 状态：',
        font=('HarmonyOS Sans SC',10)).place(x=430,y=380)
    webdav_status_combobox = tkinter.ttk.Combobox(
        tab_VIII_root, width=13, font=('HarmonyOS Sans SC', 10), values=(
            '禁用', '启用'), state='disabled')
    webdav_status_combobox.place(x=535, y=380)
    webdav_status_combobox.current(webdav_status)
    tkinter.Label(
        tab_VIII_root,
        text='WebDAV 地址：',
        font=('HarmonyOS Sans SC',10)).place(x=700,y=380)
    webdav_url_entry = tkinter.Entry(
        tab_VIII_root, width=16, font=('HarmonyOS Sans SC', 10))
    webdav_url_entry.place(x=805, y=380)
    webdav_url_entry.insert(0, 'https://dav.jianguoyun.com/dav/')
    webdav_url_entry.configure(state='readonly')
    tkinter.Label(
        tab_VIII_root,
        text='WebDAV 账号：',
        font=('HarmonyOS Sans SC',10)).place(x=430,y=420)
    webdav_account_entry = tkinter.Entry(
        tab_VIII_root, width=16, font=('HarmonyOS Sans SC', 10))
    webdav_account_entry.place(x=535, y=420)
    webdav_account_entry.insert(0, str(webdav_account))
    webdav_account_entry.configure(state='disabled')
    tkinter.Label(
        tab_VIII_root,
        text='WebDAV 密码：',
        font=('HarmonyOS Sans SC',10)).place(x=700,y=420)
    webdav_password_entry = tkinter.Entry(
        tab_VIII_root, width=16, font=('HarmonyOS Sans SC', 10), show='*')
    webdav_password_entry.place(x=805, y=420)
    webdav_password_entry.insert(0, str(webdav_password))
    webdav_password_entry.configure(state='disabled')
    tkinter.Label(
        tab_VIII_root,
        text='本地同步路径：',
        font=('HarmonyOS Sans SC',10)).place(x=430,y=460)
    file_path_string = tkinter.StringVar(value=local_filepath)
    local_filepath_entry = tkinter.Entry(
        tab_VIII_root, width=12, font=(
            'HarmonyOS Sans SC', 10), textvariable=file_path_string)
    local_filepath_entry.place(x=535, y=460)
    local_filepath_entry.configure(state='disabled')
    local_filepath_submit = tkinter.Button(tab_VIII_root, text='选择', font=(
        'HarmonyOS Sans SC', 8), state='disabled', command=filepath_display)
    local_filepath_submit.place(x=625, y=460)
    setting_submit = tkinter.Button(tab_VIII_root, width=12, text='保存设置', font=(
        'HarmonyOS Sans SC', 10, 'bold'), state='disabled', command=setting_confirm)
    setting_submit.place(x=700, y=120)
    setting_submit_exit = tkinter.Button(
        tab_VIII_root,
        width=12,
        text='保存并退出',
        font=('HarmonyOS Sans SC',10,'bold'),
        state='disabled',
        command=setting_confirm_exit)
    setting_submit_exit.place(x=805, y=120)
    tkinter.Label(
        tab_VIII_root,
        text='* 程序端 管理组件',
        font=('HarmonyOS Sans SC',10,'bold')).place(x=430,y=540)
    dev_exit_submit = tkinter.Button(
        tab_VIII_root,
        width=13,
        text='强制退出程序',
        font=('HarmonyOS Sans SC',10),
        state='disabled',
        command=root_destroy_dev)
    dev_exit_submit.place(x=430, y=580)
    log_filepath_submit = tkinter.Button(
        tab_VIII_root,
        width=13,
        text='打开日志文件夹',
        font=('HarmonyOS Sans SC',10),
        state='disabled',
        command=log_filepath_display)
    log_filepath_submit.place(x=550, y=580)
    data_analyze_submit = tkinter.Button(
        tab_VIII_root,
        width=28,
        text='Dev - 数据分析系统',
        font=('HarmonyOS Sans SC', 10, 'bold'),
        state='disabled',
        command=data_analyze_display)
    data_analyze_submit.place(x=700, y=580)
    data_upload_submit = tkinter.Button(
        tab_VIII_root,
        width=13,
        text='数据上传管理',
        font=('HarmonyOS Sans SC',10),
        state='disabled',
        command=overall_upload_display)
    data_upload_submit.place(x=430, y=620)
    watchdog_submit = tkinter.Button(
        tab_VIII_root,
        width=13,
        text='数据上传监控',
        font=('HarmonyOS Sans SC',10),
        state='disabled',
        command=watchdog_display)
    watchdog_submit.place(x=550, y=620)
    keyboard_submit = tkinter.Button(
        tab_VIII_root,
        width=28,
        text='键盘交互设置',
        font=('HarmonyOS Sans SC',10),
        state='disabled',
        command=keyboard_display)
    keyboard_submit.place(x=700, y=620)
log_file_name = '.\\logs\\LOG' + BOOT_TIME + '.log'
logging.basicConfig(
    level=logging.DEBUG,
    filename=log_file_name,
    filemode='w',
    format='%(asctime)s - %(name)-20s - %(levelname)-9s - %(filename)-8s : %(lineno)s line - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S')
logging.info('Welcome to Use the Cognitive Vigilance Simulation System')
fonts_list = [font.name for font in matplotlib.font_manager.fontManager.ttflist]
if FONTS_INCLUDED.issubset(fonts_list) == False:
    logging.info('Installing the required fonts')
    subprocess.call('cscript %s' % FONTS_INSTALL_PATH)
if not os.path.exists('./data'):
    os.mkdir('./data')
    check = False
else:
    for item in DATABASE:
        if item not in os.listdir('./data'):
            shutil.rmtree('./data')
            os.mkdir('./data')
            check = False
            break
    else:
        check = True
storage_db_connect = sqlite3.connect('./data/storage.db')
storage_db_cursor = storage_db_connect.cursor()
if not check:
    logging.info('Initializing the database file')
    database_initial()
logging.info('Getting app configuration data')
dashboard_num = int(storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "dashboard_num"''').fetchall()[0][0])
display_time = int(storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "display_time"''').fetchall()[0][0])
vacant_time = int(storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "vacant_time"''').fetchall()[0][0])
period_time = int(storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "period_time"''').fetchall()[0][0])
period_num = int(storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "period_num"''').fetchall()[0][0])
rest_time = int(storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "rest_time"''').fetchall()[0][0])
interval_length = int(storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "interval_length"''').fetchall()[0][0])
interval_change_cycle = int(storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "interval_change_cycle"''').fetchall()[0][0])
event_num_per_min_high = float(storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "event_num_per_min_high"''').fetchall()[0][0])
event_num_per_min_low = float(storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "event_num_per_min_low"''').fetchall()[0][0])
rate_handover_status = int(storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "rate_handover_status"''').fetchall()[0][0])
emergency_num_per_ten_min = float(storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "emergency_num_per_ten_min"''').fetchall()[0][0])
top_window_status = int(storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "top_window_status"''').fetchall()[0][0])
del_window_status = int(storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "del_window_status"''').fetchall()[0][0])
tip_enhanced_status = int(storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "tip_enhanced_status"''').fetchall()[0][0])
force_dark_mode_status = int(storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "force_dark_mode_status"''').fetchall()[0][0])
webdav_status = int(storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "webdav_status"''').fetchall()[0][0])
webdav_account = storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "webdav_account"''').fetchall()[0][0]
webdav_password = storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "webdav_password"''').fetchall()[0][0]
local_filepath = storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "local_filepath"''').fetchall()[0][0]
keyboard_preference_I = storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "keyboard_preference_I"''').fetchall()[0][0]
keyboard_preference_II = storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "keyboard_preference_II"''').fetchall()[0][0]
keyboard_preference_III = storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "keyboard_preference_III"''').fetchall()[0][0]
keyboard_preference_IV = storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "keyboard_preference_IV"''').fetchall()[0][0]
keyboard_preference_opt_I = storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "keyboard_preference_opt_I"''').fetchall()[0][0]
keyboard_preference_opt_II = storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "keyboard_preference_opt_II"''').fetchall()[0][0]
keyboard_preference_opt_III = storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "keyboard_preference_opt_III"''').fetchall()[0][0]
keyboard_preference_opt_IV = storage_db_cursor.execute(
    '''SELECT setting FROM options WHERE key == "keyboard_preference_opt_IV"''').fetchall()[0][0]
code_dir = os.getcwd()
if local_filepath == 'null':
    local_filepath = os.path.join(code_dir, 'data')
local_filepath = local_filepath.replace("\\", "\\\\")
display_round_per_min = 60 / (display_time + vacant_time)
event_rate_high = event_num_per_min_high / display_round_per_min
event_rate_low = event_num_per_min_low / display_round_per_min
if rate_handover_status == 0:
    RATE_CALL = event_rate_low
else:
    RATE_CALL = event_rate_high
emergency_rate = emergency_num_per_ten_min / (display_round_per_min * 10)
interval_change_time = interval_change_cycle * (display_time + vacant_time)
logging.info('Configuration Check dashboard_num: %s' % dashboard_num)
logging.info('Configuration Check display_time: %s' % display_time)
logging.info('Configuration Check vacant_time: %s' % vacant_time)
logging.info('Configuration Check period_time: %s' % period_time)
logging.info('Configuration Check period_num: %s' % period_num)
logging.info('Configuration Check rest_time: %s' % rest_time)
logging.info('Configuration Check interval_length: %s' % interval_length)
logging.info('Configuration Check interval_change_cycle: %s' %interval_change_cycle)
logging.info('Configuration Check event_num_per_min_high: %s' %event_num_per_min_high)
logging.info('Configuration Check event_num_per_min_low: %s' %event_num_per_min_low)
logging.info('Configuration Check rate_handover_status: %s' %rate_handover_status)
logging.info('Configuration Check emergency_num_per_ten_min: %s' %emergency_num_per_ten_min)
logging.info('Configuration Check top_window_status: %s' % top_window_status)
logging.info('Configuration Check del_window_status: %s' % del_window_status)
logging.info('Configuration Check tip_enhanced_status: %s' %tip_enhanced_status)
logging.info('Configuration Check force_dark_mode_status: %s' %force_dark_mode_status)
logging.info('Configuration Check webdav_status: %s' % webdav_status)
logging.info('Configuration Check webdav_account: %s' % webdav_account)
logging.info('Configuration Check webdav_password: %s' % webdav_password)
logging.info('Configuration Check local_filepath: %s' % local_filepath)
logging.info('Configuration Check keyboard_preference_I: %s' %keyboard_preference_I)
logging.info('Configuration Check keyboard_preference_II: %s' %keyboard_preference_II)
logging.info('Configuration Check keyboard_preference_III: %s' %keyboard_preference_III)
logging.info('Configuration Check keyboard_preference_IV: %s' %keyboard_preference_IV)
logging.info('Configuration Check keyboard_preference_opt_I: %s' %keyboard_preference_opt_I)
logging.info('Configuration Check keyboard_preference_opt_II: %s' %keyboard_preference_opt_II)
logging.info('Configuration Check keyboard_preference_opt_III: %s' %keyboard_preference_opt_III)
logging.info('Configuration Check keyboard_preference_opt_IV: %s' %keyboard_preference_opt_IV)
logging.info('Configuration Check display_round_per_min: %s' %display_round_per_min)
logging.info('Configuration Check event_rate_high: %s' % event_rate_high)
logging.info('Configuration Check event_rate_low: %s' % event_rate_low)
logging.info('Configuration Check emergency_rate: %s' % emergency_rate)
logging.info('Configuration Check interval_change_time: %s' %interval_change_time)
logging.info('Creating app root window')
root = tkinter.Tk()
root.title('认知性警戒作业模拟及绩效测试系统')
root.geometry('1300x750')
root.minsize(1300, 750)
#root.overrideredirect(True)
if top_window_status:
    root.attributes("-fullscreen", True)
else:
    root.maxsize(1300, 750)
root.resizable(False, False)
root.tk.call(
    'wm','iconphoto',root._w,
    tkinter.PhotoImage(file='.\\icons\\ic_gallery_discover.png'))
bottom_status_bar = tkinter.Label(
    root,
    text='欢迎使用 认知性警戒作业模拟及绩效测试系统',
    bd=1,
    relief=tkinter.SUNKEN,
    anchor=tkinter.W,
    font=('HarmonyOS Sans SC',8))
bottom_status_bar.pack(side=tkinter.BOTTOM, fill=tkinter.X)
if top_window_status:
    root.wm_attributes('-topmost', 1)
root.protocol('WM_DELETE_WINDOW', delete_root)
light_theme_list = ['cosmo','flatly','journal','lumen','minty','pulse','sandstone','united','yeti']
dark_theme_list = ['cyborg','darkly','solar','superhero']
if force_dark_mode_status:
    default_theme_setting = random.choice(dark_theme_list)
else:
    default_theme_setting = random.choice(light_theme_list)
ttkbootstrap.Style(theme=default_theme_setting)
global img_attention, img_scale
img_attention_open = PIL.Image.open('.\\img\\attention.png')
img_attention = PIL.ImageTk.PhotoImage(img_attention_open)
img_scale_open = PIL.Image.open('.\\img\\scale.png')
img_scale = PIL.ImageTk.PhotoImage(img_scale_open)
top_tab_bar = tkinter.ttk.Notebook(root)
tab_I_root = tkinter.ttk.Frame(top_tab_bar)
tab_II_root = tkinter.ttk.Frame(top_tab_bar)
tab_III_root = tkinter.ttk.Frame(top_tab_bar)
tab_IV_root = tkinter.ttk.Frame(top_tab_bar)
tab_V_root = tkinter.ttk.Frame(top_tab_bar)
tab_VI_root = tkinter.ttk.Frame(top_tab_bar)
tab_VII_root = tkinter.ttk.Frame(top_tab_bar)
tab_VIII_root = tkinter.ttk.Frame(top_tab_bar)
top_tab_bar.add(tab_I_root, text='    主页    ')
top_tab_bar.add(tab_II_root, text='    心理特征测试    ')
top_tab_bar.add(tab_III_root, text='    模拟作业教程    ')
top_tab_bar.add(tab_IV_root, text='    警戒作业测试 -O-MS    ')
top_tab_bar.add(tab_V_root, text='    警戒作业测试 -E-MS    ')
top_tab_bar.add(tab_VI_root, text='    警戒作业测试 -O-SS    ')
top_tab_bar.add(tab_VII_root, text='    警戒作业测试 -E-SS    ')
top_tab_bar.add(tab_VIII_root, text='    程序设置与高级组件    ')
top_tab_bar.pack(padx=0, pady=0, fill=tkinter.BOTH, expand=True)
tab_I_content_display()
tab_II_content_display()
tab_III_content_display()
tab_IV_content_display()
tab_V_content_display()
tab_VI_content_display()
tab_VII_content_display()
tab_VIII_content_display()
data_analysis_app.main(root)
root.mainloop()
