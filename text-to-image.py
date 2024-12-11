# Hugging Face 이용해서 text-to-image 변환

from huggingface_hub import InferenceClient
from PIL import Image

client = InferenceClient("black-forest-labs/FLUX.1-dev", token="hf_xxxxxxxxxxxxxx")

# output is a PIL.Image object
image = client.text_to_image("Astronaut riding a horse")

# 1. 이미지를 저장
image.save("output_image.png")  # output_image.png로 저장

# 2. 이미지를 띄우기
image.show()  # 기본 이미지 뷰어에서 열기
