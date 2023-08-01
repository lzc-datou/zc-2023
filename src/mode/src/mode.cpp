#include <ros/ros.h>
#include <geometry_msgs/Point.h>
#include <mavros_msgs/State.h>
#include <mavros_msgs/SetMode.h>
#include <mavros_msgs/WaypointPush.h>
#include <mavros_msgs/Waypoint.h>
#include <mavros_msgs/WaypointClear.h>
#include <mavros_msgs/WaypointReached.h>
#include <sensor_msgs/NavSatFix.h>
#include <mavros_msgs/WaypointList.h>
#include <iostream>
#include <fstream>
#include <cmath>
#include <std_msgs/Int8.h>
#include <my_msgs/Signal.h>
#include <my_msgs/Median_gps.h>
#include <csignal>

#define CONSTANTS_RADIUS_OF_EARTH 6371000

mavros_msgs::State CurrentState;
mavros_msgs::WaypointReached waypointsReached;
sensor_msgs::NavSatFix globalPos; // float64 latitude,float64 longitude,float64 altitude

geometry_msgs::Point targetPos; // x，y,z x为北，y为东，z为高度  不一定需要

const std::string scoutWpPath = "./src/mode/waypoints/test.txt";
const std::string strikePath = "./src/mode/waypoints/202301.txt";

struct keypoint
{
	double latitude;
	double longtitude;
	double altitude;
};

keypoint home;
keypoint target;
my_msgs::Signal start;
my_msgs::Signal stop;

// 测试代码001
// 获取飞机当前的模式
//  void GetMode(const mavros_msgs::State::ConstPtr& mode)
//  {

//     CurrentState=*mode;
//     ROS_INFO("获取的当前模式为：%s",mode->mode.c_str());

// }
// 测试代码002
// 获取当前执行的航点经纬度和海拔
// void GetWaypoint(const mavros_msgs::WaypointList::ConstPtr& waypoints)
// {

//     for(int i=1;i<=10;i++)
//     {

//         if(waypoints->waypoints[i].is_current)
//         {

//             ROS_INFO("目前执行的任务为航点%d,该航点的纬度为%f,该航点的经度为%f",i,waypoints->waypoints[i].x_lat,waypoints->waypoints[i].y_long);
//             break;
//         }
//     }
// }
/*             回调函数            */
// 订阅飞机状态模式
template <typename Type>
Type constrain(const Type x, const Type lower_bound, const Type upper_bound)
{
	if (lower_bound > upper_bound)
	{
		return NAN;
	}
	else if (std::isnan(x))
	{
		return NAN;
	}
	else
	{
		return std::max(lower_bound, std::min(upper_bound, x));
	}
}
void state_cb(const mavros_msgs::State::ConstPtr &msg)
{
	CurrentState = *msg;
	return;
}

