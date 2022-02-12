import math

import numpy
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.colors as mcolors


class HistInfo:

    def __init__(self):
        self.left = 0.0
        self.right = 1.0
        self.binCount = 1
        self.YData = []
        self.YLabel = []
        self.YColor = []
        self.YLineWidth = []
        self.YLineStyle = []
        self.OccupiedColor = []
        self.xLabel = ""
        self.xMinMax = None
        self.xScale = "linear"
        self.yLabel = ""
        self.yMinMax = None
        self.yScale = "linear"
        self.fontSize = 12.0
        self.graphicSizeSet = False
        self.width = 500
        self.height = 400
        self.dpi = 1

    def SetBin(self, left: float, right: float, binCount: int):
        self.left = left
        self.right = right
        self.binCount = binCount
        return self

    def AddYData(self, yData: list, label: str,
                 color: str = None, lineWidth: float = 1,
                 lineStyle: str = "solid"):
        if len(yData) != self.binCount:
            print("length of yData not fit binCount")
            return self
        bXKCDColor = False
        if color is not None and color.startswith("xkcd:"):
            bXKCDColor = True
        realColor = None
        if bXKCDColor:
            realColor = mcolors.XKCD_COLORS.get(color)
        else:
            realColor = mcolors.CSS4_COLORS.get(color)
        if realColor is None:
            print("here?")
            for colorName in mcolors.CSS4_COLORS.keys():
                if self.OccupiedColor.count(colorName) < 1:
                    self.OccupiedColor.append(colorName)
                    realColor = mcolors.CSS4_COLORS[colorName]
                    print(colorName)
                    break
        else:
            self.OccupiedColor.append(color)
        self.YData.append(yData)
        self.YLabel.append(label)
        self.YColor.append(realColor)
        self.YLineWidth.append(lineWidth)
        self.YLineStyle.append(lineStyle)
        return self

    def SetAxisInfo(self, xLabel: str, yLabel: str,
                    xMinMax: list = None, xScale: str = "linear",
                    yMinMax: list = None, yScale: str = "linear"):
        if xMinMax is None:
            xMinMax = [self.left, self.right]
        if yMinMax is None:
            yMinMax = [np.array(self.YData).min, np.array(self.YData).max]
        self.xLabel = xLabel
        self.xMinMax = xMinMax
        self.xScale = xScale
        self.yLabel = yLabel
        self.yMinMax = yMinMax
        self.yScale = yScale
        return self

    def SetFontSize(self, fontSize:float):
        self.fontSize = fontSize
        return self

    def SetGraphicSize(self, width, height, dpi: int):
        self.width = width
        self.height = height
        self.dpi = dpi
        self.graphicSizeSet = True
        return self

    def ResizeGraphic(self):
        if self.graphicSizeSet:
            return
        xMinMax = [self.left, self.right] if self.xMinMax is None else self.xMinMax
        print(self.YData)
        yMinMax = [0, np.array(self.YData).max()] if self.yMinMax is None else self.yMinMax
        print(yMinMax)
        self.width = 1.4 * (xMinMax[1] - xMinMax[0])
        self.height = 1.4 * (yMinMax[1] - yMinMax[0])
        if self.width > 500 * self.height / 400:
            self.height = self.width * 400 / 500
        else:
            self.width = 500 * self.height / 400
        self.dpi = math.ceil(max(500 / self.width, self.fontSize))
        print(self.width, self.height, self.dpi)


def HistDraw(histInfo: HistInfo, output: str):
    histInfo.ResizeGraphic()
    fig = plt.figure(figsize=(histInfo.width, histInfo.height), dpi=histInfo.dpi)
    frame = gridspec.GridSpec(1, 1)
    pad = fig.add_subplot(frame[0])
    binnings = np.linspace(histInfo.left, histInfo.right, histInfo.binCount + 1, endpoint=True)
    middlePoints = np.array([histInfo.left + (histInfo.right - histInfo.left) * (i + 0.5) / histInfo.binCount for i in range(0, histInfo.binCount)])
    print(middlePoints)
    for i in range(0, len(histInfo.YData)):
        print(histInfo.YData[i])
        pad.hist(x=middlePoints, bins=binnings, weights=np.array(histInfo.YData[i]),
                 label=histInfo.YLabel[i], histtype="step", rwidth=1.0,
                 color=histInfo.YColor[i], edgecolor=histInfo.YColor[i], linewidth=histInfo.YLineWidth[i],
                 linestyle=histInfo.YLineStyle[i],
                 bottom=None, cumulative=False, density=False, align="mid", orientation="vertical")
    plt.rc('text', usetex=False)
    plt.xlabel(histInfo.xLabel, fontsize=histInfo.fontSize, color="black")
    plt.ylabel(histInfo.yLabel, fontsize=histInfo.fontSize, color="black")
    if histInfo.xMinMax is not None:
        plt.gca().set_xlim(histInfo.xMinMax[0], histInfo.xMinMax[1])
    if histInfo.xScale == "linear":
        plt.gca().set_xscale("linear")
    elif histInfo.xScale == "log":
        plt.gca().set_xscale("log", nonposy="clip")
    if histInfo.yMinMax is not None:
        plt.gca().set_ylim(histInfo.yMinMax[0], histInfo.yMinMax[1])
    if histInfo.yScale == "linear":
        plt.gca().set_yscale("linear")
    elif histInfo.yScale == "log":
        plt.gca().set_yscale("log", nonposy="clip")
    """
    l05, = plt.plot([1, 2, 3], label="$background$", color="blue")
    l04, = plt.plot([1, 2, 3], label="$M_{N}= 30 GeV$ ", color="deeppink", linestyle="dashed")
    l03, = plt.plot([1, 2, 3], label="$M_{N}= 20 GeV$ ", color="tomato", linestyle="dashed")
    l02, = plt.plot([3, 2, 1], label="$M_{N}= 10 GeV$ ", color="gold", linestyle="dashed")
    l01, = plt.plot([3, 2, 1], label="$M_{N}= 1 GeV$ ", color="greenyellow", linestyle="dashed")
    plt.legend([l05, l04, l03, l02, l01], ["$Background$", r"$M_{N}= 30 \; {\rm GeV}$  ", r"$M_{N}= 20 \; {\rm GeV}$",
                                           r"$M_{N}= 10 \; {\rm GeV}$ ", r"$M_{N}= 1 \; {\rm GeV}$ "],
               bbox_to_anchor=(1.0, 1), loc=1, borderaxespad=0.)
    # Legend
    # plt.legend(bbox_to_anchor=(1.05,1), loc=2, borderaxespad=0.)
    # Saving the image
    """
    print("saving to: ", output)
    plt.savefig(output)
