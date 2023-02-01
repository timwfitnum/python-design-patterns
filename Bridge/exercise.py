from abc import ABC


class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None


# TODO: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer


class VectorRenderer(Renderer):
    def __str__(self):
        return "as lines"


class RasterRenderer(Renderer):
    def __str__(self):
        return "as pixels"


class Shape:
    def __init__(self, renderer) -> None:
        self.renderer = renderer

    def __str__(self):
        return f"Drawing {self.__class__.__name__} {self.renderer}"


class Triangle(Shape):
    def __init__(self, renderer) -> None:
        super().__init__(renderer)


class Square(Shape):
    def __init__(self, renderer) -> None:
        super().__init__(renderer)
