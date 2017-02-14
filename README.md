# python-crimereports

Provides basic API to [Crime Reports](http://crimereports.com).

## Install

`pip install crimereports`

## Usage

```python
import datetime
from crimereports import CrimeReports

cr = CrimeReports((lat, lng), radius, miles=True)
for incident in cr.get_incidents(datetime.datetime.now().date(), None, ['Community Policing']):
  print(incident)
```

## Development

Pull requests welcome. Must pass `tox` and include tests.

## Disclaimer

Not affiliated with crimereports.com. Use at your own risk.
