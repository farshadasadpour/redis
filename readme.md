# Redis

Redis is an in-memory data structure store, used as a distributed, in-memory key–value database, cache and message broker, with optional durability. Redis supports different kinds of abstract data structures, such as strings, lists, maps, sets, sorted sets, HyperLogLogs, bitmaps, streams, and spatial indices.
Foobar is a Python library for dealing with word pluralization.

## requirements  

```bash

apt install redis-server

```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install -r req.txt
```

## Usage

```bash
docker build --pull --rm -f "dockerfile" -t redis:latest "."
docker run -it --net=host redis:latest 
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Next phase

Start to write project with docker-compose
Monitor Redis with Monitoring tools

## License

[MIT](https://choosealicense.com/licenses/mit/)
