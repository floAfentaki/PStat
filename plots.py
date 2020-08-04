import matplotlib.pyplot as plt
import numpy as np


def plot_top(top,book,b):
    top.plot(kind='bar',title='Top5 Χώρες Προέλευσης Τουριστων',subplots="True",)
    plt.legend([book[b]])
    plt.show()





def autolabel(rects,ax):
    """Attach a text label above each bar in rects, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


def plot_year(tt,book):
        labels=['2011','2012','2013','2014','2015']
        x = np.arange(len(labels))  # the label locations
        width = 0.2  # the width of the bars


        fig,ax=plt.subplots()
        rects1=ax.bar(book[0],tt[0],width,bottom=None,  label='2011')
        rects2=ax.bar(book[1],tt[1], width,bottom=None,   label='2012')
        rects3=ax.bar(book[2],tt[2], width,bottom=None,   label='2013')
        rects4=ax.bar(book[3],tt[3], width,bottom=None,   label='2014')
        rects5=ax.bar(book[4],tt[4], width,bottom=None,   label='2015')
        #rects2 = ax.bar(x + width/2, women_means, width, label='Women')


        ax.set_ylabel('Πλήθος Τουριστών')
        plt.title('Πλήθος Τουριστών ανά Έτος')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()



        autolabel(rects1,ax)
        autolabel(rects2,ax)
        autolabel(rects3,ax)
        autolabel(rects4,ax)
        autolabel(rects5,ax)

        fig.tight_layout()

#        plt.show()

def plot_month3(year):
        labels=['Ιανουάριος-Μάρτιος','Απρίλιος-Ιούνιος','Ιούλιος-Σεπτέμβριος','Οκτώβριος-Δεκέμβριος']
        x = np.arange(len(labels))  # the label locations
        width = 0.2  # the width of the bars


        fig,ax=plt.subplots()
        rects1=ax.bar(x-4*width/2,year[0],width,bottom=None,  label='2011')
        rects2=ax.bar(x-2*width/2,year[1], width,bottom=None,   label='2012')
        rects3=ax.bar(x,year[2], width,bottom=None,   label='2013')
        rects4=ax.bar(x+2*width/2,year[2], width,bottom=None,   label='2014')
        rects5=ax.bar(x+4*width/2,year[4], width,bottom=None,   label='2015')
        #rects2 = ax.bar(x + width/2, women_means, width, label='Women')





        ax.set_ylabel('Πλήθος Τουριστών')
        plt.title('Πλήθος Τουριστών ανά 3Μηνο')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()


        autolabel(rects1,ax)
        autolabel(rects2,ax)
        autolabel(rects3,ax)
        autolabel(rects4,ax)
        autolabel(rects5,ax)

        fig.tight_layout()

#        plt.show()

def plot_rail(transport):
        labels=['Αεροπλάνο','Τραίνο','Πλοίο','Αυτοκίνητο']
        x = np.arange(len(labels))  # the label locations
        width = 0.2  # the width of the bars


        fig,ax=plt.subplots()
        rects1=ax.bar(x-4*width/2,transport[0],width,bottom=None,  label='2011')
        rects2=ax.bar(x-2*width/2,transport[1], width,bottom=None,   label='2012')
        rects3=ax.bar(x,transport[2], width,bottom=None,   label='2013')
        rects4=ax.bar(x+2*width/2,transport[2], width,bottom=None,   label='2014')
        rects5=ax.bar(x+4*width/2,transport[4], width,bottom=None,   label='2015')
        #rects2 = ax.bar(x + width/2, women_means, width, label='Women')





        ax.set_ylabel('Πλήθος Τουριστών')
        plt.title('Πλήθος Τουριστών ανά Μεταφορικό Μέσο')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()
        def autolabel(rects):
            """Attach a text label above each bar in rects, displaying its height."""
            for rect in rects:
                height = rect.get_height()
                ax.annotate('{}'.format(height),
                            xy=(rect.get_x() + rect.get_width() / 2, height),
                            xytext=(0, 3),  # 3 points vertical offset
                            textcoords="offset points",
                            ha='center', va='bottom')


        autolabel(rects1)
        autolabel(rects2)
        autolabel(rects3)
        autolabel(rects4)
        autolabel(rects5)

        fig.tight_layout()

#        plt.show()


