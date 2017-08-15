# Linux的Python-pip

刚入手了一个Service，却发现Ubuntu16.0.4没有pip，默认的源是微软的.



- 添加源（163的源都可以）

> vim /etc/apt/sources.list #编辑源文件
>
> 进入vim普通模式按 `i或o或a` 进入编辑模式

```
deb http://cn.archive.ubuntu.com/ubuntu/ xenial main restricted universe multiverse
deb http://cn.archive.ubuntu.com/ubuntu/ xenial-security main restricted universe multiverse
deb http://cn.archive.ubuntu.com/ubuntu/ xenial-updates main restricted universe multiverse
deb http://cn.archive.ubuntu.com/ubuntu/ xenial-backports main restricted universe multiverse
## 测试版源
deb http://cn.archive.ubuntu.com/ubuntu/ xenial-proposed main restricted universe multiverse
# 源码
deb-src http://cn.archive.ubuntu.com/ubuntu/ xenial main restricted universe multiverse
deb-src http://cn.archive.ubuntu.com/ubuntu/ xenial-security main restricted universe multiverse
deb-src http://cn.archive.ubuntu.com/ubuntu/ xenial-updates main restricted universe multiverse
deb-src http://cn.archive.ubuntu.com/ubuntu/ xenial-backports main restricted universe multiverse
## 测试版源
deb-src http://cn.archive.ubuntu.com/ubuntu/ xenial-proposed main restricted universe multiverse
# Canonical 合作伙伴和附加
deb http://archive.canonical.com/ubuntu/ xenial partner
deb http://extras.ubuntu.com/ubuntu/ xenial main
### shadowsocks的源（翻墙服务搭建）
deb http://shadowsocks.org/ubuntu trusty main
deb http://shadowsocks.org/debian wheezy main
```



我这里是添加的测试版的源，ESC退出到普通模式    :wq!保存

然后更新源：

> `sudo apt-get update`
>
> `sudo apt-get upgraed`

### 安装pip：

>  `sudo apt-get install python-pip`

安装完成

> `pip -V` 出现了pip的版本：
>
> `pip 9.0.1 from /usr/local/lib/python2.7/dist-packages (python 2.7)`

这样我们就安装完成了，可以尽情装逼了

``` python
pip install Django
pip install wheel
pip install scrapy
```



通过`pip list`可以查看当前安装的模块

![如图](https://raw.githubusercontent.com/yoonasy/article/master/images/pip%20list.png)

出现了一个黄色的警告是提示你升级pip：

> `pip install --upgrade pip`

> pip uninstall scrapy # 卸载scrapy框架

当然除此之外还有很多，可以直接敲个pip就能出来帮助



还有一些很好的技术文章尽情戳知了课堂官方QQ：2156600937