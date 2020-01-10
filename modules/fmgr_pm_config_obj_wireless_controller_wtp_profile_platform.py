#!/usr/bin/python
from __future__ import absolute_import, division, print_function
# Copyright 2019 Fortinet, Inc.
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
module: fmgr_pm_config_obj_wireless_controller_wtp_profile_platform
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/platform
    - /pm/config/global/obj/wireless-controller/wtp-profile/{wtp-profile}/platform
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
        description: 'WTP, FortiAP, or AP platform.'
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
        description: 'WTP, FortiAP, or AP platform.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                type:
                    type: str
                    description: 'WTP, FortiAP or AP platform type. There are built-in WTP profiles for all supported FortiAP models. You can select a built...'
                    choices:
                        - '30B-50B'
                        - '60B'
                        - '80CM-81CM'
                        - '220A'
                        - '220B'
                        - '210B'
                        - '60C'
                        - '222B'
                        - '112B'
                        - '320B'
                        - '11C'
                        - '14C'
                        - '223B'
                        - '28C'
                        - '320C'
                        - '221C'
                        - '25D'
                        - '222C'
                        - '224D'
                        - '214B'
                        - '21D'
                        - '24D'
                        - '112D'
                        - '223C'
                        - '321C'
                        - 'C220C'
                        - 'C225C'
                        - 'S321C'
                        - 'S323C'
                        - 'FWF'
                        - 'S311C'
                        - 'S313C'
                        - 'AP-11N'
                        - 'S322C'
                        - 'S321CR'
                        - 'S322CR'
                        - 'S323CR'
                        - 'S421E'
                        - 'S422E'
                        - 'S423E'
                        - '421E'
                        - '423E'
                        - 'C221E'
                        - 'C226E'
                        - 'C23JD'
                        - 'C24JE'
                        - 'C21D'
                        - 'U421E'
                        - 'U423E'
                        - '221E'
                        - '222E'
                        - '223E'
                        - 'S221E'
                        - 'S223E'
                        - 'U221EV'
                        - 'U223EV'
                        - 'U321EV'
                        - 'U323EV'
                        - '224E'
                        - 'U422EV'
                        - 'U24JEV'
                        - '321E'

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/WTP-PROFILE/{WTP-PROFILE}/PLATFORM
      fmgr_pm_config_obj_wireless_controller_wtp_profile_platform:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wtp-profile: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/WTP-PROFILE/{WTP-PROFILE}/PLATFORM
      fmgr_pm_config_obj_wireless_controller_wtp_profile_platform:
         method: <value in [set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            wtp-profile: <value of string>
         params:
            -
               data:
                  type: <value in [30B-50B, 60B, 80CM-81CM, ...]>

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
            type:
               type: str
               description: 'WTP, FortiAP or AP platform type. There are built-in WTP profiles for all supported FortiAP models. You can select a built-in p...'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/pla...'
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
            example: '/pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/pla...'

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
        '/pm/config/adom/{adom}/obj/wireless-controller/wtp-profile/{wtp-profile}/platform',
        '/pm/config/global/obj/wireless-controller/wtp-profile/{wtp-profile}/platform'
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
                        'type': {
                            'type': 'string',
                            'enum': [
                                '30B-50B',
                                '60B',
                                '80CM-81CM',
                                '220A',
                                '220B',
                                '210B',
                                '60C',
                                '222B',
                                '112B',
                                '320B',
                                '11C',
                                '14C',
                                '223B',
                                '28C',
                                '320C',
                                '221C',
                                '25D',
                                '222C',
                                '224D',
                                '214B',
                                '21D',
                                '24D',
                                '112D',
                                '223C',
                                '321C',
                                'C220C',
                                'C225C',
                                'S321C',
                                'S323C',
                                'FWF',
                                'S311C',
                                'S313C',
                                'AP-11N',
                                'S322C',
                                'S321CR',
                                'S322CR',
                                'S323CR',
                                'S421E',
                                'S422E',
                                'S423E',
                                '421E',
                                '423E',
                                'C221E',
                                'C226E',
                                'C23JD',
                                'C24JE',
                                'C21D',
                                'U421E',
                                'U423E',
                                '221E',
                                '222E',
                                '223E',
                                'S221E',
                                'S223E',
                                'U221EV',
                                'U223EV',
                                'U321EV',
                                'U323EV',
                                '224E',
                                'U422EV',
                                'U24JEV',
                                '321E'
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