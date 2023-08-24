import torch
import cv2
import torch.nn.functional as F
from model import TwoStreamNetwork
from face_detector import detect_face_and_resize
from filters import apply_hf_filters, apply_lf_filters

image_path = "1.jpg"
resized_face = detect_face_and_resize(image_path)
hf_image = apply_hf_filters(resized_face)
lf_image = apply_lf_filters(resized_face)
cv2.imwrite("hf_filtered.jpg", hf_image)
cv2.imwrite("lf_filtered.jpg", lf_image)
hf_tensor = torch.from_numpy(hf_image.transpose(2, 0, 1)).float().unsqueeze(0)
lf_tensor = torch.from_numpy(lf_image.transpose(2, 0, 1)).float().unsqueeze(0)

model = TwoStreamNetwork()
output = model(hf_tensor, lf_tensor)
probabilities = F.softmax(output, dim=1)

print(output)
print(probabilities)
