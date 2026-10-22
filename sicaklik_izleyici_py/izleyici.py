import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32


class IzleyiciNode(Node):
    def __init__(self):
        super().__init__('izleyici_node')

        # Parametre tanımlanır (varsayılan değer: 29.0)
        self.declare_parameter('esik_degeri', 29.0)

        # subscriber oluşturulur.
        self.subscription = self.create_subscription(
            Float32,
            'sicaklik',
            self.listener_callback,
            10
        )
        self.get_logger().info('Sıcaklık izleyici düğümü başlatıldı.')

    def listener_callback(self, msg):
        # güncel parametre değeri okunur.
        esik = self.get_parameter('esik_degeri').get_parameter_value().double_value

        # gelen değeri ekrana yazdırır.
        self.get_logger().info(f"Gelen sıcaklık değeri: {msg.data:.2f} °C")

        # Değer eşikten fazlaysa uyarı verir.
        if msg.data > esik:
            self.get_logger().warn(f"Uyarı: Sıcaklık değeri eşik değerini aştı! ({msg.data:.2f} °C > {esik:.2f} °C)")

def main(args=None):
    rclpy.init(args=args)
    node = IzleyiciNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()


