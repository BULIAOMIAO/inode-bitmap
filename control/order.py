from control import bitmap
from control import node_list
from model.inode import Inode

def mkfs():                  # 格式化文件系统
   bitmap.clean()            # 清空位图
   node_list.clean()        # 清空文件表

def touch(file_name):             # 创建文件
   if node_list.read_file(file_name) != -1:      # 文件已存在
      raise Exception("文件已存在，不可重复创建")
   node_list.add(Inode(file_name))

def write(file_name, add_size):           # 写入文件
   size = node_list.read_file(file_name)
   if size == -1:                          # 无此文件
      raise Exception("无此文件")
   if size + add_size > 12:           # 超出直接块上限
      raise Exception("超出直接块上限")
   try:
      blocks = bitmap.alloc_block(add_size)         #分配块
   except Exception as e:
      raise Exception("磁盘已满")

   node_list.write_file(file_name, blocks)        # 写入文件表
   return size + add_size

def read(file_name):                      # 读取文件
   size = node_list.read_file(file_name)
   if size == -1:
      raise Exception("无此文件")
   return size


def rm(file_name):                      # 删除文件
   blocks = node_list.delete_file(file_name)   # 删除文件，返回块号
   if blocks is None:
      raise Exception("无此文件")
   for block in blocks:
      bitmap.free_block(block)            # 释放块


def ls():                                # 显示文件表
   node_list.display()
   bitmap.display()