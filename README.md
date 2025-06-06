# Cognitive-Vigilance-Research

**此文档原文位于作者网站：https://harryxu.top/**

## 〇、前言

2024年初，我加入了中国民航大学安全科学与工程学院的“认知性警戒作业疲劳”大创项目，并合作为其编写了用于被试实验的软件系统整合。此文档由当时申请软著所撰写的软件系统使用手册转换格式而来，结合此站点已有的评论交流系统，希望能够帮助使用者更好地了解该项目。

## 一、软件概述

### （一）基本信息

| 项目       | 信息                             |
| ---------- | -------------------------------- |
| 软件名称   | 认知性警戒作业模拟及绩效测试系统 |
| 软件版本号 | V1.0                             |
| 软件分类   | 应用软件                         |

### （二）开发背景

自Mackworth的实验室警戒研究起，到目前为止，已有上千篇有关警戒的研究报告和几部专著出版。虽然警戒研究有如此丰富的基础，但重要程度较高的厌烦、疲劳、任务要求压力和操作者超负荷等因素却研究得很少。也就是说，以往多注重对环境应激源的研究而相对忽略了对认知应激源(厌烦、任务要求压力等)的研究。Hancock和Warm(1989)曾指出在持续注意的应激动力模型中应特别关注多种应激源间潜在的交互作用。然而目前对认知应激源部分还缺乏足够的了解，因此只有通过对认知应激源的深入研究才有可能进一步了解警戒任务中多种应激源的交互作用，从而建立更加合理完善的警戒应激模型。该项目主要研究心理特征对认知性警戒作业疲劳的影响。随着现代科技的发展,认知性警戒作业越来越普遍，其主要任务形式为仪表监控、检测、搜索、对照等，广泛存在于交通管理、车辆与飞机驾驶、质量控制、自动化作业中。认知性警戒作业需要作业者长时间监控外界信息变化，当出现异常信息时，迅速做出反应。已有研究表明，警戒作业者出现疲劳后，警觉水平降低，反应时间增加，操作准确性降低，疲劳问题严重威胁认知性警戒作业的安全。国内外研究表明，警戒绩效间存在个体差异，这就为研究者区分“好”与“差”的作业人员提供了理论依据。

本项目拟通过实验的方法，探究个体心理特征是否会对认知性警戒作业疲劳产生影响，以及产生何种影响。研究内容主要包括：①认知性警戒作业的模拟，②认知性警戒作业疲劳的测量方法及测量指标，③个体心理特征对认知性警戒作业疲劳的影响以及对其疲劳恢复情况的影响。研究结果可为科学选拔认知性警戒类作业人员，降低事故发生率、提升作业绩效提供理论支撑，具有重要的理论和现实意义。

### （三）硬件环境

硬件环境说明与下一节中的软件环境说明均以表格形式呈现，其中的“开发”列表示程序开发者的配置情况，而“运行”列表明对使用者提出的推荐配置情况要求。

|      | 开发                                            | 运行           |
| ---- | ----------------------------------------------- | -------------- |
| CPU  | AMD Ryzen 7 5800H with Radeon Graphics 3.20 GHz | 1.0 GHz 或以上 |
| 内存 | 16.0 GB                                         | 2.0 GB         |
| 硬盘 | 512 GB SSD                                      | 20 GB          |

——注：此处的运行环境要求根据软件环境推得，在实际工况中可有所浮动。

### （四）软件环境

|              | 开发                      | 运行                       |
| ------------ | ------------------------- | -------------------------- |
| 操作系统     | Windows 11 Pro 23H2       | 支持Windows 11，Windows 10 |
| 开发环境     | Python 3.10.11            | /                          |
| 开发工具     | Visual Studio Code 1.86.1 | /                          |
| 显示器分辨率 | /                         | 1366 × 768 或以上          |

——注：显示器若低于推荐分辨率，可能会导致窗口显示不全等问题。

### （五）功能特点

#### 1. 主要功能

**该软件系统主要用于认知性警戒作业的模拟。**

在首次使用前，项目管理者可先在设置界面验证口令、修改相关配置选项以更好达到测试预期目的。

每名被试在测试前需要先在主页输入相关信息（例如：人员编号、学号、姓名与性别等），输入完成后即可选择相应选项卡进行测试。

