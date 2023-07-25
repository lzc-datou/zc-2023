# {
# gnome-terminal --tab "ArduPlane" -- bash -c "cd /home/lzc/ardupilot/Tools/autotest;python3 sim_vehicle.py -v ArduPlane -f gazebo-zephyr -L Hanan"
# }& 
# sleep 8
{
gnome-terminal --tab "ArduPlane" -- bash -c "cd /home/lzc/ardupilot/Tools/autotest;sim_vehicle.py -v ArduPlane -L Hanan"
}& 
sleep 8
# {
# gnome-terminal --tab "gazebo" -- bash -c "cd /home/lzc/lzc-code;source devel/setup.bash;roslaunch plane_gazebo plane.launch"
# }& 
# sleep 3
{
gnome-terminal --tab "QGC" -- bash -c "cd /home/lzc;./QGroundControl.AppImage"
}& 
sleep 3
{
gnome-terminal --tab "roscore" -- bash -c "roscore"
}& 
sleep 2
{
gnome-terminal --tab "my_pkg" -- bash -c "cd /home/lzc/lzc-code;source ./devel/setup.bash;rosrun yolov5 detect.py"
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





