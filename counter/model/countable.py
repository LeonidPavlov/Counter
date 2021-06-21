
class Countable:

    @staticmethod
    def check_positivity(val: float) -> float:
        if val <= 0:
            val = 1.0
        return val
    
    @staticmethod
    def set_amount(cost: float, total: float) -> float:
        return total / cost

    @staticmethod
    def set_cost(amount: float, total: float) -> float:
        return total / amount
    
    @staticmethod
    def set_total(cost: float, amount :float) -> float:
        return cost * amount
    
    def __init__(self,  cost: float = 1.0,
                        amount: float = 1.0,
                        total: float = 1.0) -> None:
        self.__cost = self.check_positivity(cost)
        self.__amount = self.check_positivity(amount)
        self.__total = self.check_positivity(total)
    
    def cost(self) -> float:
        return self.__cost
    
    def amount(self) -> float:
        return self.__amount
    
    def total(self) -> float:
        return self.__total
