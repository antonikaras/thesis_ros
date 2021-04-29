#!/usr/bin/env python3
""" 
    Read the messages from the rosbags and convert them into numpy arrays 
    so that they can be used for the training of the Convolutional autoencoder
"""
import rosbag 
import numpy as np

from ros_unity_msgs.msg import MapData, PosData

rosbag_dir = "/home/antony/catkin_ws/src/thesis_ros/rosbag_processor/rosbags/"
rosbag_names = ["house_1", "new_house", "small_house", "small_house_v2"]
#rosbag_names = ["small_house"]

network_input_dims = [256, 256]

def ReadData(bag_name : str):
    print(bag_name)
    bag = rosbag.Bag(bag_name)
    maps = []
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
            maps.append(map)
            map_specs.append([msg.origin[0], msg.origin[1], msg.resolution])
        else:
            poss.append([msg.x, msg.y])
    
    bag.close()

    # Filter the map data and convert them to match the network input dimensions
    tmp1 = []
    tmp2 = []
    maps = np.array(maps)
    for i in range(0, len(maps)):
        store_data = False
        map = maps[i]
        pos = []

        # Initialize the map data
        tmp = -1 * np.ones(network_input_dims)
        if len(tmp1) == 0:
            store_data = True
        elif len(tmp1[-1]) != len(map):
            store_data = True
        elif sum(sum(np.abs(tmp1[-1]) - map)) > 1:
            store_data = True
        
        if store_data:
            h, w = map.shape
            mapIndex_j = int((poss[i][0] - map_specs[i][0]) / map_specs[i][2])
            mapIndex_i = int((poss[i][1] - map_specs[i][1]) / map_specs[i][2])

            # Get the limits for the widths
            mii = max(0, mapIndex_i - int(0.5 * network_input_dims[0]))
            mai = min(w, mapIndex_i + int(0.5 * network_input_dims[0]))
                
            # Get the limits for the heights
            mij = max(0, mapIndex_j - int(0.5 * network_input_dims[1]))
            maj = min(h, mapIndex_j + int(0.5 * network_input_dims[1]))

            pos = [(mapIndex_i - mii) / network_input_dims[0], (mapIndex_j - mij) / network_input_dims[1]]
                
            try:
               tmp[0:(maj - mij), 0:(mai - mii)] = map[mij:maj, mii:mai]
            except:
                print("Error in conversion")
                store_data = False
            if store_data:
                tmp1.append(tmp)
                tmp2.append(pos)
    
    return np.array(tmp1), np.array(tmp2)

for bag_nm in rosbag_names:
    name = rosbag_dir + bag_nm + '.bag'
    maps, poss = ReadData(name)
    np.save(rosbag_dir + bag_nm + '_maps', maps)
    np.save(rosbag_dir + bag_nm + '_poss', poss)

    print(maps.shape, len(poss))
