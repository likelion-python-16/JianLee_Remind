import requests
from typing import List, Dict


class MusinsaAPI():
    def __init__(self, keyword:str = "할인", page: int = 1, size: int = 60):
        self.url = "https://api.musinsa.com/api2/dp/v1/plp/goods"

        self.params = {
            "gf" : "A",
            "keyword" : keyword,
            "sortCode" : "POPULAR",
            "page" : page,
            "size" : size,
            "caller" : "SEARCH",
        }

        self.headers = {
            "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
            "AppleWebKit/537.36 (KHTML, like Gecko)"
            "Chrome/137.0.0.0 Safari/537.36"
        ),
        "Accept": "application/json, text/plain, */*",
        }
    
    def fetch(self) -> List[Dict]:
        response = requests.get(self.url, params=self.params, headers=self.headers)
        response.raise_for_status()
        data = response.json()

        goods_list = data.get("data", {}).get("list", [])
        if not goods_list:
            return []
        
        result: List[Dict] = []
        for g in goods_list:
            result.append({
                "goodsNo": g.get("goodsNo", ""),
                "goodsName": g.get("goodsName", ""),
                "brandName": g.get("brandName", ""),
                "normalPrice": f"{g.get('normalPrice', 0)}원",
                "price": f"{g.get('price', 0)}원",
                "imageUrl": g.get("thumbnail", ""),
                "linkUrl": "https://api.musinsa.com/" + g.get("goodsLinkUrl", "")
            })
        return result
    
    
if __name__ == "__main__":
    api = MusinsaAPI(keyword="신발", size=5)
    items = api.fetch()
    for idx, item in enumerate(items, start=1):
        print(f"{idx}. {item['goodsName']} - {item['price']} ({item['linkUrl']}), {item['imageUrl']}")