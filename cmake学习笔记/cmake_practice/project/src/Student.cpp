#include "../include/Student.h"

// 默认构造

Student::Student()
{
}

// 有参构造 学号，姓名，密码
Student::Student(int id, string name, string pwd)
{
    this->m_id = id;
    this->m_name = name;
    this->m_pwd = pwd;

    // 读取机房信息
    ifstream ifs2(COMPUTER_FILE, ios::in);
    if (!ifs2.is_open())
    {
        cout << "机房文件打开失败" << endl;
        return;
    }
    ComputerRoom com;
    while (ifs2 >> com.m_id && ifs2 >> com.m_capacity)
    {
        Vcom.push_back(com);
    }
    ifs2.close();
}

// 菜单界面 重写纯虚函数
void Student::openMenu()
{
    cout << "欢迎学生代表： " << this->m_name << " 登录！" << endl;
    cout << "1.申请预约" << endl;
    cout << "2.查看我的预约" << endl;
    cout << "3.查看所有预约" << endl;
    cout << "4.取消预约" << endl;
    cout << "0.注销登录" << endl;
    cout << "请选择您的操作" << endl;
}

// 申请预约
void Student::applyOrder()
{
    int date = 0;
    int interval = 0;
    int room = 0;
    cout << "机房开放时间为周一至周五" << endl;
    cout << "请输入申请预约的时间：" << endl;
    cout << "1.周一" << endl;
    cout << "2.周二" << endl;
    cout << "3.周三" << endl;
    cout << "4.周四" << endl;
    cout << "5.周五" << endl;

    // 检测输入日期是否正确
    while (true)
    {
        cin >> date;
        if (date >= 1 && date <= 5)
        {
            break;
        }
        cout << "输入有误，请重新输入" << endl;
    }

    cout << "请输入预约的时间段" << endl;
    cout << "1.上午" << endl;
    cout << "2.下午" << endl;
    while (true)
    {
        cin >> interval;
        if (interval == 1 || interval == 2)
        {
            break;
        }
        cout << "输入有误，请重新输入" << endl;
    }

    cout << "请选择机房：" << endl;
    cout << "1号机房容量：" << Vcom[0].m_capacity << endl;
    cout << "2号机房容量：" << Vcom[1].m_capacity << endl;
    cout << "3号机房容量：" << Vcom[2].m_capacity << endl;
    while (true)
    {
        cin >> room;
        if (room >= 1 && room <= 3)
        {
            break;
        }
        cout << "输入有误，请重新输入" << endl;
    }

    cout << "预约成功，审核中！" << endl;

    // 写入预约信息
    ofstream ofs(ORDER_FILE, ios::app);
    if (!ofs.is_open())
    {
        cout << "预约文件打开失败" << endl;
        return;
    }
    ofs << "date:" << date << "  ";
    if (interval == 1)
    {
        ofs << "interval:"
            << "上午  ";
    }
    else
    {
        ofs << "interval:"
            << "下午  ";
    }
    ofs << "stuId:" << this->m_id << "  ";
    ofs << "stuName:" << this->m_name << "  ";
    ofs << "roomId:" << room << "  ";
    ofs << "status:审核中" << endl;
    ofs.close();
    system("read");
    system("clear");
}

// 查看我的预约
void Student::showMyOrder()
{
    OrderFile order;
    if (order.m_orderData.size() == 0)
    {
        cout << "无预约记录" << endl;
        return;
    }

    int num = 0; // 计数,告知学生自己当前共有几条预约
    for (int i = 0; i < order.m_orderData.size(); i++)
    {
        // 如果学号匹配，则为自身预约
        if (atoi(order.m_orderData[i]["stuId"].c_str()) == this->m_id)
        {
            num++;
        }
    }
    cout << "您当前共有" << num << "条预约" << endl;
    cout << endl;

    for (int i = 0; i < order.m_orderData.size(); i++)
    {

        if (atoi(order.m_orderData[i]["stuId"].c_str()) == this->m_id)
        {
            cout << "预约日期：周" << order.m_orderData[i]["date"] << "  ";
            cout << "预约时段：" << order.m_orderData[i]["interval"] << "  ";
            cout << "机房：" << order.m_orderData[i]["roomId"] << "  ";
            cout << "状态：" << order.m_orderData[i]["status"] << "  " << endl;
            cout << endl;
        }
    }
    system("read");
    system("clear");
    return;
}

// 查看所有预约
void Student::showAllOrder()
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

// 取消预约
void Student::cancelOrder()
{
    OrderFile order;
    if (order.m_orderData.size() == 0)
    {
        cout << "无预约记录" << endl;
        return;
    }
    cout << "审核中或预约成功的记录可以取消" << endl;
    cout << endl;

    // 用于记录map容器对应下标
    vector<int> v;
    // 记录显示给用户的记录下标
    int index = 0;
    for (int i = 0; i < order.m_orderData.size(); i++)
    {
        // 找到自身的预约
        if (atoi(order.m_orderData[i]["stuId"].c_str()) == this->m_id)
        {
            // 在自身预约中找到状态为审核中或预约成功的预约
            if (order.m_orderData[i]["status"] == "审核中" || order.m_orderData[i]["status"] == "预约成功")
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
    }
    cout << "请输入需要取消的预约,0表示退出" << endl;
    int select = -1;
    while (true)
    {
        cin >> select;
        if (select >= 0 && select < v.size())
        {
            if (select == 0)
            {
                cout << "退出成功" << endl;
                break;
            }
            else
            {
                order.m_orderData[v[select - 1]]["status"] = "取消预约";
                order.updateOrder();
                cout << "已取消预约" << endl;
                break;
            }
        }
        cout << "输入有误，请重新输入" << endl;
    }
    system("read");
    system("clear");
}
