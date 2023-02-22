#! /usr/bin/env python
import rospy
from service.srv import add, addRequest, addResponse


def add_num(req):
    sum = req.num1 + req.num2
    rospy.loginfo("service: sum = %d",sum)
    resp = addResponse()
    resp.sum = sum

    return resp
    pass

if __name__=="__main__":
    # 初始化节点
    rospy.init_node("service",anonymous=True)
    # 创建服务对象
    srv_1 = rospy.Service("add",add,add_num)
    # 循环使用回调函数
    rospy.spin()


