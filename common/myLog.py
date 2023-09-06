import logging
import os
import time
from datetime import datetime

logger=logging.getLogger(__name__)
path_dir=str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
logpath=os.path.join(path_dir,'logs')

def create_file(filename):
    path=filename[:-7]
    if not os.path.isdir(path):
        os.mkdir(path)
    if not os.path.isdir(filename):
        fb=open(filename,mode='w',encoding='utf-8')
        fb.close()
    else:
        pass

def set_handler(level):
    if level == 'error':
        logger.addHandler(MyLog.err_handler)
    logger.addHandler(MyLog.handler)
    logger.addHandler(MyLog.console)

def remove_handler(level):
    if level == 'eror':
        logger.removeHandler(MyLog.err_handler)
    logger.removeHandler(MyLog.handler)
    logger.removeHandler(MyLog.console)

def set_now_time():
    now_time=time.strftime(MyLog.time_format,time.localtime(time.time()))
    return now_time


class MyLog:
    path=os.path.join(logpath,str(datetime.now().strftime('%Y%m%d')))
    now=time.strftime('%H-%M-%S',time.localtime(time.time()))
    log_file=path + '/log.log'
    err_file=path + '/err.log'
    create_file(log_file)
    create_file(err_file)
    time_format = "%Y-%m-%d %H:%M:%S"

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    logger.setLevel(logging.DEBUG)
    handler=logging.FileHandler(log_file,encoding='utf-8')
    err_handler=logging.FileHandler(err_file,encoding='utf-8')

    @staticmethod
    def debug(message,name='',line=''):
        set_handler('debug')
        if name !=''and line !='':
            logger.debug(
                "[" + set_now_time() + "]" + " - " + name + ', ' + 'Line %s' % line + "] " + " - " + "DEBUG:" + " " + message)
            remove_handler('debug')

        else:
            logger.debug(
                "[" + set_now_time() + "]" + " - " + "DEBUG:" + " " + message)
            remove_handler('debug')

    @staticmethod
    def info(message,name='',line=''):
        set_handler('info')
        if name !='' and line !='':
            logger.info(
                "[" + set_now_time() + "]" + " - " + name + ', ' + 'Line %s' % line + "] " + " - " + "INFO:" + " " + message)
            remove_handler('info')
        else:
            logger.info(
                "[" + set_now_time() + "]" + " - " + "INFO:" + " " + message)
            remove_handler('info')

    @staticmethod
    def warning(message, name='', line=''):
        set_handler('warning')
        if name != '' and line != '':
            logger.warning(
                "[" + set_now_time() + "]" + " - " + name + ', ' + 'Line %s' % line + "] " + " - " + "WARNING:" + " " + message)
            remove_handler('warning')
        else:
            logger.warning(
                "[" + set_now_time() + "]" + " - " + "WARNING:" + " " + message)
            remove_handler('warning')

    @staticmethod
    def error(message, name='', line=''):
        set_handler('error')
        if name != '' and line != '':
            logger.error(
                "[" + set_now_time() + "]" + " - " + name + ', ' + 'Line %s' % line + "] " + " - " + "ERROR:" + " " + message)
            remove_handler('error')
        else:
            logger.error(
                "[" + set_now_time() + "]" + " - " + "ERROR:" + " " + message)
            remove_handler('error')


