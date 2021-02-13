cmake_minimum_required(VERSION 3.0.2)
project(ros_unity)

find_package(catkin REQUIRED
<<<<<<< HEAD
    rospy
    )

catkin_package(
    CATKIN_DEPENDS
)
=======
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
>>>>>>> eadbb3568928b9459e0e0077c6f5cc274e11da2f
