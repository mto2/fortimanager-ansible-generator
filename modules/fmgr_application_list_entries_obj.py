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
module: fmgr_application_list_entries_obj
short_description: Application list entries.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get move set update ] the following apis.
    - /pm/config/adom/{adom}/obj/application/list/{list}/entries/{entries}
    - /pm/config/global/obj/application/list/{list}/entries/{entries}
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
            list:
                type: str
            entries:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'Application list entries.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                action:
                    type: str
                    description: 'Pass or block traffic, or reset connection for traffic from this application.'
                    choices:
                        - 'pass'
                        - 'block'
                        - 'reset'
                application:
                    -
                        type: int
                behavior:
                    -
                        type: str
                category:
                    type: str
                    description: 'Category ID list.'
                id:
                    type: int
                    description: 'Entry ID.'
                log:
                    type: str
                    description: 'Enable/disable logging for this application list.'
                    choices:
                        - 'disable'
                        - 'enable'
                log-packet:
                    type: str
                    description: 'Enable/disable packet logging.'
                    choices:
                        - 'disable'
                        - 'enable'
                parameters:
                    -
                        id:
                            type: int
                            description: 'Parameter ID.'
                        value:
                            type: str
                            description: 'Parameter value.'
                per-ip-shaper:
                    type: str
                    description: 'Per-IP traffic shaper.'
                popularity:
                    -
                        type: str
                        choices:
                            - '1'
                            - '2'
                            - '3'
                            - '4'
                            - '5'
                protocols:
                    -
                        type: str
                quarantine:
                    type: str
                    description: 'Quarantine method.'
                    choices:
                        - 'none'
                        - 'attacker'
                quarantine-expiry:
                    type: str
                    description: 'Duration of quarantine. (Format ###d##h##m, minimum 1m, maximum 364d23h59m, default = 5m). Requires quarantine set to atta...'
                quarantine-log:
                    type: str
                    description: 'Enable/disable quarantine logging.'
                    choices:
                        - 'disable'
                        - 'enable'
                rate-count:
                    type: int
                    description: 'Count of the rate.'
                rate-duration:
                    type: int
                    description: 'Duration (sec) of the rate.'
                rate-mode:
                    type: str
                    description: 'Rate limit mode.'
                    choices:
                        - 'periodical'
                        - 'continuous'
                rate-track:
                    type: str
                    description: 'Track the packet protocol field.'
                    choices:
                        - 'none'
                        - 'src-ip'
                        - 'dest-ip'
                        - 'dhcp-client-mac'
                        - 'dns-domain'
                risk:
                    -
                        type: int
                session-ttl:
                    type: int
                    description: 'Session TTL (0 = default).'
                shaper:
                    type: str
                    description: 'Traffic shaper.'
                shaper-reverse:
                    type: str
                    description: 'Reverse traffic shaper.'
                sub-category:
                    -
                        type: int
                technology:
                    -
                        type: str
                vendor:
                    -
                        type: str
    schema_object1:
        methods: [delete]
        description: 'Application list entries.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'Application list entries.'
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
    schema_object3:
        methods: [move]
        description: 'Application list entries.'
        api_categories: [api_tag0]
        api_tag0:
            option:
                type: str
                choices:
                    - 'before'
                    - 'after'
            target:
                type: str
                description: 'Key to the target entry.'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/APPLICATION/LIST/{LIST}/ENTRIES/{ENTRIES}
      fmgr_application_list_entries_obj:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            list: <value of string>
            entries: <value of string>
         params:
            -
               data:
                  action: <value in [pass, block, reset]>
                  application:
                    - <value of integer>
                  behavior:
                    - <value of string>
                  category: <value of string>
                  id: <value of integer>
                  log: <value in [disable, enable]>
                  log-packet: <value in [disable, enable]>
                  parameters:
                    -
                        id: <value of integer>
                        value: <value of string>
                  per-ip-shaper: <value of string>
                  popularity:
                    - <value in [1, 2, 3, ...]>
                  protocols:
                    - <value of string>
                  quarantine: <value in [none, attacker]>
                  quarantine-expiry: <value of string>
                  quarantine-log: <value in [disable, enable]>
                  rate-count: <value of integer>
                  rate-duration: <value of integer>
                  rate-mode: <value in [periodical, continuous]>
                  rate-track: <value in [none, src-ip, dest-ip, ...]>
                  risk:
                    - <value of integer>
                  session-ttl: <value of integer>
                  shaper: <value of string>
                  shaper-reverse: <value of string>
                  sub-category:
                    - <value of integer>
                  technology:
                    - <value of string>
                  vendor:
                    - <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/APPLICATION/LIST/{LIST}/ENTRIES/{ENTRIES}
      fmgr_application_list_entries_obj:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            list: <value of string>
            entries: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/APPLICATION/LIST/{LIST}/ENTRIES/{ENTRIES}
      fmgr_application_list_entries_obj:
         method: <value in [move]>
         url_params:
            adom: <value in [none, global, custom dom]>
            list: <value of string>
            entries: <value of string>
         params:
            -
               option: <value in [before, after]>
               target: <value of string>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[clone, move, set, update]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            id:
               type: int
               description: 'Entry ID.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/application/list/{list}/entries/{entries}'
