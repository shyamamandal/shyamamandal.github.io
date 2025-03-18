from ase.units import kJ
from ase.eos import EquationOfState
import matplotlib.pyplot as plt
import numpy as np

# Define volumes and energies for different configurations
bcc_volumes = [658.5, 766.06, 707.35, 743.68, 665.34, 721.73, 788.89, 672.22, 644.97, 751.09, 736.31, 773.62, 729.0, 651.71, 714.52, 693.15, 686.13, 781.23, 679.15, 758.55, 700.23]
bcc_energies = [-354.83567573, -355.55986588, -357.54658524, -356.87431111, -355.51205676, -357.51830432, -353.63303728, -356.08662228, -353.16123821, -356.50777938, -357.16635847, -354.98277489, -357.38175289, -354.05336692, -357.57393662, -357.23411916, -356.94473953, -354.33987133, -356.56309119, -356.06894267, -357.43408271]

fcc_volumes = [1481.54, 1356.57, 1435.25, 1458.27, 1577.1, 1528.82, 1401.17, 1378.75, 1412.47, 1589.32, 1367.63, 1540.8, 1493.27, 1564.94, 1469.88, 1389.93, 1446.73, 1552.84, 1516.91, 1423.83, 1505.06]
fcc_energies = [-687.67242611, -681.67390086, -687.07991275, -687.58772683, -684.12975962, -686.64075684, -685.47930042, -683.8258386, -686.12759552, -683.28611247, -682.81401494, -686.14680497, -687.56109513, -684.88926369, -687.68195163, -684.71305383, -687.38783299, -685.56276451, -687.0430168, -686.6604207, -687.35055966]

hcp_volumes = [680.92, 719.54, 732.73, 706.51, 746.08, 801.09, 700.05, 739.38, 773.26, 808.15, 713.0, 766.4, 780.16, 752.81, 687.26, 794.07, 693.64, 787.09, 759.59, 726.11, 815.26]
hcp_energies = [-341.36531755, -343.57349231, -343.73502235, -343.13470485, -343.63410067, -340.85668203, -342.80684047, -343.71662252, -342.69539403, -340.26757986, -343.38961736, -343.01830987, -342.3162794, -343.48916597, -341.92416468, -341.39536957, -342.40394598, -341.88244704, -343.28340617, -343.68807459, -339.6294896]

def process_eos(volumes, energies, filename):
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0, e0, B = eos.fit()
    eos.plot(show=False)
    plt.savefig(f'{filename}.png')
    plt.close()
    cube_root_v0 = (v0 ** (1/3))/3
    return v0, e0, cube_root_v0

bcc_v0, bcc_e0, bcc_cube_root_v0 = process_eos(bcc_volumes, bcc_energies, 'v_bcc_eos_plot')
fcc_v0, fcc_e0, fcc_cube_root_v0 = process_eos(fcc_volumes, fcc_energies, 'v_fcc_eos_plot')
hcp_v0, hcp_e0, hcp_cube_root_v0 = process_eos(hcp_volumes, hcp_energies, 'v_hcp_eos_plot')

print('BCC Cube Root Volume:', bcc_cube_root_v0)
print('FCC Cube Root Volume:', fcc_cube_root_v0)
print('HCP Cube Root Volume:', hcp_cube_root_v0)
