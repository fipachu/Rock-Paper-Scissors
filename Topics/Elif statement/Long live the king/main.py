edge = {1, 8}
edge_x, edge_y = (int(input()) in edge for _ in range(2))
is_corner = edge_x and edge_y
is_edge = edge_x ^ edge_y

print(3 if is_corner else 5 if is_edge else 8)
