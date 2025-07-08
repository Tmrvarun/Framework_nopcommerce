import logging

class Loggen:
    @staticmethod
    def loggen():

        logging.basicConfig(filename= '.\\Framework\\Logs\\testlogger.log',
                          format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%Y:%m:%d %H:%M:%S',force=True
                            )
        log=logging.getLogger()
        log.setLevel(logging.INFO)
        return log
