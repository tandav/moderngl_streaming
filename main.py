import moderngl
import numpy as np


ctx = moderngl.create_standalone_context()

prog = ctx.program(
    vertex_shader='''
        #version 330

        in vec2 in_vert;
        in vec3 in_color;

        out vec3 v_color;

        void main() {
            v_color = in_color;
            gl_Position = vec4(in_vert, 0.0, 1.0);
        }
    ''',
    fragment_shader='''
        #version 330

        in vec3 v_color;

        out vec3 f_color;

        void main() {
            f_color = v_color;
        }
    ''',
)

x = np.linspace(-1.0, 1.0, 50)
y = np.random.rand(50) - 0.5
r = np.ones(50)
g = np.zeros(50)
b = np.ones(50)

# vertices = np.dstack([x, y, r, g, b])
#
# vbo = ctx.buffer(vertices.astype('f4').tobytes())
# vao = ctx.simple_vertex_array(prog, vbo, 'in_vert', 'in_color')

import config
import sink

fbo = ctx.simple_framebuffer((config.frame_width, config.frame_height))
fbo.use()
fbo.clear(0.0, 0.0, 0.0, 1.0)
# vao.render(moderngl.LINE_STRIP)
# vao.render(moderngl.TRIANGLE_STRIP)
# vbo.write()

n = 50
buffer = ctx.buffer(reserve=n*5*4)
vao = ctx.simple_vertex_array(prog, buffer, 'in_vert', 'in_color')

with sink.ffmpeg() as ff:

    # for _ in range(30):
    while True:
        x = np.linspace(-1.0, 1.0, n)
        y = np.random.uniform(-1.0, 1.0, size=n)
        # y = np.random.random(n)

        # r = np.ones(n)
        # g = np.zeros(n)
        # b = np.ones(n)

        r = np.random.random(n)
        g = np.random.random(n)
        b = np.random.random(n)
        vertices = np.dstack([x, y, r, g, b])

        # print(len(vertices.astype('f4').tobytes()))
        # vbo = ctx.buffer(vertices.astype('f4').tobytes())
        buffer.write(vertices.astype('f4').tobytes())

        # vbo.write()

        vao.render(moderngl.TRIANGLES)
        # vao.render(moderngl.LINE_STRIP)

        ff.write(fbo.read())
        ctx.clear()
        # buffer.clear()
        # print(fbo.read())

# Image.frombytes('RGB', fbo.size, fbo.read(), 'raw', 'RGB', 0, -1).show()
