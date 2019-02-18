# leabra7

**leabra7** is an implementation of the "Local, Error-driven and Associative,
Biologically Realistic Algorithm" ([LEABRA](https://grey.colorado.edu/emergent/index.php/Leabra))
in Python. It targets quantitative equivalence with the long-term support `emergent71` branch of the [Emergent project](https://grey.colorado.edu/emergent/index.php/Main_Page)
(note: this is not the current version of emergent).

Why is this interesting? Current neural network technology struggles with
recurrence and focuses on global learning algorithms. The leabra algorithm
allows simulation of neural networks with massive recurrence and local
learning algorithms. Currently, we are using it explore interaction
between the hippocampus and neocortex during memory recall (see the
[Princeton Computational Memory Lab](https://compmem.princeton.edu/) for more
details).

To get started, check out the
**[documentation](https://leabra7.readthedocs.io/en/latest/?)** for an
installation guide and tutorial.

Please see Daniel Greenidge's **[build](https://github.com/cdgreenidge/leabra7)** for a more stable release.

### For developers

**Gitter chat is [here](https://gitter.im/leabra7/Lobby).**

First, clone the repository. It can go anywhere, as long as you do not delete
it after installation:

```
$ git clone https://github.com/PrincetonUniversity/leabra7.git
```

Run the following commands to add the necessary conda channels and
create a virtual environment for development:

```
$ conda config --append channels pytorch
$ conda config --append channels conda-forge
$ conda env create -f scripts/environment.yml
```

This will create a new conda environment, named `leabra7`, and install the
dependencies necessary for package development. Once it is created, activate it
with

```
$ source activate leabra7
```

Install the leabra7 package in development mode:

```
$ conda-develop .
```

Now, run static analysis and tests to check that everything is working:

```
$ make
```

At this point, you can use `leabra7` like a normal Python
package. Changes made to the files will be reflected in the Python
interpreter, as long as the package is reloaded or the interpreter is
restarted.

### Roadmap
See the "Projects" tab for more info.

## For developers

### Style
* "I hate code, and I want as little of it as possible in our product."
  – Jack Diederich
* In general, follow the [Khan Academy style
  guide](https://github.com/Khan/style-guides/blob/master/style/python.md).
* Don't commit code that produces broken tests, or code
  that produces warnings during the build process. Disable warnings only if
  absolutely necessary. Think three times about committing untested code (in
  general, this should only be core simulation code that doesn't have clear
  outputs or properties.)
* Read the [Suckless philosophy](http://suckless.org/philosophy) and the
  [Unix philosophy](http://www.faqs.org/docs/artu/ch01s06.html) for
  inspiration.

## Contributors
Special thanks to Fabien Benureau for providing parts of the NXX1
implementation and net input scaling.
