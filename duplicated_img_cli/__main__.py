import sys
import argparse
from .duplicate_images import IsDuplicateEmbedding, IsDuplicateHashes

def parse_args():
  """
  parse command line arguments
  """
  my_parser = argparse.ArgumentParser(description='Defines if images are duplicates',
                                      epilog='Enjoy the program! :)')

  my_parser.add_argument('image1',
                        help='first image path',
                        type=str)

  my_parser.add_argument('image2',
                        type=str,
                        help='second image path')

  my_parser.add_argument('-hash_type',
                        type=str,
                        default = 'phash', 
                        help="an optional argument; hasing function from xxx lib: 'phash', 'dhash', 'colorhash', 'average_hash")

  my_parser.add_argument('-net',
                         type=str,
                         default = 'resnet18', 
                        help="an optional argument; possbile values : 'resnet-18', 'resnet34', 'resnet50', 'resnet101', 'resnet152', 'alexnet', 'vgg', 'densenet', 'efficientnet_b0' - 'efficientnet_b7'")

  my_parser.add_argument('-layer',
                         type=str,
                         default = 'default', 
                        help='an optional argument; layer: see the doc https://github.com/christiansafka/img2vec')

  my_parser.add_argument('-threshold',
                         type=float,
                         default = '0.9', 
                        help='an optional argument; threshold for cosine similarity')

  # Execute parse_args()
  args = my_parser.parse_args()
  return args

def main():
    """run the program"""

    args = parse_args()
    my_answer = IsDuplicateHashes(args.image1, args.image2, args.hash_type)
    if not my_answer.is_duplicated():
      my_answer = IsDuplicateEmbedding(args.image1, args.image2, args.net, args.layer, args.threshold)
    print(my_answer.is_duplicated())

if __name__ == '__main__':
    main()