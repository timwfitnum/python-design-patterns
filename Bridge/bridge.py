from abc import ABC


class Renderer(ABC):
    def render_circle(self, radius):
        pass


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle with radius {radius}")
        # return super().render_circle(radius)


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing pixels from circle of radius {radius}")
        # return super().render_circle(radius)


class Shape:
    def __init__(self, renderer) -> None:
        self.renderer = renderer

    def draw(self):
        pass

    def resize(self, factor):
        pass


class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


raster = RasterRenderer()
vector = VectorRenderer()
circle = Circle(raster, 5)
circle.draw()
circle.resize(2)
circle.draw()
