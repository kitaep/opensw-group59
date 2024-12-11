# opensw term project - group 59

## Transfer text-to-image using Huggingface
---
### When you enter text, it creates an image that matches it.
- You have to install 'diffusers' first.
  Enter this code in cmd :
  ```c
  pip install -U diffusers
- Write the code in '202233151_차예린.c', Enter your token number, then commit.
- You need python 3.8 or upper version.
- This is successfully executed screen : ![input_code](https://github.com/user-attachments/assets/1cf1ec6e-4061-4501-a51f-41aadd5af0f9)
![output_image](https://github.com/user-attachments/assets/719ef260-8ada-4f42-babc-29551df5914a)


- Reference : [https://huggingface.co/black-forest-labs/FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev)
---

## Random cat image on node web server

### Prerequisite
- docker
- docker compose
- node

### Installation
To run with node: `node app.js`
To run with docker: `docker compose up -d --build`

### Usage
you could see the website on `localhost:3000` after deployment
![example](https://github.com/user-attachments/assets/465aed58-32ff-4983-9c62-37c9571f002d)

---

## Face detection project using openCV

### Project Overview
- This project uses OpenCV’s Haar Cascade Classifier to detect faces in an image. The program loads an image, detects faces, and highlights them with rectangles.

### Packages Used
- Python version: 3.x
- OpenCV version: 4.5.1 or later
- To install dependencies:
  ```c
  pip install opencv-python

### How to Run
1. Set up the environment: Install OpenCV with the above command.
2. Prepare the image: Update the file path in the code to your image location.
3. Run the code:
   ```c
   python haarcascade_detection.py
4. View results:
   A window will open showing the image with rectangles around detected faces.
   Press any key to close the window.

![example](https://github.com/user-attachments/assets/c5b33f29-578c-410c-b181-09850cceacd0)

Reference : [opencv-face-detection](https://opencv.org/blog/opencv-face-detection-cascade-classifier-vs-yunet/)

---
