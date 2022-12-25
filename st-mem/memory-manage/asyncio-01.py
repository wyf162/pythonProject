# -*- coding : utf-8 -*-
# @Time: 2022/6/24 23:03
# @Author: yefei.wang
# @File: asyncio-00.py

# concurrency: threading, async io
# parallelism: multi-processing

import asyncio


async def count():
    print('One')
    await asyncio.sleep(1)
    print('Two')


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == '__main__':
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds")
