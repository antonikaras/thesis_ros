cmake_minimum_required(VERSION 3.0.2)
project(ros_unity_msgs)

find_package(catkin REQUIRED
    message_generation
    )

  #Generate messages in the 'msg' folder
add_message_files(
  FILES
  MapData.msg
  PosData.msg
  PointGroup.msg
  PointGroups.msg
)

generate_messages(
  DEPENDENCIES
)

catkin_package(
    CATKIN_DEPENDS
    message_runtime
)
