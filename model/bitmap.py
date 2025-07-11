class Bitmap:
    def __init__(self, disk_size):
        self.blocks = [0 for _ in range(disk_size)]   # 磁盘块
        self.max_size = disk_size                      # 磁盘块的最大数量
        self.free_blocks = disk_size                  # 磁盘块中空闲块的数量

    def alloc_block(self,need_size):                              # 分配空闲块
        if need_size > self.free_blocks:         # 判断磁盘是否已满
            raise Exception("磁盘已满")
        blocks = []
        for i in range(self.max_size):          # 遍历位示图
            if self.blocks[i] == 0:
                self.blocks[i] = 1
                self.free_blocks -= 1
                blocks.append(i)
                if len(blocks) == need_size:
                    return blocks

    def free_block(self, block_num):                    # 释放一个块
        if block_num >= self.max_size:
            raise Exception("块编号超出范围")
        if self.blocks[block_num] == 1:
            self.blocks[block_num] = 0
            self.free_blocks += 1

    def clean(self):                                        # 清空位示图
        self.blocks = [0 for _ in range(self.max_size)]
        self.free_blocks = self.max_size

    def display(self):                             # 显示位示图
        print("===== 位示图(1=占用) =====")
        s = 16
        for i in range(self.max_size // s):
            # 取出当前行的16个元素，并用空格连接
            line = ' '.join(str(block) for block in self.blocks[i * s: (i + 1) * s])
            print(line)
