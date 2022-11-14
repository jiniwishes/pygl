import glfw

# init glfw library
if not glfw.init():
    raise Exception("glfw can not be initialized.")

# creating the window
window = glfw.create_window(1280, 720, "Hello OpenGL", None, None) # in: monitor for full screen mode, in: share to share resources

# check if window was created
if not window:
    glfw.terminate()
    raise Exception("glfw window can not be created!")

# set window's position
glfw.set_window_pos(window, 400, 200)

# make the context current
glfw.make_xontext_current(window)

# the main application loop
while not glfw.window_should_close(window):

    glfw.swap_buffers(window) # swap the color buffer used for rendering
    glfw.poll_events # tracks any triggered events and updates


# terminate glfw, free up allocated resources
glfw.terminate()