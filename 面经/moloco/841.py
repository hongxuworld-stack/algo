class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True
        stack = [0]

        while stack:
            cur_room = stack.pop()

            for next_room in rooms[cur_room]:
                if not visited[next_room]:
                    visited[next_room] = True
                    stack.append(next_room)
        return all(visited)