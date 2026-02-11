import rclpy
from rclpy.node import Node
from tf2_msgs.msg import TFMessage
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSDurabilityPolicy
from tf_relay.frame_utils import apply_frame_prefix


class TFStaticRelay(Node):

    def __init__(self, namespace, agent):
        super().__init__('tf_static_relay' + '_' + str(agent))
        tf_static_topic = '/' + str(namespace) + '_' + str(agent) + '/tf_static'
        self.frame_prefix = str(namespace) + '_' + str(agent) + '/'
        self.unprefixed_frames = set(
            self.declare_parameter('unprefixed_frames', ['map']).value
        )
        self.static_subscription = self.create_subscription(
            msg_type=TFMessage,
            topic=tf_static_topic,
            callback=self.static_tf_callback,
            qos_profile=QoSProfile(
                reliability=QoSReliabilityPolicy.RELIABLE,
                durability=QoSDurabilityPolicy.TRANSIENT_LOCAL,
                depth=10,
            ),
        )

        self.static_publisher = self.create_publisher(
            msg_type=TFMessage,
            topic='/tf_static',
            qos_profile=QoSProfile(
                reliability=QoSReliabilityPolicy.RELIABLE,
                durability=QoSDurabilityPolicy.TRANSIENT_LOCAL,
                depth=10,
            ),
        )

    def static_tf_callback(self, msg):
        for transform in msg.transforms:
            transform.header.frame_id = apply_frame_prefix(
                transform.header.frame_id,
                self.frame_prefix,
                self.unprefixed_frames,
            )
            transform.child_frame_id = apply_frame_prefix(
                transform.child_frame_id,
                self.frame_prefix,
                self.unprefixed_frames,
            )
        self.static_publisher.publish(msg)
