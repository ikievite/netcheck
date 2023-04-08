# netcheck

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-blueviolet.svg)](https://opensource.org/licenses/MIT)

Check if the internet is working

## Installation
```
git clone https://github.com/ikievite/netcheck

cd netcheck

make build

make package-install
```

## Usage
You need to add an env variable in json format,

for example 
```
IP_DICT='{"SRV1": "192.0.2.10", "DNS": "1.1.1.1"}'
```
after run `netcheck`

![Alt text](netcheck_example_output.svg?raw=true "netcheck")