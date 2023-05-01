from dataclasses import dataclass


@dataclass
class Car:
    mark: str
    model: str
    __car_token: str
    aquisition_price: int
    sale_price: int

    @property
    def car_token(self):
        return self.__car_token

    def __str__(self):
        return "Mark:{0} Model:{1} Car_token:{2} Aquisition_price:{3} Sale_price{4}".format(self.mark, self.model,
                                                                                            self.car_token,
                                                                                            self.aquisition_price,
                                                                                            self.sale_price)