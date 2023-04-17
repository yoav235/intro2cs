import cartoonify
import ex5_helper
from cartoonify import rotate_90
#
image = ex5_helper.load_image("ziggy.jpg")
image = cartoonify.cartoonify(image, 5,11,13,8)
ex5_helper.show_image(image)

# print(cartoonify.apply_kernel([[0,128,255]], cartoonify.blur_kernel(3)))
