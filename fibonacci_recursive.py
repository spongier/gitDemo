import logging

# 配置日志模块
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("./logs/fibonacci.log"),  # 将日志写入当前目录下的 fibonacci.log 文件
        logging.StreamHandler()  # 同时将日志输出到控制台
    ]
)

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# 示例
n = 20
result = fibonacci_recursive(n)
logging.info(f"Fibonacci number at position {n} is {result}")