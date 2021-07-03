import enum

class Table_Name(enum.Enum):
    deals: str = 'DEALS'

class Fields(enum.Enum):
    id: str = 'DEAL_ID'
    year: str = 'YEAR'
    month: str = 'MONTH'
    day: str = 'DAY'
    hours: str = 'HOURS'
    minutes: str = 'MINUTES'
    balance: str = 'BALANCE'
    type: str = 'TYPE'
    source: str = 'SOURCE'
    category: str = 'CATEGORY'
    product: str = 'PRODUCT'
    cost: str = 'COST'
    amount: str = 'AMOUNT'
    total: str = 'TOTAL'

class Order(enum.Enum):
    id: int = 0
    year: int = 1
    month: int = 2
    day: int = 3
    hours: int = 4
    minutes: int = 5
    balance: int = 6
    type: int = 7
    source: int = 8
    category: int = 9
    product: int = 10
    cost: int  = 11
    amount: int = 12
    total: int = 13

column_number: dict = \
{
    Fields.id.value : Order.id.value,
    Fields.year.value : Order.year.value,
    Fields.month.value : Order.month.value,
    Fields.day.value : Order.day.value,
    Fields.hours.value : Order.hours.value,
    Fields.minutes.value : Order.minutes.value,
    Fields.balance.value : Order.balance.value,
    Fields.type.value : Order.type.value,
    Fields.source.value : Order.source.value,
    Fields.category.value : Order.category.value,
    Fields.product.value : Order.product.value,
    Fields.cost.value : Order.cost.value,
    Fields.amount.value : Order.amount.value,
    Fields.total.value : Order.total.value 
}

column_name: dict = \
    {
        Order.id.value : Fields.id.value,
        Order.year.value : Fields.year.value,
        Order.month.value : Fields.month.value,
        Order.day.value : Fields.day.value,
        Order.hours.value : Fields.hours.value,
        Order.minutes.value : Fields.minutes.value,
        Order.balance.value : Fields.balance.value,
        Order.type.value : Fields.type.value,
        Order.source.value : Fields.source.value,
        Order.category.value : Fields.category.value,
        Order.product.value : Fields.product.value,
        Order.cost.value : Fields.cost.value,
        Order.amount.value : Fields.amount.value,
        Order.total.value : Fields.total.value
    }

month_name: dict = \
    {
        1: 'january',
        2: 'fabruary',
        3: 'march',
        4: 'april',
        5: 'may',
        6: 'june',
        7: 'july',
        8: 'august',
        9: 'september',
        10: 'october',
        11: 'november',
        12: 'december'
    }
