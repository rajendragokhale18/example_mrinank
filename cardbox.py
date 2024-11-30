def card_box(n, cards):
    from collections import defaultdict

    faces = set()

    def manage_face(face):
        if face in faces:
            faces.remove(face)
        else:
            faces.add(face)

    for x, y, z, plane in cards:
        if plane == "xy":
            manage_face((x, y, z, "xy"))
            manage_face((x, y, z + 1, "xy"))
            manage_face((x, y, z, "yz"))
            manage_face((x + 1, y, z, "yz"))
            manage_face((x, y, z, "xz"))
            manage_face((x, y + 1, z, "xz"))
        elif plane == "xz":
            manage_face((x, y, z, "xz"))
            manage_face((x, y + 1, z, "xz"))
            manage_face((x, y, z, "yz"))
            manage_face((x + 1, y, z, "yz"))
            manage_face((x, y, z, "xy"))
            manage_face((x, y, z + 1, "xy"))
        elif plane == "yz":
            manage_face((x, y, z, "yz"))
            manage_face((x + 1, y, z, "yz"))
            manage_face((x, y, z, "xz"))
            manage_face((x, y + 1, z, "xz"))
            manage_face((x, y, z, "xy"))
            manage_face((x, y, z + 1, "xy"))

    if len(faces) == 0:
        min_x = min_y = min_z = float("inf")
        max_x = max_y = max_z = float("-inf")

        for x, y, z, plane in cards:
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            min_z = min(min_z, z)
            max_x = max(max_x, x + (1 if plane in ("xy", "xz") else 0))
            max_y = max(max_y, y + (1 if plane in ("xy", "yz") else 0))
            max_z = max(max_z, z + (1 if plane in ("xz", "yz") else 0))

        volume = (max_x - min_x) * (max_y - min_y) * (max_z - min_z)
        return volume
    elif len(faces) == 6:
        missing_faces = list(faces)
        x = missing_faces[0][0]
        y = missing_faces[0][1]
        z = missing_faces[0][2]
        plane = missing_faces[0][3]
        return f"{x} {y} {z} {plane}"
    else:
        raise ValueError("Invalid configuration: more than one missing card or disjoint structure.")


n = int(input())
cards = [input().split() for _ in range(n)]
cards = [(int(x), int(y), int(z), plane) for x, y, z, plane in cards]

result = card_box(n, cards)
print(result)
