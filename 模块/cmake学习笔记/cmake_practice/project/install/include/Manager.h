#pragma once
#include "Identity.h"
#include "Student.h"
#include "Teacher.h"

class Manager : public Identity
{
public:
    // 默认构造
    Manager();

    // 有参构造
    Manager(string name, string pwd);

    // 存放老师和学生信息的容器
    vector<Student> Vstu;
    vector<Teacher> Vtea;
    vector<ComputerRoom> Vcom;
    // 初始化容器函数
    void initVector();

    // 菜单
    virtual void openMenu();

    // 添加账号
    void addPerson();

    // 检测添加的账号是否重复
    bool checkRepeat(int id, int type);

    //  查看账号
    void showPerson();

    // 查看机房信息
    void showComputer();

    // 清除预约记录
    void cleanFile();
};