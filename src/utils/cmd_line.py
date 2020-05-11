import argparse


parser = argparse.ArgumentParser(description="Template")
# model
parser.add_argument('-B', '--batch_size', default=250, type=int, help="Training batch size")
parser.add_argument('-N', '--n_neuron', default=400, type=int, help="The number of neurons")
parser.add_argument('-D', '--img_size', default=14, type=int, help="The size of image patches")
parser.add_argument('-K', '--kernel_size', default=10, type=int, help="The size of receptive field")
parser.add_argument('-S', '--stride_size', default=1, type=int, help="The size of stride")
# training
parser.add_argument('-e', '--epoch', default=100, type=int, help="Number of Epochs")
parser.add_argument('-lr', '--learning_rate', default=1e-2, type=float, help="Learning rate")
parser.add_argument('-rlr', '--r_learning_rate', default=1e-3, type=float, help="Learning rate for ISTA")
parser.add_argument('-lmda', '--reg', default=1e-3, type=float, help="Regularization")
parser.add_argument('-sess', '--session_name', default="sparsenet", type=str, help="session name")


# Parse arguments
def parse_args():
	return parser.parse_args()
