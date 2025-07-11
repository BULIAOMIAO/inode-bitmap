class Inode:
    def __init__(self, file_name):
        self.file_name = file_name              # 文件名
        self.size = 0                              # 文件大小
        self.blocks = []                       # 文件占用的磁盘块

    def add_block(self, block):          # 添加磁盘块
        self.blocks.append(block)
        self.size += 1

    def file_size(self):               # 获取文件大小
        return self.size

    def delete_block(self):               # 删除磁盘块
        delete_block = self.blocks
        self.blocks = []
        return delete_block

    def display(self):                  # 显示文件信息
        print(f"{self.file_name}",end="      ")
        print(f"{self.size}",end="      ")
        print(f"blocks:{self.blocks}")