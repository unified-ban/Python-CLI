import requests, json, os, sys
import configparser as cp

cfg = cp.ConfigParser()

class requrls():
    def_url = "https://api.unifiedban.solutions"
    
    def checkblk(uid):
        blkurl = "{}/blacklist/check/{}".format(requrls.def_url, uid)
        return blkurl


class cfgVars():
    cfg_dir = "%s/.ubtoken" % str(os.getenv('HOME'))
    cfg.read(cfg_dir)
    cfg.sections()
    token=cfg['connection']['token']

class apireqs():
    def get_userinfo(uid):
        response = requests.get(
                requrls.checkblk(uid), headers = {
                    'Authorization': cfgVars.token
                }).json()

        for var, value in response.items():
            print("{} = {}".format(var, value))

def main():
    print("token: {}".format(cfgVars.token))
    apireqs.get_userinfo(sys.argv[1])

main()
