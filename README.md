# Parametric Cookie

Processing-style Scripting add-on for Blender. 

This add-on offers configurable scripting with Blender by running scripts in the background or within Blender. It is particularly useful for generative animations that are fully scripted with the Blender API. This add-on evolved as a helpful tool through creating most of the pieces in the [Parametric Cookie](https://parametriccookie.tumblr.com/) Collection.


## Installation

Download the Parametric Cookie Add-on from Github as an [archive](https://github.com/njanakiev/parametric-cookie/archive/master.zip). Go to _File > User Preferences > Addons > Install from File_ and then choose the zip-archive and activate the flag besides the Parametric Cookie Add-on.


## Getting Started

There are a few examples to illustrate the functionality in the [examples](examples) folder. You can run them by extracting the examples folder from the archive, selecting the [config.json](examples/config.json) file in the file picker in the toolbar and pressing the _Import / Reload_ button below. This loads the scene defined in the configuration file. Below the button you can choose which scripted scene to choose from (which are again located in the examples folder).

![Screenshot](screenshot.png)


## Usage

To start write your own script copy the [simple_config.json](examples/simple_config.json) to the folder your want your project to be in and change there the name in `"scene": "minimal_cube"` from `minimal_cube` to your python file in the folder without the extension. To run properly, import the `core` module and extend `class Composition` from `core.scene.Scene` as in the following example.

```python
import core
from math import pi
PI, TAU = pi, 2*pi

class Composition(core.scene.Scene):
    def setup(self):
        # Create a simple scene with target, camera and sun
        core.simple_scene((0, 0, 0), (-5, -13, 5), (-10, -10, 4))

        # Create a cube object of size 5
        self.obj = core.geometry.cube(size=5)
```
You need to implement a `setup(self)` function which is called once. You can optionally implement a `draw(self)` function which is called for each frame change. This function can have the following form.

```python
    def draw(self):
        # Set t to be in the range between 0 and 1
        t = self.frame / self.frames

        # Rotate the cube for one full rotation on two rotation axis
        self.obj.rotation_euler = (0, t*TAU, t*TAU)
```
There you can access the current frame with `self.frame` and the number of frames with `self.frames`. There are many more functions to choose from within the [core](core) module and you can also access the `bpy` and `bmesh` modules, besides all the available Python modules you would have within Blender.

You can run the code by loading the config file in Blender with the Parametric Cookie Toolbox as previously shown or you can run it in the background by using the command

```
blender -b -a -- config.json
```
to render animations. In order to render single frames use the command

```
blender -b -f 1 -- config.json
```
When rendering animation or single frame, the frames are rendered in the specified `output_folder` folder from the config.json and there the frames are rendered to a folder or an image with the name of the scene for animation and single frame render respectively. If you want the frames or the animation folder to be overwritten you can use the `override` option in the config.json.

## License

This project uses the LGPL v3 for the code within the core folder and the code within the examples folder is licensed under the MIT license. The rest of the project is licensed under the GPL v3.
