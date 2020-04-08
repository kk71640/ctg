import json
from collections import namedtuple
import shutil

class Json_Config():
    def __init__(self, path='config.json'):
        self.path = path
        self.dic = json.load(open(path, 'r'))
        
    def export_config(self):
        object_hook = lambda x: namedtuple('config', x.keys())(*x.values())
        return json.load(open(self.path, 'r'), object_hook = object_hook)
    
    def log_and_save(self, logger):
        logger.debug('==== config ====')
        
        for k, v in self.dic.items():
            logger.debug("%s %s" % (k, v))
        logger.debug('================')
        
        shutil.copy(self.path, logger.dir_path)
    
    def save_config(self, dir_path):
        shutil(self.path, dir_path)