[![License](https://camo.githubusercontent.com/a54c47c4dc66472c38a6d33b1833d9f6e5adfc8b/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f6c2f657870726573732e737667)](https://opensource.org/licenses/MIT) [![Build Status](https://travis-ci.org/ddubson/extractd.svg?branch=master)](https://travis-ci.org/ddubson/extractd)

### How to build

- Python 2.7.x (tested on Python 2.7.11)
- Just run `make` to aggregate all the dependencies needed

### Usage
Via make
```bash
> make run host=<hostIP> user=<username> password=<password>
```

Natively
```bash
> python extractd/extractd.py --host <hostIP> --user <username> --password <password>
```

### Executing tests

Run `make test` to execute the test suite located in tests directory


