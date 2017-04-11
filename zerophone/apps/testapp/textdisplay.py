"""
test of text display
"""
import time
import datetime
import demo_arg_parser
from luma.core.render import canvas


def main():
    today_last_time = "Unknown"
    while True:
        now = datetime.datetime.now()
        today_date = now.strftime("%d %b %y")
        today_time = now.strftime("%H:%M:%S")
        if today_time != today_last_time:
            today_last_time = today_time
            with canvas(device) as draw:
                now = datetime.datetime.now()
                today_date = now.strftime("%d %b %y")

                margin = 4

                cx = 0
                cy = device.height / 2

                draw.text((2 * (cx + margin), cy - 8), today_date, fill="yellow")
                draw.text((2 * (cx + margin), cy), today_time, fill="yellow")

        time.sleep(0.1)


if __name__ == "__main__":
    try:
        device = demo_arg_parser.get_device()
        main()
    except KeyboardInterrupt:
        pass
