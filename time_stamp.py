import time

class timeStamp():
    '''
        Creates a timestamp file at keys directory. 
    '''
    def __init__(self, path) -> None:
        self.keys_dir = path
        self.path_to_timestamp_file = self.keys_dir + "\\timestamp.txt"
        
    def creationOfFile(self) -> None:
        with open(self.path_to_timestamp_file, "w") as time_file:
            time_stamp = time.strftime("Key files created: %A %m-%d-%Y at %X")
            time_file.write(time_stamp)
            time_file.close()
    
    def __call__(self):
        self.creationOfFile()
