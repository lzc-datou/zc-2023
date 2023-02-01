#! /usr/bin/env python
import rospy
# 从包.srv中导入add.srv相关内容
from service.srv import add, addRequest, addResponse

if __name__=="__main__":
    rospy.init_node("client",anonymous=True)

    client = rospy.ServiceProxy("add",add)

    # 等待服务启动再提交请求
    client.wait_for_service()

    req = addRequest()
    num1 = 1
    num2 = 2
    rate = rospy.Rate(0.5)
    while(True):
        req.num1 = num1
        req.num2 = num2
        
        resp = client.call(req)
        rospy.loginfo("client: %d + %d = %d", req.num1, req.num2, resp.sum)
        num1 = num1 + 1
        num2 = num2 + 1
        if rospy.has_param("p_double"):
            p_double = rospy.get_param("p_double")
            rospy.loginfo("p_double = %lf",p_double)
        else:
            rospy.loginfo("p_double is not exist")
        rate.sleep()
    

