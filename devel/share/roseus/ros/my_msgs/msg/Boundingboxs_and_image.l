;; Auto-generated. Do not edit!


(when (boundp 'my_msgs::Boundingboxs_and_image)
  (if (not (find-package "MY_MSGS"))
    (make-package "MY_MSGS"))
  (shadow 'Boundingboxs_and_image (find-package "MY_MSGS")))
(unless (find-package "MY_MSGS::BOUNDINGBOXS_AND_IMAGE")
  (make-package "MY_MSGS::BOUNDINGBOXS_AND_IMAGE"))

(in-package "ROS")
;;//! \htmlinclude Boundingboxs_and_image.msg.html
(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass my_msgs::Boundingboxs_and_image
  :super ros::object
  :slots (_header _bounding_boxs _image_list ))

(defmethod my_msgs::Boundingboxs_and_image
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:bounding_boxs __bounding_boxs) ())
    ((:image_list __image_list) ())
    )
   (send-super :init)
   (setq _header __header)
   (setq _bounding_boxs __bounding_boxs)
   (setq _image_list __image_list)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:bounding_boxs
   (&rest __bounding_boxs)
   (if (keywordp (car __bounding_boxs))
       (send* _bounding_boxs __bounding_boxs)
     (progn
       (if __bounding_boxs (setq _bounding_boxs (car __bounding_boxs)))
       _bounding_boxs)))
  (:image_list
   (&rest __image_list)
   (if (keywordp (car __image_list))
       (send* _image_list __image_list)
     (progn
       (if __image_list (setq _image_list (car __image_list)))
       _image_list)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; my_msgs/Bounding_box[] _bounding_boxs
    (apply #'+ (send-all _bounding_boxs :serialization-length)) 4
    ;; sensor_msgs/Image[] _image_list
    (apply #'+ (send-all _image_list :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; my_msgs/Bounding_box[] _bounding_boxs
     (write-long (length _bounding_boxs) s)
     (dolist (elem _bounding_boxs)
       (send elem :serialize s)
       )
     ;; sensor_msgs/Image[] _image_list
     (write-long (length _image_list) s)
     (dolist (elem _image_list)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; my_msgs/Bounding_box[] _bounding_boxs
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _bounding_boxs (let (r) (dotimes (i n) (push (instance my_msgs::Bounding_box :init) r)) r))
     (dolist (elem- _bounding_boxs)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; sensor_msgs/Image[] _image_list
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _image_list (let (r) (dotimes (i n) (push (instance sensor_msgs::Image :init) r)) r))
     (dolist (elem- _image_list)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get my_msgs::Boundingboxs_and_image :md5sum-) "b8d6383478d3cb0299e85875bbaf9e11")
(setf (get my_msgs::Boundingboxs_and_image :datatype-) "my_msgs/Boundingboxs_and_image")
(setf (get my_msgs::Boundingboxs_and_image :definition-)
      "# 消息说明
# header: Header类型 包含三个元素 [stamp(时间戳)  frame_id(string类型,坐标系名称) seq(int类型, 序列号)]
# bounding_boxs: Bounding_box列表类型,用于存储多个Bounding_box（一张图片中可能存在多个靶标）
# sensor_msgs/Image[] image_list   储存yolov5框出的靶标图片(多张图片）。
# 注意：这里bounding_boxs索引和image_list索引是对应的


Header header
Bounding_box[] bounding_boxs
sensor_msgs/Image[] image_list
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: my_msgs/Bounding_box
# 消息说明
# Class 类别名  (大写原因是为了避开class关键字)
# conf 置信度
# x1 Bounding_box的左上角横坐标
# y1 Bounding_box的左上角纵坐标
# x2 Bounding_box的右下角横坐标
# y2 Bounding_box的右下角纵坐标

string Class
float32 conf
int64 x1
int64 y1
int64 x2
int64 y2
================================================================================
MSG: sensor_msgs/Image
# This message contains an uncompressed image
# (0, 0) is at top-left corner of image
#

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of camera
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image
                     # If the frame_id here and the frame_id of the CameraInfo
                     # message associated with the image conflict
                     # the behavior is undefined

uint32 height         # image height, that is, number of rows
uint32 width          # image width, that is, number of columns

# The legal values for encoding are in file src/image_encodings.cpp
# If you want to standardize a new string format, join
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.

string encoding       # Encoding of pixels -- channel meaning, ordering, size
                      # taken from the list of strings in include/sensor_msgs/image_encodings.h

uint8 is_bigendian    # is this data bigendian?
uint32 step           # Full row length in bytes
uint8[] data          # actual matrix data, size is (step * rows)

")



(provide :my_msgs/Boundingboxs_and_image "b8d6383478d3cb0299e85875bbaf9e11")


