# mount

## mount

将一个已存在的目录，mount到新的格式化的 /dev/sda 盘后，原来目录下的内容“丢失”了
如果将该设备从新umount，又可以看到丢失的文件。

测试步骤如下：

```
mkdir /root/test_dir
touch a

lsscsi

/dev/sda

echo y | mkfs.ext3 /dev/sda && mount /dev/sda /root/test_dir/
// 可以看到/root/test_dir/a 文件看不到了，但是实际上还是存在原来的默认dev设备内

umount /dev/sda
touch b

// 可以看到原来的 /root/test_dir/a 文件又可以看到了，但是/root/test_dir/b 又消失了

```