# GPIO RPI-Fan-Controller

This tool toggles a fan which is connected over a GPIO Pin according to the CPU temperature.

In the RaspiOS this is already included. However there are other compatible OS with the RPI which do not have such a functionality preinstalled.

This tool behaves like any other systemd job like i.e. sshd.

# Installation

## Requirements

This tool uses systemd so make sure your system uses systemd.

This tool uses the /sys/class/thermal/thermal_zone0/temp file to read the CPU temperature. If this file is not present then the tool won't work.

The tool needs python3, gpiod and the gpiod python lib. To install on a debian based system execute
```
sudo apt install python3 gpiod python3-libgpiod
```

## Install

To install the tool type inside the cloned repository
```
sudo make install
```

After that edit the configuration file /etc/fan-control.conf.

Then launch the service using
```
sudo systemctl start fan-control.service
```

Don't forget to enable the service so that it launches on boot using
```
sudo systemctl enable fan-control.service
```

# Uninstall

To uninstall execute
```
sudo make uninstall
```

To remove the configuration execute
```
sudo make purge_config
```

# Report Bugs

First of all I'm not your local techsupport.

If you do happen to find a bug in the application write me a mail and or submit a pull request to fix it.