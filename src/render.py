from IPython.display import Image

class Render:
    def load(file, style=None):
        try:
            if style == "image":
                return Image(filename = f"../assets/{file}")
            return f"../assets/{file}"
        except FileNotFoundError:
                print("ERROR: Could not locate image!")