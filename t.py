import json

import requests

r = requests.post(url='https://hf.space/embed/shichen1231/Real-CUGAN/+/api/predict/',

                  json={"data": ["data:image/jpeg;base64,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"
                      ,

                                 "up2x-latest-conservative.pth"

                      ,

                                 2

                                 ]}, timeout=(270, 180), verify=False)
print("接受")

a = r.text
a = json.loads(a)
b = a.get("data")
c = b[0].replace("data:image/png;base64,", "base64://")
c = c.replace("data:image/jpeg;base64,", "base64://")
print("成功")