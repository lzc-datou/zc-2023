# SCP传输图片
> 2023.9.29

### 1. 简介
scp是一个linux命令行命令，基于ssh连接方式，可用于同一局域网下两台计算机之间传输文件和文件夹。但由于这个命令连接时需要进行ssh密钥验证，验证时间较长（零点几秒），所以要避免高频率反复连接（那样会很慢）。

## 2. ssh密钥认证
计算机A要与计算机B通过ssh密钥进行免密登录  
计算机A首先生成ssh密钥和公钥，然后将公钥发送给计算机B接收。然后这两台电脑就完成密钥认证了，可以通过ssh免密登录  
详细方法见[ssh免密钥登录(两种方法) 免秘钥](https://blog.csdn.net/chenxuecheng1984/article/details/115870404)或[linux系统ssh免密钥登录配置](https://blog.csdn.net/xiaoyi23000/article/details/80597516)

## 3. scp传输文件或文件夹
一般来说，使用scp传输文件需要输入目标电脑的用户名和密码，但是配置完ssh密钥认证之后就不需要了。

常用语法：
```bash
1. 文件拷贝到目录
scp local_file_path remote_username@remote_ip:remote_folder 
2. 目录拷贝到目录
scp local_folder remote_username@remote_ip:remote_folder 
3. 文件拷贝到文件
scp local_file_path remote_username@remote_ip:remote_file_path 
```
详细使用方法可自行上网搜索或者见[Linux scp命令](https://www.runoob.com/linux/linux-comm-scp.html)

## 4. python程序调用scp命令传输图片
可以让chatgpt帮你写，给他提好要求，可以有多种实现方法。目前在用的**文件夹拷贝到文件夹**的python程序如下：
```python
import subprocess
def send_img(remote_folder = folder,remote_username = username,remote_ip=ip):
    '''
    程序功能：将图片从机载电脑发送到地面段笔记本\n
    remote_folder:远程主机保存图片的文件夹（也就是接收到的图片在地面端笔记本上的保存路径)\n
    remote_username:远程主机用户名(地面端笔记本ubuntu用户名)\n
    remote_ip:远程主机ip地址(地面端笔记本ip地址)\n
    
    '''
    # 构造scp命令
    scp_command = f'scp -r {img_save_path} {remote_username}@{remote_ip}:{remote_folder}'
    # 使用pexpect执行scp命令
    subprocess.run(scp_command,shell=True)
```
该程序用到的所有参数都集成到了params.py文件中，方便修改和调用