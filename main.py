from mexc import MexcSync

import config
from place_futures_order import calc_vol_from_usdt, getPrecision
import asyncio

async def main():
    mexc = MexcSync({
        "apiKey": config.api_key,
        "secret": config.api_secret,
    })
    symbol = "SOL_USDT"
    price = 85
    usdt_amount = 10
    await getPrecision()
    vol = calc_vol_from_usdt(symbol=symbol, price=price, usdt_amount=usdt_amount)

    request = {
        "symbol": "SOL_USDT",
        # "price": 85,
        "vol": vol,
        "side": 4,       # 1 open long, 2 close short, 3 open short, 4 close long
        "leverage": 10,
        "openType": 2, # если нужно
        "type": 5,     # тип ордера если нужен
    }

    resp = mexc.contract_private_post_order_submit(request)
    print(resp)


if __name__ == "__main__":
    asyncio.run(main())