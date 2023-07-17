# SITL软件仿真启动顺序及参考写法
{
gnome-terminal --tab "ArduPlane" -- bash -c "cd /home/lzc/ardupilot/Tools/autotest;python sim_vehicle.py -v ArduPlane  -L Hanan"
}& 
sleep 2
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
sleep 2
{
gnome-terminal --tab "mavros" -- bash -c "cd /home/lzc/lzc-code;roslaunch apm.launch"
}





