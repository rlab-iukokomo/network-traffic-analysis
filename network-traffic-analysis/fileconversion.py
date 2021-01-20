import os
import pyshark
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scheduler as sch


def convert_file():
    # os.chdir("C:\\Program Files\\Wireshark") only needed if tshark is not in path
    # reads traffic data from pcap and writes it to .csv for pandas to read and manipulate
    os.system("tshark -r traffic-" + sch.ts + ".pcap -T fields -e frame.number -e frame.time -e eth.src -e eth.dst -e "
                                              "ip.src -e "
                                              "ip.dst -e ip.proto -E header=y -E separator=,  -E occurrence=f "
                                              "> network_traffic-" + sch.ts + ".csv")


def parse_data():
    # creates panda series from .csv file
    traffic_data = pd.read_csv("network_traffic-" + sch.ts + ".csv")

    # assigns columns in traffic data
    traffic_data.columns = ['No.', 'Time', 'Source', 'Destination', 'Protocol', 'Length', 'Info']

    # counts occurrences of column 'Source' to store packet numbers
    counts = traffic_data['Source'].value_counts()

    # converts panda series to DataFrame
    countsdf = counts.to_frame()
    countsdf.columns = ['packet_count']

    # sorts DataFrame by mac address (could be pointless now that we aren't hard-mapping device names?) need to keep
    # sorted index or at least maintain a parallel mapping of mac_address array and index values plotted i.e.
    # mac_address[0] holds mac address for device 'A' thus first entry of dataframe index should be 'A' for this
    # specific example for each data collection mac_address will still be dynamic but parallel relationship between
    # mac_address entries and sorted_traffic index values must be maintained. this line could be removed as long as
    # following code does not alter arrangement of sorted_traffic indexes as mac_address array has already been
    # populated.
    sorted_traffic = countsdf.sort_index(ascending=True)

    # make an array called mac_addresses from index values of sorted_traffic
    mac_addresses = sorted_traffic.index.values

    # update with new mac address:device pairs to fill dictionary
    devices = {'24:f5:a2:bf:1a:48': 'NightsWatch_2.4', '28:f0:76:5d:90:9c': 'Professor iMac',
               '60:01:94:cb:ad:26': 'KMC Plug -powerstrip', '68:ff:7b:36:62:b6': 'Kasa Plug -alexa',
               '68:ff:7b:55:9f:aa': 'Kasa Plug -wyze', '68:ff:7b:55:a4:57': 'Kasa Plug -nanoleaf',
               'b0:be:76:db:bd:87': 'Kasa Plug -wall', '44:00:49:0f:ad:7e': 'Amazon Cam',
               'e0:89:7e:6c:25:34': 'Apple TV', '84:0d:8e:6b:c0:3d': 'KMC Plug -Kasa Bulb',
               '28:6d:97:a2:e6:51': 'SmartThings Hub', '9c:43:1e:45:94:49': 'Ring bridge',
               '34:f6:4b:f7:a5:d0': 'Windows Laptop', 'ac:bc:32:aa:2d:d1': 'Student MacBook',
               '3c:f0:11:24:21:38': 'Mac near Lab', '3c:f0:11:24:e4:70': 'Mac near Lab',
               '1c:f2:9a:46:fd:ab': 'Google Device', '2c:aa:8e:1d:cf:c2': 'Wyze Camera'}

    # function to dynamically assign device names to mac addresses for visualization via
    # the dictionary devices
    def mac_to_device(d):
        device_list = []
        for i in range((len(mac_addresses))):
            if mac_addresses[i] in d.keys():
                device_list.append(d.get(mac_addresses[i]))
            else:
                device_list.append(mac_addresses[i])
        return device_list

    # inserts list returned from mac_to_device function into "Device" column in DataFrame
    sorted_traffic.insert(0, "Device", mac_to_device(devices), True)

    # assigns x and y values
    x = sorted_traffic['Device']
    y = sorted_traffic['packet_count']

    # plots data and sets titles etc.
    plt.rcdefaults()
    fig, ax = plt.subplots()
    y_pos = np.arange(len(x))
    ax.barh(x, y, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(x)
    ax.invert_yaxis()
    ax.set_xlabel('Packet Count')
    ax.set_title('Network Traffic on NightsWatch_2.4')

    # displays plot
    plt.show()

    # saves plot as .png file in directory
    fig.savefig('traffic-data-' + sch.ts + '.png')
