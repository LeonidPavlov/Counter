from datetime import datetime as dt


class Event_Time:
    """
        holds time when anythin happens in app context
        allow add arbitrary date
    """
    @staticmethod
    def check_year_out_of_range(year: int = 2021) -> int:
        """     
            range 1 ... 9999
            if out of range retun year now
        """
        if 1 <= year < 10000:
            return year
        else:
            return dt.now().year

    @staticmethod
    def check_month_out_of_range(month: int = 1) -> int:
        """     
            range 1 ... 9999
            if out of range retun year now
        """
        if 1 <= month <= 12:
            return month
        else:
            return dt.now().month
    
    @staticmethod
    def is_leap(year: int = 2021) -> bool:
            if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
                return True
            else:
                return False

    @staticmethod
    def chek_amount_days(year: int, month: int, day: int) -> int:
        """
            depend of what month
        """
        ammount_days = {1: 31, 2: 0, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31,
                        9: 30, 10: 31, 11: 30, 12: 31}

        if Event_Time.is_leap(year):
            ammount_days[2] = 29
        else:
            ammount_days[2] = 28
        
        if 1 <= day <= ammount_days[month]:
            return day
        else:
            return dt.now().day
    
    @staticmethod
    def chek_hour_out_of_range(hour: int) -> int:
        if 0 <= hour < 24:
            return hour
        else:
            return dt.now().hour

    @staticmethod
    def chek_minute_out_of_range(minute: int) -> int:
        if 0 <= minute < 60:
            return minute
        else:
            return dt.now().minute

    def __init__(self,  year: int = dt.now().year, 
                        month: int = dt.now().month, 
                        day: int = dt.now().day,
                        hour: int = dt.now().hour,
                        minute: int = dt.now().minute) -> None:
        
        self.__year = self.check_year_out_of_range(year)
        self.__month = self.check_month_out_of_range(month)
        self.__day = self.chek_amount_days(self.__year, self.__month, day)        
        self.__hour = self.chek_hour_out_of_range(hour)
        self.__minute = self.chek_minute_out_of_range(minute) 

    def event_year(self) -> int:
        return self.__year
    
    def event_month(self) -> int:
        return self.__month

    def event_day(self) -> int:
        return self.__day
    
    def event_hour(self) -> int:
        return self.__hour
    
    def event_minute(self) -> int:
        return self.__minute

