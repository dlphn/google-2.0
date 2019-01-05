from enum import Enum


class Operation(Enum):
    OR = 1
    AND = 2
    NOT = 3


class NonValidRequestException(Exception):
    def __init__(self, request):
        print("This is not a valid request, please check your arguments :{}".format(request))


class BooleanRequest:

    def __init__(self, operation: Operation, first_term, second_term=None):
        self.operation = operation
        self.first = first_term
        self.second = second_term
        if self.operation == Operation.NOT and second_term is not None:
            raise NonValidRequestException(self)
