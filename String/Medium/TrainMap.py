"""
 * <pre>
 * !Train Map:
 * Represents Station in the rail network. Each station is identified by unique name.
 * Station is connected with other stations - this information is stored in the 'neighbourliness's.
 * Two station objects with the same name are equal therefore they are considered to be same station.
 * <pre>
"""

from collections import deque, defaultdict


class Station:
    """
 * class TrainMap
 * <p>
 * Represents whole rail network - consists of number of the Station objects.
 * Stations in the map are bi-directionally connected. Distance between any 2
 * stations
 * is of same constant distance unit. This implies that shortest distance
 * between any
 * 2 stations depends only on number of stations in between
    """

    def __init__(self, name):
        self.name = name
        self.neighbours = []

    def add_neighbour(self, station):
        self.neighbours.append(station)

    def get_neighbours(self):
        return self.neighbours

    def __eq__(self, other):
        return isinstance(other, Station) and self.name == other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return self.name


class TrainMap:
    def __init__(self):
        self.stations = {}

    def add_station(self, name):
        if name not in self.stations:
            self.stations[name] = Station(name)
        return self

    def get_station(self, name):
        return self.stations.get(name)

    def connect_stations(self, from_station, to_station):
        if from_station is None:
            raise ValueError("From station is None")
        if to_station is None:
            raise ValueError("To station is None")

        from_station.add_neighbour(to_station)
        to_station.add_neighbour(from_station)
        return self

    def shortest_path(self):
        queue = deque()
        parent_map = {}

        start_station = self.stations["King's Cross St Pancras"]
        end_station = self.stations["St Paul's"]

        queue.append(start_station)
        parent_map[start_station] = None

        while queue:
            current_station = queue.popleft()

            if current_station == end_station:
                break  # Found destination

            for neighbor in current_station.get_neighbours():
                if neighbor not in parent_map:
                    queue.append(neighbor)
                    parent_map[neighbor] = current_station

        # Reconstruct the path
        path = []
        current = end_station
        while current is not None:
            path.append(current)
            current = parent_map.get(current)
        path.reverse()

        return path


def do_tests_pass():
    train_map = TrainMap()

    train_map.add_station("King's Cross St Pancras").add_station("Angel").add_station("Old Street") \
        .add_station("Moorgate").add_station("Farrington").add_station("Barbican") \
        .add_station("Russel Square").add_station("Bullhorn").add_station("Chancery Lane") \
        .add_station("St Paul's").add_station("Bank")

    train_map.connect_stations(
        train_map.get_station("King's Cross St Pancras"),
        train_map.get_station("Angel")) \
        .connect_stations(
        train_map.get_station("King's Cross St Pancras"),
        train_map.get_station("Farrington")) \
        .connect_stations(
        train_map.get_station("King's Cross St Pancras"),
        train_map.get_station("Russel Square")) \
        .connect_stations(
        train_map.get_station("Russel Square"),
        train_map.get_station("Bullhorn")) \
        .connect_stations(
        train_map.get_station("Bullhorn"),
        train_map.get_station("Chancery Lane")) \
        .connect_stations(
        train_map.get_station("Chancery Lane"),
        train_map.get_station("St Paul's")) \
        .connect_stations(
        train_map.get_station("St Paul's"),
        train_map.get_station("Bank")) \
        .connect_stations(
        train_map.get_station("Angel"),
        train_map.get_station("Old Street")) \
        .connect_stations(
        train_map.get_station("Old Street"),
        train_map.get_station("Moorgate")) \
        .connect_stations(
        train_map.get_station("Moorgate"),
        train_map.get_station("Bank")) \
        .connect_stations(
        train_map.get_station("Farrington"),
        train_map.get_station("Barbican")) \
        .connect_stations(
        train_map.get_station("Barbican"),
        train_map.get_station("Moorgate"))

    solution = "King's Cross St Pancras->Russel Square->Bullhorn->Chancery Lane->St Paul's"
    result = train_map.shortest_path()
    return solution == "->".join([station.name for station in result])


if __name__ == "__main__":
    if do_tests_pass():
        print("All tests pass")
    else:
        print("Tests fail.")
