#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from django.utils.translation import ugettext_lazy as _

import horizon

from openstack_dashboard.dashboards.{{cookiecutter.dashboard_name}} import dashboard


class {{cookiecutter.panel_name|title}}(horizon.Panel):
    name = _("{{cookiecutter.panel_name|title}}")
    slug = "{{cookiecutter.panel_name}}"


dashboard.{{cookiecutter.dashboard_name|title}}.register({{cookiecutter.panel_name|title}})
