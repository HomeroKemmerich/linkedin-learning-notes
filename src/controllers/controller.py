from views.main_view import MainView

class MainController:
    def __init__(self):
        self.view = MainView(self)

    def start(self):
        self.view.open()