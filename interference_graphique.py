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
from matplotlib.colors import LinearSegmentedColormap


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



def Intensite(N, a, l, d, enveloppe, points):
    """
    Compute the total intensity due to both the inteference and the diffraction of light going through slits
    """

    nom = "graphique.png"
    figure, (ax1) = plt.subplots(1)

    if points == 1:
    #    def Inter(N, d, l, t):
    #        return np.sin(N*np.pi*d*np.sin(t)*1000000/l)**2/(np.sin(np.pi*d*np.sin(t)*1000000/l)**2)
    #
    #    def Diff(a, l, t):
    #        return np.sin(np.pi*a*np.sin(t)*1000000/l)**2/((np.pi*a*np.sin(t)*1000000/l)**2)

        t = np.linspace(-0.03, 0.03, 5000)

        ax1.axis([-0.03, 0.03, 0, Inter(N, d, l, 0.00000001) + 0.5])
        ax1.grid(False)

    #    plt.xlabel('$θ$ (rad)')
        ax1.set_xlabel('$y$ (m)')
        ax1.set_ylabel('$I/I_0$')

        if enveloppe == True:
            ax1.plot(t, Diff(a, l, t) * Inter(N, d, l, 0.00000001), 'k--')

    # Define colour of the curve according to wavelength
        if (l <= 500):
            couleur = 'b'
        elif (l <= 600):
            couleur = 'g'
        elif (l <= 700):
            couleur = 'r'

        ax1.plot(t, Diff(a, l, t)*Inter(N, d, l, t), couleur)

    else:
        largeur = 0.1#/(N-1)

        cdictr = {'red':
                    ((0.0, 0.0, 0.0),
                    (largeur, 1.0, 1.0),
                    (1.0, 1.0, 1.0)),
                'green':
                    ((0.0, 0.0, 0.0),
                    (1.0, 0.0, 0.0)),
                'blue':
                    ((0.0, 0.0, 0.0),
                    (1.0, 0.0, 0.0))}

        cdictb= {'red':
                    ((0.0, 0.0, 0.0),
                    (1.0, 0.0, 0.0)),
                'green':
                    ((0.0, 0.0, 0.0),
                    (1.0, 0.0, 0.0)),
                'blue':
                    ((0.0, 0.0, 0.0),
                    (largeur, 1.0, 1.0),
                    (1.0, 1.0, 1.0))}

        cdictg= {'red':
                    ((0.0, 0.0, 0.0),
                    (1.0, 0.0, 0.0)),
                'green':
                    ((0.0, 0.0, 0.0),
                    (largeur, 1.0, 1.0),
                    (1.0, 1.0, 1.0)),
                'blue':
                    ((0.0, 0.0, 0.0),
                    (1.0, 0.0, 0.0))}

        red1 = LinearSegmentedColormap('red1', cdictr)
        blue1 = LinearSegmentedColormap('blue1', cdictb)
        green1 = LinearSegmentedColormap('green1', cdictg)

        ax1.set_yticks([])

        grille = np.linspace(-0.03,0.03,1000)

        alpha = 3000000

        X,Y = np.meshgrid(grille,grille)
        Z = np.sin(np.pi*a*np.sin(np.arctan(X))*1000000/l)**2/((np.pi*a*np.sin(np.arctan(X))*1000000/l)**2)*np.sin(N*np.pi*d*np.sin(np.arctan(X))*1000000/l)**2/(np.sin(np.pi*d*np.sin(np.arctan(X))*1000000/l)**2)*np.exp(-alpha*Y**2)

        ax1.pcolormesh(X,Y,Z, cmap=red1)

    figure.savefig(nom)

    plt.close()

    return nom
