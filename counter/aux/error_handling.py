class ACHTUNG:
    def __init__(self, error: Exception, file: str, context: str) -> None:
        self.___error = error
        self.__file = file
        self.__context = context

    def console (self) -> None:
        print(f'ACHTUNG !!! => file -> {self.__file}'
                f'\n                context -> {self.__context}'
                f'\n                exception -> {self.___error}')

