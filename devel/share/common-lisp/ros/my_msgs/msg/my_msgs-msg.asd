
(cl:in-package :asdf)

(defsystem "my_msgs-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :sensor_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "Bounding_box" :depends-on ("_package_Bounding_box"))
    (:file "_package_Bounding_box" :depends-on ("_package"))
    (:file "Boundingboxs_and_image" :depends-on ("_package_Boundingboxs_and_image"))
    (:file "_package_Boundingboxs_and_image" :depends-on ("_package"))
    (:file "Median_gps" :depends-on ("_package_Median_gps"))
    (:file "_package_Median_gps" :depends-on ("_package"))
    (:file "Signal" :depends-on ("_package_Signal"))
    (:file "_package_Signal" :depends-on ("_package"))
  ))