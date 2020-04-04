# Python ProtonVPN Controller

Provides a Python interface for controlling the [ProtonVPN CLI](https://protonvpn.com/support/linux-vpn-tool/) client.

# Installation

`pip install git+https://github.com/rory-linehan/pypvpnctl`

# Usage

```python
import pypvpnctl
import time
for name in ['us-tx-01', 'us-tx-02', 'us-tx-03']:
  status, message, result = pypvpnctl.connect(name, 'tcp')
  if status is True:
    time.sleep(600)
    status, message, result = pypvpnctl.disconnect()
  else:
    print('failed to connect to ' + name)
    sys.exit(1)
```
