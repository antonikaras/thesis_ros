cmake_minimum_required(VERSION 3.0.2)
project(ros_unity)

find_package(catkin REQUIRED
    nav_msgs
    message_generation
    )

  #Generate messages in the 'msg' folder
add_message_files(
  FILES
  MapData.msg
)

generate_messages(
  DEPENDENCIES
  nav_msgs
)

catkin_package(
    CATKIN_DEPENDS
    message_runtime
)
