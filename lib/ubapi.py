import requests, json
from lib.cfg import *

class requrls():
    def_url = "https://api.unifiedban.solutions"
 
    # request link
    def api_blacklist_url(uid):
        blkurl = "{}/blacklist/check/{}".format(requrls.def_url, uid)
        return blkurl


class apireqs():

    # get user info
    def get_userinfo(uid):
        response = requests.get(
                requrls.api_blacklist_url(uid), headers = {
                    'Authorization': token
                }).json()
        # print data
        for var, value in response.items():
            print("{} = {}".format(var, value))


