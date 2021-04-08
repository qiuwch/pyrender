# Set the camera matrix to render an image.
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

camera = pyrender.PerspectiveCamera(yfov=np.pi / 3.0, aspectRatio=1.0)
s = np.sqrt(2)/2

camera_pose = np.loadtxt('./camera_pose.txt')

scene.add(camera, pose=camera_pose)
light = pyrender.SpotLight(color=np.ones(3), intensity=3.0,
                           innerConeAngle=np.pi/16.0,
                           outerConeAngle=np.pi/6.0)
scene.add(light, pose=camera_pose)
r = pyrender.OffscreenRenderer(400, 400)
color, depth = r.render(scene)
plt.figure()
plt.subplot(1,2,1)
plt.axis('off')
plt.imshow(color)
plt.subplot(1,2,2)
plt.axis('off')
plt.imshow(depth, cmap=plt.cm.gray_r)
plt.show()