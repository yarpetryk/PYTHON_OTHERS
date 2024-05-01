from datetime import datetime

timestamp = 1683031061
date = datetime.fromtimestamp(timestamp).strftime("%d-%m-%y %X")
print(date)
