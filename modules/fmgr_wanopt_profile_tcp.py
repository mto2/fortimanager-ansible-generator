#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2019-2020 Fortinet, Inc.
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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

__metaclass__ = type

ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}

DOCUMENTATION = '''
---
module: fmgr_wanopt_profile_tcp
short_description: Enable/disable TCP WAN Optimization and configure TCP WAN Optimization features.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/wanopt/profile/{profile}/tcp
    - /pm/config/global/obj/wanopt/profile/{profile}/tcp
    - Examples include all parameters and values need to be adjusted to data sources before usage.

version_added: "2.10"
author:
    - Frank Shen (@fshen01)
    - Link Zheng (@zhengl)
notes:
    - There are only three top-level parameters where 'method' is always required
      while other two 'params' and 'url_params' can be optional
    - Due to the complexity of fortimanager api schema, the validation is done
      out of Ansible native parameter validation procedure.
    - The syntax of OPTIONS doen not comply with the standard Ansible argument
      specification, but with the structure of fortimanager API schema, we need
      a trivial transformation when we are filling the ansible playbook
options:
    loose_validation:
        description: Do parameter validation in a loose way
        required: False
        type: bool
        default: false
    workspace_locking_adom:
        description: the adom to lock in case FortiManager running in workspace mode
        required: False
        type: string
        choices:
          - global
          - custom adom
    workspace_locking_timeout:
        description: the maximum time in seconds to wait for other user to release the workspace lock
        required: False
        type: integer
        default: 300
    url_params:
        description: the parameters in url path
        required: True
        type: dict
        suboptions:
            adom:
                type: str
                description: the domain prefix, the none and global are reserved
                choices:
                  - none
                  - global
                  - custom dom
            profile:
                type: str
    schema_object0:
        methods: [get]
        description: 'Enable/disable TCP WAN Optimization and configure TCP WAN Optimization features.'
        api_categories: [api_tag0]
        api_tag0:
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the object will be returned.'
                 - 'object member - Return a list of object members along with other attributes.'
                 - 'chksum - Return the check-sum value instead of attributes.'
                choices:
                    - 'object member'
                    - 'chksum'
                    - 'datasrc'
    schema_object1:
        methods: [set, update]
        description: 'Enable/disable TCP WAN Optimization and configure TCP WAN Optimization features.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                byte-caching:
                    type: str
                    description: 'Enable/disable byte-caching for HTTP. Byte caching reduces the amount of traffic by caching file data sent across the WAN ...'
                    choices:
                        - 'disable'
                        - 'enable'
                byte-caching-opt:
                    type: str
                    description: 'Select whether TCP byte-caching uses system memory only or both memory and disk space.'
                    choices:
                        - 'mem-only'
                        - 'mem-disk'
                log-traffic:
                    type: str
                    description: 'Enable/disable logging.'
                    choices:
                        - 'disable'
                        - 'enable'
                port:
                    type: str
                    description: 'Single port number or port number range for TCP. Only packets with a destination port number that matches this port number...'
                secure-tunnel:
                    type: str
                    description: 'Enable/disable securing the WAN Opt tunnel using SSL. Secure and non-secure tunnels use the same TCP port (7810).'
                    choices:
                        - 'disable'
                        - 'enable'
                ssl:
                    type: str
                    description: 'Enable/disable SSL/TLS offloading.'
                    choices:
                        - 'disable'
                        - 'enable'
                ssl-port:
                    -
                        type: int
                status:
                    type: str
                    description: 'Enable/disable HTTP WAN Optimization.'
                    choices:
                        - 'disable'
                        - 'enable'
                tunnel-sharing:
                    type: str
                    description: 'Tunnel sharing mode for aggressive/non-aggressive and/or interactive/non-interactive protocols.'
                    choices:
                        - 'private'
                        - 'shared'
                        - 'express-shared'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   collections:
     - fortinet.fortimanager
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/WANOPT/PROFILE/{PROFILE}/TCP
      fmgr_wanopt_profile_tcp:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/WANOPT/PROFILE/{PROFILE}/TCP
      fmgr_wanopt_profile_tcp:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            profile: <value of string>
         params:
            -
               data:
                  byte-caching: <value in [disable, enable]>
                  byte-caching-opt: <value in [mem-only, mem-disk]>
                  log-traffic: <value in [disable, enable]>
                  port: <value of string>
                  secure-tunnel: <value in [disable, enable]>
                  ssl: <value in [disable, enable]>
                  ssl-port:
                    - <value of integer>
                  status: <value in [disable, enable]>
                  tunnel-sharing: <value in [private, shared, express-shared]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            byte-caching:
               type: str
               description: 'Enable/disable byte-caching for HTTP. Byte caching reduces the amount of traffic by caching file data sent across the WAN and i...'
            byte-caching-opt:
               type: str
               description: 'Select whether TCP byte-caching uses system memory only or both memory and disk space.'
            log-traffic:
               type: str
               description: 'Enable/disable logging.'
            port:
               type: str
               description: 'Single port number or port number range for TCP. Only packets with a destination port number that matches this port number or r...'
            secure-tunnel:
               type: str
               description: 'Enable/disable securing the WAN Opt tunnel using SSL. Secure and non-secure tunnels use the same TCP port (7810).'
            ssl:
               type: str
               description: 'Enable/disable SSL/TLS offloading.'
            ssl-port:
               type: array
               suboptions:
                  type: int
            status:
               type: str
               description: 'Enable/disable HTTP WAN Optimization.'
            tunnel-sharing:
               type: str
               description: 'Tunnel sharing mode for aggressive/non-aggressive and/or interactive/non-interactive protocols.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/wanopt/profile/{profile}/tcp'
return_of_api_category_0:
   description: items returned for method:[set, update]
   returned: always
   suboptions:
      id:
         type: int
      result:
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/wanopt/profile/{profile}/tcp'

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import FAIL_SOCKET_MSG
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import DEFAULT_RESULT_OBJ
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import FMGRCommon
from ansible_collections.fortinet.fortimanager.plugins.module_utils.common import FMGBaseException
from ansible_collections.fortinet.fortimanager.plugins.module_utils.fortimanager import FortiManagerHandler


def main():
    jrpc_urls = [
        '/pm/config/adom/{adom}/obj/wanopt/profile/{profile}/tcp',
        '/pm/config/global/obj/wanopt/profile/{profile}/tcp'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'profile',
            'type': 'string'
        }
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'object member',
                            'chksum',
                            'datasrc'
                        ]
                    },
                    'api_tag': 0
                },
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ],
            'object1': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'byte-caching': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'byte-caching-opt': {
                            'type': 'string',
                            'enum': [
                                'mem-only',
                                'mem-disk'
                            ]
                        },
                        'log-traffic': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'port': {
                            'type': 'string'
                        },
                        'secure-tunnel': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ssl': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ssl-port': {
                            'type': 'array',
                            'items': {
                                'type': 'integer'
                            }
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'tunnel-sharing': {
                            'type': 'string',
                            'enum': [
                                'private',
                                'shared',
                                'express-shared'
                            ]
                        }
                    },
                    'api_tag': 0
                },
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ]
        },
        'method_mapping': {
            'get': 'object0',
            'set': 'object1',
            'update': 'object1'
        }
    }

    module_arg_spec = {
        'loose_validation': {
            'type': 'bool',
            'required': False,
            'default': False
        },
        'workspace_locking_adom': {
            'type': 'str',
            'required': False
        },
        'workspace_locking_timeout': {
            'type': 'int',
            'required': False,
            'default': 300
        },
        'params': {
            'type': 'list',
            'required': False
        },
        'method': {
            'type': 'str',
            'required': True,
            'choices': [
                'get',
                'set',
                'update'
            ]
        },
        'url_params': {
            'type': 'dict',
            'required': False
        }
    }
    module = AnsibleModule(argument_spec=module_arg_spec,
                           supports_check_mode=False)
    method = module.params['method']
    loose_validation = module.params['loose_validation']

    fmgr = None
    payload = None
    response = DEFAULT_RESULT_OBJ

    if module._socket_path:
        connection = Connection(module._socket_path)
        tools = FMGRCommon()
        if loose_validation is False:
            tools.validate_module_params(module, body_schema)
        tools.validate_module_url_params(module, jrpc_urls, url_schema)
        full_url = tools.get_full_url_path(module, jrpc_urls)
        payload = tools.get_full_payload(module, full_url)
        fmgr = FortiManagerHandler(connection, module)
        fmgr.tools = tools
    else:
        module.fail_json(**FAIL_SOCKET_MSG)

    try:
        response = fmgr._conn.send_request(method, payload)
        fmgr.govern_response(module=module, results=response,
                             msg='Operation Finished',
                             ansible_facts=fmgr.construct_ansible_facts(response, module.params, module.params))
    except Exception as e:
        raise FMGBaseException(e)

    module.exit_json(meta=response[1])


if __name__ == '__main__':
    main()
