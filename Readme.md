# Unity ROS package

## Description

    This package contains the necessary items to connect ROS2 and ROS, ROS and Unity.

## Installation

* Follow the instructions of the repository https://github.com/antonikaras/thesis_ros2.git
* Instructions for the initial setup can be found here ```https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/ros_unity_integration/setup.md``` 

## Project packages

* ros_unity
    1. Launches the connection between ros and unity
    2. Contains the network configuration parameters for the communication between ROS and Unity, *ros_unity_params.yaml*
    3. Contains the list of topics that are transported between ROS and ROS2, *rosbridge_params.yaml*
* ros_unity_msgs
    1. Contains the messages that are transported between ROS2 and ROS, ROS and Unity
        * Customs messages are created so that they can be easier imported to Unity at once
* ROS-TCP-Endpoint
    1. Handles the communication between ROS and Unity using .Net 

## Configure Unity

 * Detailed instructions can be found at : https://github.com/Unity-Technologies/Unity-Robotics-Hub/tree/main/tutorials/ros_unity_integration
 1. Launch the unity application
 2. Add the robotics package on Unity ```https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/ros_unity_integration/setup.md```

## How to use

* Terminal 1:
```
roslaunch ros_unity launch_ros_unity_connection.launch
```
* Terminal 2:
```
rosrun robotics_demo server_endpoint.py
```