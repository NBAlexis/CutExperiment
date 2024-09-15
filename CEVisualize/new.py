from Interfaces.LHCOlympics import LoadLHCOlympics
from DataStructure.EventSample import EventSample
from DataStructure.Particles import ParticleType, ParticleStatus
from CutAndExport.Histogram import EventObservables
from matplotlib import rcParams
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.gridspec as gridspec

config = {"font.family" : 'Times New Roman', "font.size": 24 , "mathtext.fontset": 'stix'}
rcParams.update(config)

# Load events
bgEvent = LoadLHCOlympics(r"D:\\CutExperiment-master\\Applications\\gQGC\\624bg-3TeV-aftercut.lhco")
signalEvent0 = LoadLHCOlympics(r"D:\\CutExperiment-master\\Applications\\gQGC\\624gt0-3TeV-aftercut.lhco")
signalEvent1 = LoadLHCOlympics(r"D:\\CutExperiment-master\\Applications\\gQGC\\624gt1-3TeV-aftercut.lhco")
signalEvent2 = LoadLHCOlympics(r"D:\\CutExperiment-master\\Applications\\gQGC\\624gt2-3TeV-aftercut.lhco")
signalEvent3 = LoadLHCOlympics(r"D:\\CutExperiment-master\\Applications\\gQGC\\624gt3-3TeV-aftercut.lhco")
signalEvent4 = LoadLHCOlympics(r"D:\\CutExperiment-master\\Applications\\gQGC\\624gt4-3TeV-aftercut.lhco")
signalEvent5 = LoadLHCOlympics(r"D:\\CutExperiment-master\\Applications\\gQGC\\624gt5-3TeV-aftercut.lhco")
signalEvent6 = LoadLHCOlympics(r"D:\\CutExperiment-master\\Applications\\gQGC\\624gt6-3TeV-aftercut.lhco")
signalEvent7 = LoadLHCOlympics(r"D:\\CutExperiment-master\\Applications\\gQGC\\624gt7-3TeV-aftercut.lhco")

# Define the HardestPhoton function
def HardestPhoton(event: EventSample) -> float:
    largetPhotonEnergy = -1.0
    for particle in event.particles:
        if ParticleType.Photon == particle.particleType and particle.momentum.values[0] > largetPhotonEnergy:
            largetPhotonEnergy = particle.momentum.values[0]
    return largetPhotonEnergy

# Creating a new Canvas
fig = plt.figure(figsize=(12, 6), dpi=80)  # Create a new figure with specified size and resolution
frame = gridspec.GridSpec(1, 1, right=0.7)  # Create a gridspec with 1 row and 1 column
pad = fig.add_subplot(frame[0])  # Add a subplot to the gridspec

# Calculate observables
SMbg = EventObservables(bgEvent, HardestPhoton)
PTgamma_Sig0 = EventObservables(signalEvent0, HardestPhoton)
PTgamma_Sig1 = EventObservables(signalEvent1, HardestPhoton)
PTgamma_Sig2 = EventObservables(signalEvent2, HardestPhoton)
PTgamma_Sig3 = EventObservables(signalEvent3, HardestPhoton)
PTgamma_Sig4 = EventObservables(signalEvent4, HardestPhoton)
PTgamma_Sig5 = EventObservables(signalEvent5, HardestPhoton)
PTgamma_Sig6 = EventObservables(signalEvent6, HardestPhoton)
PTgamma_Sig7 = EventObservables(signalEvent7, HardestPhoton)

