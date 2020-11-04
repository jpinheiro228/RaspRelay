Install the dependencies:

```
sudo apt install -y python3-pip
sudo pip3 install -r requirements.txt
```

or

```
sudo apt install -y python3-pip
sudo pip3 install flask RPi.GPIO
```

Add the following line on the /etc/rc.local, before the `exit 0` line:

```
/usr/bin/python3 /home/pi/main.py &
```

Now you can control the Relay by accessing the following URLs:

| URL                              | Action                                           |
| -------------------------------- | ------------------------------------------------ |
| `http://<RASPBERRY_PI_IP>/on`    | Turns Relay on                                   |
| `http://<RASPBERRY_PI_IP>/off`   | Turns Relay off                                  |
| `http://<RASPBERRY_PI_IP>/reset` | Turns Relay off, waits 5 Seconds and turns it on |