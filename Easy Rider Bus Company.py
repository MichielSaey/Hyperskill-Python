# Write your code here
import json
import re
from datetime import datetime


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


class BusLine:
    saved_lines: [int] = []
    all_stops: [BusStop] = []
    all_lines = []

    all_start: [BusStop] = []
    all_stop: [BusStop] = []
    all_on_demand: [BusStop] = []

    def __init__(self, bus_id, stop):
        self.bus_id = bus_id
        self.start = None
        self.stop = None
        self.saved_lines.append(bus_id)
        self.stops_on_line = []
        self.add_stop(stop)

    def add_stop(self, stop: BusStop):

        self.all_stops.append(stop)
        self.stops_on_line.append(stop)
        # Start
        if stop.stop_type == 'S':
            if not self.start is None:
                raise Exception(stop)
            else:
                self.start = stop
                self.all_start.append(stop)
        elif stop.stop_type == 'F':
            if not self.stop is None:
                raise Exception(stop)
            else:
                self.stop = stop
                self.all_stop.append(stop)
        elif stop.stop_type == 'O':
            self.all_on_demand.append(stop)

    def validate(self):
        if self.start is None:
            raise Exception(self.bus_id)
        if self.stop is None:
            raise Exception(self.bus_id)

        time = datetime.strptime('00:00', '%H:%M')
        for stop in self.stops_on_line:
            current_stop_time = datetime.strptime(stop.a_time, '%H:%M')
            if current_stop_time > time:
                time = current_stop_time
            else:
                raise Exception(f'bus_id line {stop.bus_id}: wrong time on station {stop.stop_name}')

    def get_all_start_names(self):
        names: [str] = []
        for stop in self.all_start:
            if stop.stop_name not in names:
                names.append(stop.stop_name)
        names.sort()
        return names

    def get_all_transfer_names(self):
        names: [str] = []
        for stop in self.all_stops:
            counter = 0
            for i in self.all_stops:
                if stop.stop_id == i.stop_id:
                    counter += 1
            if counter > 1 and stop.stop_name not in names:
                names.append(stop.stop_name)
        names.sort()
        return names

    def get_all_on_demand_names(self):
        names: [str] = []
        for stop in self.all_on_demand:
            if stop.stop_name not in names:
                names.append(stop.stop_name)
        names.sort()
        return names

    def get_all_finish_names(self):
        names: [str] = []
        for stop in self.all_stop:
            if stop.stop_name not in names:
                names.append(stop.stop_name)
        names.sort()
        return names


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
    lines: [BusLine] = []
    for stop in BusStop.all_stops:
        # add to existing line
        if stop.bus_id in BusLine.saved_lines:
            for line in lines:
                if line.bus_id == stop.bus_id:
                    try:
                        line.add_stop(stop)
                    except Exception as err:
                        print("There are more than 1 starts or stops for the line: ", err)
                        exit()
        # create new line
        else:
            lines.append(BusLine(stop.bus_id, stop))
    BusLine.all_lines = lines


def dataValidation():
    n_bus_id_error = 0
    n_stop_id_error = 0
    n_stop_name_error = 0
    n_next_stop_error = 0
    n_stop_type_error = 0
    n_a_time_error = 0

    stops_dict = dict()

    for i in BusStop.all_stops:

        # bus_id
        if i.bus_id == "":
            n_bus_id_error += 1
        elif not type(i.bus_id) == int:
            n_bus_id_error += 1

        if i.bus_id in stops_dict.keys():
            stops_dict[i.bus_id] += 1
        else:
            stops_dict[i.bus_id] = 1

        # stop_id
        if i.stop_id == "":
            n_stop_id_error += 1
        elif not type(i.stop_id) == int:
            n_stop_id_error += 1

        # stop_name
        pattern = re.compile(r"([A-Z][\w ]+)+ (Road|Street|Avenue|Boulevard)\Z")
        match = pattern.match(i.stop_name)
        if pattern.match(i.stop_name) is None:
            n_stop_name_error += 1

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
        pattern = re.compile(r"\A[0-2][0-9]:[0-5][0-9]\Z")
        match = pattern.match(i.a_time)
        if match is None:
            n_a_time_error += 1

    n_total_errors = n_a_time_error + n_stop_id_error + n_next_stop_error + n_stop_name_error + n_stop_type_error \
                     + n_bus_id_error

    # print(f'Format validation: {n_total_errors} errors')
    # print("bus_id: ", n_bus_id_error)
    # print("stop_id: ", n_stop_id_error)
    # print("stop_name: ", n_stop_name_error)
    # print("next_stop: ", n_next_stop_error)
    # print("stop_type: ", n_stop_type_error)
    # print("a_time: ", n_a_time_error)

    print('Line names and number of stops:')
    for key, value in stops_dict.items():
        print(f"bus_id: {key}, stops: {value}")


def lineValidation():
    lines: [BusLine] = BusLine.all_lines

    for line in lines:
        try:
            line.validate()
        except Exception as err:
            print(f"There is no start or end stop for the line: {err}.")
            exit()

    print(f'Start stop: {len(lines[0].get_all_start_names())} {lines[0].get_all_start_names()}')
    print(f'Transfer stop: {len(lines[0].get_all_transfer_names())} {lines[0].get_all_transfer_names()}')
    print(f'Finish stop: {len(lines[0].get_all_finish_names())} {lines[0].get_all_finish_names()}')


def timeValidation():
    lines: [BusLine] = BusLine.all_lines
    fault = False
    print('Arrival time test:')
    for line in lines:
        try:
            line.validate()
        except Exception as err:
            print(err)
            fault = True
    if not fault:
        print('OK')


def typeValidation():
    print('On demand stops test:')
    wrong_types = []
    s_types = set(BusLine.all_lines[0].get_all_start_names())
    f_types = set(BusLine.all_lines[0].get_all_finish_names())
    o_types = set(BusLine.all_lines[0].get_all_on_demand_names())
    t_types = set(BusLine.all_lines[0].get_all_transfer_names())
    wrong_types = list(set.intersection(o_types, t_types))
    if not wrong_types:
        print('OK')
    else:
        wrong_types.sort()
        print(f'Wrong stop type: {wrong_types}')


def main():
    readDate()
    typeValidation()


if __name__ == "__main__":
    main()
