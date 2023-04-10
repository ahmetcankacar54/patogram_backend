import base64
from io import BytesIO
from PIL import Image
from fastapi import HTTPException
from utils.constants import Constants


def convert_to_file(bs64Text):

    if bs64Text:
        try:
            if 'base64' in bs64Text:
                format, imgstr = bs64Text.split(';base64,')
            else:
                imgstr = bs64Text

            decoded_image = Image.open(BytesIO(base64.b64decode(imgstr)))
            output_image = BytesIO()
            thumbnail = BytesIO()

            if decoded_image.mode in ("RGBA", "P"):
                decoded_image = decoded_image.convert("RGB")

            decoded_image.save(output_image, format="JPEG", quality=60)
            decoded_image = decoded_image.resize(
                (Constants.size), Image.Resampling.LANCZOS)
            decoded_image.save(thumbnail, format="JPEG", quality=10)
            output_image.seek(0)
            thumbnail.seek(0)
            return output_image, thumbnail
        except Exception:
            raise HTTPException(status_code=500, detail='Something went wrong')
        finally:
            decoded_image.close()
