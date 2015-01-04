# PianoEmulator 帮助文档

### 第一部分 文件列表

```
PYQT-PIANO-EMULATOR
|
|   build.bat
|   keyboardMap.png
|   noteUtils.py
|   pianoBoard.bmp
|   pianoEmulator.py
|   piano_emulator.ui
|   ReadMe.html
|   ReadMe.markdown
|   ui.py
|           
\---music
```

- `pianoEmulator.py`为执行的主文件
- `piano_emulator.ui`和`ui.py`为UI部分
- `noteUtils.py`为音符弹奏的杂七杂八工具类
- `pianoBoard.bmp`是钢琴键盘图
- `keyboardMap.png`是键盘音符对应图
- `build.bat`使用cxfreeze编译

---

### 第二部分 软件使用介绍

打开软件后看到的界面如下

![fistScreen][firstscreen]

各个地方的功能如下

1. 简易钢琴键盘。鼠标点击琴键可以发出相应的声音。白键上注明了音阶和音度，两个白键之间的黑键为两白键之间的音。如第一个黑键在`F3`和`G3`之间，则它的音是`FG3`。
2. 音符长度控制菜单。控制点一下钢琴发出的音符的长度。可选1/2秒，1/4秒，1/8秒。
3. 插入空音符按钮。在下方的记录区插入一个空音符，空音符长度由音符长度控制菜单决定。
4. 录制开关。当按下时会自动在下方的记录框里记下播放出的音符。
5. 记录框。记录播放出的音符。
6. 载入按钮。从文本文件中载入音符序列到记录框中。
7. 保存按钮。根据文件扩展名不同，可以选择保存为文本文件以供下次加载。
8. 键盘弹奏区。在这个文本框里按下键盘会弹出相应音调，键盘和音调的对应图标在下方给出。
9. 清空按钮。清空记录区和键盘弹奏区。
10. 播放按钮。可以播放记录区里的音符序列。

<br />
键盘音符对应图
![keyboardMap][keyboardMap]

键盘到音符的映射可以很方便的通过修改代码来完成，关键代码在`noteUtils.py`文件中

```Python
% 键盘和音符的对应Map
KEYMAP_KEY = ['1', '2', '3', '4', '5', '6', '7',
              'q', 'w', 'e', 'r', 't', 'y', 'u',
              'a', 's', 'd', 'f', 'g', 'h', 'j',
              'z', 'x', 'c', 'v', 'b', 'n', 'm']
KEYMAP_NOTE = [scale + str(degree) for degree in range(6, 2, -1)
               for scale in ['C', 'D', 'E', 'F', 'G', 'A', 'B']]
```

通过修改这里的映射关系，就可以决定按哪个键出哪个音符了。

---

### 第三部分 参考资料

[PyQt Class Reference][pyqt_ref]

[StackOverflow][sof]

---

END

Author: 7sDream

FinishTime: 2015.1.4

  [firstscreen]: http://ww4.sinaimg.cn/large/88e401f0gw1enxc8rdp4uj20ax09gjsi.jpg
  [keyboardMap]: http://ww4.sinaimg.cn/large/88e401f0tw1enuc4zmmvcj20ks06bmys.jpg
  [pyqt_ref]: http://pyqt.sourceforge.net/Docs/PyQt4/classes.html
  [sof]: http://stackoverflow.com/questions/307305/play-a-sound-with-python