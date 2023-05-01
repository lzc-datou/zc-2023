# -*- coding: utf-8 -*-
"""
Calibrate the Camera with Zhang Zhengyou Method.
Picture File Folder: "./pic/IR_camera_calib_img/", With Distortion. 

By You Zhiyuan, 2022.07.04, zhiyuanyou@foxmail.com
"""

import os

from calibrate_helper import Calibrator


def main():
    img_dir = "./pic/IR_camera_calib_img"
    shape_inner_corner = (17,17)
    size_grid = 0.015
    # create calibrator
    calibrator = Calibrator(img_dir, shape_inner_corner, size_grid)
    # calibrate the camera
    mat_intri, coff_dis = calibrator.calibrate_camera()
    with open('./arguement.txt',"w") as f:
        f.write("camera_matrix = "+str(mat_intri)+'\n')
        f.write("distCoeffs = "+str(coff_dis))
    print("camera_matrix and distCoeffs is saved to: ./arguemnet.txt")
    # dedistort and save the dedistortion result
    save_dir = "./pic/IR_dedistortion"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    calibrator.dedistortion(save_dir)


if __name__ == '__main__':
    main()
