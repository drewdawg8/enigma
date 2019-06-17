import fs


mem_fs = fs.open_fs('mem://')
mem_fs.makedirs('fruit')
mem_fs.makedirs('vegtables')
mem_fs = fs.open_fs('mem://fruit')
mem_fs.makedirs('apple')
mem_fs = fs.open_fs('mem://')
mem_fs.tree()


def create_dir()
