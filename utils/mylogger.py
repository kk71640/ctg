from logging import getLogger, DEBUG, StreamHandler, Formatter, FileHandler
import os, sys, shutil, datetime

# i.e.
# result_path = './log/'
# model_name = 'bs_{}_epoch_{}_LR_{}'.format(BATCH_SIZE, NUM_EPOCHS, LR)
# logger = NewLogger(test=False, result_path, model_name)

class NewLogger():
    def __init__(self, test=True, result_path='./log/', model_name=None):
        self.logger = getLogger('{:%y%m%d_%H%M%S}'.format(datetime.datetime.now()))
        self.logger.setLevel(DEBUG)

        handler_format = Formatter('%(asctime)s - %(message)s', "%Y-%m-%d %H:%M:%S")

        if test == False:
            dt = datetime.datetime.now()
            model_name = '{:%y%m%d_%H%M%S}_'.format(dt) + model_name
        else:
            model_name = 'test'
           
        
        self.dir_path = os.path.join(result_path, model_name)
        if os.path.exists(self.dir_path): shutil.rmtree(self.dir_path)
        os.makedirs(self.dir_path, exist_ok = True)
        self.log_path = os.path.join(self.dir_path, 'loss.log')

        file_handler = FileHandler(filename = self.log_path, mode = 'w')
        file_handler.setLevel(DEBUG)
        file_handler.setFormatter(handler_format)
        self.logger.addHandler(file_handler)

        console_handler = StreamHandler(sys.stdout)
        console_handler.setLevel(DEBUG)
        console_handler.setFormatter(handler_format)
        self.logger.addHandler(console_handler)

    def debug(self, sentence):
        self.logger.debug(sentence)
