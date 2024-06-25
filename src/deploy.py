#!/usr/bin/python3 -u

import os
import utils

# Because these deployment scripts are very long it is not easy to enclose them in
# functions, it is hard to use "import" on the scripts without some hacking..
# Since they are mostly independent from the rest of the system and just need to
# read the config file to work correctly, we simply invoke them as external
# commands instead.

# No need to pass parameters since it will know where to read the config from.

config = utils.read_config()

substrate = config["substrate"]
utils.debug(f"Starting deploy for substrate {substrate}")
if substrate in ("equinix", "maas"):
    os.execl("./src/deploy_standalone.py")
elif substrate == "maasdeployment":
    os.execl("./src/deploy_deployment.py")
else:
    utils.die(f"Invalid substrate '{substrate}' in config, aborting")
