;; Auto-generated. Do not edit!


(when (boundp 'pub_sub::Person)
  (if (not (find-package "PUB_SUB"))
    (make-package "PUB_SUB"))
  (shadow 'Person (find-package "PUB_SUB")))
(unless (find-package "PUB_SUB::PERSON")
  (make-package "PUB_SUB::PERSON"))

(in-package "ROS")
;;//! \htmlinclude Person.msg.html


(defclass pub_sub::Person
  :super ros::object
  :slots (_name _age _height ))

(defmethod pub_sub::Person
  (:init
   (&key
    ((:name __name) "")
    ((:age __age) 0)
    ((:height __height) 0.0)
    )
   (send-super :init)
   (setq _name (string __name))
   (setq _age (round __age))
   (setq _height (float __height))
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:age
   (&optional __age)
   (if __age (setq _age __age)) _age)
  (:height
   (&optional __height)
   (if __height (setq _height __height)) _height)
  (:serialization-length
   ()
   (+
    ;; string _name
    4 (length _name)
    ;; uint8 _age
    1
    ;; float32 _height
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;; uint8 _age
       (write-byte _age s)
     ;; float32 _height
       (sys::poke _height (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; uint8 _age
     (setq _age (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; float32 _height
     (setq _height (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get pub_sub::Person :md5sum-) "a1a605e7739c1dae4a9f9da042a45b0f")
(setf (get pub_sub::Person :datatype-) "pub_sub/Person")
(setf (get pub_sub::Person :definition-)
      "string name
uint8 age
float32 height
")



(provide :pub_sub/Person "a1a605e7739c1dae4a9f9da042a45b0f")


