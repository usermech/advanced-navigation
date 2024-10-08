import rospy
from std_msgs.msg import PointCloud2

class transfer_pc2:
    """
    A ROS node that subscribes to /xtion/depth/points and publishes the same message to /obstacle_rgbd_layer/rgbd_base_mark. 
    This is used to transfer the PointCloud2 message from the depth camera to the obstacle_rgbd_layer to be used for navigation.

    Attributes:
        pub (Publisher): A ROS publisher that publishes PointCloud2 messages to /obstacle_rgbd_layer/rgbd_base_mark.
        sub (Subscriber): A ROS subscriber that subscribes to PointCloud2 messages from /xtion/depth/points.
    """
    def __init__(self):
        rospy.init_node('transfer_pc2', anonymous=True)
        self.pub = rospy.Publisher('/obstacle_rgbd_layer/rgbd_base_mark', PointCloud2, queue_size=10)
        self.sub = rospy.Subscriber('/xtion/depth/points', PointCloud2, self.callback)
        rospy.spin()

    def callback(self, msg):
        self.pub.publish(msg)

if __name__ == '__main__':
    try:
        transfer_pc2()
    except rospy.ROSInterruptException:
        pass
