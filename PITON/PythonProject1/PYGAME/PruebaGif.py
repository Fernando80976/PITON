from PIL import Image

im = Image.open("soloLevelingAtaque.gif")
frames = []

try:
    while True:
        frame = im.copy()
        frames.append(frame)
        im.seek(im.tell() + 1)
except EOFError:
    pass

# Guardar frames como PNG para Pygame
for i, frame in enumerate(frames):
    frame.save(f"frame_{i}.png")
