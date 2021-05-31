import sys
import queue

# pages.txtを開いてデータをdictに読み込む
def read_pages(path):
    pages = {}
    with open(path) as f:
        for data in f.read().splitlines():  # 例) data == "1    言語"
            page = data.split('\t')  # 例) link == ["1", "言語"]
            # page[0]: id, page[1]: title
            pages[page[0]] = page[1]
    return pages


# links.txtを開いてデータをdictに読み込む
def read_links(path):
    links = {}
    with open(path) as f:
        for data in f.read().splitlines():  # 例) data == "0    955"
            link = data.split('\t')  # 例) link == ["0", "955"]
            # link[0]: id (from), link[1]: id (to)
            # dictであるlinksの値はset型
            if link[0] in links:
                links[link[0]].add(link[1])
            else:
                links[link[0]] = {link[1]}
    return links


# ページ名のIDを返す
def get_id(page_name, pages):
    for k, v in pages.items():
        if v == page_name:
            return k
    print(page_name, "は見つかりませんでした")
    exit()


# start から end までの最短経路があるかどうか
def exist_shortest_path(start, end, pages, links):
    start_id = get_id(start, pages)
    end_id = get_id(end, pages)

    # キューを作る
    q = queue.Queue()

    # グラフの頂点の訪問状態を表すstateというdictを作る
    state = {}
    for id in pages.keys():
        state[id] = "unwatch"

    # 始点から各点への最短距離を記録するdistanceというdictを作る
    distance = {}
    f_inf = float("inf")
    for id in pages.keys():
        distance[id] = f_inf  # すべてのvalueをinfinityで初期化する
    distance[start_id] = 0

    # 幅優先探索で最短経路があるかどうかを調べる
    q.put(start_id)  # start_id をキューに入れる
    while True:
        looking = q.get()
        if looking == end_id:  # キューから取り出したものが見つけたいものだった場合
            print("最短経路が見つかりました")
            # print(distance)  # デバッグ用
            return distance
        state[looking] = "watch"
        if looking in links.keys():
            for id in links[looking]:
                if state[id] != "watch":
                    q.put(id)  # キューから取り出して今見ているものから矢印が出ているものをキューにすべて追加する
                    if distance[looking]+1 < distance[id]:
                        distance[id] = distance[looking]+1
        if q.empty():
            print(pages[start_id], "から", pages[end_id], "への経路は存在しませんでした")
            return False


# トレースバックして最短経路を求める
def traceback(start, end, pages, links, distance):
    start_id = get_id(start, pages)
    end_id = get_id(end, pages)

    looking = end_id
    path = [looking]
    while looking != start_id:
        for link in links.items():  # 例) link == ('797833', {'469744', '30', '10592', '17175', '1089'})
            if looking in link[1]:
                if distance[link[0]] == distance[looking]-1:
                    path.append(link[0])
                    looking = link[0]
    return path


# 最短経路があるかどうかを調べて、ある場合は最短経路を求める
def search(start, end, pages, links):
    distance = exist_shortest_path(start, end, pages, links)
    if distance != False:
        path = traceback(start, end, pages, links, distance)
        return path
    else:
        exit()


# 最短経路を表示する
def print_result(start, end, pages, path):
    print(start, "から", end, "への最短経路 :")
    for i, p in enumerate(reversed(path)):
        page = pages[p]
        if i == len(path)-1:
            print(page)
        else:
            print(page, "→ ", end = "")


def main(start, end):
    pages = read_pages('data/pages.txt')
    links = read_links('data/links.txt')
    path = search(start, end, pages, links)
    print_result(start, end, pages, path)



if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("usage: %s start end" % sys.argv[0])
        exit(1)
    main(sys.argv[1], sys.argv[2])
