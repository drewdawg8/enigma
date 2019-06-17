import fs

class FileSystem:

    def __init__(self, rootfs):
        temp = rootfs.makedirs('root')
        self.__root = rootfs.opendir('root')
        self.__rootfs = rootfs
        self.__current = self.__root
        self.__prev = None

    #Makes a directory and sets it to the current directory
    def mkdir(self, dir_name):
        self.__current.makedirs(dir_name)

    def cd(self, path):
        self.__prev = self.__current
        self.__current = self.__current.opendir(path)

    def tree(self):
        return self.__current.desc(self.__current))

#fs = fs.open_fs('mem://')
#fs.makedirs('root')
#root = fs.opendir('/root')
#root.makedirs('Documents')
#root.makedirs('Pictures')
#documents = root.opendir('Documents')
#print(documents.desc('.'))
#root.tree()

fs = FileSystem(fs.open_fs('mem://'))
fs.mkdir('Pictures')
fs.cd('Pictures')
print(fs.tree())
