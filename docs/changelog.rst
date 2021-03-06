Change log
==========

.. currentmodule:: fl_data_downloader

0.4.3 - 2020-09-01
~~~~~~~~~~~~~~~~~~

 * get_dataset_for_course assumed all run numbers were sequential which resulted in datasets not being downloaded when they weren't!

0.4.2 - 2020-08-05
~~~~~~~~~~~~~~~~~~

 * resolve issue affecting all downloads after the FutureLearn website changed

0.4.1 - 2020-07-10
~~~~~~~~~~~~~~~~~~

 * added 30 seconds delay after a connection error before retrying

0.4.0 - 2020-06-12
~~~~~~~~~~~~~~~~~~

 * added max_retries to allow downloads to be "retried" if they fail.

0.3.0 - 2020-04-09
~~~~~~~~~~~~~~~~~~

 * added countries and country-subdivisions datasets
 * removed index from CSV files created by fl-data-dl

0.2.3 - 2020-04-03
~~~~~~~~~~~~~~~~~~

 * updated default cache directory
 * doc updates

0.2.2 - 2020-04-01
~~~~~~~~~~~~~~~~~~

 * python 3.5 incompatibility fix

0.2.1 - 2020-04-01
~~~~~~~~~~~~~~~~~~

 * minor bug fix

0.2.0 - 2020-04-01
~~~~~~~~~~~~~~~~~~

 * major refactoring of code base and API
 * introduction of caching

0.1.0
~~~~~~~~~~~~~~~~~~

 * first beta