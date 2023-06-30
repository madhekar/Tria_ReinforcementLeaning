import matplotlib.pyplot as plt
from IPython import display
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 
#plt.ion()

def plot(scores, mean_scores):
    #display.clear_output(wait=True)
    #display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.ylim(ymin=0)
    plt.text(len(scores) -1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores) -1, mean_scores[-1], str(mean_scores[-1]))
    plt.show()

def plots(scores, mean_scores):

    freq = np.arange(0, len(scores[0]), dtype=int)
    fig, ax = plt.subplots(nrows=2,ncols=2, figsize=(10,10))
    fig.tight_layout()

    ax[0,0].set_title('no model')
    ax[0,0].set_ylabel('score')
    #ax[0,0].set_xlabel('number episode')
    ax[0,0].plot( freq, scores[0])
    ax[0,0].plot(freq,mean_scores[0])
    #ax[0,0].text(len(scores) -1, scores[-1], str(scores[-1]))
    #ax[0,0].text(len(mean_scores) -1, mean_scores[-1], str(mean_scores[-1]))

    ax[0,1].set_title('ppo model')
    ax[0,1].set_ylabel('score')
    #ax[0,1].set_xlabel('number episode')
    ax[0,1].plot(freq,scores[1])
    ax[0,1].plot(freq,mean_scores[1])

    ax[1,0].set_title('neural model')
    ax[1,0].set_ylabel('score')
    #ax[1,0].set_xlabel('number episode')
    ax[1,0].plot(freq,scores[2])
    ax[1,0].plot(freq,mean_scores[2])

    ax[1,1].set_title('a2c model')
    ax[1,1].set_ylabel('score')
    #x[1,1].set_xlabel('number episode')
    ax[1,1].plot(freq,scores[3])
    ax[1,1].plot(freq,mean_scores[3])

    plt.show()

def plots_norm(scores, mean_scores):

    freq = np.arange(0, len(scores[0]), dtype=int)
    fig, ax = plt.subplots(nrows=1,ncols=2, figsize=(10,5))
    fig.tight_layout()

    ax[0].set_title('A2C model normalized obs and rewards')
    ax[0].set_ylabel(' original score')
    ax[0].set_xlabel('episode number')
    ax[0].plot( freq, scores[0])
    ax[0].plot(freq, mean_scores[0])

    ax[1].set_title('A2C model normalized obs and rewards')
    ax[1].set_ylabel(' normalized score')
    ax[1].set_xlabel(' episode number')
    ax[1].plot(freq,scores[1])
    ax[1].plot(freq,mean_scores[1])

    plt.show()    

def plots_3d(obs,acv,color):
    rows, cols = 2, 2
    fig, ax = plt.subplots(nrows=rows,ncols=cols, figsize=(15,8), subplot_kw=dict(projection='3d'))
    fig.suptitle('Tria A2C model predictions', fontsize=12)

    for row in range(rows):
        for col in range(cols):
            ax[row, col].scatter(obs[row + col][:,0],obs[row + col][:,1],obs[row + col][:,2],'.', c = color[row+col] ) 
            ax[row, col].set_title('initial obs: ' + str(round(obs[row + col][0:,0][-1],2))+ ':' + str(round(obs[row + col][0:,1][-1],2))+ ':' +str(round(obs[row + col][0:,2][-1],2))  + ' || final obs: ' + str(round(obs[row + col][0:,0][-2],2))+ ':' + str(round(obs[row + col][0:,1][-2],2)) + ':' + str(round(obs[row + col][0:,2][-2],2)), fontsize=8)
            ax[row, col].set_xlabel("T")
            ax[row, col].set_ylabel("H")
            ax[row, col].set_zlabel("AQ")
            for t,h,a,ac in zip(obs[row + col][:,0],obs[row + col][:,1],obs[row + col][:,2],acv[row + col]):
               ax[row, col].text(t,h,a,ac, fontsize=4)

    plt.subplots_adjust(left=0.13,
                    bottom=0.044,
                    right=0.91,
                    top=0.915,
                    wspace=0.32,
                    hspace=0.158)           
    plt.show()