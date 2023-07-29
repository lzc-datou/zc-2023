import os
import random
import shutil
import sys

global rate
rate = 10 #每rate个取1

def rundistribute(path):
    path1=path+'/Image'
    path2=path+'/Label'
    os.mkdir(path1)
    os.mkdir(path1+'/Train')
    os.mkdir(path1+'/Val')
    os.mkdir(path2)
    os.mkdir(path2+'/Train')
    os.mkdir(path2+'/Val')
    T=1
    flag=1
    for x in os.listdir(path+'/image'):
        T=T-1
        flag=flag-1
        if T==0:
            T=rate
            random.seed()
            flag=random.randint(0,rate-1)
        namx,formatx=os.path.splitext(x)
        
        if flag==0:
            try:
                shutil.move(path+'/label/'+namx+'.txt',path2+'/Val/'+namx+'.txt')
            except FileNotFoundError:
                print('%s.txt do not exist'%(namx))
                os.remove(path+'/image/'+x)
            else:
                shutil.move(path+'/image/'+x,path1+'/Val/'+x)
            
        else:
            try:
                shutil.move(path+'/label/'+namx+'.txt',path2+'/Train/'+namx+'.txt')
            except FileNotFoundError:
                print('%s.txt do not exist'%(namx))
                os.remove(path+'/image/'+x)
            else:
                shutil.move(path+'/image/'+x,path1+'/Train/'+x)
    for y in os.listdir(path+'/label'):
        namy,formaty=os.path.splitext(y)
        print('%s.jpg do not exist\n'%(namy))
        os.remove(path+'/label/'+y)
    os.rmdir(path+'/label')
    os.rmdir(path+'/image')

if __name__=='__main__':
    path=sys.argv[1]
    if path=='--help':
        print('启动指令：\n')
        print('python3 distribute.py ./总文件夹路径\n')
        print('修改全局变量rate以改变选取概率')
        exit(0)
    rundistribute(path)
    


