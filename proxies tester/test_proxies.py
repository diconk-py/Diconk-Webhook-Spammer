import aiohttp
import asyncio
import time

TEST_URL = "https://httpbin.org/ip"  # URL to test proxy

async def test_proxy(proxy, session):
    try:
        start = time.perf_counter()
        async with session.get(TEST_URL, proxy=proxy, timeout=10) as response:
            if response.status == 200:
                data = await response.json()
                elapsed = (time.perf_counter() - start) * 1000
                print(f"✅ {proxy} OK ({elapsed:.1f}ms) → IP seen: {data['origin']}")
                return proxy
    except Exception as e:
        print(f"❌ {proxy} failed: {e}")
    return None

async def main():
    # Load proxies from file
    try:
        with open("proxies.txt", "r") as f:
            proxies = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("File 'proxies.txt' not found.")
        return

    if not proxies:
        print("No proxies found in file.")
        return

    connector = aiohttp.TCPConnector(limit_per_host=10)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [test_proxy(proxy, session) for proxy in proxies]
        results = await asyncio.gather(*tasks)

    # Filter valid proxies
    valid = [proxy for proxy in results if proxy]
    print(f"\n🎯 {len(valid)} / {len(proxies)} proxies are working.")

    # Optional: Save working proxies to file
    if valid:
        with open("proxies_working.txt", "w") as f:
            for proxy in valid:
                f.write(proxy + "\n")
        print("✅ Working proxies saved to 'proxies_working.txt'.")

if __name__ == "__main__":
    asyncio.run(main())
