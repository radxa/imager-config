# imager-config

## 如何贡献

## 在 `products` 中添加添加文件

1. 每层文件夹下需要带config.json文件
2. 第一层为系列
3. 第二层为设备
    - 需要为设备添加描述以及指定图片地址，已预提交部分动画图，参考page分支
4. 最内层为镜像地址
    - 需要为镜像添加内容，图片、及地址，可使用`get_file_size.py`，生成预先定义的模板，根据需要修改内容，已预设部分图片，请使用。
5. 内层路径根据`sort`字段按**字典序**升序排列

## 使用`get_file_size.py`

1. 安装依赖 `pip install requests`
2. 修改文件内容
3. 运行 python3 get_file_size.py

## 进行编译检查
运行 `python build.py` 即可，如正常输出内容则构建成功，提交前请确认构建成功

## 环境说明
当主分支推送后，自动部署到`test`环境，需要推送才能到正式环境

## 推送到正式环境 （需要Action权限）

1. 打开该网址 [Deploy](https://github.com/radxa/imager-config/actions/workflows/deploy.yml)
2. 选择`Run workflow` 手动触发 Action
3. 选择分支为 `main` 并 点击 绿色 `Run workflow` 

