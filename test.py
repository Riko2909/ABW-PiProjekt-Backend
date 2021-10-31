import json
import requests
import time

import random

bums = {
      "luxMS" : 0
}

headers = {'content-type': 'application/json'}


for i in range(10):

      bums['luxMS'] = random.random()
      try:
            r = requests.post('http://localhost:3001', data=json.dumps(bums), headers=headers)
            
            payload = r.json()

            if len(payload['colorwheel']) < 1:
                  print("Empty")
            else:
                  print(payload['colorwheel'])

            time.sleep(1)
      except:
            print("Keine Verbindung. Warte 10 Sekunden!")
            time.sleep(10)