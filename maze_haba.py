dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


class State:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return (self.x << 16) | self.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def bfs(h, w, t, sx, sy, gx, gy):
    open_list = []
    closed = set()
    initial_state = State(sx, sy)
    open_list.append(initial_state)

    cost = 1
    while True:
        tmp_q = []
        while open_list:
            st = open_list.pop(0)

            if st.x == gx and st.y == gy:
                return cost
            if t[st.y][st.x] == 1:
                continue
            if st in closed:
                continue

            closed.add(st)
            for i in range(4):
                nx = st.x + dx[i]
                ny = st.y + dy[i]

                if not (0 <= nx <= w - 1 and 0 <= ny <= h - 1):
                    continue

                tmp_q.append(State(nx, ny))

        open_list = tmp_q
        cost += 1


h, w = map(int, input().split())
t = [[int(x) for x in input().split()] for _ in range(h)]

cost = bfs(h, w, t, 0, 0, w - 1, h - 1)
print(cost)
