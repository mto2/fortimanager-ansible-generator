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
module: fmgr_ips_sensor_entries_obj
short_description: IPS sensor filter.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get move set update ] the following apis.
    - /pm/config/adom/{adom}/obj/ips/sensor/{sensor}/entries/{entries}
    - /pm/config/global/obj/ips/sensor/{sensor}/entries/{entries}
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
        description: teh maximum time in seconds to wait for other user to release the workspace lock
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
            sensor:
                type: str
            entries:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'IPS sensor filter.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                action:
                    type: str
                    description: 'Action taken with traffic in which signatures are detected.'
                    choices:
                        - 'pass'
                        - 'block'
                        - 'reset'
                        - 'default'
                application:
                    -
                        type: str
                exempt-ip:
                    -
                        dst-ip:
                            type: str
                            description: 'Destination IP address and netmask.'
                        id:
                            type: int
                            description: 'Exempt IP ID.'
                        src-ip:
                            type: str
                            description: 'Source IP address and netmask.'
                id:
                    type: int
                    description: 'Rule ID in IPS database (0 - 4294967295).'
                location:
                    -
                        type: str
                log:
                    type: str
                    description: 'Enable/disable logging of signatures included in filter.'
                    choices:
                        - 'disable'
                        - 'enable'
                log-attack-context:
                    type: str
                    description: 'Enable/disable logging of attack context: URL buffer, header buffer, body buffer, packet buffer.'
                    choices:
                        - 'disable'
                        - 'enable'
                log-packet:
                    type: str
                    description: 'Enable/disable packet logging. Enable to save the packet that triggers the filter. You can download the packets in pcap fo...'
                    choices:
                        - 'disable'
                        - 'enable'
                os:
                    -
                        type: str
                protocol:
                    -
                        type: str
                quarantine:
                    type: str
                    description: 'Quarantine method.'
                    choices:
                        - 'none'
                        - 'attacker'
                        - 'both'
                        - 'interface'
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
                rule:
                    type: str
                    description: 'Identifies the predefined or custom IPS signatures to add to the sensor.'
                severity:
                    -
                        type: str
                status:
                    type: str
                    description: 'Status of the signatures included in filter. default enables the filter and only use filters with default status of enable...'
                    choices:
                        - 'disable'
                        - 'enable'
                        - 'default'
    schema_object1:
        methods: [delete]
        description: 'IPS sensor filter.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'IPS sensor filter.'
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
        description: 'IPS sensor filter.'
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
   collections:
     - fortinet.fortimanager
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/IPS/SENSOR/{SENSOR}/ENTRIES/{ENTRIES}
      fmgr_ips_sensor_entries_obj:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            sensor: <value of string>
            entries: <value of string>
         params:
            -
               data:
                  action: <value in [pass, block, reset, ...]>
                  application:
                    - <value of string>
                  exempt-ip:
                    -
                        dst-ip: <value of string>
                        id: <value of integer>
                        src-ip: <value of string>
                  id: <value of integer>
                  location:
                    - <value of string>
                  log: <value in [disable, enable]>
                  log-attack-context: <value in [disable, enable]>
                  log-packet: <value in [disable, enable]>
                  os:
                    - <value of string>
                  protocol:
                    - <value of string>
                  quarantine: <value in [none, attacker, both, ...]>
                  quarantine-expiry: <value of string>
                  quarantine-log: <value in [disable, enable]>
                  rate-count: <value of integer>
                  rate-duration: <value of integer>
                  rate-mode: <value in [periodical, continuous]>
                  rate-track: <value in [none, src-ip, dest-ip, ...]>
                  rule: <value of string>
                  severity:
                    - <value of string>
                  status: <value in [disable, enable, default]>

    - name: REQUESTING /PM/CONFIG/OBJ/IPS/SENSOR/{SENSOR}/ENTRIES/{ENTRIES}
      fmgr_ips_sensor_entries_obj:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            sensor: <value of string>
            entries: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/IPS/SENSOR/{SENSOR}/ENTRIES/{ENTRIES}
      fmgr_ips_sensor_entries_obj:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [move]>
         url_params:
            adom: <value in [none, global, custom dom]>
            sensor: <value of string>
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
               description: 'Rule ID in IPS database (0 - 4294967295).'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/ips/sensor/{sensor}/entries/{entries}'
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
            example: '/pm/config/adom/{adom}/obj/ips/sensor/{sensor}/entries/{entries}'
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
               description: 'Action taken with traffic in which signatures are detected.'
            application:
               type: array
               suboptions:
                  type: str
            exempt-ip:
               type: array
               suboptions:
                  dst-ip:
                     type: str
                     description: 'Destination IP address and netmask.'
                  id:
                     type: int
                     description: 'Exempt IP ID.'
                  src-ip:
                     type: str
                     description: 'Source IP address and netmask.'
            id:
               type: int
               description: 'Rule ID in IPS database (0 - 4294967295).'
            location:
               type: array
               suboptions:
                  type: str
            log:
               type: str
               description: 'Enable/disable logging of signatures included in filter.'
            log-attack-context:
               type: str
               description: 'Enable/disable logging of attack context: URL buffer, header buffer, body buffer, packet buffer.'
            log-packet:
               type: str
               description: 'Enable/disable packet logging. Enable to save the packet that triggers the filter. You can download the packets in pcap format ...'
            os:
               type: array
               suboptions:
                  type: str
            protocol:
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
            rule:
               type: str
               description: 'Identifies the predefined or custom IPS signatures to add to the sensor.'
            severity:
               type: array
               suboptions:
                  type: str
            status:
               type: str
               description: 'Status of the signatures included in filter. default enables the filter and only use filters with default status of enable. Fil...'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/ips/sensor/{sensor}/entries/{entries}'

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
        '/pm/config/adom/{adom}/obj/ips/sensor/{sensor}/entries/{entries}',
        '/pm/config/global/obj/ips/sensor/{sensor}/entries/{entries}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'sensor',
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
                                'reset',
                                'default'
                            ]
                        },
                        'application': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'exempt-ip': {
                            'type': 'array',
                            'items': {
                                'dst-ip': {
                                    'type': 'string'
                                },
                                'id': {
                                    'type': 'integer'
                                },
                                'src-ip': {
                                    'type': 'string'
                                }
                            }
                        },
                        'id': {
                            'type': 'integer'
                        },
                        'location': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'log': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'log-attack-context': {
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
                        'os': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'protocol': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'quarantine': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'attacker',
                                'both',
                                'interface'
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
                        'rule': {
                            'type': 'string'
                        },
                        'severity': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'status': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable',
                                'default'
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
    loose_validation = module.params['loose_validation']

    fmgr = None
    payload = None
    response = DEFAULT_RESULT_OBJ

    if module._socket_path:
        connection = Connection(module._socket_path)
        tools = FMGRCommon()
        if loose_validation == False:
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
