from os import makedirs, path as ospath
from shutil import rmtree
from json import loads, dumps

class MetaData():

    def __init__(self, temp_path):
        self.temp_path = temp_path
        self.save_file = ospath.join(self.temp_path,"metadata.json")
        if ospath.exists(self.save_file):
            self.load()
        else:
            self.completedStages = []
        self.clear_temp_folder()

    def clear_temp_folder(self):
        if ospath.exists(self.temp_path):
            rmtree(self.temp_path)
        makedirs(self.temp_path)

    def save(self):
        with open(self.save_file, "w") as file:
            file.write(dumps(self.__dict__, indent=4))

    def load(self):
        if ospath.exists(self.save_file):
            with open(self.save_file, "r") as file:
                self.__dict__ = loads(file.read())
