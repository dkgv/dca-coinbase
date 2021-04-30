import os
import sys
import cbpro


class DCA:
    def __init__(self, trading_pair: str, fiat_spend: int) -> None:
        self.client = cbpro.AuthenticatedClient(
            os.getenv('CB_PRO_API'),
            os.getenv('CB_PRO_SECRET'),
            os.getenv('CB_PRO_PASS')
        )
        self.trading_pair = trading_pair
        self.fiat_spend = fiat_spend

    def execute(self) -> dict:
        return self.client.place_market_order(
            product_id=self.trading_pair,
            side='buy',
            funds=self.fiat_spend
        )


if __name__ == '__main__':
    dca = DCA(
        trading_pair=sys.argv[1],
        fiat_spend=int(sys.argv[2])
    )
    order = dca.execute()
    if order:
        print('Executed order.')
        print(order)
    else:
        print('Failed to execute order')
