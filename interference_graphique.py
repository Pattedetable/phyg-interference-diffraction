#
# Copyright 2018 Manuel Barrette
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import numpy as np
import matplotlib.pyplot as plt


def Inter(N, d, l, t):
    """
    Intensity of light going through a series of slits due to the interference
    """
    return np.sin(N*np.pi*d*np.sin(np.arctan(t))*1000000/l)**2/(np.sin(np.pi*d*np.sin(np.arctan(t))*1000000/l)**2)


def Diff(a, l, t):
    """
    Intensity of light going through a series of slits due to the diffraction
    """
    return np.sin(np.pi*a*np.sin(np.arctan(t))*1000000/l)**2/((np.pi*a*np.sin(np.arctan(t))*1000000/l)**2)



def Intensite(N, a, l, d, enveloppe):
    """
    Compute the total intensity due to both the inteference and the diffraction of light going through slits
    """

    nom = "graphique.png"
#    def Inter(N, d, l, t):
#        return np.sin(N*np.pi*d*np.sin(t)*1000000/l)**2/(np.sin(np.pi*d*np.sin(t)*1000000/l)**2)
#
#    def Diff(a, l, t):
#        return np.sin(np.pi*a*np.sin(t)*1000000/l)**2/((np.pi*a*np.sin(t)*1000000/l)**2)

    t = np.linspace(-0.03, 0.03, 5000)

    plt.axis([-0.03, 0.03, 0, Inter(N, d ,l , 0.00000001)+0.5])
    plt.grid(False)

#    plt.xlabel('$θ$ (rad)')
    plt.xlabel('$y$ (m)')
    plt.ylabel('$I/I_0$')

    if enveloppe == True:
        plt.plot(t, Diff(a, l, t) * Inter(N, d, l, 0.00000001), 'b')

    plt.plot(t, Diff(a, l, t)*Inter(N, d, l, t), 'k')

    plt.savefig(nom)

    plt.close()

    return nom
