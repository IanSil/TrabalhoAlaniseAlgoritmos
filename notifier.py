from interfaces import Action


class Notify(Action):

    def __init__(self):
        pass

    def trigger(self) -> None:
        print("bam")
