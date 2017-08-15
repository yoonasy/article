# FTP传输

有的朋友可能购买了空间   但是FTP不太好管理
当然python就有ftp传输协议的模块


```
graph TD
连接FTP服务器-->登录
登录-->执行操作_请求服务器
执行操作_请求服务器-->退出
```


首先导入`ftplib`模块

```python
import ftplib # 导入FTP 模块
# 第一步：连接到服务器 参数为登录的服务器地址
ftp = ftplib.FTP( 'wkvs112****.dnswa.com' ) 
# 敲下ftp返回实例：
# <ftplib.FTP instance at 0x029F7738> 
# 第二步：登录
ftp.login( 'larxqf***', 't4rbQe***' )# 返回'230 OK. Current directory is /' ____230 Ok 登录成功
# 第三步：执行操作__这里通过dir显示目录内容
ftp.dir() # 返回了ftp目录列表
# 第四步：退出
ftp.quit() # 返回 '221 Goodbye.'
```

> 以上是简单的IDLE执行流程


| 方法                            | 解释                                       |
| ----------------------------- | ---------------------------------------- |
| `login( user='', passwd='' )` | 登录FTP服务器                                 |
| `pwd()`                       | 通过此方法可以获取当前所在目录与Linux类似                  |
| `cwd(path)`                   | 更改path工作目录路径                             |
| `dir([path[,cb]])`            | 显示path目录里的内容    cb回调函数  传递给retrlines()方法 |
| `nlst([path])`                | 和dir一样 返回的是文件详细信息的列表                     |
| `retrlines(cmd[,cb])`         | 给定FTP命令 用于下载文本文件  可空的回调函数用来处理文本的每一行      |
| `retrbinary()`                | 与上面方法相似   处理二进制文件                        |
| `storlines()`                 | 上传文件  参数为open打开后的对象                      |
| `storbinary()`                | 二进制 参数也是open返回的对象                        |
| `delete(path)`                | 删除位于path的远程文件                            |
| `mkd(directory)`              | 创建远程目录                                   |
| `rmd(directory)`              | 删除远程目录                                   |
| `quit()`                      | 关闭连接并退出                                  |

### 实例 FTP下载实例

```python

#!/usr/bin/env python
import ftplib
import socket,os

HOST = 'ftp.mozilla.org'
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'

def main():
    try:
        f = ftplib.FTP( host )
    except( socket.error, socket.gaierror )as e:
        print 'ERROR: cannot reach'%s %HOST
        return
    print '*** Connected to host"%s"' %HOST
    
    try:
        f.login()
    except ftplib.error_perm:
        print 'ERROR: cannot login anonymously'
        f.quit()
        return
    print '*** Logged in as "anonymous"'
    
    try:
        f.cwd(DIRN)
    except ftplib.error_perm:
        print 'ERROR: cannot CD to "%s"' %DIRN
        f.quit()
        return
    print '*** Changed to "%s" folder' %DIRN
    
    try:
        f.retrbinary( 'RETR %s' %FILE )
        os.unlink( FILE )
    else:
        print '*** Downloaded "%s" to CWD' %FILE
    f.quit()
    
    
if __name__ == '__main__':
    main()
        
```

想了解FTP对象更多信息，请参阅以下：

[ python交流群：526929231![image](http://pub.idqqimg.com/wpa/images/group.png)](http://shang.qq.com/wpa/qunwpa?idkey=91644f71013b35aafb647cfb95b643ccea29a46d83acc00bebd7d0b1727f54e2)





还有一些很好的技术文章尽情戳知了课堂官方QQ：2156600937