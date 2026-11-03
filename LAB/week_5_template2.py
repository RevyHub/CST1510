class Record:
    def __init__(self, source_ip, failed_logins, total_attempts):
        self.source_ip = source_ip
        self.failed_logins = float(failed_logins)
        self.total_attempts = float(total_attempts)

    def status(self):
        percentage = (self.failed_logins / self.total_attempts) * 100
        if percentage >= 100:
            return "Over Limit"
        elif percentage >= 90:
            return "Warning"
        else:
            return "Okay"
    