
#!/usr/bin/env python
# -*- coding:utf-8-*-
# Author:Eio
import json,os
from conf import settings


group={'test':['h1','h2','h3'],
       'web_clusters':['h1','h2'],
       'db_servers':['h2','h3']}

with open(os.path.join(settings.CONFIG_DIR,'group.json'),"w") as file:
    file.write(json.dumps(group))