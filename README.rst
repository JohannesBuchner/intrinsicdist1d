InstrinsicDist1d
=====================

Estimate population distribution from a sample of posteriors.

About
-------

This is work in progress.



In this approach, a hierarchical bayesian model (HBM) is set up,
where the population distribution (a gaussian) is fitted.
Uncertainties in object measurements (quantified by user-supplied
posterior samples) are fully taken into account.


Usage
---------

Generate test data::

	$ python generate.py

This makes files which contain one posterior chain per column.


Fit with various simplistic approaches::

	$ python analyse.py someinputfile.txt

Fit with HBM::

	$ python analysehbm.py someinputfile.txt



