class NodeList:
    def __init__(self):
        self.body = []

    def add(self, node):               # 添加文件
        self.body.append(node)

    def read_file(self, file_name):              # 读取文件大小
       for file in self.body:
           if file.file_name == file_name:
               return file.file_size()
       return -1

    def write_file(self, file_name, blocks):               # 写入文件
        for file in self.body:
            if file.file_name == file_name:
               for block in blocks:
                   file.add_block(block)
               return True
        return False

    def delete_file(self, file_name):                       # 删除文件
        for file in self.body:
            if file.file_name == file_name:
                delete_blocks = file.delete_block()
                self.body.remove(file)
                return delete_blocks
        return None

    def clean(self):                                  # 清空文件表
        self.body = []

    def display(self):                               # 显示文件表
        print("===== inode 表 =====")
        for file in self.body:
            file.display()
        print("===================")