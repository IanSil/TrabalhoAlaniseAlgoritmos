from apscheduler.schedulers.background import BackgroundScheduler


class Schedule:

    def __init__(self):
        self.__scheduler = BackgroundScheduler()

    def start(self, Comparator):
        try:
            self.__scheduler.add_job(Comparator.compare, "interval", minutes=Comparator.interval)
            self.__scheduler.start()
            print("Scheduler iniciado.")
        except (KeyboardInterrupt, SystemExit):
            self.__scheduler.shutdown()

    def stop(self):
        if self.__scheduler.running:
            self.__scheduler.shutdown()
            print("Scheduler desligado.")
