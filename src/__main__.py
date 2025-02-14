from controllers.app_controller import AppController
from services import FileService

if __name__ == '__main__':
    app_controller = AppController(file_service=FileService())
    app_controller.start()
