class MyLogger():
    """
    Create new log class.
    :param filename | filename to log:
    :return:
    """

    def __init__(self, filename=None):
        self.filename = filename

    def log(self, msg):
        """
        :param msg | message  to log:
        :return:
        """
        # Open a file with access mode 'a'
        with open(self.filename + ".log", "a") as file_object:
            # Append LOG at the end of file
            file_object.write("{time} {msg} \n".format(
                time=datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S.%f'),
                msg=msg,
            ))
