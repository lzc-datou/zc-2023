#pragma once
#include "Identity.h"
#include "orderFile.h"

class Teacher : public Identity
{
public:
    // 默认构造
    Teacher();

    // 有参构造
    Teacher(int empId, string name, string pwd);

    // 菜单界面
    virtual void openMenu();

    // 查看所有预约
    void showAllOrder();

    // 审核预约  课程中用的名字是validOrder(); 我认为意思不准确
    void auditOrder();

    // 教师编号
    int m_empId;
};