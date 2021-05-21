from IPython.display import Image

class Render:
    def load(image, type):
        try:
            return Image(filename = f"assets/{image}.{type}")
        except FileNotFoundError:
            return Image(filename = f"../assets/{image}.{type}")