#include <eigen3/Eigen/Core>
#include <Eigen/Dense>
#include <iostream>
using namespace std;

int main()
{
    Eigen::Matrix<float, 2, 3> matrix_23;
    Eigen::Matrix<float, 3, 4> matrix_34;
    Eigen::Matrix<float, 2, 4> result;
    matrix_34 << 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12;
    matrix_23 << 1, 2, 3, 4, 5, 6;
    result = matrix_23 * matrix_34;
    cout << "result = " << result << endl;

    Eigen::Matrix3d matrix33;
    matrix33 = Eigen::Matrix3d::Random();

    Eigen::Vector3d v_3d = Eigen::Vector3d::Random();
    cout << "33 = " << matrix33 << endl;
    cout << "v_3d = " << v_3d << endl;

    Eigen::Matrix<double, Eigen::Dynamic, Eigen::Dynamic> matrix_dynamic;

    matrix_dynamic = matrix_34.cast<double>();
    cout
        << "dynamic = " << matrix_dynamic << endl;

    cout << matrix33.transpose() << endl;
    cout << matrix33.sum() << endl;
    cout << matrix33.inverse() << endl;
    cout << matrix33.determinant() << endl;
    cout << matrix33.trace() << endl;
}