from federated_learning.arguments import Arguments
from federated_learning.nets import FashionMNISTCNN
import os
import torch
from loguru import logger

if __name__ == '__main__':
    args = Arguments(logger)
    if not os.path.exists(args.get_default_model_folder_path()):
        os.mkdir(args.get_default_model_folder_path())
    # ---------------------------------
    # -------- FashionMNISTCNN --------
    # ---------------------------------
    full_save_path = os.path.join(args.get_default_model_folder_path(), 
    	"FashionMNISTCNN.model")
    torch.save(FashionMNISTCNN().state_dict(), full_save_path)
