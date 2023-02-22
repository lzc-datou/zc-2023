#include <sys/stat.h>
#include "../include/Identity.h"
#include "../include/Student.h"
#include "../include/Teacher.h"
#include "../include/Manager.h"

void logIn(string fileName, int type);

void managerMenu(Identity *&manager);
void studentMenu(Identity *&student);
void teacherMenu(Identity *&teacher);
int main()
{

    int select = 0;

    while (true)
    {
        cout << "欢迎来到机房预约系统" << endl;
        cout << "请输入对应数字选择相应的身份进行登录" << endl;
        cout << "1.学生代表" << endl;
        cout << "2.老师" << endl;
        cout << "3.管理员" << endl;
        cout << "0.退出" << endl;

        cin >> select;
        switch (select)
        {
        case 1:
            // 学生代表
            // 登录
            logIn(STUDENT_FILE, 1);
            break;
        case 2:
            // 老师
            // 登录
            logIn(TEACHER_FILE, 2);

            break;
        case 3:
            // 管理员
            // 登录
            logIn(ADMIN_FILE, 3);

            break;
        case 0:
            // 退出
            cout << "欢迎下次使用" << endl;
            system("read");
            exit(0);
            break;
        default:
            cout << "您的输入有误，请重新输入" << endl;
            system("read");
            system("clear");
            break;
        }
    }

    // 通过判断宏定义根据不同的操作系统调用不同的命令行命令以实现暂停
#ifdef linux
    cout << "it's linux OS" << endl;
    system("read");
#endif
#ifdef _WIN64
    system("pause");
#endif
    return 0;
}

void logIn(string fileName, int type)
{
    // 1 学生   2 老师  3 管理员
    // 定义父类指针
    Identity *person = NULL;

    // 打开文件
    fstream in_file(fileName, ios::in);
    // 注意：相对路径的基准是执行make命令的目录

    // 判断文件是否存在,不存在则创建
    if (!in_file.is_open())
    {
        in_file.close();

        // 创建文件
        mkdir("document", 0777);        // 先创建文件夹
        ofstream create_file(fileName); // 再创建文件  此命令只能在有文件夹的基础上创建文件
        cout << create_file.is_open() << endl;
        cout << "文件不存在，但现已创建" << endl;
        create_file.close();

        return;
    }

    // 输入登录信息

    // 定义接收变量
    int id = 0;
    string name;
    string pwd;

    // 教师与学生有id号而管理员没有
    if (type == 1)
    {
        cout << "请输入您的学号" << endl;
        cin >> id;
    }
    else if (type == 2)
    {
        cout << "请输入您的教师编号" << endl;
        cin >> id;
    }
    cout << "请输入您的姓名" << endl;
    cin >> name;
    cout << "请输入您的密码" << endl;
    cin >> pwd;

    // 分别验证登录

    if (type == 1)
    {
        // 学生验证登录
        int fid; // file_id
        string fname;
        string fpwd;

        // 只有当从文件中读取的数据与定义的数据类型匹配时条件才为真，即读取的数据需要为 int string string 循环方可，否则就跳出循环了
        while (in_file >> fid && in_file >> fname && in_file >> fpwd)
        {
            // cout << "fid = " << fid << endl;
            // cout << "fname = " << fname << endl;
            // cout << "fpwd = " << fpwd << endl;
            if (fid == id && fname == name && fpwd == pwd)
            {

                cout << "登录成功" << endl;
                system("read");
                system("clear");
                // 父类指针接收子类指针
                person = new Student(id, name, pwd);
                studentMenu(person);
                return;
            }
        }
    }

    else if (type == 2)
    {
        // 老师验证登录
        int fid; // file_id
        string fname;
        string fpwd;

        // 只有当从文件中读取的数据与定义的数据类型匹配时条件才为真，即读取的数据需要为 int string string 循环方可，否则就跳出循环了
        while (in_file >> fid && in_file >> fname && in_file >> fpwd)
        {

            if (fid == id && fname == name && fpwd == pwd)
            {

                cout << "登录成功" << endl;
                system("read");
                system("clear");
                // 父类指针接收子类指针
                person = new Teacher(id, name, pwd);
                teacherMenu(person);
                return;
            }
        }
    }
    else if (type == 3)
    {
        // 管理员验证登录
        string fname;
        string fpwd;

        // 只有当从文件中读取的数据与定义的数据类型匹配时条件才为真，即读取的数据需要为 int string string 循环方可，否则就跳出循环了
        while (in_file >> fname && in_file >> fpwd)
        {

            if (fname == name && fpwd == pwd)
            {

                cout << "登录成功" << endl;
                system("read");
                system("clear");
                // 父类指针接收子类指针
                person = new Manager(name, pwd);
                managerMenu(person);
                return;
            }
        }
    }

    // 如果验证失败
    cout << "登录失败" << endl;
    system("read");
    system("clear");
    return;
}

void managerMenu(Identity *&manager)
{
    while (true)
    {
        manager->openMenu();

        Manager *man = (Manager *)manager;

        int select = 0;
        cin >> select;

        if (select == 1)
        {
            cout << "添加账号" << endl;
            man->addPerson();
        }
        else if (select == 2)
        {
            cout << "查看账号" << endl;
            man->showPerson();
        }
        else if (select == 3)
        {
            cout << "查看机房" << endl;
            man->showComputer();
        }
        else if (select == 4)
        {
            cout << "清空预约" << endl;
            man->cleanFile();
        }
        else
        {
            delete manager;
            cout << "注销成功" << endl;
            system("read");
            system("clear");
            return;
        }
    }
}
void studentMenu(Identity *&student)
{

    while (true)
    {
        student->openMenu();
        Student *stu = (Student *)student;

        int select = 0;
        cin >> select;
        if (select == 1)
        {
            cout << "申请预约" << endl;
            stu->applyOrder();
        }
        else if (select == 2)
        {
            cout << "查看自身预约" << endl;
            stu->showMyOrder();
        }
        else if (select == 3)
        {
            cout << "查看所有预约" << endl;
            stu->showAllOrder();
        }
        else if (select == 4)
        {
            cout << "取消预约" << endl;
            stu->cancelOrder();
        }
        else
        {
            delete student;
            cout << "注销成功" << endl;
            system("read");
            system("clear");
            return;
        }
    }
}
void teacherMenu(Identity *&teacher)
{
    while (true)
    {
        teacher->openMenu();

        Teacher *t = (Teacher *)teacher;

        int select = 0;
        cin >> select;

        if (select == 1)
        {
            cout << "查看所有预约" << endl;
            t->showAllOrder();
        }
        else if (select == 2)
        {
            cout << "审核预约" << endl;
            t->auditOrder();
        }
        else
        {
            delete teacher;
            cout << "注销成功" << endl;
            system("read");
            system("clear");
            return;
        }
    }
}