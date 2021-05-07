# lrc-timetag-change  
将lrc歌词的时间标签整体提前或推迟  
想把以前下载的一些歌配上歌词，但有的歌词比歌曲整体慢了几秒，一句句手改就太麻烦了，于是写了这个python脚本，顺便练练手，将lrc中的时间标签全部加或减一点儿。(当然，要手动听一下确认要加还是减，加减的幅度)  
本来lrc是支持时间补偿的，就是在前面注释的位置加上`[Offset:毫秒数]`就可以，但我的播放器不支持这样，只好改一下时间标签了。  
## 说明  
因为是覆盖保存，使用前请备份您要修改的文件。  
如果出现文件编码不支持，请将 .lrc 文件以 UTF-8 保存。可以用记事本打开>文件>另存为>编码，选择 UTF-8 保存。  
## 使用方法  
> **1.** 输入要修改的 .lrc 文件名，若不在同一目录下，需输入完整路径，带不带引号均可。  
例： `TheStar-阿泱.lrc`，`D:\Desktop\TheStar-阿泱.lrc`，`“D:\Desktop\TheStar-阿泱.lrc”` 等。  
> **2.** 输入歌词要提前的时间，单位为秒(s)，推迟时间用负数。  
例： `1`，`0.5`，`-2` 等。  
> **3.** 确认覆盖并保存。   

## 完整代码  

[查看完整代码](https://github.com/mlyde/lrc-timetag-change/blob/main/lrc-timetag-change.py) (2021.5 by mlyde)  

[下载Windows命令行程序](https://github.com/mlyde/lrc-timetag-change/raw/main/lrc-timetag-change.exe) (用`pyinstaller`编译为exe，大小：6.53MB，无python环境可下载运行)  
