import requests
from cachetools import cached , TTLCache

cache = TTLCache(maxsize= 100 , ttl=3 * 60 * 60)
@cached(cache)
def get_echange_rate(basecourncy: str,target_courncy: str) -> float:
    responce = requests.get(f'https://v6.exchangerate-api.com/v6/1372f6c4870cf7bca0a1d949/latest/{basecourncy}')
    if responce.status_code != 200:
        return None
    return responce.json()['conversion_rates'][target_courncy]


def convert_courncy(amount: float,exchange_rate: float)-> float:
    return amount * exchange_rate


if __name__=="__main__":
    base_courncy = input("eEnter Base CurEncy: ")
    target_courncy = input("Enter Target CurEncy: ")
    amount = float(input("Enter AMOUNT: "))
    echange_rate = get_echange_rate(base_courncy,target_courncy)
    convert_amount = convert_courncy(amount,echange_rate)
    print(f'{amount} {base_courncy} is {convert_amount} {target_courncy}')
    