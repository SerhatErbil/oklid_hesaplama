points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

min_distance = min(distances)

print("Noktalar:", points)
print("Hesaplanan Mesafeler:", distances)
print("Minimum Mesafe:", min_distance)
