from socketserver import ThreadingUDPServer
import PIL
from imagehash import *
from img2vec_pytorch import Img2Vec
import torch
import torch.nn as nn
from abc import ABC, abstractmethod
import numpy as np



class IsDuplicate(ABC):
    """
    Abstract class for duplicate detection
    """
    def __init__(self, image1: str, image2: str):
        self.image1 = image1
        self.image2 = image2

    @abstractmethod
    def is_duplicated(self):
        pass


class IsDuplicateHashes(IsDuplicate):
    """Duplicate detection using hashes """

    def __init__(self, image1: str, image2: str, hash_type: str):
        self.hash_type = hash_type
        # invoking the __init__ of the parent class
        IsDuplicate.__init__(self, image1, image2)


    @staticmethod
    def compute_hash(path_to_image: str, hash_type: str) -> np.array:
        """
        path_to_image - path to image of which hashes are computed
        hashf - hash function name
        output: 
        """
        image = PIL.Image.open(path_to_image)
        if hash_type == "phash":
            return phash(image)
        elif hash_type == "phash":
            return dhash(image)
        else:
            return averagehash(image)
        

    def is_duplicated(self) -> bool:
        """implement method definig if images are duplicated"""
        print("[INFO] computing image hash...")
        if self.compute_hash(self.image1, self.hash_type) == self.compute_hash(self.image2, self.hash_type):
            return True
        else:
            return False


class IsDuplicateEmbedding(IsDuplicate):
    """Duplicate detection using embedding"""
    def __init__(self, image1: str, image2: str, net: str, layer: str, thr: float):
        self.net = net
        self.layer = layer
        self.threshold = thr
        # invoking the __init__ of the parent class
        IsDuplicate.__init__(self, image1, image2)


    @staticmethod
    def get_similarity(pic1vec: torch.Tensor, pic2vec: torch.Tensor) -> torch.Tensor:
        """obtain consine similarity between two pictures
        vec1: tensor embedding of image1
        vec2: tensor embedding of image2
        output: cosine similarity tensor
        """
        cos = nn.CosineSimilarity(dim=1, eps=1e-6)
        cos_sim = cos(pic1vec.reshape((1, -1)),
                        pic2vec.reshape((1, -1)))[0]
        return cos_sim
            
    @staticmethod
    def compute_embedding(image: str, net: str, layer: str)-> torch.Tensor:
        """Compute vector embedding of an image based on precomputed network
        image: image path
        net: network name
        layer: layer of the network
        output: tensor with embedding
        """

        img2vec = Img2Vec(cuda=torch.cuda.is_available(), model=net, layer=layer)
        img = PIL.Image.open(image)     
        vec = img2vec.get_vec(img, tensor=True)
        return vec

    def is_duplicated(self)-> bool:
        """implement method definig if images are duplicated"""
        print("[INFO] computing embeddings...")
        emb1 = self.compute_embedding(self.image1, self.net, self.layer)
        emb2 = self.compute_embedding(self.image2, self.net, self.layer)
        cosine = self.get_similarity(emb1, emb2)
        if float(cosine) > self.threshold:
            return True
        return False
         

        
