from OpenGL.GL import *
from OpenGL.GL.shaders import compileShader, compileProgram
import glfw, os

def load_code(filename): # read shader file located at shader
    shader_dir_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"shader")
    shader_path = os.path.join(shader_dir_path, filename)
    return open(shader_path, 'r').read()


if not glfw.init():
    raise Exception("glfw can not be initialized.")

# create the window
window = glfw.create_window(1280, 720, "New Window", None, None)

# check if window was created
if not window:
    glfw.terminate()
    raise Exception("glfw window can not be created!")

# set window's position
glfw.set_window_pos(window, 400, 200)

# make the context current
glfw.make_context_current(window)

# the main application loop
while not glfw.window_should_close(window):
    glfw.poll_events()
    
    
    glfw.swap_buffers(window)
    
    
    
glfw.terminate()
