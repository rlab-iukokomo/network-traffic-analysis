import fileconversion as fc
import scheduler as sch


# runs the scheduled tasks and then parses the data afterwords
if __name__ == '__main__':
    # sch.my_schedule()
    sch.run_capture_code()
    sch.run_convert_code()
    fc.parse_data()
