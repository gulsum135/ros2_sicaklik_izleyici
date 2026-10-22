import random
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class Sensor(Node):
    def __init__(self):
        super().__init__("sensor_node")
        self.publisher_ = self.create_publisher(Float32, "sicaklik", 10)
        self.timer_ = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info("Sıcaklık sensör düğümü başlatıldı.")

    def timer_callback(self):
        msg = Float32()
        msg.data = round(random.uniform(28.0, 30.0), 2)
        self.publisher_.publish(msg)
        self.get_logger().info(f"Sıcaklık değeri yayınlandı: {msg.data:.2f} °C")

def main(args=None):
    rclpy.init(args=args)
    node = Sensor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()