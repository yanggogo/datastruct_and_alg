# Crash工具使用

## Crash工具使用

以ubuntu为例
参考自：https://askubuntu.com/questions/859125/make-flex-command-not-found

1. 下载linux源码

apt-get install linux-source

apt-get install libncurses5-dev

tar -jxf /usr/src/linux-source-4.15.0/linux-source-4.15.0.tar.bz2 -C /usr/src/

2. 编译linux源码

cp /boot/config-4.15.0-88-generic /usr/src/linux-source-4.15.0/.config

make -j8

中间遇到的问题基本上用apt-get install安装解决
