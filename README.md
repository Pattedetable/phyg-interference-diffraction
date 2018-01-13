# Interférence et diffraction

![screenshot](https://raw.githubusercontent.com/Pattedetable/interference-diffraction/master/interference_screenshot.png)

## Français

Ce programme a pour but de visualiser l'effet de divers paramètres sur l'interférence et la diffraction que subit la lumière qui passe au-travers d'un réseau de fentes minces.  Dans le système d'éducation québécois, cette notion se place au niveau collégial.

Le programme est disponible pour Linux, MacOS et Windows.  Il s'agit en même temps d'un projet personnel d'apprentissage de programmation.  Si vous trouvez des erreurs, sentez-vous bien à l'aise de les souligner à partir de l'onglet "Issues" sur [GitHub](https://github.com/Pattedetable/interference-diffraction).

Le fichier utilisé pour démarrer le programme est ```interference.py```.


### Utilisation

Afin d'utiliser ce programme, vous aurez besoin des logiciels suivants :

  * Python 3

Si vous utilisez Linux, Python sera généralement déjà installé.  Si ce n'est pas déjà fait, vous pouvez installer Python 3 à partir des dépôts de logiciels de votre distribution.

Que vous utilisiez Linux, MacOS ou Windows, vous pouvez aussi installer Python à partir du [site officiel](https://www.python.org/).  Sélectionnez ensuite le paquet correspondant à votre système d'exploitation.

Vous aurez aussi besoin des modules Python suivants :

  * Numpy
  * Matplotlib
  * PyQt5

Si vous utilisez Linux, il est fort probable qu'ils se trouvent dans les dépôts logiciels de votre distribution.

Pour tous les systèmes d'exploitation supportés, à partir de la version 3.4, Python inclus de plus `pip`, un gestionnaire de paquet qui permet d'installer des modules pour Python.  Pour vérifer la version de Python installée sur votre système, ouvrez un terminal (Linux, MacOS) ou une invite de commande (Windows) et tappez :

```python --version```

Si le numéro de version affiché à l'écran commence par 2, dans tout ce qui suit, utilisez `python3` au lieu de `python`, et `pip3` au lieu de `pip`.

Vous pouvez vous servir de `pip` pour installer les divers modules nécessaires.  Par exemple, pour installer Numpy sur Linux, une fois les droits administrateurs obtenus, entrez dans un terminal :

```python pip install numpy```

Sur Windows, vous n'avez pas besoin des droits administrateurs, et la commande est plutôt :

```pip install numpy```

Une fois ces modules installés, dans le terminal sous Linux et MacOS ou l'invite de commande sous Windows, entrez :

```python interference.py```

Sous Windows, vous pouvez aussi double-cliquer sur le fichier ```interference.py```.



## English

This program serves to illustrate how different parameters affect the interference and the diffraction of light passing through thin slits.  In Québec's education system, this notion belongs at the college level.

This program is available for Linux, MacOS and Windows.  It is also a personal learning project.  Please report any errors you find using the "Issues" tab on [GitHub](https://github.com/Pattedetable/interference-diffraction).

The file used to start the program is ```interference.py```.


### Usage

You will need some software to use this program, namely:

  * Python 3

If you are using Linux, Python will generally already be installed.  If not, you can install it from your distribution's repositories.

You can also install Python from the [official website](https://www.python.org/).  Once there, select the appropriate package for your operating system.

You will also need the following Python modules:

  * Numpy
  * Matplotlib
  * PyQt5

On Linux, you will most likely find these modules in your distribution's repositories.

On all supported operating systems, starting with version 3.4, Python includes `pip`, a package manager for Python which can be used to install the necessary modules.  To check the version of Python that is installed on your system, open a terminal (Linux, MacOS) or a command prompt (Windows) and type in:

```python --version```

If the version number displayed on screen begins with 2, replace `python` with `python3` and `pip` with `pip3` in every command that follows.

You can then use `pip` to install the necessary modules.  For instance, to install Numpy on Linux, acquire administrator rights and then type in a terminal:

```python pip install numpy```

On Windows, administrator rights are not required, and the command is instead:

```pip install numpy```

Once these are installed, open a terminal on Linux or MacOS (or command prompt on Windows) and enter:

```python interference.py```

Moreover, on Windows, you can simply double-click on the ```interference.py``` file.