void gps_receive(my_msgs::Median_gps msg)
{
	target.longtitude = msg.longitude;
	target.latitude = msg.latitude;
	std::cout << "get longitude = " << target.longtitude << std::endl;
	std::cout << "get latitude = " << target.latitude << std::endl;
}
// 订阅飞机执行航点序号
void wp_reached_cb(const mavros_msgs::WaypointReached::ConstPtr &msg)
{
	waypointsReached = *msg;
	return;
}
// 订阅飞机当前位置（经纬度和海拔）
void global_pos_cb(const sensor_msgs::NavSatFix::ConstPtr &msg)
{
	globalPos = *msg;
	return;
}
// 靶标的位置xyz
void target_pos_cb(const geometry_msgs::Point::ConstPtr &msg)
{
	targetPos = *msg;
	return;
}
// 函数功能：实现GPS坐标到相对坐标的转化
// 参数1，2：待转化点的经纬坐标(lat 纬度，lon 经度)
// 参数3，4：参考点的经纬坐标
// 参数5，6：输出的相对座标(x:北，y:东)
void gps_to_xy(double lat, double lon, double _ref_lat, double _ref_lon, double &x, double &y)
{
	std::cout << "Input lat, lon, ref_lat, ref_lon: " << lat << ", " << lon << ", " << _ref_lat << ", " << _ref_lon << std::endl;
	_ref_lat = _ref_lat * M_PI / 180;
	_ref_lon = _ref_lon * M_PI / 180;
	const double _ref_sin_lat = sin(_ref_lat);
	const double _ref_cos_lat = cos(_ref_lat);

	const double lat_rad = lat * M_PI / 180;
	const double lon_rad = lon * M_PI / 180;

	const double sin_lat = sin(lat_rad);
	const double cos_lat = cos(lat_rad);

	const double cos_d_lon = cos(lon_rad - _ref_lon);

	const double arg = constrain(_ref_sin_lat * sin_lat + _ref_cos_lat * cos_lat * cos_d_lon, -1.0, 1.0);
	const double c = acos(arg);

	double k = 1.0;

	if (fabs(c) > 0)
	{
		k = (c / sin(c));
	}

	x = static_cast<float>(k * (_ref_cos_lat * sin_lat - _ref_sin_lat * cos_lat * cos_d_lon) * CONSTANTS_RADIUS_OF_EARTH);
	y = static_cast<float>(k * cos_lat * sin(lon_rad - _ref_lon) * CONSTANTS_RADIUS_OF_EARTH);

	// std::cout << std::setprecision(8) << "Input lat, lon: " << lat << ", " << lon << "Output x, y: " << x << ", " << y << std::endl;
	std::cout << "Output x, y: " << x << ", " << y << std::endl;
	return;
}
// 函数功能：实现相对座标到GPS坐标的转化
// 参数1，2：需要转化的相对于原点的坐标(x:北，y:东)
// 参数3，4：输出的GPS坐标(lat 纬度，lon 经度)
// 参数5，6：原点的GPS坐标
void xy_to_gps(double x, double y, double &lat, double &lon, const double ref_lat, const double ref_lon)
{
	const double x_rad = (double)x / CONSTANTS_RADIUS_OF_EARTH;
	const double y_rad = (double)y / CONSTANTS_RADIUS_OF_EARTH;
	const double c = sqrt(x_rad * x_rad + y_rad * y_rad);

	double ref_lat_rad = ref_lat * M_PI / 180.0;
	double ref_lon_rad = ref_lon * M_PI / 180.0;
	double ref_sin_lat = sin(ref_lat_rad);
	double ref_cos_lat = cos(ref_lat_rad);

	if (fabs(c) > 0)
	{
		const double sin_c = sin(c);
		const double cos_c = cos(c);

		const double lat_rad = asin(cos_c * ref_sin_lat + (x_rad * sin_c * ref_cos_lat) / c);
		const double lon_rad = (ref_lon_rad + atan2(y_rad * sin_c, c * ref_cos_lat * cos_c - x_rad * ref_sin_lat * sin_c));

		lat = (lat_rad * 180) / M_PI;
		lon = (lon_rad * 180) / M_PI;
	}
	else
	{
		lat = (lat * 180) / M_PI;
		lon = (lon * 180) / M_PI;
	}
	// std::cout << std::setprecision(8) << "Input x, y: " << x << ", " << y << "  " << "Output lat, lon: " << lat << ", " << lon << std::endl;
	std::cout << "Input x, y: " << x << ", " << y << "  "
			  << "Output lat, lon: " << lat << ", " << lon << std::endl;
	return;
}
// 坐标转换函数的限制函数（千万不能删，否则转换函数会出错）

