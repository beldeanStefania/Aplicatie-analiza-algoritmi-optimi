import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__} Took {total_time:.4f} seconds')
        return result

    return timeit_wrapper

class CarConsole:
    def __init__(self, car_service):
        self.__car_service = car_service

    def run_car_console(self):
        print_options = {
            "all": self.ui_print_cars
        }
        search_options = {
            "token": self.ui_search_by_token
        }
        bsearch_options = {
            "token": self.ui_binary_search_token
        }
        sort_options = {
            "token": self.ui_selection_sort,
            "markModel": self.ui_selection_sort_mark_model,
            "markModelToken": self.ui_selection_sort_mark_model_token,
            "profit": self.ui_selection_sort_profit,
        }
        quicksort_options = {
            "token": self.ui_quicksort,
            "markModel": self.ui_quicksort_mark_model,
            "markModelToken": self.ui_quicksort_mark_model_token,
            "profit": self.ui_quicksort_profit
        }
        options = {
            "PRINT": print_options,
            "SEARCH": search_options,
            "BSEARCH": bsearch_options,
            "SORT": sort_options,
            "QUICKSORT": quicksort_options
        }
        while True:
            opt = input("Command :")
            opt = opt.strip()
            if opt == "exit":
                break
            # elif opt == "HELP":
            #     print(print_options.keys())
            #     continue
            try:
                command, parameter = opt.split(" ")
                options[command][parameter]()
            except KeyError:
                print("Option do not exist")
            except ValueError:
                print("Invalid command")

    def ui_print_cars(self):
        if self.__car_service.get_all_cars().__len__() == 0:
            print("There are no cars")
        else:
            print("Car list")
            for car in self.__car_service.get_all_cars().values():
                print(car)

    @timeit
    def ui_search_by_token(self):
        token = input("Token:")
        print(self.__car_service.sequantial_search(token))

    @timeit
    def ui_binary_search_token(self):
        token = input("Token:")
        print(self.__car_service.binary_search(token))

    @timeit
    def ui_selection_sort(self):
        cars = self.__car_service.selection_sort(self.__car_service.comparator_by_token)
        for car in cars:
            print(car)

    @timeit
    def ui_quicksort(self):
        cars = list(self.__car_service.get_all_cars().values())
        cars = self.__car_service.quicksort(cars, self.__car_service.comparator_by_token)
        for car in cars:
            print(car)

    @timeit
    def ui_quicksort_mark_model(self):
        cars = list(self.__car_service.get_all_cars().values())
        cars = self.__car_service.quicksort(cars, self.__car_service.comparator_by_mark_model)
        for car in cars:
            print(car)

    @timeit
    def ui_selection_sort_mark_model(self):
        cars = self.__car_service.selection_sort(self.__car_service.comparator_by_mark_model)
        for car in cars:
            print(car)

    @timeit
    def ui_selection_sort_mark_model_token(self):
        cars = self.__car_service.selection_sort(self.__car_service.comparator_by_mark_model_token)
        for car in cars:
            print(car)

    @timeit
    def ui_quicksort_mark_model_token(self):
        cars = list(self.__car_service.get_all_cars().values())
        cars = self.__car_service.quicksort(cars, self.__car_service.comparator_by_mark_model_token)
        for car in cars:
            print(car)

    @timeit
    def ui_selection_sort_profit(self):
        cars = self.__car_service.selection_sort(self.__car_service.comparator_by_profit)
        for car in cars * 5:
            print(car)

    @timeit
    def ui_quicksort_profit(self):
        cars = list(self.__car_service.get_all_cars().values())
        cars = self.__car_service.quicksort(cars, self.__car_service.comparator_by_profit)
        for car in cars * 5:
            print(car)