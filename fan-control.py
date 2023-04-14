#!/usr/bin/python3

import time
import gpiod

def read_config(config_path) -> (float, int):
    temp_threshhold, gpio_port = None, None

    lines = open(config_path).readlines()
    for line_num, tmp_line in enumerate(lines):
        line = tmp_line.split("#")[0].strip()

        # skip empty lines
        if len(line) == 0:
            continue
        
        # split into components
        comp = line.split()
        if len(comp) > 2:
            raise Exception("configuration error in", config_path, "on line", line_num)
        
        # read value
        if comp[0] == "TemperatureThreshhold":
            temp_threshhold = float(comp[1])
        elif comp[0] == "GPIOPort":
            gpio_port = int(comp[1])
        else:
            raise Exception("configuration error in", config_path, "on line", line_num)
    
    if temp_threshhold == None:
        raise Exception("failed to find configuration for TemperatureThreshhold in", config_path)
    if gpio_port == None:
        raise Exception("failed to find configuration for GPIOPort in", config_path)

    return temp_threshhold, gpio_port

def get_temp() -> float:
    num = int(open("/sys/class/thermal/thermal_zone0/temp").read())
    return num / 1000

def init_gpio(gpio_port : int) -> (gpiod.Chip, gpiod.Line):
    chip = gpiod.Chip('0', gpiod.Chip.OPEN_BY_NUMBER)
    line = chip.get_line(gpio_port)
    line.request("GPIO fan-control service")
    return chip, line

def set_fan(output : int, line : gpiod.Line) -> None:
    line.set_direction_output(output)

def main() -> None:
    temp_threshhold, gpio_port = read_config("/etc/fan-control.conf")
    chip, line = init_gpio(gpio_port)

    while True:
        cur_temp = get_temp()
    
        if (cur_temp >= temp_threshhold):
            set_fan(1, line)
        else:
            set_fan(0, line)
        
        time.sleep(10)

if __name__ == "__main__":
    main()