"""
# Plot histograms
pad.hist(bghard, bins=100, range=[0, 1700], histtype="step", density=True, label="Background", color="blue", linestyle="solid")
pad.hist(PTgamma_Sig0, bins=100, range=[0, 1700], histtype="step", density=True, label="$\mathcal{O}_{gT,0}$ 3 TeV", color="green", linestyle="solid")
pad.hist(PTgamma_Sig1, bins=100, range=[0, 1700], histtype="step", density=True, label="$\mathcal{O}_{gT,1}$ 3 TeV", color="red", linestyle="solid")
pad.hist(PTgamma_Sig2, bins=100, range=[0, 1700], histtype="step", density=True, label="$\mathcal{O}_{gT,2}$ 3 TeV", color="purple", linestyle="solid")
pad.hist(PTgamma_Sig3, bins=100, range=[0, 1700], histtype="step", density=True, label="$\mathcal{O}_{gT,3}$ 3 TeV", color="brown", linestyle="solid")
pad.hist(PTgamma_Sig4, bins=100, range=[0, 1700], histtype="step", density=True, label="$\mathcal{O}_{gT,4}$ 3 TeV", color="gold", linestyle="solid")
pad.hist(PTgamma_Sig5, bins=100, range=[0, 1700], histtype="step", density=True, label="$\mathcal{O}_{gT,5}$ 3 TeV", color="orange", linestyle="solid")
pad.hist(PTgamma_Sig6, bins=100, range=[0, 1700], histtype="step", density=True, label="$\mathcal{O}_{gT,6}$ 3 TeV", color="saddlebrown", linestyle="solid")
pad.hist(PTgamma_Sig7, bins=100, range=[0, 1700], histtype="step", density=True, label="$\mathcal{O}_{gT,7}$ 3 TeV", color="lightcoral", linestyle="solid")
"""
# 定义颜色列表
colors = ['blue', 'green', 'red', 'purple', 'brown', 'gold', 'orange', 'saddlebrown', 'lightcoral']

# 标签列表，对应于每个颜色
labels = ['SM', '$\mathcal{O}_{gT_0}$', '$\mathcal{O}_{gT_1}$', '$\mathcal{O}_{gT_2}$', '$\mathcal{O}_{gT_3}$', '$\mathcal{O}_{gT_4}$', '$\mathcal{O}_{gT_5}$', '$\mathcal{O}_{gT_6}$', '$\mathcal{O}_{gT_7}$']

# 绘制柱状图
for i, (label, energies) in enumerate(zip(labels, [SMbg, PTgamma_Sig0, PTgamma_Sig1, PTgamma_Sig2, PTgamma_Sig3, PTgamma_Sig4, PTgamma_Sig5, PTgamma_Sig6, PTgamma_Sig7])):
    if label == 'SM':
        # 'Background' 数据集使用虚线
        linestyle = '--'
    else:
        # 其他数据集使用实线
        linestyle = '-'

    plt.hist(energies, bins=100, range=[0, 1700], histtype="step", density=True, label=label, color=colors[i % len(colors)], linestyle=linestyle)

# 创建代表每个直方图样式的临时线对象
lines = []
for i, color in enumerate(colors):
    line, = plt.plot([], [], color=color, linestyle='-', label=labels[i]) # 设置标签
    lines.append(line)

# 添加图例，使用带颜色的线和自定义的标签
plt.legend(handles=lines, bbox_to_anchor=(0.75, 0.9), fontsize=12)


# Axis labels
plt.rc('text', usetex=False)
plt.xlabel(r"$E_{\gamma} \;\rm{ [ GeV ]}$", fontsize=16, color="black")
plt.ylabel(r"${\rm Events \; ( scaled \; to \; one ) }$", fontsize=16, color="black")
plt.tick_params(axis='both', which='major', labelsize=16) # 'both'表示同时修改x轴和y轴

# Add text
plt.text(0.35, 0.9, r"$\sqrt{S}=3~ $TeV", fontsize=16, color="black", transform=plt.gca().transAxes, ha='center')

# 确保x,y轴的最小值为0
plt.ylim(0, plt.ylim()[1])
plt.xlim(0, plt.xlim()[1])

# 防止科学计数法表达，并始终显示为0
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

# 如果需要，可以重新绘制y轴的刻度
#plt.gca().yaxis.set_major_locator(plt.MaxNLocator(5))


# Saving the image as PDF
plt.savefig('E-gamma3.pdf', format='pdf')

# Show the plot
plt.show()



