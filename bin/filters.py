#PIL=Python Imanging Library
#Image: Is used to store the image data
#ImageFilter: Is used to apply the pre-configured filter transformations
from PIL import Image, ImageFilter
import io

#file: The image that was received as a file object
#filter: The filter that will be applied as a string
def apply_filter(file: object, filter: str) -> object:
    """
    TODO:
    1. Accept the image as file object, and the filter type as string
    2. Open the file as an PIL Image object
    3. Apply the filter
    4. Convert the PIL Image object to file object
    5. Return the file object
    """
    #Open the image as a PIL object
    image = Image.open(file)
    #Conver the variable filter to uppercase
    #Then, append the filter to "ImageFilter"
    #Finally convert that to a valid Python code using the "eval()" method which comverts a string to a Python command for execution
    image = image.filter(eval( f"ImageFilter. {filter.upper()} " ))

    #Now, our filter is applied 
    #convert the PIL Image Object to file object before returning
    file = io.BytesIO() #Empty buffer memory
    image.save(file, "JPEG" ) #Store file in memory
    file.seek( 0 ) #Reset the pointer to start with file.seek(0)

    return file