// 航点信息结构体
struct result_read_mission
{
	// 航点序号
	int index;
	// 航线任务
	mavros_msgs::WaypointPush mission;
	// 单个航点
	mavros_msgs::Waypoint wp;
	// 读取是否成功的标志位
	bool read_flag;
};
// 从文件中读取航线
//  result_read_mission Readpointfromfile(const std::string& filepath)
//  {
//  	int line=1;
//  	int number=1;
//  	double data;
//  	result_read_mission readresult;
//      std::ifstream readfile;
//  	readfile.open(filepath,std::ios::in);
//  	if(!readfile.is_open())
//  	{
//         ROS_INFO("File read failed");
//  	}
//      else
//  	{
//        while(readfile>>data)
//  	{
//  		if(number==1)
//  		{readresult.index=int(data);}
//  		else if(number==2)
//  		{readresult.wp.is_current=bool(data);}
//  		else if(number==3)
//  		{readresult.wp.frame=int(data);}
//  		else if(number==4)
//  		{readresult.wp.command=int(data);}
//  		else if(number==5)
//  		{
//  			if(readresult.index==0)
//  			{
//                readresult.wp.param1=int(data);
//  			}
//  			else
//  			{
//                  readresult.wp.param1=data;
//  			}
//  		}
//  		else if(number==6)
//  		{
//  			if(readresult.index==0)
//  			{
//                readresult.wp.param2=data;
//  			}
//  			else
//  			{
//                  readresult.wp.param2=data;
//  			}
//  		}
//  		else if(number==7)
//  		{
//  			if(readresult.index==0)
//  			{
//                readresult.wp.param3=data;
//  			}
//  			else
//  			{
//                  readresult.wp.param3=data;
//  			}
//  		}
//  		else if(number==8)
//  		{
//  			if(readresult.index==0)
//  			{
//                readresult.wp.param4=data;
//  			}
//  			else
//  			{
//                  readresult.wp.param4=data;
//  			}
//  		}
//  		else if(number==9)
//  		{readresult.wp.x_lat=data;}
//  		else if(number==10)
//  		{readresult.wp.y_long=data;}
//  		else if(number==11)
//  		{readresult.wp.z_alt=data;}
//  		else if(number==12)
//  		{ readresult.wp.autocontinue=bool(data);}
//          else{
//  			number=0;
//              readresult.mission.request.waypoints.push_back(readresult.wp);
//  		}
//  		number++;
//  	}

// 	}
// 	ros::spinOnce();
// 	return readresult;
// }

// 飞行中飞手接管飞机认为出现重大问题需杀死上位机
void manaul_control_detect()
{
	ros::spinOnce();
	if (CurrentState.mode == "MANUAL")
	{
		exit(0);
	}
	return;
}

// 从文件中读取航线
result_read_mission Readpointfromfile(const std::string &filepath)
{
	int number = 1;
	double data;
	result_read_mission readresult;
	std::ifstream readfile;
	readfile.open(filepath, std::ios::in);
	if (!readfile.is_open())
	{
		readresult.read_flag = false;
		ROS_INFO("File read failed");
	}
	else
	{
		readresult.read_flag = true;
		while (readfile >> data)
		{
			if (number == 1)
			{
				readresult.index = int(data);
			}
			else if (number == 2)
			{
				readresult.wp.is_current = bool(data);
			}
			else if (number == 3)
			{
				readresult.wp.frame = int(data);
			}
			else if (number == 4)
			{
				readresult.wp.command = int(data);
				//??????
				if (readresult.wp.command == 21)
				{
					readresult.index--;
				}
			}
			else if (number == 5)
			{
				readresult.wp.param1 = data;
			}
			else if (number == 6)
			{
				readresult.wp.param2 = data;
			}
			else if (number == 7)
			{
				readresult.wp.param3 = data;
			}
			else if (number == 8)
			{
				readresult.wp.param4 = data;
			}
			else if (number == 9)
			{
				readresult.wp.x_lat = data;
				if (readresult.index == 0)
				{
					home.latitude = data;
				}
			}
			else if (number == 10)
			{
				readresult.wp.y_long = data;
				if (readresult.index == 0)
				{
					home.longtitude = data;
				}
			}
			else if (number == 11)
			{
				readresult.wp.z_alt = data;
				if (readresult.index == 0)
				{
					home.altitude = data;
				}
			}
			else if (number == 12)
			{
				readresult.wp.autocontinue = bool(data);
				readresult.mission.request.waypoints.push_back(readresult.wp);
				number = 0;
			}
			number++;
		}
	}
	readfile.close();
	// ros::spinOnce();
	return readresult;
}

// 上传侦察航线
void upload(ros::ServiceClient &uploadWpClient, result_read_mission &result)
{
	ros::Rate rate = 10;
	result = Readpointfromfile(scoutWpPath);
	if (result.read_flag == false)
	{
		ROS_INFO("Read detect waypoints failed.");
	}
	else
	{
		ROS_INFO("Read detect waypoints succeed.");
		uploadWpClient.call(result.mission);
		// ros::spinOnce();
	}
	if (result.mission.response.success)
	{
		ROS_INFO("Upload waypoints success.");
	}
	else
	{
		ROS_WARN("Upload waypoints failed. Retrying...");
		while (!result.mission.response.success)
		{
			uploadWpClient.call(result.mission);
			rate.sleep();
		}
		ROS_INFO("Upload waypoints success.");
	}
}

