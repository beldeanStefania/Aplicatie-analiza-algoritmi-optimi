class Repository:
    def __init__(self, ):
        self.__all_entities = {}

    def get_entities(self):
        return self.__all_entities.copy()

    def add_entity(self, entity):
        self.__all_entities[entity.car_token] = entity