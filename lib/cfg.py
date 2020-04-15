import os
import configparser as cp

cfg = cp.ConfigParser()

cfg_dir = "%s/.ubtoken" % str(os.getenv('HOME'))

if os.path.exists(cfg_dir): 
    try:             
        cfg.read(cfg_dir)
        cfg.sections()                   
        token = cfg['connection']['token']
    except:
        print("No token in config file")
        exit(1)
else:
    token = None
       
# config
def conf_token(token_in):

    if token is None:
        # create base config scheme
        cfg.add_section('connection')
        cfg['connection']['token'] = token_in
        
        print("New token added!")
    elif token is not token_in:
        # update token
        cfg['connection']['token'] = token_in
        
        print("Token updated!")
    else:
        print("This token already exist in the config!")
       
    # write config
    with open(cfg_dir, 'w') as cfg_file:
        cfg.write(cfg_file)
    print("Token has been written in the config file")




    


