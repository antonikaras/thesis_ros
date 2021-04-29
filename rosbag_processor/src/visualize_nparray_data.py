#!/usr/bin/env python3
""" 
    Read the stored np.array data and display them as images
"""
import numpy as np
import cv2 as cv

rosbag_dir = "/home/antony/catkin_ws/src/thesis_ros/rosbag_processor/rosbags/"
rosbag_names = ["house_1", "new_house", "small_house", "small_house_v2"]

def array2img(data : np.array, pos : np.array) -> np.array:
    "Convert the map into a grayscale image"
    h, w = data.shape
    img = np.zeros((h, w, 1))
    img[data == -1] = 80
    img[data > 0.25] = 255

    # Add the robot position in the image
    i = int(pos[0] * w)
    j = int(pos[1] * h)
    img[j, i] = 160
    
    return img.astype(np.uint8)

for bag_nm in rosbag_names:
    maps_nm = rosbag_dir + bag_nm + '_maps.npy'
    poss_nm = rosbag_dir + bag_nm + '_poss.npy'

    maps = np.load(maps_nm)
    poss = np.load(poss_nm)

    for map, pos in zip(maps, poss):
        img = array2img(map, pos)
        cv.namedWindow("img", cv.WINDOW_NORMAL)
        cv.imshow("img", img)
        if cv.waitKey(100) == ord('q'):
            break
        