不同的选项卡在测试细节上有所不同，但任务总体上可归纳为：每个独立的测试都需要被试完成较长时间的认知性警戒作业。被试会在计算机屏幕窗口上观察到四个独立的模拟工况面板，每个面板均由第一行的一组中间包含破折号的数字对以及第二行的一组由空格隔开的数字对构成。被试需要在给定的时间内快速计算所有面板中第二行的数字对相加是否落于第一行所表明的数字区间中（我们将“数字对相加落入规定区间”定义为异常事件；并且，异常事件出现的不同概率可通过管理员模式调整或切换），当四个面板的任意一个面板出现异常事件时，要求被试在给定的时间范围内按压键盘上的相应键位（我们将 “QWAS” 四个键位与呈现的四个模拟面板进行对应，即“Q”对应左上方面板一，“W”对应右上方面板二，“A”对应左下方面板三，“S”对应右下方面板四。并且我们对按下时的大小写状态不作严格要求，但不能是中文输入状态）作出反应。（例如：四个面板中的第三个面板此时出现异常事件。第一行“12—16”，第二行“7 8”。则被试需要立刻按下 “A” 键位作出反应）

对于部分测试页面，被试还需在测试中途快速填写状态自测量表（会将长时间测试分阶段，在每阶段之间安排较短时间的状态自测）或还需对突发的应急时间作出反应（由按压键盘对应键位改为点击屏幕指定区域的按钮操作）。

当被试完成任意一个小项或管理员强制通过按钮实现上传操作时，程序会进行数据上传。此系统的数据云端同步功能依托坚果云的 WebDAV 第三方应用管理功能。当管理员已在设置界面正确填写 WebDAV 相关配置选项后，程序每次均会在云盘目录下生成带有被试标识码的文件夹，并在其中同步该被试人员的所有实验数据。

针对实际进行被试测试过程中会遇到的数据管理问题，我们设计了数据上传监控功能。当管理员已在设置界面正确填写 WebDAV 相关配置选项以及本地同步路径后，程序将实时反馈云端数据变化，更好地帮助项目组成员收集和管理数据。

#### 2. 技术特点

本软件系统具备实用性和前瞻创新性，我们开发了可供多种场景使用的警戒作业类型，并且实现了各组件功能配置的高度可定制化，还同时引入了数据的云端存储功能，为实际的使用场景提供便利。

具体而言，本软件系统基于 Python 环境开发，在图形用户界面呈现上依托 tkinter 标准 GUI 库。通过加密口令实现被试人员与项目管理人员的区分。对程序被试端，我们基于 threading 多线程库实现不同标签页测试内容的完全独立，为多标签页的功能实现提供了极大便利。

对程序控制端，我们基于 watchdog 库实现了对被试端上传数据文件的实时监控；基于 sqlite3 与 pandas 库实现了软件系统整体数据文件的本地存储；基于 webdav4 库实现了数据文件的云端存储，在很大程度上解决了多终端操作的数据收集问题，基于 logging 库实现了程序运行阶段的日志记录，将为后续的数据分析提供支持。

## 二、软件目录说明

