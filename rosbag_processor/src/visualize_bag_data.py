#!/usr/bin/env python3
""" 
    Read the stored np.array data and display them as images
"""
import rosbag
import numpy as np
import cv2 as cv

rosbag_dir = "/home/antony/catkin_ws/src/thesis_ros/rosbag_processor/rosbags/"
rosbag_names = ["house_1", "new_house", "small_house", "small_house_v2"]

def ReadData(bag_name : str):
    print(bag_name)
    bag = rosbag.Bag(bag_name)
    map = []
    poss = []
    map_specs = []

    # Read the map and position data from the rosbags
    for topic, msg, _ in bag.read_messages(topics=['/rosbridge_msgs_publisher/map', '/rosbridge_msgs_publisher/robot_pos']):
        if topic == '/rosbridge_msgs_publisher/map':
            tmp = np.array(msg.map)
            tmp[tmp == -1] = -100
            tmp = tmp / 100
            map = np.array(tmp).reshape(msg.height, msg.width)
            map = np.flip(map, 1)
            map_specs = [msg.origin[0], msg.origin[1], msg.resolution]
        elif len(map) > 0:
            h, w = map.shape
            mapIndex_i = ((msg.x - map_specs[0]) / map_specs[2]) / w 
            mapIndex_j = ((msg.y - map_specs[1]) / map_specs[2]) / h

            img = array2img(map, [mapIndex_i, mapIndex_j])
            cv.namedWindow("img", cv.WINDOW_NORMAL)
            cv.imshow("img", img)
            if cv.waitKey(100) == ord('q'):
                break
    
    bag.close()


def array2img(data : np.array, pos : np.array) -> np.array:
    "Convert the map into a grayscale image"
    h, w = data.shape
    img = np.zeros((h, w, 1))
    img[data == -1] = 80
    img[data > 0.25] = 255

    # Add the robot position in the image
    i = int(pos[0] * w)
    j = int(pos[1] * h)
    try:
        img[i, j] = 160
    except:
        print(w, h, pos)

    return img.astype(np.uint8)

for bag_nm in rosbag_names:
    name = rosbag_dir + bag_nm + '.bag'
    ReadData(name)
        
        
