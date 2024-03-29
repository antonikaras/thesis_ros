#!/usr/bin/env python3

import rospy

from ros_tcp_endpoint import TcpServer, RosPublisher, RosSubscriber, RosService
from ros_unity_msgs.msg import MapData, PosData, PointGroups, Nav2Waypoints

def main():
    ros_node_name = rospy.get_param("/TCP_NODE_NAME", 'TCPServer')
    buffer_size = rospy.get_param("/TCP_BUFFER_SIZE", 1024)
    connections = rospy.get_param("/TCP_CONNECTIONS", 10)
    tcp_server = TcpServer(ros_node_name, buffer_size, connections)
    rospy.init_node(ros_node_name, anonymous=True)
    
    tcp_server.start({
        'rosbridge_msgs_publisher/robot_pos': RosSubscriber('rosbridge_msgs_publisher/robot_pos', PosData, tcp_server),
        'rosbridge_msgs_publisher/map': RosSubscriber('rosbridge_msgs_publisher/map', MapData, tcp_server),
        'rosbridge_msgs_unity/nav_goals': RosPublisher('rosbridge_msgs_unity/nav_goals', Nav2Waypoints, queue_size=10),
        'rosbridge_msgs_unity/interactive_map': RosPublisher('rosbridge_msgs_unity/interactive_map', MapData, queue_size=10),
        'rosbridge_msgs_unity/point_groups': RosPublisher('rosbridge_msgs_unity/point_groups', PointGroups, queue_size=10),
        'rosbridge_msgs_publisher/point_groups': RosSubscriber('rosbridge_msgs_publisher/point_groups', PointGroups, tcp_server),
        'rosbridge_msgs_publisher/current_target': RosSubscriber('rosbridge_msgs_publisher/current_target', PosData, tcp_server)
    })
    
    rospy.spin()


if __name__ == "__main__":
    main()