![屏幕截图_179_.png](https://s2.loli.net/2024/03/15/KAuGCl6x17UsVTN.png)

在下载并解压本软件包后，会在程序目录下生成如上图所示的各个文件夹及主程序文件。其中：

“data”文件夹内存储了本系统的配置文件数据库，同时也是后续测试过程中被试产生数据文件的本地保存路径。后续章节将会详细介绍本系统数据文件的存储方式。

“fonts”文件夹内存储了本系统运行过程中会用到的所有字体文件以及一个字体安装脚本，可实现对缺少字体的自动安装。

“icons”与“img”两个文件夹内分别存储了程序各窗体的图标库以及程序运行过程中会用到的图片文件。

“logs”文件夹内存储了随程序运行（例如：被试在测试全过程中的操作、程序配置文件的修改）而产生和记录的日志文件。

“main_ver_1.0.exe”这是本软件系统的启动入口，在打开此程序前请确保其与上述文件夹之间的层级关系正确。

**注：除测试过程中产生的被试数据和日志文件外，不建议直接修改程序目录下的其他文件，除非你能明确知道你在做什么。**

## 三、软件操作说明

接下来我们将介绍系统中每个标签页的具体功能和操作流程。

### （一）标签页I - 主页

![屏幕截图_180_.png](https://s2.loli.net/2024/03/15/D3FplY9krIJmgTO.png)

**此页面主要实现功能**：被试信息采集、提醒事项告知。

需注意，在被试信息采集中，学号、姓名及性别由被试自行填写，被试编号应由项目管理员具体安排后告知被试填写。

在此系统中，被试填写信息并提交是后续所有操作的前置条件。并且被试提交的信息会成为后续数据文件的命名依据。

在被试完成信息填写并点击“信息提交”按钮之后，相关的交互框以及按钮会被锁定，并且程序底部状态栏将会呈现被试信息及填写时间，具体样式可参见下图。

![屏幕截图_181_.png](https://s2.loli.net/2024/03/15/J3bBAtmQEFqDzRC.png)

### （二）标签页II - 心理特征测试

![屏幕截图_182_.png](https://s2.loli.net/2024/03/15/cZnjwWvhgXar6M9.png)

**此页面主要实现功能**：正式警戒作业开始前的特征测试。

我们在这里预留了空白页面，若其他管理员需要进行特征测试即可修改相应代码在此页面实现，若已通过其他方式完成了特征测试（例如：其他平台的在线问卷调查），便可将此页面留空。

### （三）标签页III - 模拟作业教程

![屏幕截图_183_.png](https://s2.loli.net/2024/03/15/O3iwuLUDnGEZk8l.png)

**此页面主要实现功能**：对警戒作业过程的模拟教程。

该功能实现的前置条件是被试人员已在软件主页填写相应信息。

此页面组件构成：模拟工况面板区域、信息区域、提交区域以及量表区域。系统后续测试中用到的大多数组件均会在此页面展示。

在此页面中，被试可点击信息区域中的“开始模拟”按钮来启动功能。系统将会依次呈现教程信息，被试可通过“继续模拟”按钮切换下一提示。在所有提示展示完成后，“开始模拟”按钮将会重新开放，被试可再次点击开始教程，如下图所示。

![屏幕截图_190_.png](https://s2.loli.net/2024/03/15/9uj4KG8atcLBv2J.png)

![屏幕截图_191_.png](https://s2.loli.net/2024/03/15/2cRVsGkCwiKyOzb.png)

![屏幕截图_192_.png](https://s2.loli.net/2024/03/15/dvGlhEyaZKW45rU.png)

![屏幕截图_193_.png](https://s2.loli.net/2024/03/15/yK6Xz27RFIMCOZv.png)

在这里底部的“预警提交”按钮是为后续的包含突发应急事件测试的页面预留的，在其余页面呈现灰色底色并标注“此环节已禁用”。

在这里右侧量表区域显示的相关按钮，用于让被试提前熟悉自测量表的文本顺序以便后续快速做出反应，因此在这里点按系统将不会给出反馈。

注：当被试已完成信息填写这一前置条件后，点按“开始模拟”按钮会在底部状态栏呈现相关信息，具体样式参见下图，后续页面中也存在有类似功能，将不再赘述。

![屏幕截图_194_.png](https://s2.loli.net/2024/03/15/3YgiafTcRul6vyb.png)

### （四）标签页IV - 模拟警戒作业 -O-S

注：此标签页及后续的三个标签页均采用字母后缀代号来区分不同功能细节。这里给出后缀说明，后续将不再重复说明：

-O 代表作业中只出现异常事件；

-E 代表作业中包含有突发应急事件。

-S 代表每阶段时间后出现自测量表；

-NaS 代表不显示量表。

![屏幕截图_184_.png](https://s2.loli.net/2024/03/15/djLrpAsHtmgySlN.png)

**此页面主要实现功能**：警戒作业模拟（无突发事件、有量表）。

此页面的各区域划分与上一个教程页面相同。在被试点击“开始测试”按钮2秒后，测试正式开始，同时，右侧信息区域会给出相关时间信息以供参考。在测试过程中，系统会在各个模拟面板中不断给出数字对（每一轮中，数字对的呈现时间与空置时间均可由管理员具体设置），被试需要迅速对各面板数据给出反应（即点按键盘“QWAS”相应键位，右侧信息区域的“键盘输入检查”栏会实时反馈被试当前输入情况，当输入情况异常时会给出相关建议）。

此页面包含有自测量表阶段，所以在每一阶段结束后会在右侧呈现短时间的量表信息需要被试提交。

测试的各阶段如下图所示。依次是数字对显示、量表显示和测试完成提示（信息区域会显示“测试结束，此界面即将关闭”文本）。另外由于屏幕截图会触发软件系统内的键盘输入检查，因此可在第一幅图中看到“当前处于中文输入状态”的提示信息。

![屏幕截图_195_.png](https://s2.loli.net/2024/03/15/gjLWoPKnCtV9ls2.png)

![屏幕截图 2024-03-15 022700.png](https://s2.loli.net/2024/03/15/q398CGDEbrwTVyk.png)

![屏幕截图 2024-03-15 022808.png](https://s2.loli.net/2024/03/15/fny2vTGbzORJWj7.png)

### （五）标签页V - 模拟警戒作业 -E-S

![屏幕截图_185_.png](https://s2.loli.net/2024/03/15/P2RSA57dwLz3OsB.png)

**此页面主要实现功能**：警戒作业模拟（有突发事件、有量表）。

此页面的其他组件与上一界面相似，不再赘述。

此页面含有极低概率（此概率可在程序设置界面进行具体调整）的突发事件模拟，当突发事件发生时（页面中会呈现红色高亮字体并且设备蜂鸣器会发声），被试需要立即按下右侧的“预警提交”按钮。

突发事件发生时的页面样例如下图所示。

![屏幕截图_196_.png](https://s2.loli.net/2024/03/15/MpW4fTmVPKxEn52.png)

### （六）标签页VI - 模拟警戒作业 -O-NaS

![屏幕截图_186_.png](https://s2.loli.net/2024/03/15/Mw2gLQXcBpxzAPT.png)

**此页面主要实现功能**：警戒作业模拟（无突发事件、无量表）。

此页面的其他组件与上述界面相似，不再赘述。

此页面不含有状态自测量表，因此右侧的“量表区域”被标记为“此环节已禁用”，并且测试过程中也不会包含间隔过渡时间。

### （七）标签页VII - 模拟警戒作业 -E-NaS

![屏幕截图_187_.png](https://s2.loli.net/2024/03/15/4n6EbfQTBsMj2W3.png)

**此页面主要实现功能**：警戒作业模拟（有突发事件、无量表）。

此页面的其他组件与上述界面相似，不再赘述。

### （八）标签页VIII - 程序设置

![屏幕截图_188_.png](https://s2.loli.net/2024/03/15/f2QYkCvSri4NczO.png)

**此页面主要实现功能**：软件系统设置、备用组件和帮助信息。

首先，修改系统设置需要先验证口令，只有口令正确时才会释放所有设置项的交互框和相关按钮，并且底部状态栏也会同步更新文本内容。如下图是口令验证成功后的界面。

![屏幕截图_189_.png](https://s2.loli.net/2024/03/15/Nfqu6mIidVTJctX.png)

其次，我们将给出一些计算公式说明。

<center>每轮次时间 = 数字显示时间 + 数字空置时间</center>

<center>每分钟显示轮次 = 60 / 每轮次时间</center>

<center>高事件率 = 较高事件比率 / 每分钟显示轮次</center>

<center>低事件率 = 较低事件比率 / 每分钟显示轮次</center>

<center>突发事件率 = 突发事件比率 / （每分钟显示轮次 * 10）</center>

对于包含量表显示的测试中：

<center>测试总时长 = 测试阶段时间 * 测试阶段总量 + 间隔过渡时间 * 每轮次时间 *（测试阶段总量 - 1）/ 60</center>

对于不包含量表显示的测试中：

<center>测试总时长 = 测试阶段时间 * 测试阶段总量</center>

接下来将会对所有设置项和相关组件进行说明。

**顶层组件说明**：“保存设置”与“保存并退出”按钮用于提交配置修改的操作，更建议使用“保存并退出”按钮进行修改，防止在修改设置项后忘记重启程序（设置项更改提交后，需要重启程序才能真正生效）。页面右侧区域会显示此程序的相关版本信息。

**“测试端** **组件设置”**，此处的设置会直接影响警戒作业的测试方式。“数字显示时间”与“数字空置时间”控制每一轮各个模拟面板中数字对的呈现时间与消失时间，两者相加后得到的总时间也会影响被试对异常事件的反应难度；“测试阶段时间”、“测试阶段总量”与“间隔过渡时间”共同控制每一次警戒作业的总时长（具体可参见上方的公式说明，注意时间设置应与每轮次时间成倍数关系）。

**“程序端** **组件设置”**，此处的设置会直接影响程序界面的呈现方式。“窗口置顶接管”选项启用后将会强制置顶软件系统的所有窗口界面；“退出界面接管”选项启用后将会禁止被试通过“关闭”按钮来退出程序，可在一定程度上防止被试的误操作；“增强型提示框”选项启用后将会显示更多的提示（例如：将会告知被试突发应急事件的定义），会对测试难度产生一定的影响；“强制深色模式”选项启用后系统界面将会切换至深色状态，界面样例如下图所示。

![屏幕截图_197_.png](https://s2.loli.net/2024/03/15/wdjvBoVQX8qJ9tN.png)

**“WebDAV 组件设置”**，此处的设置会直接影响程序是否将数据文件上传至云端网盘。其中，在选项逻辑上，“WebDAV 状态”设置项具有最高优先级，若将此项禁用会直接重置其余设置项。“WebDAV 地址”目前不支持更改，仅可使用坚果云实现；“WebDAV 账号”与“WebDAV 密码”可在坚果云软件设置中打开第三方应用管理进行添加来获得。“本地同步路径”选项将用于数据上传监控页面，具体而言有两种填写方式：第一种维持默认值（该路径位于本程序目录下的“data”文件夹），此时程序仅能监控本机的数据文件变化；第二种将其改为坚果云的本地路径（等效于直接对网盘数据的监控），此路径在Windows系统下可能为隐藏文件，路径大致位于“C:\Users\<你的用户名>\Nutstore\1\”，此时程序可监控云端的数据文件变化。管理员可通过点击“选择”按钮进行路径输入。

**“程序端 管理组件”**，此处的四个按钮面向管理员提供。具体而言，“强制退出程序”按钮在点击后会直接退出程序（会弹出消息框进行二次确认）；“打开程序日志文件夹”按钮在点击后将会打开位于程序根目录下的“logs”文件夹。“数据上传管理”按钮在点击后会弹出一个子窗口，具体如下图所示。

![屏幕截图_198_.png](https://s2.loli.net/2024/03/15/XDbv3oA6lK5NuBj.png)

“数据上传管理”子窗口由被试者信息、数据统计时间、所有数据文件记录、相关按钮选项和说明文字几部分组成。其中，“警戒测试过程记录”与“心理特征量表抽测”栏的数据记录由几组数字组成，这里的数字代表文件的长度（数据记录以四个标签页进行区分，显示“-1”则表示无此数据记录）；“程序日志文件备份”栏会显示此次运行中生成的日志文件路径。下方的按钮“打开数据文件夹”与“打开日志文件夹”点击后会打开相应的文件夹路径，按钮“数据上传”点击后会将此时所有存在的数据文件上传至云端（需要相关设置项配合）。

*（接上一段的“程序端 管理组件”说明）*“数据上传监控”按钮在点击后同样会弹出一个子窗口，具体如下图所示。

当禁用 WebDAV 相关设置项时的界面样例：

![屏幕截图_199_.png](https://s2.loli.net/2024/03/15/EMocDfxms21CeSb.png)

当启用 WebDAV 相关设置项时的界面样例：

![屏幕截图_202_.png](https://s2.loli.net/2024/03/15/aWx4fDmKIwYVOHh.png)

“数据上传管理”子窗口说明，当图中所示的监控路径下的文件发生变更时，子窗口中会实时给出提示。实际使用案例情境：当同时有多台终端和多位被试进行测试时，整理数据文件可能会成为一件麻烦事儿。系统在前面已经实现了数据云端同步，但还是缺少了提示信息。此功能组件可以帮助管理员更好地知晓网盘端数据信息的变更情况。如图所示（两幅图依次表示禁用以及启用 WebDAV 相关设置项时的子窗口界面样例）。

![屏幕截图_200_.png](https://s2.loli.net/2024/03/15/fYD78Fd1LboU6Sm.png)

![屏幕截图_201_.png](https://s2.loli.net/2024/03/15/b1VW8p4ZPQLGqeO.png)

## 四、数据文件说明

因为此软件系统除了警戒作业模拟外，还含有大量的数据分析内容，因此我们接下来将会单独介绍程序运行和被试作业的过程中生成的各类数据文件的结构。

### （一）数据目录介绍

#### 1. 本地存储

数据文件存储于“data”与“logs”两个文件夹内。“data”文件夹中的数据采用文件夹形式进行分类，命名依据为被试填写的信息。

需注意，当使用本地存储时，系统在文件导出完成后还可能会自动调用默认文本编辑器打开数据文件。

![屏幕截图_203_.png](https://s2.loli.net/2024/03/15/RCNir2vaB8TE1AZ.png)

![屏幕截图_204_.png](https://s2.loli.net/2024/03/15/SZF4U7onbsCEXl9.png)

#### 2. 云端网盘存储

数据文件存储于网盘根目录下的“appdata_upload”文件夹下。数据同样采用文件夹形式进行分类，命名依据为被试填写的信息。

![屏幕截图_205_.png](https://s2.loli.net/2024/03/15/nJvReZhtWoswPCG.png)

接下来，我们将会说明数据采用云端同步的另一大优势。

![1710492061114.jpg](https://s2.loli.net/2024/03/15/kAnTYMt2QaPbKqi.jpg)

![1710492061102.jpg](https://s2.loli.net/2024/03/15/dsO5XaBlPYW4Hjo.jpg)

如图所示，实验数据依托坚果云的同步功能，在移动端同样可以实时监控数据变化。这可以为后续项目管理提供极大的便利。这也是本系统创新性的一个案例体现。

### （二）警戒测试过程记录数据

**命名样例**：Tab_IV-Work-O-S_Test-Data_Collection_0002-231241024-测试人员-男-20240315-022521-022806.csv。

**命名格式**：页面编码（Tab_IV-Work-O-S）_ 测试数据记录（Test-Data_Collection）_被试信息（0002-231241024-测试人员-男-20240315-022521-022806）.文件格式（csv）。

**文件格式**：csv 数据表，我们建议使用 Excel 或 Notepad3 等软件打开。

**数据栏目**：显示轮次，面板编码，区间起点，区间终点，数字一，数字二，系统判定，被试反应，反应时间。（注：对于突发应急事件的记录在同一文件内，数据格式为，-1，“DashBoard_Emergency”，-1，-1，-1，-1，系统判定，被试反应，反应时间）

![屏幕截图_170_.png](https://s2.loli.net/2024/03/15/rwLepmxoQjb4inI.png)

### （三）心理特征量表抽测数据

**命名样例**：Tab_V-Work-E-S_Mental-Data_Collection_0016-231248256-测试人员-女-20240315-023853-024304.csv。

**命名格式**：页面编码（Tab_V-Work-E-S）_ 测试数据记录（Mental-Data_Collection）_被试信息（0016-231248256-测试人员-女-20240315-023853-024304）.文件格式（csv）。

**文件格式**：csv 数据表，我们建议使用 Excel 或 Notepad3 等软件打开。

**数据栏目**：显示轮次，量表作答，反应时间。其中，“量表作答”采用了数字索引形式，数字0到6分别对应“完全警觉，完全清醒”、“很有活力，反应灵敏，但非最好状态”、“情况一般，稍微清醒”、“有点累，不怎么清醒”、“挺累的，无精打采”、“非常疲惫，难以集中精神”以及“精疲力尽，无法有效地工作”这六种状态。

![屏幕截图_171_.png](https://s2.loli.net/2024/03/15/9aUJflxouyPgcWb.png)

### （四）程序日志文件备份数据

**命名样例**：LOG20240314-190658.log。

**命名格式**：日志文件（LOG）程序启动时间（20240314-190658）.文件格式（log）。

**文件格式**：log日志文件，我们建议使用 Notepad3 等软件打开。

![屏幕截图_172_.png](https://s2.loli.net/2024/03/15/qDGa64HhLAQfwot.png)
