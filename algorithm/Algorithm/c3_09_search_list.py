class MyNode:
    """Node Class"""
    def __init__(self, key):
        self.key = key
        self.next = None

top = MyNode('h')

def search_list(param):
    node = top
    while node:
        if node.key == param:
            return '探索成功'
        node = node.next
    return '探索失敗'

if __name__ == '__main__':
    print(search_list('h'))