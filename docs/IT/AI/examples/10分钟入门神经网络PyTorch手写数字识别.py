## https://gitee.com/kongfanhe/pytorch-tutorial/blob/master/test.py#
import torch
from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision.datasets import MNIST
import matplotlib.pyplot as plt

from torchviz import make_dot


class Net(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.fc1 = torch.nn.Linear(28*28, 64)
        self.fc2 = torch.nn.Linear(64, 64)
        self.fc3 = torch.nn.Linear(64, 64)
        self.fc4 = torch.nn.Linear(64, 10)

    def forward(self, x):
        """
        x   e.g
        tensor([[
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.2353, 0.5451, 0.9412, 1.0000, 0.6863, 0.1804, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.7412, 0.9961, 0.9961, 0.9961, 0.9961, 0.9529, 0.2588, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.2392, 0.8078, 0.9922, 0.9451, 0.4275, 0.1412, 0.8706, 0.9961, 0.5725,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.2392, 0.9412, 0.9961, 0.8510, 0.2588, 0.0000, 0.0000, 0.5882, 0.9961,
         0.9176, 0.0706, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0667, 0.7961, 0.9961, 0.9412, 0.2392, 0.0000, 0.0000, 0.0000, 0.2588,
         0.9961, 0.9961, 0.4549, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.4510, 0.9961, 0.9961, 0.4039, 0.0000, 0.0000, 0.0000, 0.0000,
         0.1216, 0.9961, 0.9961, 0.5882, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.5922, 0.9961, 0.6039, 0.0118, 0.0000, 0.0000, 0.0000,
         0.0000, 0.3059, 0.8471, 0.9961, 0.5882, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.8902, 0.9961, 0.4392, 0.0000, 0.0000, 0.0000,
         0.1725, 0.5255, 0.9725, 0.9961, 0.9961, 0.5882, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.7529, 0.9961, 0.7294, 0.2275, 0.1882,
         0.4196, 0.9725, 0.9961, 0.9961, 0.9961, 0.9961, 0.5882, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.4235, 0.9961, 0.9961, 0.9961,
         0.9961, 0.9961, 0.9961, 0.9137, 0.6157, 0.9961, 0.9961, 0.5882, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0431, 0.4000, 0.2431,
         0.8039, 0.8431, 0.6706, 0.3412, 0.0902, 0.2863, 0.9961, 0.9961, 0.3098,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.4588, 0.9961, 0.9961,
         0.2510, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.6118, 0.9961,
         0.8863, 0.0510, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.1412, 0.9529,
         0.9961, 0.5373, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0157, 0.5176,
         0.9961, 0.9216, 0.1373, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.2941,
         0.9961, 0.9961, 0.5529, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.6235, 0.9961, 0.9961, 0.5373, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.8275, 0.9961, 0.9490, 0.1373, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.8275, 0.9961, 0.8706, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.5961, 0.9961, 0.4275, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000,
         0.0000]])
         """
        """
        >>> self.fc1(x)
        tensor([[-0.2061, -0.0460, -0.1057, -0.1472, -0.3040, -0.3163, -0.0722,  0.2298,
          0.2842,  0.1700,  0.0497,  0.1675, -0.0818,  0.2143, -0.1343, -0.0022,
         -0.2398,  0.3886,  0.2906,  0.0093, -0.1121, -0.3072, -0.2354, -0.0600,
         -0.1236,  0.1955,  0.1362,  0.2903,  0.1226, -0.3445, -0.2875,  0.1446,
         -0.0047, -0.2096,  0.1232,  0.1187,  0.0778,  0.0297,  0.1449, -0.0888,
          0.0792,  0.0690,  0.2337, -0.3789,  0.0727,  0.1375, -0.0050,  0.0119,
          0.2231,  0.4218,  0.1564,  0.4467,  0.0152,  0.1361,  0.0457, -0.0295,
         -0.1431,  0.1231,  0.2504,  0.0062, -0.2557, -0.0679, -0.0647,  0.3651],
        [-0.3436, -0.0230,  0.0298, -0.2203, -0.1953, -0.1217,  0.1118,  0.0276,
          0.0941,  0.2168, -0.0400,  0.1763,  0.0422,  0.2430, -0.1195,  0.0141,
         -0.1443,  0.0906,  0.0217,  0.1013, -0.0102, -0.2826, -0.2403, -0.1431,
         -0.1441, -0.0652, -0.0337,  0.2383, -0.1876, -0.1643, -0.1917,  0.1347,
         -0.1009,  0.0645, -0.0755,  0.3012,  0.1910, -0.1299,  0.0130,  0.0225,
          0.0191,  0.1205,  0.1814, -0.1351, -0.0209, -0.0122, -0.0266,  0.0913,
          0.1031,  0.0232, -0.1450,  0.0640, -0.0458, -0.0065,  0.1558, -0.1002,
         -0.2586,  0.3925, -0.0999,  0.0498,  0.0958, -0.0821, -0.3779,  0.1724],
        [-0.0522,  0.0509, -0.1852, -0.4974, -0.1834,  0.0994,  0.2279,  0.0372,
          0.1312,  0.2166,  0.4227,  0.1612, -0.1016,  0.1084, -0.0136,  0.1641,
         -0.1401,  0.1360,  0.3253,  0.1373,  0.1736, -0.1770, -0.3215, -0.3366,
         -0.0751,  0.1324,  0.0759,  0.3407,  0.1020, -0.0212, -0.2191, -0.1317,
          0.0630,  0.0593, -0.3326,  0.2105, -0.0772, -0.0798,  0.4266, -0.5752,
         -0.4439,  0.0958,  0.2152, -0.0578, -0.1009, -0.1052,  0.2703,  0.1666,
          0.2538, -0.0917, -0.0610,  0.0625,  0.0466,  0.0067, -0.1236,  0.0808,
          0.1266,  0.3461,  0.0174,  0.1255,  0.0541, -0.1991, -0.2268,  0.1345],
        [-0.4478, -0.1640,  0.1156, -0.2719, -0.1579,  0.1928, -0.0420,  0.2893,
          0.3382,  0.1182,  0.2591,  0.4559, -0.2125,  0.0351, -0.1477,  0.2134,
         -0.3746,  0.5115,  0.5849, -0.0590, -0.1147,  0.0161, -0.3764, -0.1180,
         -0.1108,  0.0425,  0.2293,  0.2122, -0.0949, -0.1234, -0.2544,  0.0167,
          0.1203, -0.1136, -0.1270,  0.2536,  0.1725,  0.2695,  0.0448, -0.1559,
         -0.2131,  0.3040,  0.1716, -0.0667, -0.1994,  0.2415,  0.1835,  0.1012,
         -0.2159,  0.0192,  0.1931,  0.4516,  0.1780,  0.0319, -0.3031, -0.1368,
          0.0489, -0.2747,  0.0239,  0.2144, -0.0105,  0.1416,  0.0881,  0.1601],
        [-0.1384, -0.0632, -0.2408, -0.0518, -0.1097, -0.0192, -0.0668,  0.1013,
          0.2433,  0.2435, -0.1157,  0.1203, -0.1690,  0.0906,  0.0472,  0.1705,
         -0.0269,  0.1648,  0.1692, -0.2334,  0.0080,  0.2231, -0.1888, -0.1233,
         -0.1457,  0.0683,  0.0894,  0.1292, -0.0071, -0.1345, -0.1055,  0.1889,
         -0.0880,  0.1141, -0.0221,  0.1281,  0.0227,  0.1174,  0.1477, -0.0613,
          0.0512,  0.0829,  0.0869,  0.0360,  0.0697, -0.0510,  0.0778, -0.1523,
          0.0075,  0.1453,  0.0879,  0.0938,  0.0326,  0.0687,  0.0636,  0.2132,
         -0.1691, -0.0719,  0.1732,  0.1265,  0.1603, -0.0728,  0.0448,  0.0561],
        [-0.1113, -0.0939, -0.0753, -0.2481, -0.1558,  0.1132,  0.0435, -0.1619,
          0.0658,  0.4980,  0.2295, -0.1422, -0.2266,  0.1338,  0.1084,  0.0829,
          0.0360, -0.0826,  0.2198,  0.2786,  0.0861, -0.3111, -0.2623, -0.2472,
         -0.1901, -0.0653, -0.0622,  0.2150,  0.0080, -0.2149, -0.1582, -0.1446,
         -0.0269,  0.0662, -0.1243,  0.3332,  0.0787, -0.3049, -0.1145, -0.2111,
         -0.3857,  0.1522, -0.0482,  0.0338,  0.1482,  0.2596,  0.3481,  0.0473,
          0.2365,  0.0058, -0.1060, -0.4525,  0.2909,  0.1801,  0.0750, -0.0086,
         -0.1887,  0.1620,  0.1242, -0.0792,  0.0244,  0.0860, -0.0099,  0.1965],
        [-0.2058,  0.2006,  0.1568,  0.1253, -0.4191,  0.0219,  0.2742, -0.1154,
          0.3873,  0.1646,  0.1073, -0.1500, -0.2087,  0.4202, -0.2665, -0.0384,
         -0.1778,  0.3100,  0.0871,  0.2054, -0.0813, -0.0857, -0.3270, -0.0417,
         -0.2580,  0.1576, -0.0405,  0.0506, -0.0953, -0.2536, -0.0319, -0.0260,
          0.1891,  0.0646,  0.0113,  0.0665,  0.0109, -0.0889,  0.1150,  0.0311,
         -0.0500,  0.4574,  0.0088, -0.0526, -0.0604, -0.0948,  0.0863, -0.1355,
         -0.0322, -0.0955, -0.1555,  0.5484, -0.1306,  0.1251, -0.4121, -0.1044,
         -0.2670,  0.1253,  0.0077,  0.0091,  0.0123,  0.1239, -0.3694,  0.0320],
        [ 0.0924,  0.2541,  0.1870, -0.2086, -0.2972,  0.3988,  0.1741,  0.1674,
          0.2120,  0.3064,  0.1161,  0.5551, -0.1195,  0.0017, -0.0990, -0.1821,
         -0.2679,  0.1115,  0.2151,  0.0771, -0.0887, -0.0991, -0.5409, -0.1382,
         -0.3586,  0.0066, -0.1437,  0.4289,  0.0226,  0.1920, -0.3070, -0.1306,
         -0.1107,  0.0023, -0.2222,  0.5886,  0.3617,  0.0625,  0.1021, -0.2370,
         -0.5065,  0.3339,  0.3183, -0.1329, -0.0380,  0.3262,  0.4254,  0.1094,
          0.2077, -0.0262, -0.2327,  0.6472, -0.0404, -0.1024, -0.3716, -0.0911,
         -0.0330,  0.2489,  0.0427, -0.0102, -0.1212,  0.1153,  0.1828,  0.0067],
        [-0.3917, -0.0762, -0.1850, -0.0788,  0.0147, -0.1418,  0.1383,  0.0675,
          0.1761, -0.0021,  0.0774,  0.2563, -0.1603, -0.0091, -0.1199,  0.2541,
         -0.0884,  0.0756,  0.3116, -0.0550,  0.0955,  0.1425, -0.1398, -0.3406,
         -0.1698,  0.0171,  0.0876,  0.3171, -0.2151, -0.0681, -0.2451, -0.0745,
         -0.0684,  0.0279, -0.2121,  0.2572, -0.1016, -0.0654,  0.2389, -0.2114,
         -0.3339, -0.0095,  0.0500, -0.1692, -0.0179, -0.1239,  0.1773,  0.0654,
          0.0947, -0.0555,  0.1021, -0.0916,  0.0167,  0.0008,  0.0943, -0.1061,
         -0.2164,  0.3427,  0.0903, -0.0653,  0.1581, -0.2553, -0.3376,  0.3355],
        [-0.0701, -0.0942,  0.0281, -0.2525, -0.0655, -0.1802,  0.0884,  0.0538,
          0.2067,  0.1576,  0.0096,  0.0448,  0.0655,  0.0805, -0.0321, -0.0322,
         -0.0552,  0.1486,  0.1117,  0.1328, -0.0610, -0.2056, -0.2023,  0.0612,
         -0.0458,  0.0528, -0.0778,  0.1144, -0.0751, -0.2215, -0.0940,  0.2527,
         -0.0402, -0.1418,  0.0497,  0.2032,  0.1580, -0.0633,  0.3519,  0.0481,
          0.0980, -0.0771,  0.0937, -0.0288,  0.0708,  0.0275,  0.1804,  0.0505,
          0.0100,  0.0850,  0.1600,  0.1034,  0.1116,  0.0929,  0.0975, -0.0280,
         -0.1598,  0.0449,  0.0858, -0.1415, -0.0832, -0.1562, -0.1819,  0.2133],
        [-0.1718, -0.2371, -0.2125, -0.2439,  0.0429, -0.0330, -0.1440,  0.0119,
          0.0598,  0.0916,  0.0720, -0.0317, -0.1641,  0.3056, -0.0344, -0.0955,
          0.1979,  0.1597,  0.4274,  0.0379, -0.0878, -0.0696, -0.3576, -0.1732,
         -0.0645,  0.1154,  0.0657,  0.3871,  0.1679, -0.2466, -0.1904,  0.0601,
         -0.0483, -0.1578, -0.0124,  0.0666, -0.1029,  0.0090,  0.1711, -0.2197,
         -0.0588,  0.1515,  0.0931, -0.0788,  0.0897, -0.0443,  0.1838, -0.0940,
         -0.1931, -0.0337,  0.0453,  0.3416,  0.0974,  0.1438, -0.2181,  0.1705,
          0.0372, -0.0701,  0.1305, -0.0387,  0.0212, -0.0495, -0.1536,  0.1197],
        [-0.0744,  0.1482,  0.0460, -0.1443, -0.1417,  0.3079,  0.0302, -0.0957,
          0.2422,  0.3514,  0.1165,  0.4116, -0.0072,  0.1230, -0.0871,  0.0762,
         -0.4160,  0.1232,  0.1805,  0.2032, -0.2642,  0.0229, -0.3528, -0.1328,
         -0.0341,  0.1414, -0.1248,  0.2611, -0.2538,  0.0722, -0.2846,  0.0809,
         -0.0764,  0.0322, -0.2345,  0.5872,  0.1894, -0.1481,  0.1018, -0.1939,
         -0.4256,  0.2234,  0.2091, -0.0093, -0.0535,  0.1184,  0.4564,  0.0400,
         -0.0332,  0.1815, -0.1769,  0.0947,  0.1313, -0.1098, -0.2138, -0.2045,
          0.2423,  0.2324, -0.4940,  0.1949,  0.0606, -0.2332, -0.0107, -0.1038],
        [-0.1562, -0.0818, -0.1736, -0.2550, -0.2241, -0.0719,  0.0860,  0.1359,
          0.2581,  0.2624, -0.1365,  0.0558,  0.1230,  0.1717, -0.0668,  0.0379,
         -0.0656,  0.1361,  0.2365,  0.0637,  0.1202,  0.0411, -0.4143, -0.1575,
         -0.0550,  0.1061, -0.0079,  0.3260, -0.2038, -0.1466, -0.1023,  0.2575,
         -0.1238,  0.0360,  0.0076,  0.1476, -0.0266, -0.0238,  0.2524, -0.0881,
          0.0529, -0.0131,  0.2050, -0.0980,  0.1845,  0.0829,  0.2592, -0.1377,
         -0.1035,  0.0801,  0.1220,  0.2899,  0.0504,  0.1509, -0.0688, -0.0788,
         -0.0360,  0.1066,  0.0092, -0.1072,  0.1010, -0.3332, -0.0826,  0.0886],
        [-0.4896,  0.2280, -0.1531, -0.3615, -0.1993, -0.0062, -0.1195, -0.1159,
          0.1564,  0.4962,  0.0699,  0.1488, -0.1435,  0.1899, -0.2057,  0.1050,
         -0.1055,  0.3438,  0.3788,  0.2953, -0.0027, -0.2482, -0.3919, -0.2273,
          0.0673,  0.0857, -0.0918,  0.3409, -0.2993, -0.3808, -0.3787,  0.0456,
          0.0182, -0.3052, -0.4104,  0.6907,  0.4837, -0.2774,  0.1928, -0.1884,
         -0.3703,  0.5611,  0.1731, -0.0786, -0.0636,  0.0956,  0.1446, -0.0226,
          0.2450,  0.0402, -0.3338,  0.0726,  0.0977,  0.0595,  0.0195, -0.0803,
         -0.2087,  0.4867, -0.2699,  0.3087, -0.1770,  0.1310,  0.0387,  0.1423],
        [-0.3868, -0.0135, -0.1957, -0.0426, -0.2244,  0.1620, -0.0250,  0.1989,
          0.3643,  0.3048,  0.0419,  0.2704, -0.1387,  0.1529, -0.1763,  0.1619,
         -0.2122,  0.3476,  0.3208, -0.2048,  0.0831, -0.0487, -0.2492, -0.1296,
          0.0504, -0.0539,  0.2955,  0.0103, -0.0527, -0.1394, -0.2235,  0.2376,
          0.0924, -0.0321, -0.0844,  0.2692,  0.1447,  0.1501,  0.4973, -0.1628,
         -0.2218,  0.4956,  0.1350,  0.0406,  0.0393, -0.1275,  0.2750,  0.0011,
         -0.1080, -0.1170,  0.0914,  0.4602,  0.1913,  0.1136, -0.1234,  0.0117,
         -0.4577, -0.0981, -0.0015,  0.1655,  0.1291,  0.1565,  0.1499,  0.2153]])
        """
        x = torch.nn.functional.relu(self.fc1(x))
        x = torch.nn.functional.relu(self.fc2(x))
        x = torch.nn.functional.relu(self.fc3(x))
        x = torch.nn.functional.log_softmax(self.fc4(x), dim=1)
        """
        >>> x
        tensor([[-2.2051, -2.2747, -2.3922, -2.3257, -2.3268, -2.2008, -2.3640, -2.3096,
         -2.4503, -2.2086],
        [-2.1786, -2.2598, -2.4039, -2.3424, -2.3442, -2.2051, -2.3815, -2.2944,
         -2.4424, -2.2106],
        [-2.1985, -2.2638, -2.3618, -2.3417, -2.3445, -2.2091, -2.3612, -2.3061,
         -2.4488, -2.2200],
        [-2.1976, -2.2673, -2.3871, -2.3324, -2.3276, -2.2092, -2.3758, -2.2931,
         -2.4453, -2.2212],
        [-2.1990, -2.2737, -2.3758, -2.3271, -2.3482, -2.1962, -2.3704, -2.3127,
         -2.4385, -2.2151],
        [-2.1982, -2.2644, -2.3671, -2.3384, -2.3435, -2.2009, -2.3666, -2.3038,
         -2.4582, -2.2172],
        [-2.2023, -2.2680, -2.3837, -2.3189, -2.3385, -2.2024, -2.3724, -2.3061,
         -2.4391, -2.2239],
        [-2.1999, -2.2659, -2.3639, -2.3261, -2.3474, -2.2071, -2.3644, -2.3160,
         -2.4383, -2.2248],
        [-2.1907, -2.2583, -2.4030, -2.3273, -2.3503, -2.1957, -2.3673, -2.3119,
         -2.4420, -2.2143],
        [-2.1852, -2.2668, -2.3846, -2.3411, -2.3483, -2.2027, -2.3507, -2.3090,
         -2.4478, -2.2222],
        [-2.2085, -2.2635, -2.3737, -2.3146, -2.3445, -2.1990, -2.3622, -2.3205,
         -2.4396, -2.2277],
        [-2.1878, -2.2628, -2.3857, -2.3400, -2.3523, -2.2049, -2.3483, -2.3195,
         -2.4434, -2.2137],
        [-2.1963, -2.2739, -2.3830, -2.3199, -2.3370, -2.1994, -2.3615, -2.3136,
         -2.4463, -2.2253],
        [-2.1857, -2.2546, -2.4092, -2.3428, -2.3470, -2.1913, -2.3660, -2.3016,
         -2.4419, -2.2224],
        [-2.1839, -2.2634, -2.4078, -2.3549, -2.3459, -2.2054, -2.3529, -2.3025,
         -2.4407, -2.2045]])
        """
        return x


def get_data_loader(is_train):
    to_tensor = transforms.Compose([transforms.ToTensor()])
    data_set = MNIST("", is_train, transform=to_tensor, download=True)
    return DataLoader(data_set, batch_size=15, shuffle=True)


def evaluate(test_data, net):
    n_correct = 0
    n_total = 0
    with torch.no_grad():
        for (x, y) in test_data:
            # 变量x e.g
            # tensor([[[[0., 0., 0.,  ..., 0., 0., 0.],
            #           [0., 0., 0.,  ..., 0., 0., 0.],
            #           [0., 0., 0.,  ..., 0., 0., 0.],
            #           ...,
            #           [0., 0., 0.,  ..., 0., 0., 0.],
            #           [0., 0., 0.,  ..., 0., 0., 0.],
            #           [0., 0., 0.,  ..., 0., 0., 0.]]],
            #         [[[0., 0., 0.,  ..., 0., 0., 0.],
            #           [0., 0., 0.,  ..., 0., 0., 0.],
            #           [0., 0., 0.,  ..., 0., 0., 0.],
            #           ...,
            #           [0., 0., 0.,  ..., 0., 0., 0.],
            #           [0., 0., 0.,  ..., 0., 0., 0.],
            #           [0., 0., 0.,  ..., 0., 0., 0.]]],
            #         [[[0., 0., 0.,  ..., 0., 0., 0.],
            #           [0., 0., 0.,  ..., 0., 0., 0.],
            #           [0., 0., 0.,  ..., 0., 0., 0.],
            #           ...,
            #           [0., 0., 0.,  ..., 0., 0., 0.],
            #           [0., 0., 0.,  ..., 0., 0., 0.],
            #           [0., 0., 0.,  ..., 0., 0., 0.]]],
            #         ...,
            #         [[[0., 0., 0.,  ..., 0., 0., 0.],
            #           [0., 0., 0.,  ..., 0., 0., 0.],
            #           [0., 0., 0.,  ..., 0., 0., 0.],
            #           ...,
            #           [0., 0., 0.,  ..., 0., 0., 0.],
            #           [0., 0., 0.,  ..., 0., 0., 0.],
            #           [0., 0., 0.,  ..., 0., 0., 0.]]],
            #         [[[0., 0., 0.,  ..., 0., 0., 0.],
            #           [0., 0., 0.,  ..., 0., 0., 0.],
            #           [0., 0., 0.,  ..., 0., 0., 0.],
            #           ...,
            #           [0., 0., 0.,  ..., 0., 0., 0.],
            #           [0., 0., 0.,  ..., 0., 0., 0.],
            #           [0., 0., 0.,  ..., 0., 0., 0.]]],
            #         [[[0., 0., 0.,  ..., 0., 0., 0.],
            #           [0., 0., 0.,  ..., 0., 0., 0.],
            #           [0., 0., 0.,  ..., 0., 0., 0.],
            #           ...,
            #           [0., 0., 0.,  ..., 0., 0., 0.],
            #           [0., 0., 0.,  ..., 0., 0., 0.],
            #           [0., 0., 0.,  ..., 0., 0., 0.]]]])
            # ---------------------------------------------------
            # y  e.g  tensor([1, 9, 4, 7, 9, 2, 4, 0, 7, 4])
            outputs = net.forward(x.view(-1, 28*28))
            for i, output in enumerate(outputs):
                if torch.argmax(output) == y[i]:
                    n_correct += 1
                n_total += 1
    return n_correct / n_total


def main():

    train_data = get_data_loader(is_train=True)
    test_data = get_data_loader(is_train=False)

    # print('-----------test_data')
    # print(test_data)
    # raise

    net = Net()
    
    # make_dot(net)

    print("initial accuracy:", evaluate(test_data, net))
    optimizer = torch.optim.Adam(net.parameters(), lr=0.001)
    for epoch in range(2):
        # y: tensor([4, 2, 9, 8, 6, 3, 2, 0, 1, 7, 9, 3, 0, 3, 5])
        for (x, y) in train_data:
            net.zero_grad()
            """
            >>> output (每个list的元素个数是10)， 共15个list，与y的元素个数一致
            tensor([[-2.3984, -2.2332, -2.2603, -2.4097, -2.3305, -2.2679, -2.2419, -2.3996,
                    -2.3026, -2.2073],
                    [-2.4098, -2.2122, -2.2668, -2.4253, -2.3268, -2.2653, -2.2445, -2.4127,
                    -2.2913, -2.2026],
                    [-2.4042, -2.2297, -2.2643, -2.4147, -2.3330, -2.2677, -2.2346, -2.4091,
                    -2.2989, -2.1987],
                    [-2.4222, -2.2221, -2.2621, -2.4223, -2.3219, -2.2638, -2.2404, -2.3943,
                    -2.3136, -2.1942],
                    [-2.3992, -2.2371, -2.2184, -2.4399, -2.3167, -2.2499, -2.2481, -2.4242,
                    -2.3010, -2.2240],
                    [-2.4067, -2.2245, -2.2583, -2.4230, -2.3301, -2.2776, -2.2429, -2.3994,
                    -2.2887, -2.2032],
                    [-2.4011, -2.2387, -2.2370, -2.4253, -2.3183, -2.2690, -2.2554, -2.4158,
                    -2.2944, -2.2006],
                    [-2.4090, -2.2310, -2.2531, -2.4199, -2.3328, -2.2592, -2.2402, -2.4102,
                    -2.2965, -2.2038],
                    [-2.3969, -2.2319, -2.2374, -2.4356, -2.3308, -2.2514, -2.2566, -2.4151,
                    -2.2925, -2.2086],
                    [-2.4039, -2.2177, -2.2608, -2.4210, -2.3263, -2.2636, -2.2493, -2.3997,
                    -2.3034, -2.2081],
                    [-2.4165, -2.2164, -2.2498, -2.4284, -2.3246, -2.2618, -2.2337, -2.3998,
                    -2.3032, -2.2222],
                    [-2.4137, -2.2368, -2.2536, -2.4184, -2.3101, -2.2635, -2.2421, -2.4028,
                    -2.3038, -2.2089],
                    [-2.4190, -2.2094, -2.2649, -2.4247, -2.3343, -2.2621, -2.2245, -2.4050,
                    -2.2893, -2.2243],
                    [-2.4047, -2.2260, -2.2626, -2.4167, -2.3319, -2.2753, -2.2444, -2.3985,
                    -2.2899, -2.2031],
                    [-2.4017, -2.2213, -2.2658, -2.4138, -2.3220, -2.2771, -2.2384, -2.3884,
                    -2.3078, -2.2144]], grad_fn=<LogSoftmaxBackward0>)
            """
            output = net.forward(x.view(-1, 28*28))
            # loss: tensor(2.2861, grad_fn=<NllLossBackward0>)
            loss = torch.nn.functional.nll_loss(output, y)
            # print('-------------output')
            # print(output)
            # raise
            loss.backward()
            optimizer.step()
        print("epoch", epoch, "accuracy:", evaluate(test_data, net))

    for (n, (x, _)) in enumerate(test_data):
        if n > 3:
            break
        predict = torch.argmax(net.forward(x[0].view(-1, 28*28)))
        plt.figure(n)
        plt.imshow(x[0].view(28, 28))
        plt.title("prediction: " + str(int(predict)))
    plt.show()


if __name__ == "__main__":
    main()
