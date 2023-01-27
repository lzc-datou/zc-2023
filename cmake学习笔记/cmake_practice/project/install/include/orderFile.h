#pragma once
#include "Identity.h"

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