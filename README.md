# FTPImageRender
根据一张经典FTP分级图，根据群友的数据，添加头像至图片。不用再每次打开photoshop进行手动编辑，一劳永逸。
## 效果
![!image](https://github.com/209jkjkjk/FTPImageRender/blob/master/READMEImage/%E6%95%88%E6%9E%9C%E5%9B%BE.png)
## 使用方法
1. 手动输入配置
- **第一行和无效数据行会被忽略**
- 姓名目前并无实际用处
- 其中“工体比”和“FTP与体重”只用输入一项，如果都输入，最终以“工体比”为准。
- 头像为文件路径

![!image](https://github.com/209jkjkjk/FTPImageRender/blob/master/READMEImage/%E9%85%8D%E7%BD%AE.png)

2. 运行main.py文件文件中的main函数
## 已知缺陷
- 当同一行的头像过多时，程序会报错，目前还没有改进。可以考虑手动增大最终的图片效果
- 就如同输入的数据，仅对阈值工体比进行头像插入
- 使用起来不够直观
