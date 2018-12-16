import asyncio
import base64


# 3rd Party Install
from baybars.timber import get_logger
import requests

logger = get_logger('resnet_client')

# The server URL specifies the endpoint of your server running the ResNet
# model with the name "resnet" and using the predict interface.
RESNET_STATUS_URL = 'http://localhost:8501/v1/models/resnet'
SERVER_URL = 'http://localhost:8501/v1/models/resnet:predict'

# The image URL is the location of the image we should send to the server
IMAGE_URL = 'https://tensorflow.org/images/blogs/serving/cat.jpg'


async def get_as_base64(url):
  out = None
  response = requests.get(url)
  if response.status_code == 200:
    out = base64.b64encode(response.content) 

  return out 


async def main():
  response = requests.get(RESNET_STATUS_URL)
  logger.info('resnet status: {}'.format(response.json()))
  image_content = await get_as_base64(IMAGE_URL)
  predict_request = {
    'instances': [{'b64': image_content.decode()}],
  }

  # Send few requests to warm-up the model.
  for _ in range(3):
    response = requests.post(SERVER_URL, json=predict_request)
    response.raise_for_status()

  # Send few actual requests and report average latency.
  total_time = 0
  num_requests = 100
  for _ in range(num_requests):
    response = requests.post(SERVER_URL, json=predict_request)
    response.raise_for_status()
    total_time += response.elapsed.total_seconds()
    prediction = response.json()['predictions'][0]

  print('Prediction class: {}, avg latency: {} ms'.format(
      prediction['classes'], (total_time*1000)/num_requests))


if __name__ == '__main__':
  loop = asyncio.new_event_loop()
  asyncio.set_event_loop(loop)
  result = loop.run_until_complete(main())