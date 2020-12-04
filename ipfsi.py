import os
import sys
import shlex


ipfs_path = '/opt/IPFS Desktop/resources/app.asar.unpacked/node_modules/go-ipfs/go-ipfs/ipfs'

print(f'Using IPFS path: {ipfs_path}')

if len(sys.argv) > 1 and sys.argv[1] == 'daemon':
    uid = os.getuid()
    args = [
        'systemd-run',
        *shlex.split(f'--scope --uid={uid} --unit=ipfs --no-ask-password --collect -p MemoryLimit=256M'),
        ipfs_path,
        *sys.argv[1:],
    ]
    os.setuid(0)
    os.execv('/usr/bin/systemd-run', args)
else:
    os.execl(ipfs_path, 'ipfs', *sys.argv[1:])
