import asyncio

async def make_coffee():
    print('1. Кофе заваривается')

    await asyncio.sleep(2)
    print('2. Кофе готово!')

async def main():
    await make_coffee()

asyncio.run(main())


# async def seal():
#     print('Тюленьчик начинает ползти')
#
#     await asyncio.sleep(6)
#
#     print('Тюленьчик дополз!')
#
# asyncio.run(seal())
# print()

async def seal():
    print('Тюлень начинает ползти')

    await asyncio.sleep(5)

    print('Тюлень уже близко')

    await asyncio.sleep(3)

    print("Тюлень дополз!")

asyncio.run(seal())