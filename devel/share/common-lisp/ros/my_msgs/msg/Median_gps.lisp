; Auto-generated. Do not edit!


(cl:in-package my_msgs-msg)


;//! \htmlinclude Median_gps.msg.html

(cl:defclass <Median_gps> (roslisp-msg-protocol:ros-message)
  ((longitude
    :reader longitude
    :initarg :longitude
    :type cl:float
    :initform 0.0)
   (latitude
    :reader latitude
    :initarg :latitude
    :type cl:float
    :initform 0.0))
)

(cl:defclass Median_gps (<Median_gps>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Median_gps>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Median_gps)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name my_msgs-msg:<Median_gps> is deprecated: use my_msgs-msg:Median_gps instead.")))

(cl:ensure-generic-function 'longitude-val :lambda-list '(m))
(cl:defmethod longitude-val ((m <Median_gps>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader my_msgs-msg:longitude-val is deprecated.  Use my_msgs-msg:longitude instead.")
  (longitude m))

(cl:ensure-generic-function 'latitude-val :lambda-list '(m))
(cl:defmethod latitude-val ((m <Median_gps>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader my_msgs-msg:latitude-val is deprecated.  Use my_msgs-msg:latitude instead.")
  (latitude m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Median_gps>) ostream)
  "Serializes a message object of type '<Median_gps>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'longitude))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'latitude))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Median_gps>) istream)
  "Deserializes a message object of type '<Median_gps>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'longitude) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'latitude) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Median_gps>)))
  "Returns string type for a message object of type '<Median_gps>"
  "my_msgs/Median_gps")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Median_gps)))
  "Returns string type for a message object of type 'Median_gps"
  "my_msgs/Median_gps")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Median_gps>)))
  "Returns md5sum for a message object of type '<Median_gps>"
  "fd6c3d0b911e124b1f0b5a2ade9c1a01")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Median_gps)))
  "Returns md5sum for a message object of type 'Median_gps"
  "fd6c3d0b911e124b1f0b5a2ade9c1a01")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Median_gps>)))
  "Returns full string definition for message of type '<Median_gps>"
  (cl:format cl:nil "# 发送中位数靶标的gps坐标~%float64 longitude~%float64 latitude~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Median_gps)))
  "Returns full string definition for message of type 'Median_gps"
  (cl:format cl:nil "# 发送中位数靶标的gps坐标~%float64 longitude~%float64 latitude~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Median_gps>))
  (cl:+ 0
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Median_gps>))
  "Converts a ROS message object to a list"
  (cl:list 'Median_gps
    (cl:cons ':longitude (longitude msg))
    (cl:cons ':latitude (latitude msg))
))
