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
module: fmgr_wtpprofile_lbs
short_description: Set various location based service (LBS) options.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/lbs
    - /pm/config/global/obj/wireless-controller/wtp-profile/{wtp-profile}/lbs
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
            wtp-profile:
                type: str
    schema_object0:
        methods: [get]
        description: 'Set various location based service (LBS) options.'
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
        description: 'Set various location based service (LBS) options.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                aeroscout:
                    type: str
                    description: 'Enable/disable AeroScout Real Time Location Service (RTLS) support.'
                    choices:
                        - 'disable'
                        - 'enable'
                aeroscout-ap-mac:
                    type: str
                    description: 'Use BSSID or board MAC address as AP MAC address in the Aeroscout AP message.'
                    choices:
                        - 'bssid'
                        - 'board-mac'
                aeroscout-mmu-report:
                    type: str
                    description: 'Enable/disable MU compounded report.'
                    choices:
                        - 'disable'
                        - 'enable'
                aeroscout-mu:
                    type: str
                    description: 'Enable/disable AeroScout support.'
                    choices:
                        - 'disable'
                        - 'enable'
                aeroscout-mu-factor:
                    type: int
                    description: 'AeroScout Mobile Unit (MU) mode dilution factor (default = 20).'
                aeroscout-mu-timeout:
                    type: int
                    description: 'AeroScout MU mode timeout (0 - 65535 sec, default = 5).'
                aeroscout-server-ip:
                    type: str
                    description: 'IP address of AeroScout server.'
                aeroscout-server-port:
                    type: int
                    description: 'AeroScout server UDP listening port.'
                ekahau-blink-mode:
                    type: str
                    description: 'Enable/disable Ekahua blink mode (also called AiRISTA Flow Blink Mode) to find the location of devices connected to a wire...'
                    choices:
                        - 'disable'
                        - 'enable'
                ekahau-tag:
                    type: str
                    description: 'WiFi frame MAC address or WiFi Tag.'
                erc-server-ip:
                    type: str
                    description: 'IP address of Ekahua RTLS Controller (ERC).'
                erc-server-port:
                    type: int
                    description: 'Ekahua RTLS Controller (ERC) UDP listening port.'
                fortipresence:
                    type: str
                    description: 'Enable/disable FortiPresence to monitor the location and activity of WiFi clients even if they dont connect to this WiFi n...'
                    choices:
                        - 'disable'
                        - 'enable'
                        - 'enable2'
                        - 'foreign'
                        - 'both'
                fortipresence-frequency:
                    type: int
                    description: 'FortiPresence report transmit frequency (5 - 65535 sec, default = 30).'
                fortipresence-port:
                    type: int
                    description: 'FortiPresence server UDP listening port (default = 3000).'
                fortipresence-project:
                    type: str
                    description: 'FortiPresence project name (max. 16 characters, default = fortipresence).'
                fortipresence-rogue:
                    type: str
                    description: 'Enable/disable FortiPresence finding and reporting rogue APs.'
                    choices:
                        - 'disable'
                        - 'enable'
                fortipresence-secret:
                    -
                        type: str
                fortipresence-server:
                    type: str
                    description: 'FortiPresence server IP address.'
                fortipresence-unassoc:
                    type: str
                    description: 'Enable/disable FortiPresence finding and reporting unassociated stations.'
                    choices:
                        - 'disable'
                        - 'enable'
                station-locate:
                    type: str
                    description: 'Enable/disable client station locating services for all clients, whether associated or not (default = disable).'
                    choices:
                        - 'disable'
                        - 'enable'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/WTP-PROFILE/{WTP-PROFILE}/LBS
      fmgr_wtpprofile_lbs:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wtp-profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/WTP-PROFILE/{WTP-PROFILE}/LBS
      fmgr_wtpprofile_lbs:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wtp-profile: <value of string>
         params:
            -
               data:
                  aeroscout: <value in [disable, enable]>
                  aeroscout-ap-mac: <value in [bssid, board-mac]>
                  aeroscout-mmu-report: <value in [disable, enable]>
                  aeroscout-mu: <value in [disable, enable]>
                  aeroscout-mu-factor: <value of integer>
                  aeroscout-mu-timeout: <value of integer>
                  aeroscout-server-ip: <value of string>
                  aeroscout-server-port: <value of integer>
                  ekahau-blink-mode: <value in [disable, enable]>
                  ekahau-tag: <value of string>
                  erc-server-ip: <value of string>
                  erc-server-port: <value of integer>
                  fortipresence: <value in [disable, enable, enable2, ...]>
                  fortipresence-frequency: <value of integer>
                  fortipresence-port: <value of integer>
                  fortipresence-project: <value of string>
                  fortipresence-rogue: <value in [disable, enable]>
                  fortipresence-secret:
                    - <value of string>
                  fortipresence-server: <value of string>
                  fortipresence-unassoc: <value in [disable, enable]>
                  station-locate: <value in [disable, enable]>

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
            aeroscout:
               type: str
               description: 'Enable/disable AeroScout Real Time Location Service (RTLS) support.'
            aeroscout-ap-mac:
               type: str
               description: 'Use BSSID or board MAC address as AP MAC address in the Aeroscout AP message.'
            aeroscout-mmu-report:
               type: str
               description: 'Enable/disable MU compounded report.'
            aeroscout-mu:
               type: str
               description: 'Enable/disable AeroScout support.'
            aeroscout-mu-factor:
               type: int
               description: 'AeroScout Mobile Unit (MU) mode dilution factor (default = 20).'
            aeroscout-mu-timeout:
               type: int
               description: 'AeroScout MU mode timeout (0 - 65535 sec, default = 5).'
            aeroscout-server-ip:
               type: str
               description: 'IP address of AeroScout server.'
            aeroscout-server-port:
               type: int
               description: 'AeroScout server UDP listening port.'
            ekahau-blink-mode:
               type: str
               description: 'Enable/disable Ekahua blink mode (also called AiRISTA Flow Blink Mode) to find the location of devices connected to a wireless ...'
            ekahau-tag:
               type: str
               description: 'WiFi frame MAC address or WiFi Tag.'
            erc-server-ip:
               type: str
               description: 'IP address of Ekahua RTLS Controller (ERC).'
            erc-server-port:
               type: int
               description: 'Ekahua RTLS Controller (ERC) UDP listening port.'
            fortipresence:
               type: str
               description: 'Enable/disable FortiPresence to monitor the location and activity of WiFi clients even if they dont connect to this WiFi networ...'
            fortipresence-frequency:
               type: int
               description: 'FortiPresence report transmit frequency (5 - 65535 sec, default = 30).'
            fortipresence-port:
               type: int
               description: 'FortiPresence server UDP listening port (default = 3000).'
            fortipresence-project:
               type: str
               description: 'FortiPresence project name (max. 16 characters, default = fortipresence).'
            fortipresence-rogue:
               type: str
               description: 'Enable/disable FortiPresence finding and reporting rogue APs.'
            fortipresence-secret:
               type: array
               suboptions:
                  type: str
            fortipresence-server:
               type: str
               description: 'FortiPresence server IP address.'
            fortipresence-unassoc:
               type: str
               description: 'Enable/disable FortiPresence finding and reporting unassociated stations.'
            station-locate:
               type: str
               description: 'Enable/disable client station locating services for all clients, whether associated or not (default = disable).'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/lbs'
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
            example: '/pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/lbs'

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
        '/pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/lbs',
        '/pm/config/global/obj/wireless-controller/wtp-profile/{wtp-profile}/lbs'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'wtp-profile',
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
                        'aeroscout': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'aeroscout-ap-mac': {
                            'type': 'string',
                            'enum': [
                                'bssid',
                                'board-mac'
                            ]
                        },
                        'aeroscout-mmu-report': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'aeroscout-mu': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'aeroscout-mu-factor': {
                            'type': 'integer'
                        },
                        'aeroscout-mu-timeout': {
                            'type': 'integer'
                        },
                        'aeroscout-server-ip': {
                            'type': 'string'
                        },
                        'aeroscout-server-port': {
                            'type': 'integer'
                        },
                        'ekahau-blink-mode': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ekahau-tag': {
                            'type': 'string'
                        },
                        'erc-server-ip': {
                            'type': 'string'
                        },
                        'erc-server-port': {
                            'type': 'integer'
                        },
                        'fortipresence': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable',
                                'enable2',
                                'foreign',
                                'both'
                            ]
                        },
                        'fortipresence-frequency': {
                            'type': 'integer'
                        },
                        'fortipresence-port': {
                            'type': 'integer'
                        },
                        'fortipresence-project': {
                            'type': 'string'
                        },
                        'fortipresence-rogue': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'fortipresence-secret': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'fortipresence-server': {
                            'type': 'string'
                        },
                        'fortipresence-unassoc': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'station-locate': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
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
