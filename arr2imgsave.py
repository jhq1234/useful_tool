def arr2imgsave(x, save_dir):
    # save the input image x and return PIL.Image.Image
    
    # Environment needed
    # from PIL import Image
    # import numpy as np
    # import torch
    
    # transform to numpy array
    if type(x) is torch.Tensor:
        x = x.permute(1,2,0).numpy()
    elif type(x) is np.ndarray:
        x = x
    else:
        print('Data type is not a numpy.ndarray or torch.tensor')
        return 0
    
    # numpy array normalize
    x = (x-x.min()) / (x.max() - x.min())
    x = (x * 255).astype(np.uint8)
    img = Image.fromarray(x)
    img.save(save_dir)
    
    return img
