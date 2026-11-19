import sys,asyncio
from playwright.async_api import async_playwright
async def main(d,n):
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome')
        pg=await b.new_page(viewport={'width':1080,'height':1350})
        await pg.goto(f'file://{d}/slides.html'); await pg.wait_for_timeout(800)
        for i in range(1,n+1):
            await pg.locator(f'#s{i}').screenshot(path=f'{d}/post1_slide{i}.png')
        await b.close()
asyncio.run(main(sys.argv[1],int(sys.argv[2])))
