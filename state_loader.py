import csv


def load_state(file_name):
    with open(file_name, mode='r') as file:
        initial_state = set()
        csv_reader = csv.reader(file)
        for row in csv_reader:
            initial_state.add((int(row[0]), int(row[1])))
        return initial_state
