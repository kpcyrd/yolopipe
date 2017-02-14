# yolopipe

Receive data from restricted ssh clients and add it to a redis list.

## How to read it back?

```
def stream(redis, queue):
    while True:
        _, value = redis.brpop(queue, 0)
        value = str(value, 'utf-8')
        value = json.loads(value)
        yield value


redis = StrictRedis('localhost')
for x in stream(redis, 'test-q'):
    print(x)
```

## Why?

Because, obviously:

- you hacked together a bunch of scripts
- at some point you ended up receiving data over ssh
- you needed to pass this data to another script that might run on a different host
- you aren't that serious about this data
- therefore lost messages ain't that big of a deal

## But why?

Because at some point I hacked together a bunch of scripts that needed to pass data over ssh due to space restrictions, abusing redis lists for ghetto queues seemed the best option due to cpu restrictions and messages going through most of the time works for me™.

## License?

GPLv3
