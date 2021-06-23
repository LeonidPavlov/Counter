from counter.model.countable import Countable
from counter.model.event_time import Event_Time

class Deal:

    balance_type = ('debet', 'credit')

    def __init__(self,  deal_id: int = 0,
                        event_time: Event_Time = Event_Time(),
                        countable: Countable = Countable(),
                        balance: str = balance_type[0],
                        type: str = 'kind of deal',
                        source: str = 'source or recipient',
                        category: str = 'category',
                        product: str = 'concrete thing') -> None:
        self.__deal_id = deal_id
        self.__event_time = event_time
        self.__countable = countable
        self.__balance = balance
        self.__type = type
        self.__source = source
        self.__category = category
        self.__product = product

    def id(self) -> int:
        return self.__deal_id

    def event_time(self) -> Event_Time:
        return self.__event_time
    
    def countable(self) -> Countable:
        return self.__countable

    def balance(self) -> str:
        return self.__balance
    
    def type(self) -> str:
        return self.__type

    def source(self) -> str:
        return self.__source
    
    def category(self) -> str:
        return self.__category
    
    def product(self) -> str:
        return self.__product