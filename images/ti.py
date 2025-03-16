from ase.units import kJ
from ase.eos import EquationOfState
import matplotlib.pyplot as plt
import numpy as np

# Define volumes and energies for different configurations
bcc_volumes = [1006.01, 860.09, 988.05, 979.15, 893.06, 952.76, 884.74, 868.25, 961.5, 970.3, 997.0, 1015.08, 901.43, 843.91, 926.86, 876.47, 909.85, 918.33, 935.44, 944.08, 851.97]
bcc_energies = [-307.87308566, -309.82922987, -308.85658472, -309.28464946, -310.79509373, -310.27814747, -310.64423005, -310.16268781, -309.99356211, -309.66258648, -308.38646777, -307.31796998, -310.88720266, -308.97022558, -310.82460381, -310.43397931, -310.91892391, -310.89903706, -310.69605466, -310.51361938, -309.43227473]

fcc_volumes = [1780.36, 2000.38, 2014.7, 1860.87, 1767.17, 1847.28, 1902.01, 1740.99, 1874.52, 1915.86, 1833.77, 1986.12, 1929.78, 1971.94, 1754.05, 1793.61, 1957.82, 1820.32, 1806.93, 1888.23, 1943.76]
fcc_energies = [-625.90813885, -622.03002213, -621.25914395, -626.45404935, -625.55800685, -626.54445343, -625.79110779, -624.6149366, -626.2965855, -625.43826403, -626.56288886, -622.74757845, -625.01955122, -623.40928581, -625.12577803, -626.18308258, -624.00684323, -626.51039508, -626.38421231, -626.07479527, -624.54272264]

hcp_volumes = [855.9, 904.44, 921.01, 888.06, 937.79, 1006.95, 879.94, 929.38, 971.96, 1015.82, 896.22, 963.34, 980.63, 946.26, 863.86, 998.12, 871.88, 989.35, 954.77, 912.7, 1024.75]
hcp_energies = [-314.41436498, -316.12620552, -316.21320288, -315.80538886, -316.0777187, -313.52792991, -315.55371217, -316.17260191, -315.18369041, -313.00402338, -315.99577107, -315.48186956, -314.83801936, -315.93008086, -314.85973002, -314.00917246, -315.23908989, -314.44611009, -315.73108764, -316.19831152, -312.43834782]

def process_eos(volumes, energies, filename):
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    eos.plot(show=False)
    plt.savefig(f'{filename}.png')
    plt.close()
    cube_root_v0 = (v0 ** (1/3))/3
    return v0, e0, cube_root_v0

bcc_v0, bcc_e0, bcc_cube_root_v0 = process_eos(bcc_volumes, bcc_energies, 'bcc_eos_plot')
fcc_v0, fcc_e0, fcc_cube_root_v0 = process_eos(fcc_volumes, fcc_energies, 'fcc_eos_plot')
hcp_v0, hcp_e0, hcp_cube_root_v0 = process_eos(hcp_volumes, hcp_energies, 'hcp_eos_plot')

print('BCC Cube Root Volume:', bcc_cube_root_v0)
print('FCC Cube Root Volume:', fcc_cube_root_v0)
print('HCP Cube Root Volume:', hcp_cube_root_v0)
