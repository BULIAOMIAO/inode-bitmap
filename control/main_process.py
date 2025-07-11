from control.order import *
def main_process():
    while True:
        print("fs>")
        user_input = input()
        command_parts = user_input.split()

        if not command_parts:
            print("无效命令，请重新输入。")
            continue

        command = command_parts[0]

        if command == "mkfs": # 格式化
            mkfs()
            print("格式化完成")

        elif command == "touch":   # 创建文件
            if len(command_parts) != 2:   # 参数数量错误
                print("无效命令，请重新输入。")
                continue
            file_name = command_parts[1]
            try:
                touch(file_name)
                print(f"创建文件成功：{file_name}")
            except Exception as e:
                print(e)

        elif command == "write":         # 写入文件
            if len(command_parts) != 3:  # 参数数量错误
                print("无效命令，请重新输入。")
                continue
            file_name = command_parts[1]
            add_size = int(command_parts[2])
            try:
                size = write(file_name, add_size)
                print(f"写入完成，文件大小为：{size}")
            except Exception as e:
                print(e)

        elif command == "read": # 读取文件
            if len(command_parts) != 2: # 参数数量错误
                print("无效命令，请重新输入。")
                continue
            file_name = command_parts[1]
            try:
                size = read(file_name)
                print(f"{file_name}: {size}")
            except Exception as e:
                print(e)
        elif command == "rm": # 删除文件
            if len(command_parts) != 2: # 参数数量错误
                print("无效命令，请重新输入。")
                continue
            file_name = command_parts[1]
            try:
                rm(file_name)
            except Exception as e:
                print(e)
        elif command == "ls": # 列出文件
            ls()
        elif command == "exit": # 退出
            print("退出文件系统")
            exit()
        else:
            print("无效命令，请重新输入。")
