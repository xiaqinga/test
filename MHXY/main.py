from automator import Automator
from image import Image
#Device3 = '37a01c54'
#instance = Automator(Device3)
instance = Image()
print(instance.template_match('./home.jpg','./2.jpg'))
