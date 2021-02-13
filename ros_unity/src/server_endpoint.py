#!/usr/bin/env python3

import rospy

from ros_tcp_endpoint import TcpServer, RosPublisher, RosSubscriber, RosService
from ros_unity_msgs.msg import MapData, PosData

def main():
    ros_node_name = rospy.get_param("/TCP_NODE_NAME", 'TCPServer')
    buffer_size = rospy.get_param("/TCP_BUFFER_SIZE", 1024)
    connections = rospy.get_param("/TCP_CONNECTIONS", 10)
    tcp_server = TcpServer(ros_node_name, buffer_size, connections)
    rospy.init_node(ros_node_name, anonymous=True)
    
    tcp_server.start({
        'robot_pos': RosSubscriber('robot_pos', PosData, tcp_server),
        'map_data': RosSubscriber('map_data', MapData, tcp_server)
    })
    
    rospy.spin()


if __name__ == "__main__":
    main()
