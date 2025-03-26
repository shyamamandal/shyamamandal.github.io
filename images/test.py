from ase.units import kJ
from ase.eos import EquationOfState
import matplotlib.pyplot as plt
import numpy as np

# Define volumes and energies for different configurations
bcc_volumes = [658.5, 580.09, 567.66, 543.34, 611.96, 592.7, 573.86, 631.63, 644.97, 555.41, 561.52, 638.28, 618.47, 605.5, 651.71, 625.03, 549.35, 586.38, 537.37, 531.44, 599.08]
bcc_energies = [-199.06868513, -205.86469099, -205.87781678, -204.69213999, -204.29499322, -205.48499441, -205.91998087, -202.4393614, -200.87294934, -205.49886496, -205.73960895, -201.68718979, -203.74630557, -204.76973451, -199.99930584, -203.1267437, -205.15094592, -205.71849616, -204.11799022, -203.42310769, -205.16746621]

fcc_volumes = [1177.58, 1157.62, 1118.39, 1259.71, 1207.95, 1228.48, 1249.24, 1147.73, 1218.19, 1187.65, 1167.58, 1197.77, 1137.89, 1270.24, 1108.72, 1089.55, 1238.83, 1080.05, 1099.1, 1128.11, 1070.6]
fcc_energies = [-434.65547213, -435.74138592, -436.53504743, -426.38075635, -432.24830893, -430.16350886, -427.72508061, -436.11769328, -431.25178435, -433.95344958, -435.25263811, -433.15002941, -436.37814103, -424.95698968, -436.42336784, -435.7990902, -428.98699993, -435.27754723, -436.17951537, -436.51863916, -434.61025896]

hcp_volumes = [523.39, 553.08, 563.21, 543.06, 573.47, 615.76, 538.1, 568.33, 594.37, 621.19, 548.05, 589.1, 599.67, 578.65, 528.27, 610.37, 533.17, 605.0, 583.86, 558.13, 626.65]
hcp_energies = [-214.89748137, -217.08074852, -217.19444224, -216.67409602, -217.03325536, -214.00074971, -216.35444689, -217.14696514, -215.96251648, -213.38544363, -216.91543538, -216.31883385, -215.55062746, -216.85575588, -215.46892049, -214.56789599, -215.95373194, -215.08511304, -216.61670547, -217.17308754, -212.72427003]

def process_eos(volumes, energies, filename):
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    eos.plot(show=False)
    plt.savefig(f'{filename}.png')
    plt.close()
    cube_root_v0 = (v0 ** (1/3))/3
    return v0, e0, cube_root_v0

bcc_v0, bcc_e0, bcc_cube_root_v0 = process_eos(bcc_volumes, bcc_energies, 'co_bcc_eos_plot')
fcc_v0, fcc_e0, fcc_cube_root_v0 = process_eos(fcc_volumes, fcc_energies, 'co_fcc_eos_plot')
hcp_v0, hcp_e0, hcp_cube_root_v0 = process_eos(hcp_volumes, hcp_energies, 'co_hcp_eos_plot')

print('BCC Cube Root Volume:', bcc_cube_root_v0)
print('FCC Cube Root Volume:', fcc_cube_root_v0)
print('HCP Cube Root Volume:', hcp_cube_root_v0)
