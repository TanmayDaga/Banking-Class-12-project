import os


class Log:
    __OKGREEN = '\033[92m'
    __WARNING = '\033[93m'
    __ERROR = '\033[91m'
    __ENDC = '\033[0m'

    @classmethod
    def info(cls, filePath: str, message: str):
        print(f"{cls.__OKGREEN}Info{cls.__ENDC}: {os.path.basename(filePath)}/: {message}")

    @classmethod
    def warn(cls, filePath: str, message: str):
        print(f"{cls.__WARNING}Warning{cls.__ENDC}: {os.path.basename(filePath)}/: {message}")

    @classmethod
    def error(cls, filePath: str, message: str):
        print(f"{cls.__ERROR}Error{cls.__ENDC}: {os.path.basename(filePath)}/: {message}")


if __name__ == "__main__":
    Log.warn(__file__,"warning")
    Log.error(__file__, "error")
    Log.info(__file__, "info")
