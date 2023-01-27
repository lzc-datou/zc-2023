#pragma once
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <algorithm>
#include "globalFile.h"
#include "computerRoom.h"

using namespace std;

class Identity
{
public:
    virtual void openMenu() = 0;

    string m_name; // 姓名
    string m_pwd;  // 密码
};