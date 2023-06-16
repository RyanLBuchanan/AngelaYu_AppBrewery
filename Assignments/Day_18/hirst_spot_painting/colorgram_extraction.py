###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 25)
# for color in colors:
#     rgb_colors.append(color.rgb)
#
# print(rgb_colors)
# print(len(rgb_colors))


"""FROM resource: https://pypi.org/project/colorgram.py/"""
# # Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 25)
#
# # colorgram.extract returns Color objects, which let you access
# # RGB, HSL, and what proportion of the image was that color.
# first_color = colors[0]
# rgb = first_color.rgb # e.g. (255, 151, 210)
# hsl = first_color.hsl # e.g. (230, 255, 203)
# proportion  = first_color.proportion # e.g. 0.34
#
# # RGB and HSL are named tuples, so values can be accessed as properties.
# # These all work just as well:
# red = rgb[0]
# red = rgb.r
# saturation = hsl[1]
# saturation = hsl.s

"""Lesson code"""
"""RUN FIRST PART ONLY ONCE"""
# rgb_colors = []
#
# colors = colorgram.extract('hirst_72_dots.jpg', 72)
#
# for color in colors:
#     # rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(176, 48, 79), (42, 98, 146), (205, 161, 94), (223, 210, 102), (137, 90, 64), (177, 164, 38),
              (109, 176, 207), (212, 131, 173), (227, 73, 49), (201, 75, 117), (88, 105, 192), (28, 143, 89),
              (124, 218, 207), (120, 43, 71), (94, 158, 65), (227, 170, 187), (131, 184, 161), (48, 187, 202),
              (172, 187, 222), (232, 173, 164), (154, 209, 219), (100, 51, 43), (34, 64, 115), (44, 80, 79),
              (215, 207, 37), (52, 58, 66), (31, 87, 90), (76, 51, 43), (40, 67, 65), (84, 37, 55)]
