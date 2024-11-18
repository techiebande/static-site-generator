import re

def extract_markdown_images(text):
    image_attributes_regex = r'!\[([^\]]+)\]\((https?://[^\)]+)\)'

    return re.findall(image_attributes_regex, text)


