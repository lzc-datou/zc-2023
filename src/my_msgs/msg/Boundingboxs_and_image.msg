# 消息说明
# header: Header类型 包含三个元素 [stamp(时间戳)  frame_id(string类型,坐标系名称) seq(int类型, 序列号)]
# bounding_boxs: Bounding_box列表类型,用于存储多个Bounding_box（一张图片中可能存在多个靶标）
# sensor_msgs/Image[] image_list   储存yolov5框出的靶标图片(多张图片）。
# 注意：这里bounding_boxs索引和image_list索引是对应的


Header header
Bounding_box[] bounding_boxs
sensor_msgs/Image[] image_list