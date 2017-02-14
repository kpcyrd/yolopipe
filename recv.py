#!/usr/bin/env python3
from redis import StrictRedis
import json
import sys
import os

K = 1024
M = 1024 * K

LIMIT = 10 * M

REDIS_HOST = 'localhost'
REDIS_PASSWD = None


def main():
    try:
        queue = sys.argv[1]
    except IndexError:
        print('missing queue name')
        return

    data = sys.stdin.read(LIMIT)
    x = json.dumps({
        'argv': sys.argv[2:],
        'cmd': os.environ.get('SSH_ORIGINAL_COMMAND', ''),
        'data': data
    })
    redis = StrictRedis(REDIS_HOST, password=REDIS_PASSWD)
    redis.lpush(queue, x)
    redis.disconnect()


if __name__ == '__main__':
    main()
