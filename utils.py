import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt




def plot_curve(train_losses, valid_losses, savefig = True, showfig = False, filename = 'training_curve.png'):

    x = np.arange(len(train_losses))
    y1 = train_losses
    y2 = valid_losses
#     y3 = train_losses

    fig, ax1 = plt.subplots(figsize = (12,8))
#     ax2 = ax1.twinx()

    ax1.plot(x, y1, color = 'b', marker = 'o', label = 'Training Loss')
    ax1.plot(x, y2, color = 'g', marker = 'o', label = 'Validation Loss')
#     ax2.plot(x, y3, color = 'r', marker = 'o', label = 'Training Loss')

    ax1.set_xlabel('Epochs')
    ax1.set_ylabel('Loss')
#     ax2.set_ylabel('Loss')

    ax1.legend()
#     ax2.legend()

    if savefig:
        fig.savefig(filename, format = 'png', dpi = 600, bbox_inches = 'tight')
    if showfig:
        plt.show()
    plt.close()

    return 