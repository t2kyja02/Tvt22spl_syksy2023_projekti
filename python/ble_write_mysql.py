import asyncio
from bleak import BleakClient
import mysql.connector
import struct

counter = 0
data_list = []

# Connect to the MySQL server
db = mysql.connector.connect(user='dbaccess_rw',
                             password='fasdjkf2389vw2c3k234vk2f3',
                             host='172.20.241.9',
                             database='measurements')
cursor = db.cursor()

def on_disconnect(client):
    print (f"Disconnected from {client.address}")


def handle_notification(sender: int, data: bytearray):
    global counter
    global data_list

    # Convert bytes to int
    data = struct.unpack('i', data)[0]
    data_list.append(data)

    counter += 1


    if counter == 4:
        add_data = ("INSERT INTO rawdata (groupid, from_mac, to_mac, sensorvalue_a, sensorvalue_b, sensorvalue_c, sensorvalue_d, sensorvalue_e, sensorvalue_f) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")

        data_tuple = tuple([13, 'nRF5340', 'raspberrypi'] + data_list + [0, 0])
        print(data_tuple)

        cursor.execute(add_data, (data_tuple))
        db.commit()

        counter = 0
        data_list = []


async def run(address, loop):
    async with BleakClient(address, loop=loop) as client:
        client.set_disconnected_callback(on_disconnect)
        try:
            await client.start_notify('00001526-1212-efde-1523-785feabcd123',
                                        handle_notification)
            while True:
                await asyncio.sleep(1.0)
        except KeyboardInterrupt:
            await client.disconnect()
            cursor.close()
            db.close()

address = "C5:1B:05:74:C7:A2"
loop = asyncio.get_event_loop()
loop.run_until_complete(run(address, loop))
