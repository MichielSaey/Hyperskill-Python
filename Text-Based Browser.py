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

    n_bus_id_error = 0
    n_stop_id_error = 0
    n_stop_name_error = 0
    n_next_stop_error = 0
    n_stop_type_error = 0
    n_a_time_error = 0

    for i in BusStop.all_stops:

        # bus_id
        if i.bus_id == "":
            n_bus_id_error += 1
        elif not type(i.bus_id) == int:
            n_bus_id_error += 1

        # stop_id
        if i.stop_id == "":
            n_stop_id_error += 1
        elif not type(i.stop_id) == int:
            n_stop_id_error += 1

        # stop_name
        suffix = ["boulevard", "street", "avenue", "road"]
        if i.stop_name == "":
            n_stop_name_error += 1
        elif not type(i.stop_name) == str:
            n_stop_name_error += 1
        # elif not i.stop_name.lower().endswith(tuple(suffix)):
            # print(i.stop_name)
            # n_stop_name_error += 1
        # elif not i.stop_name[0].isupper():
            # n_stop_name_error += 1

        # next_stop
        if i.next_stop == "":
            n_next_stop_error += 1
        elif not type(i.next_stop) == int:
            n_next_stop_error += 1

        # stop_type
        types = ["S", "O", "F", ""]
        if i.stop_type not in types:
            n_stop_type_error += 1

        # a_time
        if i.a_time == "":
            n_a_time_error += 1
        elif not type(i.a_time) == str:
            n_a_time_error += 1

    n_total_errors = n_a_time_error + n_stop_id_error + n_next_stop_error + n_stop_name_error + n_stop_type_error \
                     + n_bus_id_error

    print(f'Type and required field validation: {n_total_errors} errors')
    print("bus_id: ", n_bus_id_error)
    print("stop_id: ", n_stop_id_error)
    print("stop_name: ", n_stop_name_error)
    print("next_stop: ", n_next_stop_error)
    print("stop_type: ", n_stop_type_error)
    print("a_time: ", n_a_time_error)


if __name__ == "__main__":
    main()
