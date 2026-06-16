from django.core.exceptions import ValidationError
import os

def validate_size(file):
    max_size  = 10
    max_size_bytes = max_size * 1024 * 1024
    if file.size > max_size_bytes:
        raise ValidationError(f"File size should not exceed {max_size} MB.")
    
def validate_image_format(file):
    # valid_formats = [ 'image/png', 'image/gif']
    # if file.content_type not in valid_formats:
    #     raise ValidationError("Unsupported file format. Allowed formats: JPEG, PNG, GIF.")
    valid_extensions = ['.jpg', '.jpeg', '.png', '.webp']
    ext = os.path.splitext(file.name)[1].lower()
    if ext not in valid_extensions:
        raise ValidationError(f"Unsupported file extension. Allowed: {', '.join(valid_extensions)}")