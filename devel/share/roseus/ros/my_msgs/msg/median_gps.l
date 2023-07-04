;; Auto-generated. Do not edit!


(when (boundp 'my_msgs::median_gps)
  (if (not (find-package "MY_MSGS"))
    (make-package "MY_MSGS"))
  (shadow 'median_gps (find-package "MY_MSGS")))
(unless (find-package "MY_MSGS::MEDIAN_GPS")
  (make-package "MY_MSGS::MEDIAN_GPS"))

(in-package "ROS")
;;//! \htmlinclude median_gps.msg.html


(defclass my_msgs::median_gps
  :super ros::object
  :slots (_longitude _latitude ))

(defmethod my_msgs::median_gps
  (:init
   (&key
    ((:longitude __longitude) 0.0)
    ((:latitude __latitude) 0.0)
    )
   (send-super :init)
   (setq _longitude (float __longitude))
   (setq _latitude (float __latitude))
   self)
  (:longitude
   (&optional __longitude)
   (if __longitude (setq _longitude __longitude)) _longitude)
  (:latitude
   (&optional __latitude)
   (if __latitude (setq _latitude __latitude)) _latitude)
  (:serialization-length
   ()
   (+
    ;; float64 _longitude
    8
    ;; float64 _latitude
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _longitude
       (sys::poke _longitude (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _latitude
       (sys::poke _latitude (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _longitude
     (setq _longitude (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _latitude
     (setq _latitude (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get my_msgs::median_gps :md5sum-) "fd6c3d0b911e124b1f0b5a2ade9c1a01")
(setf (get my_msgs::median_gps :datatype-) "my_msgs/median_gps")
(setf (get my_msgs::median_gps :definition-)
      "# 发送中位数靶标的gps坐标
float64 longitude
float64 latitude
")



(provide :my_msgs/median_gps "fd6c3d0b911e124b1f0b5a2ade9c1a01")


