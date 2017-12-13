============================================
Instructions on running the Odoo support
============================================

This plugin has been created by Akretion and is
heavily inspired from the Django plugin, so you can see:
http://www.davekuhlman.org/generateDS.html#django-generating-models-and-forms

Although, there are likely other configurations that will work, one
reasonably simple way is the following:

1. Download the source distribution of generateDS with the
   following::

       $ hg clone https://dkuhlman@bitbucket.org/rvalyi/generateds

   Alternatively, you can download a Zip file from here:
   https://bitbucket.org/rvalyi/generateds/downloads/

2. Change directory to the ``odoo`` directory (i.e. the directory
   containing this file)::

       $ cd generateds/odoo

3. In that directory, either, (a) create, a symbolic link to
   ``generateDS.py``::

       $ ln -s ../generateDS.py

   Or, (b) copy ``generateDS.py`` to that directory::

       $ cp ../generateDS.py .

4. In that directory, Run ``gends_run_gen_odoo.py``.  For
   example::

       $ cp ../tests/people.xsd .
       $ ./gends_run_gen_odoo.py -f -v people.xsd

If the above ran successfully, it should have created this file:

    models.py


.. vim:ft=rst:
