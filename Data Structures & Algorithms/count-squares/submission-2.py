class CountSquares:

    def __init__(self):
        self.points_freq = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points_freq[(point[0],point[1])] += 1

    def count(self, point: List[int]) -> int:
        qx = point[0]
        qy = point[1]
        ans = 0

        print(point)
        # assume every other point is diagonal
        for p, freq in self.points_freq.items():
            x = p[0]
            y = p[1]

            # find qx, y
            a = self.points_freq.get((qx,y), 0)
            b = self.points_freq.get((x,qy), 0)

            if not a or not b:
                continue
            
            width = abs(qx-x)
            height = abs(qy-y)
            if width != height:
                continue
            if width == 0:
                continue
            

            c = freq
            print(a,b,c)
            ans += a*b*c

        return ans








