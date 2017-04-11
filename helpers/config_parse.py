#!/usr/bin/env python
import os 
import json 
import logging
logger = logging.getLogger(__name__)

def read_config(config_path):
    logger.debug("os.getcwd() = %s", os.getcwd())
    with open(config_path, 'r') as f:
        data = json.load(f)
    return data
     
def write_config(config, config_path):
    with open(config_path, 'w') as f:
        json.dump(config, f)
     
if __name__ == "__main__":
    config = read_config("../config.json")
    print config
