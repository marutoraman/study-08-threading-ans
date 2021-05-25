import threading
import time
from common.driver import *

MAX_THREAD_NUM = 5 # 最大マルチスレッド数を指定(多くすると処理が重くなるため、PCのスペックにより調整)

def process(id:int, arg2, arg3, arg4):
    '''
    Webブラウザを起動してGoolgeを開いて、５秒待つ
    arg2～4のように任意の引数を指定できる
    '''
    print(f"[begin] thread id:{id}")
    driver = Driver()
    driver.driver.get("https://google.com")
    time.sleep(5)
    print(f"[end] thread id:{id}")
    driver.quit()


def main():
    print("開始")
    thread_list = []
    # MAX_THREAD_NUMの数だけマルチスレッド処理
    for id in range(MAX_THREAD_NUM):
        # targetに呼び出す関数名を指定、argsに関数の引数を指定
        t = threading.Thread(target=process, args=[id+1,"","",""])
        t.start()
        thread_list.append(t)
    # 全スレッドの終了を待ち受ける
    for thread i
    
if __name__ == "__main__":
    main()