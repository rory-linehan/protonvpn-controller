# Python ProtonVPN Controller

Provides a Python interface for controlling the
[ProtonVPN CLI](https://protonvpn.com/support/linux-vpn-tool/) client.
This doesn't work on Windows natively because why would I bother with that?

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
    if status is False:
      print(message + ': ' + str(result.stdout))
  else:
    print(message + ': ' + str(result.stdout))
    sys.exit(1)
```
