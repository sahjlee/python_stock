# hello.py
import sys

def check_env():
    print("--- 練習環境測試 ---")
    print(f"Python 版本: {sys.version}")
    print("恭喜！程式碼已成功從電腦送到主機。")

if __name__ == "__main__":
    check_env()