return_of_api_category_0:
   description: items returned for method:[delete]
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
            example: '/pm/config/adom/{adom}/obj/application/list/{list}/entries/{entries}'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            action:
               type: str
               description: 'Pass or block traffic, or reset connection for traffic from this application.'
            application:
               type: array
               suboptions:
                  type: int
            behavior:
               type: array
               suboptions:
                  type: str
            category:
               type: str
               description: 'Category ID list.'
            id:
               type: int
               description: 'Entry ID.'
            log:
               type: str
               description: 'Enable/disable logging for this application list.'
            log-packet:
               type: str
               description: 'Enable/disable packet logging.'
            parameters:
               type: array
               suboptions:
                  id:
                     type: int
                     description: 'Parameter ID.'
                  value:
                     type: str
                     description: 'Parameter value.'
            per-ip-shaper:
               type: str
               description: 'Per-IP traffic shaper.'
            popularity:
               type: array
               suboptions:
                  type: str
            protocols:
               type: array
               suboptions:
                  type: str
            quarantine:
               type: str
               description: 'Quarantine method.'
            quarantine-expiry:
               type: str
               description: 'Duration of quarantine. (Format ###d##h##m, minimum 1m, maximum 364d23h59m, default = 5m). Requires quarantine set to attacker.'
            quarantine-log:
               type: str
               description: 'Enable/disable quarantine logging.'
            rate-count:
               type: int
               description: 'Count of the rate.'
            rate-duration:
               type: int
               description: 'Duration (sec) of the rate.'
            rate-mode:
               type: str
               description: 'Rate limit mode.'
            rate-track:
               type: str
               description: 'Track the packet protocol field.'
            risk:
               type: array
               suboptions:
                  type: int
            session-ttl:
               type: int
               description: 'Session TTL (0 = default).'
            shaper:
               type: str
               description: 'Traffic shaper.'
            shaper-reverse:
               type: str
               description: 'Reverse traffic shaper.'
            sub-category:
               type: array
               suboptions:
                  type: int
            technology:
               type: array
               suboptions:
                  type: str
            vendor:
               type: array
               suboptions:
                  type: str
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/application/list/{list}/entries/{entries}'

'''
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.connection import Connection
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.common import FAIL_SOCKET_MSG
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.common import DEFAULT_RESULT_OBJ
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.common import FMGRCommon
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.common import FMGBaseException
from ansible_collections.chillancezen.fortimanager.plugins.module_utils.fortimanager import FortiManagerHandler


def main():
    jrpc_urls = [
        '/pm/config/adom/{adom}/obj/application/list/{list}/entries/{entries}',
        '/pm/config/global/obj/application/list/{list}/entries/{entries}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'list',
            'type': 'string'
        },
        {
            'name': 'entries',
            'type': 'string'
        }
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'type': 'dict',
                    'dict': {
                        'action': {
                            'type': 'string',
                            'enum': [
                                'pass',
                                'block',
                                'reset'
                            ]
                        },
                        'application': {
                            'type': 'array',
                            'items': {
                                'type': 'integer'
                            }
                        },
                        'behavior': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'category': {
                            'type': 'string'
                        },
                        'id': {
                            'type': 'integer'
                        },
                        'log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'log-packet': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'parameters': {
                            'type': 'array',
                            'items': {
                                'id': {
                                    'type': 'integer'
                                },
                                'value': {
                                    'type': 'string'
                                }
                            }
                        },
                        'per-ip-shaper': {
                            'type': 'string'
                        },
                        'popularity': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    '1',
                                    '2',
                                    '3',
                                    '4',
                                    '5'
                                ]
                            }
                        },
                        'protocols': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'quarantine': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'attacker'
                            ]
                        },
                        'quarantine-expiry': {
                            'type': 'string'
                        },
                        'quarantine-log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'rate-count': {
                            'type': 'integer'
                        },
                        'rate-duration': {
                            'type': 'integer'
                        },
                        'rate-mode': {
                            'type': 'string',
                            'enum': [
                                'periodical',
                                'continuous'
                            ]
                        },
                        'rate-track': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'src-ip',
                                'dest-ip',
                                'dhcp-client-mac',
                                'dns-domain'
                            ]
                        },
                        'risk': {
                            'type': 'array',
                            'items': {
                                'type': 'integer'
                            }
                        },
                        'session-ttl': {
                            'type': 'integer'
                        },
                        'shaper': {
                            'type': 'string'
                        },
                        'shaper-reverse': {
                            'type': 'string'
                        },
                        'sub-category': {
                            'type': 'array',
                            'items': {
                                'type': 'integer'
                            }
                        },
                        'technology': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'vendor': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        }
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
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ],
            'object2': [
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
            'object3': [
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'before',
                            'after'
                        ]
                    },
                    'api_tag': 0
                },
                {
                    'type': 'string',
                    'name': 'target',
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
            'clone': 'object0',
            'delete': 'object1',
            'get': 'object2',
            'move': 'object3',
            'set': 'object0',
            'update': 'object0'
        }
    }

    module_arg_spec = {
        'params': {
            'type': 'list',
            'required': False
        },
        'method': {
            'type': 'str',
            'required': True,
            'choices': [
                'clone',
                'delete',
                'get',
                'move',
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

    fmgr = None
    payload = None
    response = DEFAULT_RESULT_OBJ

    if module._socket_path:
        connection = Connection(module._socket_path)
        tools = FMGRCommon()
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

    module.exit_json(**response[1])


if __name__ == '__main__':
    main()