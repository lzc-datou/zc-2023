#include <iostream>
#include <cmath>
using namespace std;
#include <Eigen/Core>
#include <Eigen/Geometry>

int main()
{
    // 描述三维旋转的三种方式:1.旋转矩阵 2.角轴 3.四元数
    // 用于直观理解三维旋转的方式：欧拉角
    // 描述三维坐标变换的方法（旋转+平移）：欧式变换矩阵

    // 旋转矩阵
    Eigen::Matrix3d rotation_matrix = Eigen::Matrix3d::Identity();

    // 旋转向量+旋转角 表示旋转 ---角轴表示法
    Eigen::AngleAxisd rotation_vector(M_PI / 4, Eigen::Vector3d(0, 0, 1));
    // 表示绕z轴旋转九十度
    cout << "M_PI=" << M_PI << endl;
    cout.precision(3);

    // 转换成旋转矩阵形式
    rotation_matrix = rotation_vector.toRotationMatrix();
    cout << "rotation_matrix=\n"
         << rotation_matrix << endl;

    Eigen::Vector3d v_rotated = rotation_matrix * Eigen::Vector3d(1, 0, 0);

    cout << "旋转矩阵：(1,0,0) after rotation is (" << v_rotated.transpose() << ")" << endl;

    // 旋转矩阵转换成欧拉角
    Eigen::Vector3d euler_angle = rotation_matrix.eulerAngles(2, 1, 0); // 2,1,0用于指定yaw pitch roll顺序
    cout << "yaw pitch roll = " << euler_angle.transpose() << endl;

    // 欧式变换矩阵
    Eigen::Isometry3d T = Eigen::Isometry3d::Identity();

    // 旋转向量
    T.rotate(rotation_vector);
    // 位移向量
    T.pretranslate(Eigen::Vector3d(1, 2, 3));

    Eigen::Vector3d v_transform = T * Eigen::Vector3d(1, 0, 0);

    cout
        << "Transform matrix =\n"
        << T.matrix() << endl;
    cout << "(1,0,0) after transform is (" << v_transform.transpose() << ")" << endl;

    // 四元数

    // 直接将AngleAxis赋值给四元数
    Eigen::Quaterniond q = Eigen::Quaterniond(rotation_vector);
    v_transform = q * Eigen::Vector3d(1, 0, 0);
    cout
        << "quaternion = \n"
        << q.coeffs() << endl; // coeffs顺序为实部+3虚部（xyz）
    cout << "(1,0,0) after rotation is (" << v_transform.transpose() << ")" << endl;
    // 也可以将旋转矩阵直接赋值给四元数
    q = Eigen::Quaterniond(rotation_matrix);

    v_transform = q * Eigen::Vector3d(1, 0, 0);
    cout << "quaternion = \n"
         << q.coeffs() << endl;

    cout << "(1,0,0) after rotation is (" << v_transform.transpose() << ")" << endl;
    cout.precision(6);
    cout << 0.383 * 0.383 + 0.924 * 0.924 << endl;
}