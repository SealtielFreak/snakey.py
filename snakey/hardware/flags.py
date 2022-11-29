
RENDER_GPU = 0x00000002
RENDER_CPU = 0x00000001


def check_valid(flag):
    if not flag in [RENDER_GPU, RENDER_CPU]:
        raise "Invalid flag"