from domain.entities import Car
from repository.car_repo import Repository


class FileCarRepository(Repository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load_data()

    def __load_data(self):
        with open(self.__file_name, "r") as f:
            for line in f:
                line = line.strip()
                array = line.split(" ")
                car = Car(array[0], array[1], array[2], int(array[3]), int(array[4]))
                self.add_entity(car)