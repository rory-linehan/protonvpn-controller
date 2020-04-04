import subprocess


def connect(name, protocol):
    result = subprocess.run(
        [
            'sudo',
            'protonvpn',
            'connect',
            name,
            '-p',
            protocol
        ],
        capture_output=True
    )
    if result.returncode == 0:
        if 'Connected!' in str(result.stdout):
            return True, None, result
        else:
            return False, 'pypvpnctl.connect: unexpected output', result
    else:
        return False, 'pypvpnctl.connect: return code not zero', result


def disconnect():
    result = subprocess.run(
        [
            'sudo',
            'protonvpn',
            'disconnect'
        ],
        capture_output=True
    )
    if result.returncode == 0:
        if 'Disconnected.' in str(result.stdout):
            return True, None, result
        else:
            return False, 'pypvpnctl.disconnect: unexpected output', result
    else:
        return False, 'pypvpnctl.disconnect: return code not zero', result
