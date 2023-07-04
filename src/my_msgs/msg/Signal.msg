# 消息作用：发送状态信号，表示飞机目前是处于侦查状态还是已经结束侦查航线（结束侦查后程序就要开始处理数据了）

# header：利用header.stamp为消息打上时间戳，方便使用ApproximateTimeSynchronizer同步消息。
# signal: 状态信号，0表示仍然处于侦查状态，1表示已经结束侦查


Header header
int32 signal