from apscheduler.schedulers.background import BackgroundScheduler

from comparator import Comparator


class Schedule:
    """
    Executa um processo em intervalos definidos pelo Comparator
    """
    def __init__(self):
        self.__scheduler = BackgroundScheduler()

    def start(self, comparator: Comparator) -> None:
        try:
            self.__scheduler.add_job(comparator.compare, "interval", minutes=comparator.interval)
            self.__scheduler.start()
            print("Scheduler iniciado.")
        except (KeyboardInterrupt, SystemExit):
            self.__scheduler.shutdown()

    def stop(self) -> None:
        if self.__scheduler.running:
            self.__scheduler.shutdown()
            print("Scheduler desligado.")
