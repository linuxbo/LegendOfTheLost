import os
import datetime

import requests

credentials = 'fengqing.nemo@bytedance.com', 'wehta0-niwfox-Kifdus'
zendesk = 'https://larksuite.zendesk.com'
language = 'en-us'



date = datetime.date.today()
backup_path = os.path.join(str(date), language)
if not os.path.exists(backup_path):
    os.makedirs(backup_path)
