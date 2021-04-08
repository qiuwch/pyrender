# This is an example modified from https://pyrender.readthedocs.io/en/latest/examples/quickstart.html

from pyrender import scene
import trimesh
import pyrender
import numpy as np
import matplotlib.pyplot as plt


def get_scene():
    fuze_trimesh = trimesh.load('examples/models/fuze.obj')
    mesh = pyrender.Mesh.from_trimesh(fuze_trimesh)
    scene = pyrender.Scene()
    scene.add(mesh)
    return scene

scene = get_scene()
pyrender.Viewer(scene, use_raymond_lighting=True)

camera = pyrender.PerspectiveCamera(yfov=np.pi / 3.0, aspectRatio=1.0)
s = np.sqrt(2)/2