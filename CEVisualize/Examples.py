import matplotlib.colors as mcolors
from CEVisualize.Hist import HistDraw
from CEVisualize.Hist import HistInfo

HistDraw(HistInfo().SetBin(0, 1, 5).AddYData([1.1, 1.2, 1.3, 1.4, 1.1], "y1").AddYData([1.0, 1.2, 1.1, 1.0, 1.1], "y2"), "_Output/a.eps")

# print(mcolors.CSS4_COLORS.keys())
