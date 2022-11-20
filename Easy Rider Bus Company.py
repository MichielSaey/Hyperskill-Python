# Write your code here
import json


class BusStop:
    all_stops = []

    def __init__(self, bus_id, stop_id, stop_name, next_stop, stop_type, a_time):
        self.bus_id = bus_id
        self.stop_id = stop_id
        self.stop_name = stop_name
        self.next_stop = next_stop
        self.stop_type = stop_type
        self.a_time = a_time
        self.all_stops.append(self)


    def check_data(self):

        self

def readDate():
    json_string = input()
    bus_list = json.loads(json_string)

    for stop in bus_list:
        new_stop = BusStop(
            bus_id=stop["bus_id"],
            stop_id=stop["stop_id"],
            next_stop=stop["next_stop"],
            stop_name=stop["stop_name"],
            stop_type=stop["stop_type"],
            a_time=stop["a_time"]
        )


def main():
    readDate()

    for i in BusStop.all_stops:
        print(i.bus_id, i.stop_name)


if __name__ == "__main__":
    main()