// 投靶航线上传
void upload2(ros::ServiceClient &uploadWpClient, result_read_mission &result)
{
	ros::Rate rate = 10;
	uploadWpClient.call(result.mission);
	if (result.mission.response.success)
	{
		ROS_INFO("Upload strike waypoints success.");
	}
	else
	{
		ROS_WARN("Upload waypoints failed. Retrying...");
		while (!result.mission.response.success)
		{
			uploadWpClient.call(result.mission);
			rate.sleep();
			ros::spinOnce();
		}
		ROS_INFO("Upload  strike waypoints success.");
	}
}

// 判断航线是否走完，进入AUTO后执行完当前航线会自主切换到RTL
void wait_detect_over(ros::Rate &rate)
{
	ros::spinOnce();
	if (CurrentState.mode == "RTL")
	{

		ROS_INFO("Mission is complete");
		ros::Duration(5).sleep(); // 延时2s调整航线  -------------------------------------
		return;					  // 退出该函数
	}
	while (CurrentState.mode != "RTL")
	{
		manaul_control_detect();
		ros::spinOnce();
		// 延时1S
		rate.sleep();
		std::cout << "Current mode is " << CurrentState.mode << std::endl;
	}
	ros::Duration(5).sleep();
	std::cout << "Current mode is " << CurrentState.mode << ". Mission is over !" << std::endl;
	// printf("Current mode is %s . Mission is over !",CurrentState.mode);
}
// 函数功能：为常规飞行航点的参数赋值
// 参数1：飞行航点
// 参数2：纬度
// 参数3：经度
// 参数4：高度
void fill_wp_of_mission(result_read_mission &re, double latitude, double longtitude, double altitude)
{
	re.wp.is_current = bool(0);
	re.wp.frame = int(3);
	re.wp.command = int(16);
	re.wp.param1 = 0.0;
	re.wp.param2 = 0.0;
	re.wp.param3 = 0.0;
	re.wp.param4 = 0.0;
	re.wp.x_lat = latitude;
	re.wp.y_long = longtitude;
	re.wp.z_alt = altitude;
	re.wp.autocontinue = 1;
	return;
}

