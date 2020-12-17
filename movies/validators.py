def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext=os.path.splitext(value.name)[1]
    valid_ext=['.pdf','.doc','.docx',]
    if not ext.lower() in valid_ext:
        raise ValidationError('Unsupported file format')