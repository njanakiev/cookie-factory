import bpy
import bmesh
import core
from math import sin, cos, pi
PI, TAU = pi, 2*pi


class Composition(core.scene.Scene):
    def setup(self):
        # Create a simple scene with target, camera and sun
        core.simple_scene((0, 0, 0), (-5, -13, 5), (-10, -10, 4))

        # Create a cube object of size 5
        self.obj = core.geometry.cube(size=5)

    def draw(self):
        t = self.frame / self.frames
        x, y, z = sin(TAU*t), cos(TAU*t), 0

        self.obj.location = (x, y, z)
        self.obj.rotation_euler = (0, t*TAU, t*TAU)
