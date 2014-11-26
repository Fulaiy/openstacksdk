# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from openstack.network import network_service
from openstack import resource
from openstack import utils


class Router(resource.Resource):
    resource_key = 'router'
    resources_key = 'routers'
    base_path = '/v2.0/routers'
    service = network_service.NetworkService()

    # capabilities
    allow_create = True
    allow_retrieve = True
    allow_update = True
    allow_delete = True
    allow_list = True
    put_update = True

    # Properties
    admin_state_up = resource.prop('admin_state_up', type=bool)
    external_gateway_info = resource.prop('external_gateway_info', type=dict)
    name = resource.prop('name')
    project_id = resource.prop('tenant_id')
    status = resource.prop('status')

    def add_interface(self, session, subnet_id):
        body = {'subnet_id': subnet_id}
        url = utils.urljoin(self.base_path, self.id, 'add_router_interface')
        resp = session.put(url, service=self.service, json=body).body
        return resp

    def remove_interface(self, session, subnet_id):
        body = {'subnet_id': subnet_id}
        url = utils.urljoin(self.base_path, self.id, 'remove_router_interface')
        resp = session.put(url, service=self.service, json=body).body
        return resp
