import schedule
import time
from datetime import datetime
import os
import fileconversion as fc

dateTimeObj = datetime.now()
ts = dateTimeObj.strftime("%d-%b-%Y_%H%M%S")  # generates new timestamp for unique filename on run


def capture_traffic():
    # os.chdir("C:\\Program Files\\Wireshark") only needed if tshark/wireshark is not in path run tshark within a
    # command line interface for a given time on a specified internet interface and remove mac addresses that we do
    # not want to keep track of
    os.system("tshark -i en0 -a duration:200 -w traffic-" + ts + ".pcap ether host not ac:bc:32:aa:2d:d1 and not "
                                                                "34:f6:4b:f7:a5:d0 and not 28:f0:76:5d:90:9c and not "
                                                                "3c:f0:11:24:21:38 and not 3c:f0:11:24:e4:70 ")


# specific function to run the 'capture_traffic()' function along with any other possible future code to run on a
# scheduled basis
def run_capture_code():
    capture_traffic()


# specific function to run the 'convert_file()' function from fileconversion.py along with any other possible future
# code to run on a scheduled basis
def run_convert_code():
    fc.convert_file()


# create a function that can be run from main that will run the scheduled functions
def my_schedule():
    # run the capture jobs first and then the convert jobs to automate whole system. schedule.every().friday.at(
    # "16:00").do(run_capture_code) schedule.every().thursday.at("14:00").do(run_capture_code) schedule.every(
    # ).tuesday.at("18:00").do(run_capture_code) schedule.every().friday.at("18:00").do(run_convert_code)
    # schedule.every().thursday.at("16:00").do(run_convert_code) schedule.every().tuesday.at("20:00").do(
    # run_convert_code) these two jobs test the system change time to see program run after two jobs done program
    # will continue to run due to the 'every()' part of each job
    schedule.every().wednesday.at("20:00").do(run_capture_code)
    schedule.every().wednesday.at("20:50").do(run_convert_code)
    while 1:
        schedule.run_pending()
        time.sleep(1)
