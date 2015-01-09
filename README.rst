horizon-dashboard-cookiecutter
==============================

.. image:: https://travis-ci.org/b1-systems/horizon-dashboard-cookiecutter.svg
   :target: https://travis-ci.org/b1-systems/horizon-dashboard-cookiecutter

Cookiecutter template for an OpenStack Horizon dashboard. See
https://github.com/audreyr/cookiecutter.

Based on http://docs.openstack.org/developer/horizon/topics/tutorial.html.

To manually create the files or to add further panels you can use the
following example commands like mentioned in the referenced tutorial.

::

  mkdir openstack_dashboard/dashboards/mydashboard

  ./run_tests.sh -m startdash mydashboard \
                --target openstack_dashboard/dashboards/mydashboard

  mkdir openstack_dashboard/dashboards/mydashboard/mypanel

  ./run_tests.sh -m startpanel mypanel \
                 --dashboard=openstack_dashboard.dashboards.mydashboard \
                 --target=openstack_dashboard/dashboards/mydashboard/mypanel

Usage
-----

Generate a Horizon dashboard project::

    cookiecutter https://github.com/b1-systems/horizon-dashboard-cookiecutter.git

To use the generated dashboard place the generated directory inside the directory
``openstack_dashboard/dashboards`` of your Horizon installation and move
the file ``_50_mydashboard.py`` to the directory ``openstack_dashboards/enabled``.
