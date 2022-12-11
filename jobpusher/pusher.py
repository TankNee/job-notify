import logging


class Pusher:
    def __init__(self, driver_name: str, driver_config: dict):
        self.driver_name = driver_name
        self.driver_config = driver_config
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(logging.StreamHandler())

        self.drivers = ['mail']

        if driver_name not in self:
            raise Exception(f'Driver {driver_name} not found')
        self.driver = self[driver_name](driver_config)

    def push(self, job: dict):
        self.logger.info("Pushing job %s", job)
        self.driver.auth()
        self.driver.send(job['to'], job['subject'], job['content'], job['attachments'])

    def __contains__(self, driver_name):
        return driver_name in self.drivers

    def __getitem__(self, driver_name):
        if driver_name == 'mail':
            from jobpusher.drivers.mail import MailDriver
            return MailDriver