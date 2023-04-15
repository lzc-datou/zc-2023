// Auto-generated. Do not edit!

// (in-package my_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let Bounding_box = require('./Bounding_box.js');
let sensor_msgs = _finder('sensor_msgs');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class Boundingboxs_and_image {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.bounding_boxs = null;
      this.image_list = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('bounding_boxs')) {
        this.bounding_boxs = initObj.bounding_boxs
      }
      else {
        this.bounding_boxs = [];
      }
      if (initObj.hasOwnProperty('image_list')) {
        this.image_list = initObj.image_list
      }
      else {
        this.image_list = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Boundingboxs_and_image
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [bounding_boxs]
    // Serialize the length for message field [bounding_boxs]
    bufferOffset = _serializer.uint32(obj.bounding_boxs.length, buffer, bufferOffset);
    obj.bounding_boxs.forEach((val) => {
      bufferOffset = Bounding_box.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [image_list]
    // Serialize the length for message field [image_list]
    bufferOffset = _serializer.uint32(obj.image_list.length, buffer, bufferOffset);
    obj.image_list.forEach((val) => {
      bufferOffset = sensor_msgs.msg.Image.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Boundingboxs_and_image
    let len;
    let data = new Boundingboxs_and_image(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [bounding_boxs]
    // Deserialize array length for message field [bounding_boxs]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.bounding_boxs = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.bounding_boxs[i] = Bounding_box.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [image_list]
    // Deserialize array length for message field [image_list]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.image_list = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.image_list[i] = sensor_msgs.msg.Image.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    object.bounding_boxs.forEach((val) => {
      length += Bounding_box.getMessageSize(val);
    });
    object.image_list.forEach((val) => {
      length += sensor_msgs.msg.Image.getMessageSize(val);
    });
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'my_msgs/Boundingboxs_and_image';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'b8d6383478d3cb0299e85875bbaf9e11';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # 消息说明
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Boundingboxs_and_image(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.bounding_boxs !== undefined) {
      resolved.bounding_boxs = new Array(msg.bounding_boxs.length);
      for (let i = 0; i < resolved.bounding_boxs.length; ++i) {
        resolved.bounding_boxs[i] = Bounding_box.Resolve(msg.bounding_boxs[i]);
      }
    }
    else {
      resolved.bounding_boxs = []
    }

    if (msg.image_list !== undefined) {
      resolved.image_list = new Array(msg.image_list.length);
      for (let i = 0; i < resolved.image_list.length; ++i) {
        resolved.image_list[i] = sensor_msgs.msg.Image.Resolve(msg.image_list[i]);
      }
    }
    else {
      resolved.image_list = []
    }

    return resolved;
    }
};

module.exports = Boundingboxs_and_image;
