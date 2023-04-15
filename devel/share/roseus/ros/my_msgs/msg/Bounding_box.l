;; Auto-generated. Do not edit!


(when (boundp 'my_msgs::Bounding_box)
  (if (not (find-package "MY_MSGS"))
    (make-package "MY_MSGS"))
  (shadow 'Bounding_box (find-package "MY_MSGS")))
(unless (find-package "MY_MSGS::BOUNDING_BOX")
  (make-package "MY_MSGS::BOUNDING_BOX"))

(in-package "ROS")
;;//! \htmlinclude Bounding_box.msg.html


(defclass my_msgs::Bounding_box
  :super ros::object
  :slots (_Class _conf _x1 _y1 _x2 _y2 ))

(defmethod my_msgs::Bounding_box
  (:init
   (&key
    ((:Class __Class) "")
    ((:conf __conf) 0.0)
    ((:x1 __x1) 0)
    ((:y1 __y1) 0)
    ((:x2 __x2) 0)
    ((:y2 __y2) 0)
    )
   (send-super :init)
   (setq _Class (string __Class))
   (setq _conf (float __conf))
   (setq _x1 (round __x1))
   (setq _y1 (round __y1))
   (setq _x2 (round __x2))
   (setq _y2 (round __y2))
   self)
  (:Class
   (&optional __Class)
   (if __Class (setq _Class __Class)) _Class)
  (:conf
   (&optional __conf)
   (if __conf (setq _conf __conf)) _conf)
  (:x1
   (&optional __x1)
   (if __x1 (setq _x1 __x1)) _x1)
  (:y1
   (&optional __y1)
   (if __y1 (setq _y1 __y1)) _y1)
  (:x2
   (&optional __x2)
   (if __x2 (setq _x2 __x2)) _x2)
  (:y2
   (&optional __y2)
   (if __y2 (setq _y2 __y2)) _y2)
  (:serialization-length
   ()
   (+
    ;; string _Class
    4 (length _Class)
    ;; float32 _conf
    4
    ;; int64 _x1
    8
    ;; int64 _y1
    8
    ;; int64 _x2
    8
    ;; int64 _y2
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _Class
       (write-long (length _Class) s) (princ _Class s)
     ;; float32 _conf
       (sys::poke _conf (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; int64 _x1
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _x1 (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _x1) (= (length (_x1 . bv)) 2)) ;; bignum
              (write-long (ash (elt (_x1 . bv) 0) 0) s)
              (write-long (ash (elt (_x1 . bv) 1) -1) s))
             ((and (class _x1) (= (length (_x1 . bv)) 1)) ;; big1
              (write-long (elt (_x1 . bv) 0) s)
              (write-long (if (>= _x1 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _x1 s)(write-long (if (>= _x1 0) 0 #xffffffff) s)))
     ;; int64 _y1
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _y1 (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _y1) (= (length (_y1 . bv)) 2)) ;; bignum
              (write-long (ash (elt (_y1 . bv) 0) 0) s)
              (write-long (ash (elt (_y1 . bv) 1) -1) s))
             ((and (class _y1) (= (length (_y1 . bv)) 1)) ;; big1
              (write-long (elt (_y1 . bv) 0) s)
              (write-long (if (>= _y1 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _y1 s)(write-long (if (>= _y1 0) 0 #xffffffff) s)))
     ;; int64 _x2
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _x2 (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _x2) (= (length (_x2 . bv)) 2)) ;; bignum
              (write-long (ash (elt (_x2 . bv) 0) 0) s)
              (write-long (ash (elt (_x2 . bv) 1) -1) s))
             ((and (class _x2) (= (length (_x2 . bv)) 1)) ;; big1
              (write-long (elt (_x2 . bv) 0) s)
              (write-long (if (>= _x2 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _x2 s)(write-long (if (>= _x2 0) 0 #xffffffff) s)))
     ;; int64 _y2
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _y2 (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _y2) (= (length (_y2 . bv)) 2)) ;; bignum
              (write-long (ash (elt (_y2 . bv) 0) 0) s)
              (write-long (ash (elt (_y2 . bv) 1) -1) s))
             ((and (class _y2) (= (length (_y2 . bv)) 1)) ;; big1
              (write-long (elt (_y2 . bv) 0) s)
              (write-long (if (>= _y2 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _y2 s)(write-long (if (>= _y2 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _Class
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _Class (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float32 _conf
     (setq _conf (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; int64 _x1
#+(or :alpha :irix6 :x86_64)
      (setf _x1 (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _x1 (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _y1
#+(or :alpha :irix6 :x86_64)
      (setf _y1 (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _y1 (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _x2
#+(or :alpha :irix6 :x86_64)
      (setf _x2 (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _x2 (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;; int64 _y2
#+(or :alpha :irix6 :x86_64)
      (setf _y2 (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _y2 (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(setf (get my_msgs::Bounding_box :md5sum-) "963f940de3c1365ed4d3926e5efc6c5f")
(setf (get my_msgs::Bounding_box :datatype-) "my_msgs/Bounding_box")
(setf (get my_msgs::Bounding_box :definition-)
      "# 消息说明
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
")



(provide :my_msgs/Bounding_box "963f940de3c1365ed4d3926e5efc6c5f")


