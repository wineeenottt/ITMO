import numpy as np

def get_color(iter_val: int, max_iter: int) -> int:
    if iter_val == max_iter:
        return 0xFF000000  # Black (ARGB)

    t = iter_val / max_iter
    r = int(255 * (t ** 0.5))
    g = int(255 * (t ** 3.0))
    b = int(255 * (t ** 6.0))
    return 0xFF000000 | (b << 16) | (g << 8) | r

def render_mandelbrot(width: int, height: int, zoom: float, center_x: float, center_y: float) -> bytes:
    max_iter = 100
    aspect = width / height
    scale_y = 1.0 / zoom
    scale_x = scale_y * aspect

    pixels = bytearray(width * height * 4)  # 4 bytes per pixel (RGBA/ABGR – Raylib expects ABGR in uint format)

    for y in range(height):
        for x in range(width):
            c_re = (x / width - 0.5) * scale_x + center_x
            c_im = (y / height - 0.5) * scale_y + center_y

            z_re = z_im = 0.0
            iter_count = 0

            while z_re * z_re + z_im * z_im <= 4.0 and iter_count < max_iter:
                z_re, z_im = z_re * z_re - z_im * z_im + c_re, 2.0 * z_re * z_im + c_im
                iter_count += 1

            color = get_color(iter_count, max_iter)
            idx = (y * width + x) * 4
            # Raylib expects ABGR in memory as [B, G, R, A] when using uint[], but we pack as uint directly
            # We'll return as raw uint32 array via int list, but easier: return as bytes of uint32 in little-endian
            # So we pack each color as little-endian uint32
            pixels[idx:idx+4] = color.to_bytes(4, byteorder='little')

    return bytes(pixels)