// 根据靶标计算出侦察航线
// 1.已知Home,靶标位置
// 2.已知飞机位置，Home,靶标位置  即飞机在当前位置直接以圆弧航迹切入靶点与Home构成的直线
result_read_mission Striker_planner()
{
	result_read_mission strike_task;
	// 靶标的经纬度为全局变量，视觉自定义消息发送经纬度，接受即可
	double plan1, plan2, plan3;
	double pla, plo, hla, hlo, hal, tla, tlo;
	double d1 = 80, d2 = 80;
	double k, fx, fy;
	double px, py, tx, ty;

	pla = globalPos.latitude;  // 飞机纬度
	plo = globalPos.longitude; // 飞机经度

	hla = home.latitude;   // 家（航点0）纬度   以航点0坐标为坐标系原点（东北坐标系）
	hlo = home.longtitude; // 家（航点0）经度
	hal = home.altitude;   // 家（航点0）海拔

	tla = target.latitude;	 // 靶标维度
	tlo = target.longtitude; // 靶标经度

	gps_to_xy(pla, plo, hla, hlo, px, py); // 飞机的相对坐标
	gps_to_xy(tla, tlo, hla, hlo, tx, ty); // 靶标的相对坐标
	k = fabs(ty / tx);
	fx = fabs(tx) / tx;
	fy = fabs(ty) / ty;
	double point3_x;
	double point3_y;
	point3_x = d1 * (1 / sqrt(k * k + 1)) * fx + tx;
	point3_y = d1 * (k / sqrt(k * k + 1)) * fy + ty;
	double point1_x;
	double point1_y;
	point1_x = point3_x + d2 * (k / sqrt(k * k + 1));
	point1_y = point3_x * (tx / ty) + point3_y - (tx / ty) * point1_x;
	double point2_x;
	double point2_y;
	point2_x = (point1_x + point3_x) / 2 + (d2 / 2) * fx * 1 / sqrt(k * k + 1);
	point2_y = (point1_y + point3_y) / 2 + (d2 / 2) * fy * k / sqrt(k * k + 1);
	// xy_to_gps(double x, double y, double& lat, double& lon, const double ref_lat, const double ref_lon);

	// 上传规划出的航点
	// home上传
	strike_task.wp.is_current = bool(1);
	strike_task.wp.frame = int(0);
	strike_task.wp.command = int(16);
	strike_task.wp.param1 = 0;
	strike_task.wp.param2 = 0;
	strike_task.wp.param3 = 0;
	strike_task.wp.param4 = 0;
	strike_task.wp.x_lat = hla;
	strike_task.wp.y_long = hlo;
	strike_task.wp.z_alt = hal;
	strike_task.wp.autocontinue = 1;
	strike_task.mission.request.waypoints.push_back(strike_task.wp);

	// 航点1
	xy_to_gps(point1_x, point1_y, plan1, plan2, hla, hlo);
	plan3 = 20;
	fill_wp_of_mission(strike_task, plan1, plan2, plan3);
	strike_task.mission.request.waypoints.push_back(strike_task.wp);
	// 航点2
	xy_to_gps(point2_x, point2_y, plan1, plan2, hla, hlo);
	plan3 = 20;
	fill_wp_of_mission(strike_task, plan1, plan2, plan3);
	strike_task.mission.request.waypoints.push_back(strike_task.wp);
	// 航点3
	xy_to_gps(point3_x, point3_y, plan1, plan2, hla, hlo);
	plan3 = 20;
	fill_wp_of_mission(strike_task, plan1, plan2, plan3);
	strike_task.mission.request.waypoints.push_back(strike_task.wp);

	// 投放辅助航点4 用于启动Lua的投靶动作即下一个航点为投靶点
	strike_task.wp.is_current = bool(0);
	strike_task.wp.frame = int(3);
	strike_task.wp.command = int(183);
	strike_task.wp.param1 = 7;
	strike_task.wp.param2 = 1900;
	strike_task.wp.param3 = 0;
	strike_task.wp.param4 = 0;
	strike_task.wp.x_lat = 0;
	strike_task.wp.y_long = 0;
	strike_task.wp.z_alt = 0;
	strike_task.wp.autocontinue = 1;
	strike_task.mission.request.waypoints.push_back(strike_task.wp);

	// 航点5(靶点)
	// 靶点
	target.altitude = 20;
	fill_wp_of_mission(strike_task, target.latitude, target.longtitude, target.altitude);
	strike_task.mission.request.waypoints.push_back(strike_task.wp);

	// 航点6     //模拟降落点
	strike_task.wp.is_current = bool(0);
	strike_task.wp.frame = int(3);
	strike_task.wp.command = int(16);
	strike_task.wp.param1 = 0;
	strike_task.wp.param2 = 0;
	strike_task.wp.param3 = 0;
	strike_task.wp.param4 = 0;
	strike_task.wp.x_lat = hla;
	strike_task.wp.y_long = hlo;
	strike_task.wp.z_alt = 20;
	strike_task.wp.autocontinue = 1;
	strike_task.mission.request.waypoints.push_back(strike_task.wp);

	return strike_task;
}

void mission_clear(ros::ServiceClient &missionClearClient, ros::Rate &rate)
{
	mavros_msgs::WaypointClear missionClear;
	while (1)
	{
		if (missionClear.response.success)
		{
			ROS_INFO("Previous mission has been clear! New mission permitted!");
			return;
		}
		else
		{
			missionClear.request = {};
			missionClearClient.call(missionClear);
			ros::spinOnce();
		}
		rate.sleep();
	}
}

void Set_AutoMode(ros::ServiceClient &setModeClient, ros::Rate &rate) // ------------------------------------------------
{

	mavros_msgs::SetMode change_mode;
	change_mode.request.custom_mode = "AUTO";
	setModeClient.call(change_mode);
	ros::spinOnce();

	if (change_mode.response.mode_sent)
	{
		ROS_INFO("Current mode is AUTO");
	}
	else
	{
		while (!change_mode.response.mode_sent)
		{
			mavros_msgs::SetMode change_mode;
			change_mode.request.custom_mode = "AUTO";
			setModeClient.call(change_mode);
			ros::spinOnce();
			rate.sleep();
		}
	}
	std::cout << "Current mode is " << CurrentState.mode << ". Mode change is over !" << std::endl;
	// printf("Current mode is %s . Mode change is over !",CurrentState.mode);
}

