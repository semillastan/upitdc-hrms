from imagekit.specs import ImageSpec
from imagekit import processors

class Enhance(processors.Adjustment):
    contrast = 1.2
    sharpness = 1.1

class ResizeDisplay(processors.Resize):  
    height = 220
    width = 300
    crop = True

class ResizeProfile(processors.Resize):  
    width = 125

class ResizeThumb(processors.Resize):
    height = 91
    width = 91
    crop = True
    
class ResizeIcon(processors.Resize):
    height = 50
    width = 50
    crop = True
    
class Display(ImageSpec):
    access_as = 'display'
    processors = [ResizeDisplay]
    
class Profile(ImageSpec):
    access_as = 'profile_photo'
    processors = [ResizeProfile]
    
class Thumbnail(ImageSpec):
    access_as = 'thumbnail'
    processors = [ResizeThumb, Enhance]
    
class Icon(ImageSpec):
    access_as = 'icon'
    processors = [ResizeIcon, Enhance]
