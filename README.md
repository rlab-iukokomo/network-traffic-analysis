# IoT Household Network Traffic Analysis
This project is designed to collect and analyze traffic within a network with<br>
the use of Python scripts and libraries with the following external libraries:<br>
<i>-tshark<br>
-pandas<br>
-matplotlib<br>
-numpy<br></i>

## Included files:

### fileconversion.py

-<b>convert_file()</b>: reads traffic data from pcap and writes it to .csv for pandas to<br>
read and manipulate.<br>
-<b>parse_data()</b>: creates <a href='https://pandas.pydata.org/docs/user_guide/index.html'>panda</a> series from .csv 
file and parses the data obtained<br>
for the purpose of creating visualizations for analysis with 
<a href='https://matplotlib.org/3.3.3/contents.html'>matplotlib</a><br>
-<b>mac_to_device(d)</b>: accepts a dictionary named {devices} of mapped MAC addresses to device<br>
names for user readability.<br>

### scheduler.py

-<b>capture_traffic()</b>: function called to begin capturing traffic via 
<a href='https://www.wireshark.org/docs/man-pages/tshark.html'>tshark</a> external library<br>
-<b>run_capture_code()</b>: calls capture_traffic() function.<br>
-<b>run_convert_code()</b>: calls functions in 'fileconversion.py'.<br>
-<b>my_schedule()</b>: uses <a href='https://docs.python.org/3.8/library/time.html'>time</a> library to allow user to
schedule their traffic scans and analyses.

### /sample-data/ directory

This folder includes sample traffic collected for analysis and resulting visualizations from our lab.
