# {
# gnome-terminal --tab "ArduPlane" -- bash -c "cd /home/lzc/ardupilot/Tools/autotest;python3 sim_vehicle.py -v ArduPlane -f gazebo-zephyr -L Hanan"
# }& 
# sleep 8
{
gnome-terminal --tab "roscore" -- bash -c "roscore"
}& 
sleep 5
{
gnome-terminal --tab "gazebo" -- bash -c "cd /home/lzc/ardupilot_gazebo;gazebo --verbose -s libgazebo_ros_api_plugin.so ./worlds/target.world"
}& 
sleep 3
{
gnome-terminal --tab "ardupilot/ArduPlane" -- bash -c "cd /home/lzc/ardupilot/Tools/autotest;sim_vehicle.py -v ArduPlane -f gazebo-zephyr -L Hanan --out 127.0.0.1:14551 "
}& 
sleep 3
{
gnome-terminal --tab "QGC" -- bash -c "cd /home/lzc;./QGroundControl.AppImage"
}& 
sleep 3
{
gnome-terminal --tab "my_pkg" -- bash -c "cd /home/lzc/lzc-code;source ./devel/setup.bash;rosrun yolov5 detect_simulation.py"
}& 
sleep 2
{
gnome-terminal --tab "my_pkg" -- bash -c "cd /home/lzc/lzc-code;source ./devel/setup.bash;rosrun process_imgs getNum_and_locate.py;"
}& 
sleep 2
{
gnome-terminal --tab "my_pkg" -- bash -c "cd /home/lzc/lzc-code;source ./devel/setup.bash;rosrun mode mode;"
}&
sleep 5
{
gnome-terminal --tab "mavros" -- bash -c "cd /home/lzc/lzc-code;roslaunch apm.launch"
}





