import json, re
from bs4 import BeautifulSoup
from cloudscraper import create_scraper
from urllib.parse import quote

class Converter:
    def __init__(self) -> None:
        self.req = create_scraper()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36','Cookie': r'__cf_bm=7_PFc.VLR7P5nI5fo5pgnZksbbq6Ia9xOvwVKKv2xQI-1719438159-1.0.1.1-3hn7rAJ0hJ4V3Tmbfgq4NbLWOPLovQyeKDMU70Yc1TdbGspQ3VhfrkMmsUc8OvyOwRwqrj3G_sVH06BoN8_hK6rH0Nmn1I8Wo.MWBNqvGmM; _ga=GA1.1.1562226974.1719438156; cf_clearance=xJuhcyw6KrywVu3dSDMwrnTTAtLbB6XnOyu2Xp34MC4-1719438160-1.0.1.1-eo4ZvAXHpaCcYvWjN_x7glxLg6VWDlUZq85hnLvBc61dgQZtK2iRuSDxn22tsvFDTXhhIXf6PEQNpbHcZ.aK9g; _pbjs_userid_consent_data=3524755945110770; _lr_retry_request=true; _lr_env_src_ats=false; pbjs-unifiedid=%7B%22TDID%22%3A%227ab4956a-9f0d-4b54-b64b-94c864036d15%22%2C%22TDID_LOOKUP%22%3A%22TRUE%22%2C%22TDID_CREATED_AT%22%3A%222024-05-26T21%3A42%3A46%22%7D; pbjs-unifiedid_last=Wed%2C%2026%20Jun%202024%2021%3A42%3A41%20GMT; panoramaId_expiry=1720042966256; _cc_id=1e187d15d3c2897417daec5df364e78d; panoramaId=b5576b8453709a2b431e1a2629c8185ca02c1cd2e35916442cf243b572b4b447; _ga_HWSV72GK8X=GS1.1.1719438155.1.1.1719439130.0.0.0; cto_bundle=Q50rSV9MMXk0cXhNdUhCTnlXY0xRckFwRDlyRSUyRkF5RUl2OFNodWYlMkJ6b29xNnclMkZoUTYwejVMJTJCT25DeSUyRldMcFQ3U3FmT21VekdUM2ZkQ0dwVlNJQVglMkZkdDJ3dGZPSG5KUyUyQjNUMkRuJTJCUTZyazJMUXd1cnZZbFd5RHNzeGZ4MlU5UVZKMnFMbE9FcDZSS1p0SWJBaFNWUHhGckNnJTNEJTNE; __gads=ID=c528e4a4a026a638:T=1719438163:RT=1719439137:S=ALNI_MY-Wr5N29z8BYu4WpVPxNP_YZ_RLA; __gpi=UID=00000a31b887679b:T=1719438163:RT=1719439137:S=ALNI_MZKX5-cs5lO3jZFvOlbfjcAY55DBg; __eoi=ID=9202eade2c4fa1a0:T=1719438163:RT=1719439137:S=AA-AfjaKC0IQzPg6vaxx-KYuVfQk'}

    def parse_name(self, name):
        if name is None:
            return ''
        else:
            return quote(name)
    
    def get_seasons(self, name):
        name = self.parse_name(name=name)

        if name == '':
            return ''
        else:
            extract = self.req.get(f'https://tracker.gg/valorant/profile/riot/{name}/overview', headers=self.headers)

            soup = BeautifulSoup(extract.text, 'html.parser')
            get_json = soup.find('script', text=re.compile(r'window\.__INITIAL_STATE__'))
        
            if get_json:
                data = json.loads(get_json.string.split('<script>')[0].split('window.__INITIAL_STATE__ = ')[1])
                return data['valorantDb']['typeLists']['seasons']
            else:
                print('err.')