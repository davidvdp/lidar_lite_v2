import smbus2
import time
import argparse


class LidarLiteV2:
    type_name = "LidarLiteV2"

    def __init__(self, bus=1):
        self.SubVariables = {
        }
        self.address = 0x62
        self.distWriteReg = 0x00
        self.distWriteVal = 0x04
        self.distReadReg1 = 0x8f
        self.distReadReg2 = 0x10
        # self.velWriteReg = 0x04
        # self.velWriteVal = 0x08
        # self.velReadReg = 0x09
        self.bus = None
        self.__connect(bus)

    def __connect(self, bus):
        self.bus = smbus2.SMBus(bus)
        time.sleep(0.5)

    def __write_and_wait(self, register, value):
        self.bus.write_byte_data(self.address, register, value)
        time.sleep(0.01)

    def __read_and_wait(self, register):
        res = self.bus.read_byte_data(self.address, register)
        time.sleep(0.001)
        return res

    def get_distance(self):
        self.__write_and_wait(self.distWriteReg, self.distWriteVal)
        dist1 = self.__read_and_wait(self.distReadReg1)
        dist2 = self.__read_and_wait(self.distReadReg2)
        return (dist1 << 8) + dist2


def main():
    from datetime import datetime
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--bus',
        '-b',
        help='I2C bus for Lidar Lite',
        default=1
    )
    args = parser.parse_args()

    bus = args.bus
    lidar_lite = LidarLiteV2(bus)
    previous_time = datetime.now()
    while True:
        try:
            now = datetime.now()
            duration = now - previous_time
            previous_time = now
            print('{} cm @ {} seconds per measurement'.format(lidar_lite.get_distance(), duration.total_seconds()))
        except KeyboardInterrupt:
            exit(0)


if __name__ == '__main__':
    main()
