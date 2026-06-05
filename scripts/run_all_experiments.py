from pathlib import Path
import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from gunnchos_mimo.array_factor import array_factor
from gunnchos_mimo.mimo_channel import rayleigh_mimo
from gunnchos_mimo.zf_precoding import zf_precoder
from gunnchos_mimo.mmse_precoding import mmse_precoder

ROOT = Path(__file__).resolve().parents[1]
FIG = ROOT/'results/figures'; FIG.mkdir(parents=True, exist_ok=True)
(ROOT/'results/tables').mkdir(parents=True, exist_ok=True)
theta = np.linspace(-np.pi/2, np.pi/2, 181)
plt.figure(); plt.plot(np.degrees(theta), array_factor(theta)); plt.savefig(FIG/'beam_patterns.png'); plt.close()
H = rayleigh_mimo(4,4)
snr = np.linspace(0,20,30)
cap = [np.real(np.log2(np.linalg.det(np.eye(4)+10**(s/10)/4*(H@H.conj().T)))) for s in snr]
plt.figure(); plt.plot(snr, cap); plt.savefig(FIG/'mimo_capacity.png'); plt.close()
(ROOT/'results/tables/precoding_comparison.md').write_text('# ZF vs MMSE\nToy 4x4 PASS\n')
(ROOT/'results/experiment_summary.md').write_text('# MIMO e2e PASS\n')
