class CarService:
    def __init__(self, car_repo):
        self.__car_repo = car_repo

    def get_all_cars(self):
        return self.__car_repo.get_entities()

    def sequantial_search(self, token):
        all_cars = self.get_all_cars().values()
        for car in all_cars:
            if car.car_token == token:
                return car

    def binary_search(self, token):
        all_cars = list(self.get_all_cars().values())
        all_cars.sort(key=lambda car: car.car_token)
        left = 0
        right = len(all_cars) - 1
        while left <= right:
            mid = (left + right) // 2
            if all_cars[mid].car_token == token:
                return all_cars[mid]
            elif all_cars[mid].car_token < token:
                left = mid + 1
            else:
                right = mid - 1
        return None

    @staticmethod
    def comparator_by_token(first_car, other_car):
        return first_car.car_token < other_car.car_token

    @staticmethod
    def comparator_by_mark_model(first_car, other_car):
        if first_car.mark == other_car.mark:
            return first_car.model < other_car.model
        return first_car.mark < other_car.mark

    @staticmethod
    def comparator_by_mark_model_token(first_car, other_car):
        if first_car.mark == other_car.mark:
            if first_car.model == other_car.model:
                return first_car.car_token < other_car.car_token
            return first_car.model < other_car.model
        return first_car.mark < other_car.mark

    @staticmethod
    def comparator_by_profit(first_car, other_car):
        profit_car1 = first_car.sale_price - first_car.aquisition_price
        profit_car2 = other_car.sale_price - other_car.aquisition_price
        return profit_car1 < profit_car2

    def selection_sort(self, comparator):
        cars = list(self.get_all_cars().values())
        for i in range(len(cars)):
            min_index = i
            for j in range(i + 1, len(cars)):
                if comparator(cars[j], cars[min_index]):
                    min_index = j
            cars[i], cars[min_index] = cars[min_index], cars[i]
        return cars

    def quicksort(self, cars, comparator):
        if len(cars) <= 1:
            return cars
        pivot = cars[-1]
        left = []
        right = []
        for car in cars[:-1]:
            if comparator(car, pivot):
                left.append(car)
            else:
                right.append(car)
        return self.quicksort(left, comparator) + [pivot] + self.quicksort(right, comparator)



