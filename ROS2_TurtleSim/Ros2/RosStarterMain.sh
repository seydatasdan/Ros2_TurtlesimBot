cd ~/ros2_ws;
. install/local_setup.bash;
colcon build --packages-select kpackage1;
ros2 run kpackage1 knode1 --ros-args -p turtleName:=turtle1 -p letter:=g & ros2 run kpackage1 knode1 --ros-args -p turtleName:=turtle2 -p letter:=h & ros2 run kpackage1 knode1 --ros-args -p turtleName:=turtle3 -p letter:=x & ros2 run kpackage1 knode1 --ros-args -p turtleName:=turtle4 -p letter:=w;
