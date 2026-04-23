import customtkinter
from datetime import datetime
from validator import Validator
from selector import Selection
from comparator import Comparator
from reactiontest import Reaction
from scheduler import Schedule


class Gui(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.infos = {
            "url": "",
            "conteudo": "",
            "first_time": "",
            "change": "",
            "interval": "",
        }
        self.selection = None
        self.comparator = None
        self.reaction = Reaction()
        self.schedule = None
        self.resizable(False, False)
        self.geometry("700x500")
        self.title("Web element monitor")

        self.text = "Sit back and relax!\nThe element is being monitored"
        self.label_log = customtkinter.CTkLabel(
            self, text=self.text, font=("Roboto", 14)
        )
        self.label_log.pack(pady=(20, 0))

        self.textbox = customtkinter.CTkTextbox(
            self, width=500, height=300, wrap="word"
        )
        self.textbox.pack(pady=20)

        self.button = customtkinter.CTkButton(
            self, text="Reselect element", command=self.button_callbck
        )
        self.button.pack(pady=20)

        self.start()

        self.mainloop()

    def start(self):
        self.is_url_valid = False
        self.is_interval_valid = False
        self.select_element()
        if not self.is_url_valid:
            return

        self.selection = Selection(self.infos["url"])
        self.select_interval()
        if not self.is_interval_valid:
            return

        self.comparator = Comparator(
            self.selection, self.reaction, int(self.infos["interval"])
        )
        self.schedule = Schedule()
        self.schedule.start(self.comparator)
        time = f"{datetime.now():%d/%m/%Y %H:%M:%S}"
        self.infos["conteudo"] = self.selection.conteudo
        self.infos["first_time"] = time
        self.infos["change"] = self.comparator.last_change_detected
        self.infos["interval"] = self.comparator.interval

        self.update_info()

    def button_callbck(self):
        try:
            if hasattr(self, 'schedule'):
                self.schedule.stop()
                print("Scheduler parado com sucesso.")
        except Exception as e:
            print(f"Aviso: Não foi possível parar o scheduler ou scheduler não existe: {e}")

        try:
            if hasattr(self, 'reaction'):
                self.reaction.close_driver()
                print("Driver encerrado com sucesso.")
        except Exception as e:
            print(f"Aviso: Erro ao fechar o driver ou driver não existe: {e}")

        self.start()

    def read_input(self):
        dialog = customtkinter.CTkInputDialog(
            text="Type in an URL and click on an element to monitor:",
            title="Selecting an element",
        )
        return dialog.get_input()

    def select_element(self):
        url = self.read_input()
        self.validate_url(url)
        self.infos["url"] = url

    def update_info(self):
        infos = self.infos
        self.textbox.insert(
            "0.0",
            f"Monitor details\n\n\nSelected ULR: {infos["url"]}\n\nOriginal element text: {infos["conteudo"]}\n\nTime of first selection: {infos["first_time"]}\n\nLast change detected: {infos["change"]}\n\nInterval: {infos["interval"]} minutes",
        )

    def validate_url(self, url):
        validator = Validator()
        self.is_url_valid = validator.is_url(url)
        if not self.is_url_valid:
            self.show_error("Invalid URL. Please reselect element")

    def select_interval(self):
        dialog = customtkinter.CTkInputDialog(
            text="Type in a time interval in minutes (positive integer):",
            title="Selecting a time interval",
        )
        interval_str = dialog.get_input()

        if interval_str is not None:
            try:
                interval_int = int(interval_str)

                if interval_int > 0:
                    self.infos["interval"] = interval_int
                    self.is_interval_valid = True

                    print(f"Intervalo definido para: {interval_int} minutos")
                else:
                    self.show_error("The interval must be a number greater than 0.\nPlease reselect the element")
            except ValueError:

                self.show_error(
                    "Invalid input. Please reselect the element and type a whole number."
                )

    def show_error(self, mensagem):
        error_window = customtkinter.CTkToplevel(self)
        error_window.title("Erro")
        error_window.geometry("800x150")

        error_window.attributes("-topmost", True)

        label = customtkinter.CTkLabel(error_window, text=mensagem, pady=20)
        label.pack()

        btn_ok = customtkinter.CTkButton(
            error_window, text="Ok", command=error_window.destroy
        )
        btn_ok.pack(pady=10)

    def on_closing(self):
        print("Fechando o programa e desligando o scheduler")
        try:
            if self.schedule is not None:
                self.schedule.stop()
            self.reaction.close_driver()
        except Exception as e:
            print(e)
        finally:
            self.destroy()
