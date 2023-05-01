from repository.file_car_repo import FileCarRepository
from service.car_service import CarService
from ui.console import CarConsole

if __name__ == '__main__':
    car_repo = FileCarRepository("files/cars")

    car_serivce = CarService(car_repo)
    console = CarConsole(car_serivce)

    console.run_car_console()