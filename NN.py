import \
    time

import Push
from datetime import \
    datetime

while True:
    currentDate = datetime.now().time()
    if  (currentDate.minute == 7) and (currentDate.second == 0):
        Push.push("NN",is_at_all=True)
    time.sleep(1)
