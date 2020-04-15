import sys
from lib.ubapi import * 
from lib.cfg import * 

arg = sys.argv[1]

def main():
    if arg == "check":
        print("token: {}".format(token))
        apireqs.get_userinfo(sys.argv[2])
    elif arg == "token":
        conf_token(sys.argv[2])

main()