// 将航线写入文件
//  void write_waypoints(result_read_mission& read_result)
//  {
//      std::fstream wpfile;
//      wpfile.open(strikePath, std::ios::out);
//      if(!wpfile.is_open())
//      {
//          ROS_INFO("Write strike file failed.");
//      }
//      for(int i=0; i<read_result.mission.request.waypoints.size(); i++)
//      {
//  		wpfile << (i) << "\t";
//          wpfile << (read_result.mission.request.waypoints[i].is_current) << "\t";
//          wpfile << (read_result.mission.request.waypoints[i].frame) << "\t";
//          wpfile << (read_result.mission.request.waypoints[i].command) << "\t";
//          wpfile << (read_result.mission.request.waypoints[i].param1) << "\t";
//          wpfile << (read_result.mission.request.waypoints[i].param2) << "\t";
//          wpfile << (read_result.mission.request.waypoints[i].param3) << "\t";
//          wpfile << (read_result.mission.request.waypoints[i].param4) << "\t";
//          wpfile << (read_result.mission.request.waypoints[i].x_lat) << "\t";
//          wpfile << (read_result.mission.request.waypoints[i].y_long) << "\t";
//          wpfile <<(read_result.mission.request.waypoints[i].z_alt) << "\t";
//  		wpfile << (read_result.mission.request.waypoints[i].autocontinue) << "\t";
//          wpfile << std::endl;
//      }
//      return;
//  }

// 将航线写入文件
void write_waypoints(result_read_mission &read_result)
{
	std::fstream wpfile;
	wpfile.open(strikePath, std::ios::out);
	if (!wpfile.is_open())
	{
		ROS_INFO("Write strike file failed.");
	}
	for (int i = 0; i < read_result.mission.request.waypoints.size(); i++)
	{
		wpfile << std::to_string(i) << "\t";
		wpfile << std::to_string(read_result.mission.request.waypoints[i].is_current) << "\t";
		wpfile << std::to_string(read_result.mission.request.waypoints[i].frame) << "\t";
		wpfile << std::to_string(read_result.mission.request.waypoints[i].command) << "\t";
		wpfile << std::to_string(read_result.mission.request.waypoints[i].param1) << "\t";
		wpfile << std::to_string(read_result.mission.request.waypoints[i].param2) << "\t";
		wpfile << std::to_string(read_result.mission.request.waypoints[i].param3) << "\t";
		wpfile << std::to_string(read_result.mission.request.waypoints[i].param4) << "\t";
		wpfile << std::to_string(read_result.mission.request.waypoints[i].x_lat) << "\t";
		wpfile << std::to_string(read_result.mission.request.waypoints[i].y_long) << "\t";
		wpfile << std::to_string(read_result.mission.request.waypoints[i].z_alt) << "\t";
		wpfile << std::to_string(read_result.mission.request.waypoints[i].autocontinue) << "\t";
		wpfile << std::endl;
	}
	return;
}

void wait_auto_mode(ros::Rate &rate, ros::Publisher &vision_command)
{
	ros::spinOnce();
	if (CurrentState.mode != "AUTO")
	{
		ROS_INFO("Please change to AUTO mode.");
	}
	while (CurrentState.mode != "AUTO")
	{
		vision_command.publish(start);
		ros::spinOnce();
		rate.sleep();
	}
	ROS_INFO("Start.");
	return;
}

// 侦察结束，接收靶点函数
void target_get(ros::Rate &rate, ros::Publisher &vision_command)
{
	for (int i = 0; i < 50; i++)
	{

		vision_command.publish(stop);
		rate.sleep();
	}
}

// 定义信号处理函数
void signalHandler(int signum)
{
	std::cout << "手动终止" << std::endl;
	exit(signum);
}

