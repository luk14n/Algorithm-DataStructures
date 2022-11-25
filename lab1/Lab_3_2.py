from  DSU import DSU,Graph

def DSU_p1():
    vertices = [1, 2, 3, 4, 5, 6, 7]
    dsu = DSU()
    for v in vertices:
        dsu.set_make(v)
    dsu.set_find(4)
    print(dsu.previous)
    dsu.set_union(4, 6)
    print(dsu.previous)
def krus_p1():
    print("Граф:")
    g = Graph(4)
    g.set_make(0, 1, 10)
    g.set_make(0, 2, 6)
    g.set_make(0, 3, 5)
    g.set_make(1, 3, 15)
    g.set_make(2, 3, 4)
    # Граф
    g.show_krus()
    # Мінімальний каркас
    g.Kruskal()

def prim_p2():
    g = Graph(4)
    g.set_make(0, 1, 10)
    g.set_make(0, 2, 6)
    g.set_make(0, 3, 5)
    g.set_make(1, 3, 15)
    g.set_make(2, 3, 4)
    g.show_krus() # Вивід графу
    print(g.primMST())

if __name__ == '__main__':
    ## part 1
    # DSU
    # DSU_p1()
    ### Krus
    # krus_p1()
    # ### part 2
    print("PART 2")

    prim_p2()
