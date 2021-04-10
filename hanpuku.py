from ppadb.client import Client

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('No device attached.')
    quit()

device = devices[0]

while True:
    # center
    device.shell('input touchscreen tap 735 2410 735 2410')
    # right
    device.shell('input touchscreen tap 1200 2410 1200 2410')
    # center
    device.shell('input touchscreen tap 735 2410 735 2410')
    # left
    device.shell('input touchscreen tap 250 2410 250 2410')


if __name__ == '__main__':
    print('PyCharm')