   '''
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].
A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.
   '''
  def minKnightMoves(self, x: int, y: int) -> int:
        #Bidirectional BFS
        queue1=deque([(0,0)])
        queue2=deque([(x,y)])
        dist1=defaultdict(lambda:0)
        dist2=defaultdict(lambda:0)
        dist1[(0,0)]=0
        dist2[(x,y)]=0
        visited1=set()
        visited2=set()
        knight_moves=[(2,1),(1,2),(-2,1),(-1,2),(2,-1),(1,-2),(-2,-1),(-1,-2)]
        while queue1 and queue2:
            u1x,u1y=queue1.popleft()
            u2x,u2y=queue2.popleft()
            if((u1x,u1y) in dist2):
                return dist1[(u1x,u1y)]+dist2[(u1x,u1y)]
            if((u2x,u2y) in dist1):
                return dist1[(u2x,u2y)]+dist2[(u2x,u2y)]
            for dx,dy in knight_moves:
                v1x=u1x+dx
                v1y=u1y+dy
                v2x=u2x+dx
                v2y=u2y+dy
                if((v1x,v1y) not in visited1):
                    visited1.add((v1x,v1y))
                    dist1[(v1x,v1y)]=dist1[(u1x,u1y)]+1
                    queue1.append((v1x,v1y))
                if((v2x,v2y) not in visited2):
                    visited2.add((v2x,v2y))
                    dist2[(v2x,v2y)]=dist2[(u2x,u2y)]+1
                    queue2.append((v2x,v2y))
