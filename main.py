import threading
import time
from common.driver import *
from engine.scraping import run, fetch_searched_page_num
from datetime import datetime

def main(keyword: str):
    start = time.time()
    run_at = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    print("開始")
    thread_list = []

    # 最大ページ数を取得
    try:
        max_page_num = fetch_searched_page_num(keyword)
    except Exception as e:
        logger.error(f"fetch page error: {e}")
        return None

    # MAX_THREAD_NUMの数だけマルチスレッド処理
    print(max_page_num)
    print(list(range(0, max_page_num)))
    page = 1
    for id in range(max_page_num):
        # targetに呼び出す関数名を指定、argsに関数の引数を指定
        t = threading.Thread(target=run, args=[keyword, page, id, run_at])
        t.start()
        thread_list.append(t)
        page += 1
    # 全スレッドの終了を待ち受ける
    for thread in thread_list:
        thread.join()
    print("終了")
    logger.info(f"time(s): {time.time() - start} | page:{max_page_num}")

    
if __name__ == "__main__":
    main("SE")