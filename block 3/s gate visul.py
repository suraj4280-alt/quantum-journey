
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(14, 6))

# ============================================
# LEFT PANEL: Bloch Sphere (3D) - Where the STATE lives
# ============================================
ax1 = fig.add_subplot(121, projection='3d')

# Draw sphere wireframe
u = np.linspace(0, 2 * np.pi, 40)
v = np.linspace(0, np.pi, 40)
x = np.outer(np.cos(u), np.sin(v))
y = np.outer(np.sin(u), np.sin(v))
z = np.outer(np.ones(np.size(u)), np.cos(v))
ax1.plot_surface(x, y, z, alpha=0.08, color='#3498db', rstride=2, cstride=2)

# Axes
ax1.plot([0, 1.3], [0, 0], [0, 0], 'k-', lw=1.5, alpha=0.4)
ax1.plot([0, 0], [0, 1.3], [0, 0], 'k-', lw=1.5, alpha=0.4)
ax1.plot([0, 0], [0, 0], [0, 1.3], 'k-', lw=1.5, alpha=0.4)
ax1.text(1.35, 0, 0, 'X', fontsize=11, color='#1a3a5c')
ax1.text(0, 1.35, 0, 'Y', fontsize=11, color='#1a3a5c')
ax1.text(0, 0, 1.35, 'Z', fontsize=11, color='#1a3a5c')

# Equator
theta = np.linspace(0, 2*np.pi, 100)
ax1.plot(np.cos(theta), np.sin(theta), np.zeros_like(theta), '--', color='#d0d8e0', lw=1.5, alpha=0.6)

# |0⟩ at North Pole
ax1.plot([0], [0], [1], 'o', markersize=14, color='#2ecc71', zorder=5)
ax1.text(0.1, 0.1, 1.1, '|0⟩', fontsize=13, fontweight='bold', color='#2ecc71')

# |1⟩ at South Pole - BEFORE and AFTER are the SAME point!
ax1.plot([0], [0], [-1], 'o', markersize=18, color='#ff006e', zorder=5)
ax1.text(0.15, 0.15, -1.15, '|1⟩', fontsize=14, fontweight='bold', color='#ff006e')

# State vector arrow from origin to South Pole
ax1.quiver(0, 0, 0, 0, 0, -1, length=1.0, normalize=True, color='#ff006e', 
           arrow_length_ratio=0.15, linewidth=4)

ax1.set_title('Bloch Sphere (3D)\nWhere the QUANTUM STATE lives', fontsize=14, fontweight='bold', color='#1a3a5c', pad=20)
ax1.set_xlim([-1.2, 1.2])
ax1.set_ylim([-1.2, 1.2])
ax1.set_zlim([-1.2, 1.2])
ax1.view_init(elev=20, azim=45)
ax1.set_box_aspect([1,1,1])

# Annotation
ax1.text2D(0.5, 0.02, 'For |1⟩, S gate does NOT move the state!\nIt stays at the South Pole (global phase).', 
           transform=ax1.transAxes, fontsize=11, ha='center', color='#888', style='italic')


# ============================================
# RIGHT PANEL: Complex Plane (2D) - Where the AMPLITUDE lives
# ============================================
ax2 = fig.add_subplot(122)
ax2.set_xlim(-1.3, 1.3)
ax2.set_ylim(-1.3, 1.3)
ax2.set_aspect('equal')
ax2.set_title('Complex Plane (2D)\nWhere the AMPLITUDE of |1⟩ lives', fontsize=14, fontweight='bold', color='#1a3a5c', pad=15)

# Axes
ax2.annotate('', xy=(1.2, 0), xytext=(-1.2, 0), arrowprops=dict(arrowstyle='->', color='#1a3a5c', lw=2))
ax2.annotate('', xy=(0, 1.2), xytext=(0, -1.2), arrowprops=dict(arrowstyle='->', color='#1a3a5c', lw=2))
ax2.text(1.25, 0.05, 'Real', fontsize=11, color='#1a3a5c', va='center')
ax2.text(0.05, 1.25, 'Imaginary', fontsize=11, color='#1a3a5c', ha='center')

# Unit circle
circle = plt.Circle((0, 0), 1.0, fill=False, color='#e8ecf0', linewidth=2)
ax2.add_patch(circle)

# BEFORE: amplitude = 1 (points RIGHT)
ax2.annotate('', xy=(1, 0), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color='#ff006e', lw=4, alpha=0.4))
ax2.plot(1, 0, 'o', markersize=12, color='#ff006e', alpha=0.4, zorder=5)
ax2.text(1.15, 0.12, '1  (before)', fontsize=12, color='#ff006e', alpha=0.6, fontweight='bold')

# AFTER: amplitude = i (points UP)
ax2.annotate('', xy=(0, 1), xytext=(0, 0), arrowprops=dict(arrowstyle='->', color='#ffd700', lw=5))
ax2.plot(0, 1, 'o', markersize=16, color='#ffd700', zorder=5)
ax2.text(0.2, 1.15, 'i  (after S)', fontsize=14, color='#b8860b', fontweight='bold',
         bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='#ffd700', linewidth=2))

# Rotation arc
arc = patches.Arc((0, 0), 0.7, 0.7, angle=0, theta1=0, theta2=90, color='#ffd700', lw=3, ls='--')
ax2.add_patch(arc)
ax2.text(0.35, 0.35, '90°', fontsize=12, color='#ffd700', ha='center', fontweight='bold')

# Labels
ax2.text(0, -0.55, 'Phase = 0°', fontsize=12, color='#ff006e', ha='center', fontweight='bold', alpha=0.6)
ax2.text(0.45, 0.5, 'Phase = 90°', fontsize=12, color='#b8860b', ha='center', fontweight='bold')

# Info box
ax2.text(0, -1.15, 'Amplitude of |1⟩ component:\nBEFORE: 1 + 0i    →    AFTER: 0 + 1i', 
         fontsize=12, color='#1a3a5c', ha='center',
         bbox=dict(boxstyle='round,pad=0.4', facecolor='#fff8e6', edgecolor='#ffd700', linewidth=2))

ax2.axis('off')

plt.suptitle('Two Different Spaces! The State vs Its Amplitude', 
             fontsize=18, fontweight='bold', color='#1a3a5c', y=1.02)
plt.tight_layout()
plt.savefig('/mnt/agents/output/state_vs_amplitude_3d.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.show()
