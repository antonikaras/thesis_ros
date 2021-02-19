#!/usr/bin/env python3

import rospy 
import numpy as np
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

from ros_unity_msgs.msg import MapData

class PrintMap:
    """
        Read the map transfered from ROS2 through ros1_bridge to ROS
        and display it to RVIZ
    """

    def __init__(self):
        
        # Initialize node
        rospy.init_node('print_map')

        self.bridge = CvBridge()

        # Setup subscribers
        # /rosbridge_msgs_publisher/map
        #rospy.Subscriber('/rosbridge_msgs_publisher/map', MapData, self._mapCallback)

        # Setup publishers
        self.map_image_pub_ = rospy.Publisher('/image_pub', Image, queue_size=10)
        self.fake_map_pub = rospy.Publisher('/rosbridge_msgs_publisher/map', MapData, queue_size=10)

        self.PubData()

        rospy.spin()

    def PubData(self):
        map = MapData()
            
        tmp = np.array([0, 0, 0, 100,
                        0, 100, 0, 0,
                        0, 0, 0, 0
                        ]).reshape((3, 4))   
        #tmp = np.flip(tmp, 0)
        tmp = np.rot90(np.fliplr(tmp), -1)
        tmp = np.flip(tmp, 0)
        
        map.map = tmp.flatten()
        map.width = 3
        map.height = 4
        print(tmp)
        print(map.map)

        while not rospy.is_shutdown():
            self.fake_map_pub.publish(map)      

            rospy.sleep(5)

    def _mapCallback(self, data):

        map = data.map
        height = data.height
        width = data.width

        mapSize = height * width

        map_img = np.zeros((height, width))
        for cnt in range(mapSize):
            i = int(cnt / width)
            j = int(cnt - i * width)

            val = 255
            map_val = map[cnt]

            if map_val == -1:
                val = 100
            elif map_val == 100:
                val = 0

            map_img[i][j] = val

        map_img = map_img.astype(np.uint8)
        #self.get_logger().info("---> {}, {}".format(map_img.shape, type(map_img)))

        #map_img = cv.UMat.get(map_img)

        self.map_image_pub_.publish(self.bridge.cv2_to_imgmsg(map_img.T, 'mono8'))
        
###################################################################################################
if __name__ == "__main__":
    PrintMap()