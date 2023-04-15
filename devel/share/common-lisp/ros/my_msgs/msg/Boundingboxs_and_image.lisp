; Auto-generated. Do not edit!


(cl:in-package my_msgs-msg)


;//! \htmlinclude Boundingboxs_and_image.msg.html

(cl:defclass <Boundingboxs_and_image> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (bounding_boxs
    :reader bounding_boxs
    :initarg :bounding_boxs
    :type (cl:vector my_msgs-msg:Bounding_box)
   :initform (cl:make-array 0 :element-type 'my_msgs-msg:Bounding_box :initial-element (cl:make-instance 'my_msgs-msg:Bounding_box)))
   (image_list
    :reader image_list
    :initarg :image_list
    :type (cl:vector sensor_msgs-msg:Image)
   :initform (cl:make-array 0 :element-type 'sensor_msgs-msg:Image :initial-element (cl:make-instance 'sensor_msgs-msg:Image))))
)

(cl:defclass Boundingboxs_and_image (<Boundingboxs_and_image>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Boundingboxs_and_image>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Boundingboxs_and_image)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name my_msgs-msg:<Boundingboxs_and_image> is deprecated: use my_msgs-msg:Boundingboxs_and_image instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <Boundingboxs_and_image>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader my_msgs-msg:header-val is deprecated.  Use my_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'bounding_boxs-val :lambda-list '(m))
(cl:defmethod bounding_boxs-val ((m <Boundingboxs_and_image>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader my_msgs-msg:bounding_boxs-val is deprecated.  Use my_msgs-msg:bounding_boxs instead.")
  (bounding_boxs m))

(cl:ensure-generic-function 'image_list-val :lambda-list '(m))
(cl:defmethod image_list-val ((m <Boundingboxs_and_image>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader my_msgs-msg:image_list-val is deprecated.  Use my_msgs-msg:image_list instead.")
  (image_list m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Boundingboxs_and_image>) ostream)
  "Serializes a message object of type '<Boundingboxs_and_image>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'bounding_boxs))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'bounding_boxs))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'image_list))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'image_list))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Boundingboxs_and_image>) istream)
  "Deserializes a message object of type '<Boundingboxs_and_image>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'bounding_boxs) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'bounding_boxs)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'my_msgs-msg:Bounding_box))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'image_list) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'image_list)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'sensor_msgs-msg:Image))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Boundingboxs_and_image>)))
  "Returns string type for a message object of type '<Boundingboxs_and_image>"
  "my_msgs/Boundingboxs_and_image")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Boundingboxs_and_image)))
  "Returns string type for a message object of type 'Boundingboxs_and_image"
  "my_msgs/Boundingboxs_and_image")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Boundingboxs_and_image>)))
  "Returns md5sum for a message object of type '<Boundingboxs_and_image>"
  "b8d6383478d3cb0299e85875bbaf9e11")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Boundingboxs_and_image)))
  "Returns md5sum for a message object of type 'Boundingboxs_and_image"
  "b8d6383478d3cb0299e85875bbaf9e11")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Boundingboxs_and_image>)))
  "Returns full string definition for message of type '<Boundingboxs_and_image>"
  (cl:format cl:nil "# 消息说明~%# header: Header类型 包含三个元素 [stamp(时间戳)  frame_id(string类型,坐标系名称) seq(int类型, 序列号)]~%# bounding_boxs: Bounding_box列表类型,用于存储多个Bounding_box（一张图片中可能存在多个靶标）~%# sensor_msgs/Image[] image_list   储存yolov5框出的靶标图片(多张图片）。~%# 注意：这里bounding_boxs索引和image_list索引是对应的~%~%~%Header header~%Bounding_box[] bounding_boxs~%sensor_msgs/Image[] image_list~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: my_msgs/Bounding_box~%# 消息说明~%# Class 类别名  (大写原因是为了避开class关键字)~%# conf 置信度~%# x1 Bounding_box的左上角横坐标~%# y1 Bounding_box的左上角纵坐标~%# x2 Bounding_box的右下角横坐标~%# y2 Bounding_box的右下角纵坐标~%~%string Class~%float32 conf~%int64 x1~%int64 y1~%int64 x2~%int64 y2~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of camera~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in include/sensor_msgs/image_encodings.h~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Boundingboxs_and_image)))
  "Returns full string definition for message of type 'Boundingboxs_and_image"
  (cl:format cl:nil "# 消息说明~%# header: Header类型 包含三个元素 [stamp(时间戳)  frame_id(string类型,坐标系名称) seq(int类型, 序列号)]~%# bounding_boxs: Bounding_box列表类型,用于存储多个Bounding_box（一张图片中可能存在多个靶标）~%# sensor_msgs/Image[] image_list   储存yolov5框出的靶标图片(多张图片）。~%# 注意：这里bounding_boxs索引和image_list索引是对应的~%~%~%Header header~%Bounding_box[] bounding_boxs~%sensor_msgs/Image[] image_list~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: my_msgs/Bounding_box~%# 消息说明~%# Class 类别名  (大写原因是为了避开class关键字)~%# conf 置信度~%# x1 Bounding_box的左上角横坐标~%# y1 Bounding_box的左上角纵坐标~%# x2 Bounding_box的右下角横坐标~%# y2 Bounding_box的右下角纵坐标~%~%string Class~%float32 conf~%int64 x1~%int64 y1~%int64 x2~%int64 y2~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of camera~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in include/sensor_msgs/image_encodings.h~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Boundingboxs_and_image>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'bounding_boxs) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'image_list) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Boundingboxs_and_image>))
  "Converts a ROS message object to a list"
  (cl:list 'Boundingboxs_and_image
    (cl:cons ':header (header msg))
    (cl:cons ':bounding_boxs (bounding_boxs msg))
    (cl:cons ':image_list (image_list msg))
))
