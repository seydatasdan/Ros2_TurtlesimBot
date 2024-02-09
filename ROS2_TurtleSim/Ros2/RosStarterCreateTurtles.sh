cd ~/ros2_ws;
ros2 run turtlesim turtlesim_node --ros-args --remap /turtle1/cmd_vel:=/turtle1/cmd_vel & ros2 run turtlesim turtlesim_node --ros-args --remap /turtle1/cmd_vel:=/turtle2/cmd_vel & ros2 run turtlesim turtlesim_node --ros-args --remap /turtle1/cmd_vel:=/turtle3/cmd_vel & ros2 run turtlesim turtlesim_node --ros-args --remap /turtle1/cmd_vel:=/turtle4/cmd_vel;
