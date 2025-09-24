import argparse

import vertexai 
from vertexai.preview.vision_model import ImageGenerationModel

def generate_image (project_id: str, location: str, ouput_file: str, prompt: str) -> vertexai.preview.vision_models.ImageGenerationResponses:
  """
  Gen an img using a text prompt

  Args:
      project_id: Google Cloud project ID, used to initialize Vertex AI.
      location: Google Cloud region, used to initialize Vertex AI.
      output_file: Local path to the output image file.
      prompt: The text prompt describing what you want to see.
  """
  
  vertexai.init(project = project_id, location = location)
  
  model = ImageGenerationModel.from_pretrained("image-3.0-generate-002")


  img = model.generate_images(
    prompt = prompt,
    number_of_images = 3,
    seed = 1,
    add_watermark = False,    
  )

  img[0].save(location = output_file)

  return img

generate_image(
  project_id='<PROJECT_ID>',
  location='<REGION>',
  output_file='image.jpeg',
  prompt='Create an image containing a bouquet of 2 sunflowers and 3 roses',
)