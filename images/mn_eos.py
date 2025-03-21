from ase.units import kJ
from ase.eos import EquationOfState
import matplotlib.pyplot as plt
import numpy as np

# Define volumes and energies for different configurations
bcc_volumes = [580.09, 567.66, 543.34, 611.96, 525.56, 592.7, 573.86, 631.63, 644.97, 555.41, 561.52, 638.28, 618.47, 605.5, 651.71, 625.03, 549.35, 586.38, 537.37, 531.44, 599.08]
bcc_energies = [-338.14387051, -337.84215276, -335.69012084, -336.94178607, -332.57030897, -337.98240879, -338.05239485, -335.03785671, -333.33728056, -337.03665703, -337.5051132, -334.22825489, -336.39845029, -337.38943537, -332.36764633, -335.76235598, -336.43290477, -338.11905145, -334.80386502, -333.76630841, -337.73752528]

fcc_volumes = [1167.58, 1070.6, 1033.36, 1051.87, 1099.1, 1089.55, 1042.59, 1207.95, 1128.11, 1228.48, 1137.89, 1177.58, 1118.39, 1157.62, 1147.73, 1108.72, 1187.65, 1218.19, 1061.21, 1080.05, 1197.77]
fcc_energies = [-683.97374264, -677.1494034, -669.35640013, -673.65759043, -680.96700389, -679.87646676, -671.61091901, -682.45960848, -683.20876502, -680.92936652, -683.62909126, -683.79814603, -682.6279654, -684.00708965, -683.89348294, -681.88257999, -683.48445703, -681.75573894, -675.50159522, -678.60567703, -683.03700472]

hcp_volumes = [528.95, 558.95, 569.2, 548.83, 579.57, 622.3, 543.81, 574.37, 600.68, 627.79, 553.87, 595.36, 606.04, 584.8, 533.88, 616.85, 538.83, 611.43, 590.06, 564.06, 633.31]
hcp_energies = [-339.33701537, -342.97468272, -343.43408231, -342.15390681, -343.55371691, -341.02994433, -341.60039025, -343.53504843, -342.85285995, -340.41473585, -342.61100814, -343.13848777, -342.49692524, -343.49197339, -340.19457817, -341.58339573, -340.94801564, -342.07312253, -343.3518247, -343.24841254, -339.73980688]

def process_eos(volumes, energies, filename):
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    eos.plot(show=False)
    plt.savefig(f'{filename}.png')
    plt.close()
    cube_root_v0 = (v0 ** (1/3))/3
    return v0, e0, cube_root_v0

bcc_v0, bcc_e0, bcc_cube_root_v0 = process_eos(bcc_volumes, bcc_energies, 'mn_bcc_eos_plot')
fcc_v0, fcc_e0, fcc_cube_root_v0 = process_eos(fcc_volumes, fcc_energies, 'mn_fcc_eos_plot')
hcp_v0, hcp_e0, hcp_cube_root_v0 = process_eos(hcp_volumes, hcp_energies, 'mn_hcp_eos_plot')

print('BCC Cube Root Volume:', bcc_cube_root_v0)
print('FCC Cube Root Volume:', fcc_cube_root_v0)
print('HCP Cube Root Volume:', hcp_cube_root_v0)
