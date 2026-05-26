import torch
import torchvision
from thop import profile
from models import HFDS

print('==> Building model..')
model = HFDS()

dummy_input = torch.randn(4, 3, 256, 256)
flops, params = profile(model, (dummy_input,))
print('flops: ', flops, 'params: ', params)
print('flops: %.2f M, params: %.4f M' % (flops / 1000000.0, params / 1000000.0))
