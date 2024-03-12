#NOTE:  This must be the first call in order to work properly!
from deoldify import device
from deoldify.device_id import DeviceId
import fastai
from deoldify.visualize import *
import warnings
import collections.abc
collections.Sized = collections.abc.Sized


#choices:  CPU, GPU0...GPU7
device.set(device=DeviceId.GPU0)

import torch

if not torch.cuda.is_available():
    print('GPU not available.')

warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")

colorizer = get_image_colorizer(artistic=True)

source_url = 'https://1.bp.blogspot.com/-7VlPE1Phras/VC_D7D3UQ9I/AAAAAAAA_ZU/oDagILZMaKI/s1600/Daily%2BLife%2Bin%2BFinland%2Bin%2B1941%2B(12).jpg' #@param {type:"string"}
render_factor = 35  #@param {type: "slider", min: 7, max: 40}
watermarked = True #@param {type:"boolean"}

if source_url is not None and source_url !='':
    image_path = colorizer.plot_transformed_image_from_url(url=source_url, render_factor=render_factor, compare=True, watermarked=watermarked)
    show_image_in_notebook(image_path)
else:
    print('Provide an image url and try again.')