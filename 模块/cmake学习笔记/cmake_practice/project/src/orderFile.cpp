#include "../include/orderFile.h"

// 提取键值对的key值和value值,并返回一个键值对
pair<string, string> fetchKV(string s)
{
    // 找到字符串中冒号的位置
    int pos = s.find(":");
    // substr(截取的起始位置，截取的长度)
    string key = s.substr(0, pos);
    string value = s.substr(pos + 1, s.size() - pos - 1);

    return make_pair(key, value);
}

OrderFile::OrderFile()
{
    ifstream ifs(ORDER_FILE, ios::in);

    string date;     // 日期
    string interval; // 时间段
    string stuId;    // 学号
    string stuName;  // 姓名
    string roomId;   // 机房号
    string status;   // 申请的状态

    this->m_size = 0;

    while (ifs >> date && ifs >> interval && ifs >> stuId && ifs >> stuName && ifs >> roomId && ifs >> status)
    { // 注意：此处map需要定义在循环内部，使得每次使用的都是一个全新的空map
        map<string, string> m;

        m.insert(fetchKV(date));
        m.insert(fetchKV(interval));
        m.insert(fetchKV(stuId));
        m.insert(fetchKV(stuName));
        m.insert(fetchKV(roomId));
        m.insert(fetchKV(status));
        this->m_orderData.insert(make_pair(this->m_size, m));
        this->m_size++;
    }
    // // 测试map容器是否生成成功
    // for (int i = 0; i < this->m_orderData.size(); i++)
    // {
    //     cout << m_orderData.size();
    //     cout << "date=" << m_orderData[i]["date"] << "  ";
    //     cout << "interval=" << m_orderData[i]["interval"] << "  " << endl;
    // }
    ifs.close();
}

void OrderFile::updateOrder()
{
    if (m_orderData.size() == 0)
    {
        return;
    }

    // 重新创建文件
    ofstream ofs(ORDER_FILE, ios::out | ios::trunc);

    for (int i = 0; i < m_orderData.size(); i++)
    {
        // 将最新的预约记录写入文件中
        ofs << "date:" << m_orderData[i]["date"] << "  ";
        ofs << "interval:" << m_orderData[i]["interval"] << "  ";
        ofs << "stuId:" << m_orderData[i]["stuId"] << "  ";
        ofs << "stuName:" << m_orderData[i]["stuName"] << "  ";
        ofs << "roomId:" << m_orderData[i]["roomId"] << "  ";
        ofs << "status:" << m_orderData[i]["status"] << endl;
    }
    ofs.close();
}
