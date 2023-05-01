# -*- coding: utf-8 -*-
"""
Calibrate the Camera with Zhang Zhengyou Method.
Picture File Folder: "./pic/RGB_camera_calib_img/", Without Distortion. 

By You Zhiyuan, 2022.07.04, zhiyuanyou@foxmail.com
"""

import os

from calibrate_helper import Calibrator


def main():
    img_dir = "./pic/RGB_camera_calib_img"
    shape_inner_corner = (17, 17)
    size_grid = 0.015
    # create calibrator
    calibrator = Calibrator(img_dir, shape_inner_corner, size_grid)
    # calibrate the camera
    mat_intri, coff_dis = calibrator.calibrate_camera()
    with open('./arguement.txt',"w") as f:
        f.write("camera_matrix = "+str(mat_intri)+'\n')
        f.write("distCoeffs = "+str(coff_dis))
    print("camera_matrix and distCoeffs is saved to: ./arguemnet.txt")

if __name__ == '__main__':
    main()
