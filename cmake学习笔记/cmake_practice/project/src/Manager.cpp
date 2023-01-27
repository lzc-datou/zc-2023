#include "../include/Manager.h"

// 默认构造
Manager::Manager()
{
}

// 有参构造
Manager::Manager(string name, string pwd)
{
    this->m_name = name;
    this->m_pwd = pwd;

    this->initVector();
}
// 初始化容器函数
void Manager::initVector()
{
    // 清除容器，避免重复读取
    this->Vstu.clear();
    this->Vtea.clear();
    this->Vcom.clear();
    // 读取学生信息
    ifstream ifs(STUDENT_FILE, ios::in);

    if (!ifs.is_open())
    {
        cout << "学生文件打开失败" << endl;
        return;
    }

    Student s;
    while (ifs >> s.m_id && ifs >> s.m_name && ifs >> s.m_pwd)
    {
        Vstu.push_back(s);
    }
    cout << "当前学生数量为:" << Vstu.size() << endl;
    ifs.close();

    // 读取老师信息
    ifstream ifs1(TEACHER_FILE, ios::in);

    if (!ifs1.is_open())
    {
        cout << "老师文件打开失败" << endl;
        return;
    }

    Teacher t;
    while (ifs1 >> t.m_empId && ifs1 >> t.m_name && ifs1 >> t.m_pwd)
    {
        Vtea.push_back(t);
    }
    cout << "当前老师数量为:" << Vtea.size() << endl;
    ifs1.close();

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
    cout << "当前机房数量为： " << Vcom.size() << endl;
    ifs2.close();
}
// 检测添加的账号是否重复,重复返回true，不重复返回false
bool Manager::checkRepeat(int id, int type)
{
    // type=1为学生
    if (type == 1)
    {
        for (int i = 0; i < Vstu.size(); i++)
        {
            if (Vstu[i].m_id == id)
            {
                return true;
            }
        }
    }
    // type=2或其他为老师
    else
    {
        for (int i = 0; i < Vtea.size(); i++)
        {
            if (Vtea[i].m_empId == id)
            {
                return true;
            }
        }
    }

    // 如果都没有重复，返回false
    return false;
}
// 菜单
void Manager::openMenu()
{
    cout << "欢迎管理员:" << this->m_name << "登录！" << endl;
    cout << "1.添加账号" << endl;
    cout << "2.查看账号" << endl;
    cout << "3.查看机房" << endl;
    cout << "4.清空预约" << endl;
    cout << "0.注销登录" << endl;
    cout << "请选择您的操作" << endl;
}

// 添加账号
void Manager::addPerson()
{
    cout << "请输入添加账号的类型" << endl;
    cout << "1.添加学生" << endl;
    cout << "2.添加老师" << endl;

    string fileName;
    string tip;      // 添加id的提示
    string errorTip; // 添加错误提示
    ofstream ofs;

    int select = 0;

    while (true)
    {
        cin >> select;
        if (select == 1)
        {
            fileName = STUDENT_FILE;
            tip = "请输入您的学号";
            errorTip = "学号重复，请重新输入";
            break;
        }
        else if (select == 2)
        {
            fileName = TEACHER_FILE;
            tip = "请输入您的教师编号";
            errorTip = "教师编号重复，请重新输入";
            break;
        }
        else
        {
            cout << "您的选择有误，请重新选择" << endl;
        }
    }

    // 输入编号
    int id = 0;
    cout << tip << endl;
rpt: // repeat
    cin >> id;
    if (checkRepeat(id, select))
    {
        cout << errorTip << endl;
        goto rpt;
    }
    // 输入姓名
    string name;
    cout << "请输入您的姓名" << endl;
    cin >> name;

    // 输入密码
    string pwd;
    cout << "请输入您的密码" << endl;
    cin >> pwd;

    // 写入文件
    ofs.open(fileName, ios::out | ios::app);
    ofs << id << " " << name << " " << pwd << endl;
    cout << "添加账号成功!" << endl;
    system("read");
    system("clear");
    initVector();
    return;
}
// 打印老师信息
void printTea(Teacher &t)
{
    cout << "教师编号： " << t.m_empId << " "
         << "姓名： " << t.m_name << " "
         << "密码： " << t.m_pwd << endl;
}
// 打印学生信息
void printStu(Student &s)
{
    cout << "学号： " << s.m_id << " "
         << "姓名： " << s.m_name << " "
         << "密码： " << s.m_pwd << endl;
}
// 查看账号
void Manager::showPerson()
{
    cout << "请选择查看内容" << endl;
    cout << "1.查看所有学生" << endl;
    cout << "2.查看所有老师" << endl;

    int select = 0;
    cin >> select;

    if (select == 1)
    {
        cout << "所有学生的信息如下：" << endl;

        // 注意：for_each()算法不能操作成员函数
        for_each(Vstu.begin(), Vstu.end(), printStu);
    }
    else
    {
        cout << "所有老师的信息如下：" << endl;
        for_each(Vtea.begin(), Vtea.end(), printTea);
    }
    system("read");
    system("clear");
}

void printComRoom(ComputerRoom &com)
{
    cout << com.m_id << "号机房  "
         << "容量： " << com.m_capacity << endl;
}
// 查看机房信息
void Manager::showComputer()
{
    cout << "目前共有" << Vcom.size() << "个机房" << endl;
    for_each(Vcom.begin(), Vcom.end(), printComRoom);
    system("read");
    system("clear");
}

// 清除预约记录
void Manager::cleanFile()
{ // trunc方式打开文件，如果文件原来存在，则会删除该文件并重新创建
    ofstream ofs(ORDER_FILE, ios::trunc);
    ofs.close();

    cout << "清空成功！" << endl;
    system("read");
    system("clear");
}
