import threading
from .serialRead import start

threading.Thread(target=start).start()
