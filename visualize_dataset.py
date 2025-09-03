import argparse
import numpy as np
import matplotlib.pylab as plt
import matplotlib as mp
from datasets import load_dataset


def visualize_dataset(repo_name, n_examples):
    """
    Concatenates Hugging Face datasets from a list of repositories and pushes to the Hugging Face Hub.
    Adds a 'source_dataset' column to each component dataset, using only the name after the backslash.

    Args:
        repo_name (str): The name for the dataset repository.
    """

    ds = load_dataset(repo_name, split="train")
    print('Number of rows in dataset:', len(ds))

    indices = np.random.choice(np.arange(0, len(ds)), size=n_examples, replace=False).tolist()
    print('Random indices ready ...')
    subdata = [ds[i]['spike_counts'] for i in indices]
    print('Subdata ready ...')

    n_1 = int(np.sqrt(n_examples))
    n_2 = int(np.ceil(n_examples / n_1))

    plt.clf()
    ax = n_examples * [None]

    for i in range(n_examples):
        ax[i] = plt.subplot(n_1, n_2, i + 1)
        x = np.array(subdata[i])
        plt.imshow(x, interpolation='nearest', aspect='auto', cmap='gray_r')
        plt.xlim([0, x.shape[-1]+1])
        plt.ylim([0, x.shape[0]+1])
        plt.xticks([0, x.shape[-1]], ['0', str(x.shape[-1])], fontsize=6)
        plt.yticks([0, x.shape[0]], ['1', str(x.shape[0])], fontsize=6)
        ax[i].spines["right"].set_visible(False)
        ax[i].spines["top"].set_visible(False)
        ax[i].yaxis.set_ticks_position('left')
        ax[i].xaxis.set_ticks_position('bottom')
        if i == n_examples - n_2:
            plt.xlabel('Time (x 20 ms)', fontsize=6)
            plt.ylabel('Units', fontsize=6)
        
    plt.tight_layout()
    mp.rcParams['axes.linewidth'] = 0.75
    mp.rcParams['patch.linewidth'] = 0.75
    mp.rcParams['patch.linewidth'] = 1.15
    mp.rcParams['font.sans-serif'] = ['FreeSans']
    mp.rcParams['mathtext.fontset'] = 'cm'
    plt.savefig(repo_name.split("/")[-1] + '.jpg', bbox_inches='tight', dpi=300)


def get_args_parser():
    parser = argparse.ArgumentParser('Consolidate data in multiple files into a single file', add_help=False)
    parser.add_argument('--repo_name',default="eminorhan/vbn",type=str, help='HF repo name')
    parser.add_argument('--n_examples',default=6,type=int, help='number of examples to display')
    return parser

if __name__ == '__main__':

    # list of admissible dataset repositories
    # repo_list = [
    #     "eminorhan/vbn", "eminorhan/ibl", "eminorhan/shield", "eminorhan/vcn", "eminorhan/vcn-2", "eminorhan/v2h", "eminorhan/petersen",
    #     "eminorhan/oddball", "eminorhan/illusion", "eminorhan/huszar", "eminorhan/steinmetz", "eminorhan/steinmetz-2", "eminorhan/finkelstein",
    #     "eminorhan/giocomo", "eminorhan/mehrotra", "eminorhan/iurilli", "eminorhan/gonzalez", "eminorhan/li" 
    # ]

    args = get_args_parser()
    args = args.parse_args()
    print(args)

    visualize_dataset(args.repo_name, args.n_examples)