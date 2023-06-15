import matplotlib.pyplot as plt
import numpy as np
import webbrowser
a0=np.loadtxt('data_sample\\sample.csv', delimiter=',', encoding='utf-8', skiprows=1)
fig_1, ax=plt.subplots(figsize=(6,4))
ax.plot(a0[:,0]*1e3, a0[:,1], color="blue", lw=1, ls='-', marker='o', markersize=6.5, label='A')
ax.plot(a0[:,0]*1e3, a0[:,2], color="red", lw=1, ls='-', marker='o', markersize=6.5, label='B')
ax.set_xscale('linear')
ax.set_xlim([0, 1000])
ax.set_ylim([-120, -20])
ax.set_xlabel('Frequency [MHz]', fontsize=11)
ax.set_ylabel('Power [dBm]', fontsize=11)
ax.legend(loc='upper left') 
plt.title('Frequency characteristics of radiated power', fontsize=12)
ax.grid(ls=':')
PngFile='data_sample\\sample.png'
PdfFile='data_sample\\sample.pdf'
fig_1.subplots_adjust(left=0.13, right=0.95, bottom=0.13, top=0.93)
fig_1.savefig(PngFile, facecolor='white')
fig_1.savefig(PdfFile, facecolor='white')
webbrowser.open_new(PngFile)
webbrowser.open_new(PdfFile)