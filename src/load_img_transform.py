from torchvision import transforms
from PIL import Image

def transform_image(image):
    # Load Image
    img = Image.open(image)
    img = img.convert('RGB')
    
    # Transform Image
    crop_size = 224

    transform = transforms.Compose([
        transforms.Resize(crop_size),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                            std=[0.229, 0.224, 0.225])
    ])

    input = transform(img)
    input = input.unsqueeze(0)

    return input