int main(int argc, char *argv[])
{

	bool FlagMode = true;
	result_read_mission result; // 侦察航点结构体
	result_read_mission target_result;
	setlocale(LC_ALL, "");
	// 创建节点
	ros::init(argc, argv, "hahaha");
	// 创建句柄
	ros::NodeHandle nh;
	// 订阅飞机state话题
	// ros::Subscriber sub=nh.subscribe<mavros_msgs::State>("/mavros/state",10,GetMode);
	// 订阅飞机航线信息话题
	// ros::Subscriber sub_1=nh.subscribe<mavros_msgs::WaypointList>("/mavros/mission/waypoints",10,GetWaypoint);
	ros::Subscriber plane_state = nh.subscribe<mavros_msgs::State>("/mavros/state", 10, state_cb);
	ros::Subscriber pointreached = nh.subscribe<mavros_msgs::WaypointReached>("/mavros/mission/reached", 10, wp_reached_cb);
	ros::Subscriber plane_current_position = nh.subscribe<sensor_msgs::NavSatFix>("/sensor_msgs/global_position/global", 10, global_pos_cb);
	ros::Subscriber gps_sub = nh.subscribe<my_msgs::Median_gps>("/median_gps", 10, gps_receive);

	// 视觉命令
	ros::Publisher vision_command = nh.advertise<my_msgs::Signal>("/is_investigation_over", 10);

	ros::ServiceClient missionClearClient = nh.serviceClient<mavros_msgs::WaypointClear>("/mavros/mission/clear");
	ros::ServiceClient uploadWpClient = nh.serviceClient<mavros_msgs::WaypointPush>("/mavros/mission/push");
	ros::ServiceClient setModeClient = nh.serviceClient<mavros_msgs::SetMode>("/mavros/set_mode");
	result_read_mission read_result;
	ros::Rate rate(10);
	mavros_msgs::WaypointClear missionClear;

	// 侦察视觉启动与结束
	start.signal = 0;
	stop.signal = 1;
	// 45.5614448	126.6185532	170.326400

	std::cout << "载入数据" << std::endl;
	signal(SIGINT, signalHandler); // SIGINT表示Ctrl+C信号
	// 关键点家的经纬度
	home.latitude = 45.5614448;
	home.longtitude = 126.6185532;
	home.altitude = 170.326400;

	// 测试靶点的经纬度 45.56456740	126.61732350
	// target.latitude = 45.56456740;
	// target.longtitude = 126.61732350;

	// target.latitude=result.mission.request.waypoints[5].x_lat;      这样赋值 会报Segmentation fault (core dumped)
	// target.longtitude=result.mission.request.waypoints[5].y_long;

	std::cout << "载完数据" << std::endl;
	// 发送请求将飞控的航线清空
	missionClear.request = {};
	missionClearClient.call(missionClear);
	ros::spinOnce();
	mission_clear(missionClearClient, rate);

	// //read_upload_scout_mission(read_result, uploadWpClient, rate);
	// //out_waypoints(read_result);
	// //Readpointfromfile(scoutWpPath);

	// //上传侦察航线
	upload(uploadWpClient, result);
	ros::spinOnce;

	// 提示飞手切换自动
	wait_auto_mode(rate, vision_command);

	// 等待航线任务执行完成
	wait_detect_over(rate);
	target_get(rate, vision_command);

	// Set_AutoMode(setModeClient,rate);

	std::cout << "zzh target lat, lon: " << target.latitude << ", " << target.longtitude << std::endl;

	// 清除侦察航线
	missionClearClient.call(missionClear);
	ros::spinOnce();
	mission_clear(missionClearClient, rate);
	ros::spinOnce();
	// ros::spinOnce();
	ros::Duration(3).sleep();
	// ros::spinOnce();
	// ros::spinOnce();
	// ros::spinOnce();
	// 上传规划的投靶航线
	target_result = Striker_planner();
	write_waypoints(target_result); /////---------------
	upload2(uploadWpClient, target_result);

	manaul_control_detect();
	// 等待
	ros::Duration(10).sleep();
	manaul_control_detect();

	// 切换到阿auto以执行投靶任务
	Set_AutoMode(setModeClient, rate);

	// 等待航线任务执行完成
	wait_detect_over(rate);

	manaul_control_detect();
	// // 清除投靶航线
	// missionClearClient.call(missionClear);
	// ros::spinOnce();
	// mission_clear(missionClearClient,rate);

	while (1)
	{
		manaul_control_detect();
		rate.sleep();
	}

	// ros::spin();
	return 0;
}
