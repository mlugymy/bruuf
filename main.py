import ssl
import requests
from threading import active_count, Thread
from random import randint
from urllib3.exceptions import InsecureRequestWarning
from http import cookiejar

class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context

r = requests.Session()
r.cookies.set_policy(BlockCookies())

def stats(item_id):
    while True:
        try:  # this request is used to make views
            with r.post(f"https://api22-core-c-useast1a.tiktokv.com/aweme/v1/aweme/stats/?os=android&_rticket={randint(1111111111111, 9999999999999)}&is_pad=0&host_abi=arm64-v8a&ts={randint(1111111111, 9999999999)}", headers={"content-type": "application/x-www-form-urlencoded; charset=UTF-8", "user-agent": "com.zhiliaoapp.musically/2023105030 (Linux; U; Android 12; en_US; SM-A315F; Build/SP1A.210812.016; Cronet/TTNetVersion:2fdb62f9 2023-09-06 QuicVersion:bb24d47c 2023-07-19)", "X-Common-Params-V2": f"ab_version=31.5.3&ac=wifi&ac2=wifi&aid=1233&app_language=en&app_name=musical_ly&app_type=normal&build_number=31.5.3&carrier_region=US&carrier_region_v2=505&cdid=2d8395df-aede-4ba4-92d3-8f74d4f85926&channel=googleplay&device_brand=samsung&device_id={randint(1000000000000000000, 9999999999999999999)}&device_platform=android&device_type=SM-A315F&dpi=420&iid=7294948246764635910&language=en&locale=en&manifest_version_code=2023105030&mcc_mnc=60401&op_region=US&openudid=0c13a0d5ba1f8f2e&os_api=31&os_version=12&region=US&resolution=1080*2195&ssmix=a&sys_region=US&timezone_name=Africa%2FCasablanca&timezone_offset=0&uoo=0&update_version_code=2023105030&version_code=310503&version_name=31.5.3"}, data=f"item_id={item_id}&play_delta=1", stream=True, verify=True)

                   as response:


                if (response.json()["status_code"] == 0):
                    break
                else:
                    continue
        except:
            continue

if (__name__ == "__main__"):
    # lol idiot skid
    item_id = str(input('''

██████╗░██╗░░░██╗░██████╗██╗░░██╗░█████╗░██████╗░░░░██╗░██╗░██████╗░░█████╗░░█████╗░░░███╗░░
██╔══██╗██║░░░██║██╔════╝██║░██╔╝██╔══██╗██╔══██╗██████████╗╚════██╗██╔══██╗██╔══██╗░████║░░
██████╔╝██║░░░██║╚█████╗░█████═╝░███████║██████╔╝╚═██╔═██╔═╝░█████╔╝╚██████║╚██████║██╔██║░░
██╔══██╗██║░░░██║░╚═══██╗██╔═██╗░██╔══██║██╔═══╝░██████████╗░╚═══██╗░╚═══██║░╚═══██║╚═╝██║░░
██║░░██║╚██████╔╝██████╔╝██║░╚██╗██║░░██║██║░░░░░╚██╔═██╔══╝██████╔╝░█████╔╝░█████╔╝███████╗
╚═╝░░╚═╝░╚═════╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░░╚═╝░╚═╝░░░╚═════╝░░╚════╝░░╚════╝░╚══════╝
                                Pasted by: rUsKaP#3991

[?] Video Link >>> 
'''))

    if ("vm.tiktok.com" in item_id or "vt.tiktok.com" in item_id):
        item_id = r.head(item_id, stream=True, verify=False, allow_redirects=True).url.split("/")[5].split("?", 1)[0]
    else:
        item_id = item_id.split("/")[5].split("?", 1)[0]
    amount = int(input("[?] How many views do you want (0 = Infinite) >>> "))  # infinite stop at 6M views..
    print("")
    print("[i] Sending Views...")  # sending skid views
    if (amount == 0):
        for _ in iter(int, 1):
            while True:
                if (active_count() <= 5000):  # 5000 views per seconds
                    Thread(target=(stats), args=(item_id,)).start()
                    break
    else:
        for _ in range(amount):
            while True:
                if (active_count() <= 5000):
                    Thread(target=(stats), args=(item_id,)).start()
                    break
