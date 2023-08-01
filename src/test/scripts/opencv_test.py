


num_and_location = dict()
class Times_and_GPS:
    
        
    '单个数字出现的次数和多次获取到的该数字的经纬度'
    times = 0
    '次数'
    longitude = []
    '经度列表'
    latitude = []
    '纬度列表'
    def __init__(self) -> None:
        self.times = 0
        self.longitude = []
        self.latitude = []
        pass
def num_dict_add(input_num, locate_is_accurate: bool, longitude, latitude):
        ''' 函数功能：将定位到的数字及其经纬度放入全局变量num_and_location中\n
            input_num：识别到的数字\n
            locate_is_accurate: 判断定位是否精确的标志变量,bool类型\n
            longitude:定位得到的数字靶标经度\n
            latitude:定位得到的数字靶标纬度\n
            返回值：True,则该数字在字典中已存在，输出为False，则该数字在字典中还没存在\n
        '''
        global num_and_location
        for key in num_and_location.keys():
            if key == input_num:
                print("key = input num")
                # 该数字计数增加,返回true
                num_and_location[key].times = num_and_location[key].times + 1
                # 如果定位精确，才将定位得到的靶标经纬度放入num_and_location中，否则只增加该数字出现的次数，而不采用其定位
                if locate_is_accurate == True:
                    num_and_location[key].longitude.append(longitude)
                    num_and_location[key].latitude.append(latitude)
                    
                return True
            else:
                continue
        # 如果字典里没有该数字，则添加该数字及其位置并且将其计数调为1，返回false
        print("key != input num")
        times_and_gps = Times_and_GPS()
        times_and_gps.times = 1
        if locate_is_accurate == True:
            print("longitude list = ",times_and_gps.longitude)
            times_and_gps.longitude.append(longitude)
            times_and_gps.latitude.append(latitude)
        
        num_and_location[input_num] = times_and_gps
        
        
        return False

if __name__ == "__main__":
    for j in range(10):
        for i in range(10):
            num_dict_add(i,True,i,i)
    data_save_path = "./data.txt"
        # data.txt覆盖写入
    with open(data_save_path,'w') as file:
        for key in num_and_location.keys():
            data_times = num_and_location[key].times
            data_longitude = num_and_location[key].longitude
            data_latitude = num_and_location[key].latitude
            file.write(str(key) + ":" + str(data_times) + "\n")
            file.write("longitude = " + str(data_longitude) + "\n")
            file.write("latitude = " + str(data_latitude) + "\n")
            file.write('\n')
            pass
