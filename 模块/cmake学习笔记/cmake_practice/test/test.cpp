#include <iostream>
#include <fstream>
#include <map>
using namespace std;

class OrderFile
{
public:
    // 构造函数
    OrderFile();

    // 更新预约记录
    void updateOrder();

    // 预约记录的储存容器  map
    // int 表示记录的条数，每条记录再用一个map容器保存
    map<int, map<string, string>> m_orderData;

    // 预约记录的条数
    int m_size;
};
// 提取键值对的key值和value值,并返回一个键值对
pair<string, string> fetchKV(string s)
{
    // 找到字符串中冒号的位置
    int pos = s.find(":");
    // substr(截取的起始位置，截取的长度)
    string key = s.substr(0, pos);
    string value = s.substr(pos + 1, s.size() - pos - 1);
    cout << "key=" << key << "  "
         << "value=" << value << endl;
    return make_pair(key, value);
}

OrderFile::OrderFile()
{
    ifstream ifs("../order.txt", ios::in);

    string date;     // 日期
    string interval; // 时间段
    string stuId;    // 学号
    string stuName;  // 姓名
    string roomId;   // 机房号
    string status;   // 申请的状态

    this->m_size = 0;

    while (ifs >> date && ifs >> interval && ifs >> stuId && ifs >> stuName && ifs >> roomId && ifs >> status)
    {
        map<string, string> m;
        cout << date << "  " << interval << endl;
        m.insert(fetchKV(date));
        m.insert(fetchKV(interval));
        m.insert(fetchKV(stuId));
        m.insert(fetchKV(stuName));
        m.insert(fetchKV(roomId));
        m.insert(fetchKV(status));
        cout << "m_size=" << this->m_size << endl;
        this->m_orderData.insert(make_pair(this->m_size, m));
        this->m_size++;
    }
    // 测试map容器是否生成成功
    for (int i = 0; i < this->m_orderData.size(); i++)
    {
        cout << m_orderData.size() << endl;

        cout << "date=" << m_orderData[i]["date"] << "  ";
        cout << "interval=" << m_orderData[i]["interval"] << "  " << endl;
    }
    ifs.close();
}
int main()
{
    OrderFile order;
}
