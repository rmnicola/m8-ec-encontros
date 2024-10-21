point_dict = {
        "ponto 1": (0.0, 0.0, 0.0, 1.0, 0.0, 0.0)
        }

def go_to(point):
    if point in point_dict:
        print(f"Indo para '{point}': {point_dict[point]}")
    else:
        print("Esse ponto não está cadastrado: {point}")
