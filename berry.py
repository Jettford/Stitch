#
#   Developed by Elena Winters (ElenaBerry#2561), aka Tracer
#   Contributions by: Raine Bannister and RingoMar
#
#   This bot is used and hosted by me (Elena), for others to use.
#
#

from core.logger import log, trace, json
from dateutil import parser
from core import manager
from core import utils
from data import data
from core import web
import threading
import datetime
import extends
import debug
import time
import sys


if __name__ == '__main__':
    extends.Initialize()  # Setup
    data.Initialize()  # Launch dataset

    # Start threads
    threads = manager.Initialize().threads
    log.debug(f'Current threads: {threads}')

    host = json.orm['api']  # Post current time to api
    web.Client(f"http://{host['host']}:{host['port']}/uptime/").post({'uptime': str(datetime.datetime.utcnow())})

    debug.Initialize()  # Run debugging functions

    while all(x.is_alive() for x in threads):  # Kill program if a thread dies
        time.sleep(2)

    uptime = web.Client(f"http://{host['host']}:{host['port']}/uptime/").get()
    log.debug(parser.parse(uptime.json()['uptime']))

    sys.exit(0)
