#include "../include/Teacher.h"

// 默认构造
Teacher::Teacher()
{
}

// 有参构造
Teacher::Teacher(int empId, string name, string pwd)
{
    this->m_empId = empId;
    this->m_name = name;
    this->m_pwd = pwd;
}

// 菜单界面
void Teacher::openMenu()
{
    cout << "欢迎教师： " << this->m_name << "登录！" << endl;
    cout << "1.查看所有预约" << endl;
    cout << "2.审核预约" << endl;
    cout << "0.注销登录" << endl;
    cout << "请选择您的操作" << endl;
}

// 查看所有预约
void Teacher::showAllOrder()
{
    OrderFile order;
    cout << "当前总共有" << order.m_orderData.size() << "条预约" << endl;
    for (int i = 0; i < order.m_orderData.size(); i++)
    {

        cout << endl;
        // 通过下标匹配key值的方式来获取value值
        cout << "第" << i + 1 << "条"
             << "  ";
        cout << "date:" << order.m_orderData[i]["date"] << "  ";
        cout << "interval:" << order.m_orderData[i]["interval"] << "  ";
        cout << "stuId:" << order.m_orderData[i]["stuId"] << "  ";
        cout << "stuName:" << order.m_orderData[i]["stuName"] << "  ";
        cout << "roomId:" << order.m_orderData[i]["roomId"] << "  ";
        cout << "status:" << order.m_orderData[i]["status"] << endl;

        cout << endl;
    }
    system("read");
    system("clear");
    return;
}

// 审核预约  课程中用的名字是validOrder(); 我认为意思不准确
void Teacher::auditOrder()
{
    system("clear");
again:
    this->openMenu();
    OrderFile order;
    if (order.m_orderData.size() == 0)
    {
        cout << "无预约记录" << endl;
        return;
    }
    cout << "待审核的预约如下：" << endl;
    cout << endl;

    // 用于记录map容器对应下标
    vector<int> v;
    // 记录显示给用户的记录下标
    int index = 0;
    for (int i = 0; i < order.m_orderData.size(); i++)
    {
        // 找到审核中的预约
        if (order.m_orderData[i]["status"] == "审核中")
        {

            index++;
            v.push_back(i);

            cout << index << "、"
                 << "  ";
            cout << "预约日期：周" << order.m_orderData[i]["date"] << "  ";
            cout << "预约时段：" << order.m_orderData[i]["interval"] << "  ";
            cout << "机房：" << order.m_orderData[i]["roomId"] << "  ";
            cout << "状态：" << order.m_orderData[i]["status"] << "  " << endl;
            cout << endl;
        }
    }
    cout << "请输入审核的预约记录，0表示退出" << endl;
    int select = -1;
    int shenHe = -1;
    while (true)
    {
        cin >> select;
        if (select >= 0 && select <= v.size())
        {
            if (select == 0)
            {
                cout << "退出成功" << endl;
                break;
            }
            else
            {
                while (true)
                {
                    cout << "请输入审核结果" << endl;
                    cout << "1.审核通过" << endl;
                    cout << "2.审核不通过" << endl;
                    cin >> shenHe;
                    if (shenHe == 1)
                    {
                        order.m_orderData[v[select - 1]]["status"] = "预约成功";
                        order.updateOrder();
                        cout << "审核通过成功" << endl;
                        system("read");
                        system("clear");
                        goto again;
                    }
                    else if (shenHe == 2)
                    {
                        order.m_orderData[v[select - 1]]["status"] = "预约失败";
                        order.updateOrder();
                        cout << "审核不通过成功" << endl;
                        system("read");
                        system("clear");
                        goto again;
                    }
                    else
                    {
                        cout << "输入有误，请重新输入" << endl;
                    }
                }
                break;
            }
        }
        cout << "输入有误，请重新输入" << endl;
    }
    system("read");
    system("clear");
}