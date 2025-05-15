#!/usr/bin/env python3
import asyncio
import aiohttp
import random
import datetime
import shutil
from colorama import init, Style
from itertools import cycle

init(autoreset=True)

# Generate a smooth RGB gradient list (violet -> blue)
def generate_gradient(start_rgb, end_rgb, steps):
    gradient = []
    for i in range(steps):
        r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * i / steps)
        g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * i / steps)
        b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * i / steps)
        gradient.append(f"\033[38;2;{r};{g};{b}m")
    return gradient

# Smooth violet → blue gradient (start: purple, end: cyan)
VIOLET_TO_BLUE = generate_gradient((199, 21, 133), (0, 191, 255), 80)

def apply_gradient(text):
    result = ""
    steps = len(text)
    gradient = generate_gradient((199, 21, 133), (0, 191, 255), steps)
    for i, char in enumerate(text):
        result += gradient[i] + char
    return result + Style.RESET_ALL

# ASCII banner (new custom block-style text)
ASCII = [
    "                                              ",
    "██████╗ ██╗ ██████╗ ██████╗ ███╗   ██╗██╗  ██╗",
    "██╔══██╗██║██╔════╝██╔═══██╗████╗  ██║██║ ██╔╝",
    "██║  ██║██║██║     ██║   ██║██╔██╗ ██║█████╔╝ ",
    "██║  ██║██║██║     ██║   ██║██║╚██╗██║██╔═██╗ ",
    "██████╔╝██║╚██████╗╚██████╔╝██║ ╚████║██║  ██╗",
    "╚═════╝ ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝",
    "                                              "
]

def print_header():
    width = shutil.get_terminal_size().columns
    gradient = generate_gradient((199, 21, 133), (0, 191, 255), len(ASCII))
    for i, line in enumerate(ASCII):
        centered = line.center(width)
        print(gradient[i] + centered + Style.RESET_ALL)

# Cycle colors for threads
THREAD_COLORS = cycle(VIOLET_TO_BLUE)

# Global proxy usage
USE_PROXIES = False
PROXY_LIST = []

async def spam_task(session, name, url, message):
    headers = {"Content-Type": "application/json"}
    payload = {"content": message}
    color = next(THREAD_COLORS)
    count = 0

    while True:
        proxy = random.choice(PROXY_LIST) if USE_PROXIES and PROXY_LIST else None
        try:
            async with session.post(url, json=payload, headers=headers, proxy=proxy) as resp:
                if resp.status == 204:
                    count += 1
                    now = datetime.datetime.now().strftime("%H:%M:%S:%f")[:-3]
                    print(f"{color}[{now}] Message Successfully Sent. [{count}]", end="\r")
                elif resp.status == 429:
                    data = await resp.json()
                    await asyncio.sleep(data.get("retry_after", 1.0))
                else:
                    await asyncio.sleep(1)
        except Exception:
            await asyncio.sleep(1)

async def main():
    global USE_PROXIES, PROXY_LIST

    print_header()

    # Proxy usage
    use_proxy_input = input(apply_gradient("🧪 Do you want to use proxies? [yes/no]: ")).strip().lower()
    if use_proxy_input == "yes":
        USE_PROXIES = True
        try:
            with open("proxies.txt", "r") as f:
                PROXY_LIST = [line.strip() for line in f if line.strip()]
            if not PROXY_LIST:
                print("\033[38;2;255;0;80mNo proxies found in proxies.txt. Continuing without proxies.")
                USE_PROXIES = False
        except FileNotFoundError:
            print("\033[38;2;255;0;80mproxies.txt not found. Continuing without proxies.")
            USE_PROXIES = False

    # Webhook input
    raw = input(apply_gradient("🔗 Paste your Discord webhook URLs (comma/space separated):\n> ")).strip()
    urls = [u for token in raw.replace(",", " ").split() 
            for u in [token.strip()] if u.startswith("https://discord.com/api/webhooks/")]
    if not urls:
        print("\033[38;2;255;0;80mNo valid webhooks found, exiting.")
        return

    # Message input
    message = input(apply_gradient("🟣 Enter the message to spam:\n> ")).strip()
    if not message:
        print("\033[38;2;255;0;80mEmpty message, exiting.")
        return

    # Async HTTP session
    connector = aiohttp.TCPConnector(limit=0)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        concurrency_per_hook = 5
        for idx, url in enumerate(urls, start=1):
            name = f"WH{idx}"
            for i in range(concurrency_per_hook):
                tasks.append(asyncio.create_task(
                    spam_task(session, f"{name}-T{i+1}", url, message)
                ))
            print(f"\033[38;2;128;128;255mStarted {concurrency_per_hook} tasks for {name}")

        print("\033[38;2;100;100;255m\nSpamming started! Press Ctrl+C to stop.\n")
        try:
            await asyncio.gather(*tasks)
        except asyncio.CancelledError:
            pass

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n\033[38;2;255;0;80mInterrupted by user. Exiting.")
