;; Auto-generated. Do not edit!


(when (boundp 'my_msgs::Signal)
  (if (not (find-package "MY_MSGS"))
    (make-package "MY_MSGS"))
  (shadow 'Signal (find-package "MY_MSGS")))
(unless (find-package "MY_MSGS::SIGNAL")
  (make-package "MY_MSGS::SIGNAL"))

(in-package "ROS")
;;//! \htmlinclude Signal.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass my_msgs::Signal
  :super ros::object
  :slots (_header _signal ))

(defmethod my_msgs::Signal
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:signal __signal) 0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _signal (round __signal))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:signal
   (&optional __signal)
   (if __signal (setq _signal __signal)) _signal)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; int32 _signal
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; int32 _signal
       (write-long _signal s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; int32 _signal
     (setq _signal (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get my_msgs::Signal :md5sum-) "78f41e618127bce049dd6104d9c31dc5")
(setf (get my_msgs::Signal :datatype-) "my_msgs/Signal")
(setf (get my_msgs::Signal :definition-)
      "# 消息作用：发送状态信号，表示飞机目前是处于侦查状态还是已经结束侦查航线（结束侦查后程序就要开始处理数据了）

# header：利用header.stamp为消息打上时间戳，方便使用ApproximateTimeSynchronizer同步消息。
# signal: 状态信号，0表示仍然处于侦查状态，1表示已经结束侦查


Header header
int32 signal
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

")



(provide :my_msgs/Signal "78f41e618127bce049dd6104d9c31dc5")


