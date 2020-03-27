# Custom exception


class CrBaseError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class CrFileNotFoundError(CrBaseError):
    pass


class CrNotImplementedError(CrBaseError):
    pass


class CrEnvironmentError(CrBaseError):
    pass

class CrObjectTagNotFoundInCatalogChmError(CrBaseError):
    pass