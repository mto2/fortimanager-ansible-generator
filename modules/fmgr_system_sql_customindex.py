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
module: fmgr_system_sql_customindex
short_description: List of SQL index fields.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /cli/global/system/sql/custom-index
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
    schema_object0:
        methods: [add, set, update]
        description: 'List of SQL index fields.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    case-sensitive:
                        type: str
                        default: 'disable'
                        description:
                         - 'Disable/Enable case sensitive index.'
                         - 'disable - Build a case insensitive index.'
                         - 'enable - Build a case sensitive index.'
                        choices:
                            - 'disable'
                            - 'enable'
                    device-type:
                        type: str
                        default: 'FortiGate'
                        description:
                         - 'Device type.'
                         - 'FortiGate - Device type to FortiGate.'
                         - 'FortiManager - Set device type to FortiManager'
                         - 'FortiClient - Set device type to FortiClient'
                         - 'FortiMail - Device type to FortiMail.'
                         - 'FortiWeb - Device type to FortiWeb.'
                         - 'FortiCache - Set device type to FortiCache'
                         - 'FortiSandbox - Set device type to FortiSandbox'
                         - 'FortiDDoS - Set device type to FortiDDoS'
                         - 'FortiAuthenticator - Set device type to FortiAuthenticator'
                         - 'FortiProxy - Set device type to FortiProxy'
                        choices:
                            - 'FortiGate'
                            - 'FortiManager'
                            - 'FortiClient'
                            - 'FortiMail'
                            - 'FortiWeb'
                            - 'FortiCache'
                            - 'FortiSandbox'
                            - 'FortiDDoS'
                            - 'FortiAuthenticator'
                            - 'FortiProxy'
                    id:
                        type: int
                        default: 0
                        description: 'Add or Edit log index fields.'
                    index-field:
                        type: str
                        description: 'Log field name to be indexed.'
                    log-type:
                        type: str
                        default: 'traffic'
                        description:
                         - 'Log type.'
                         - 'none - none'
                         - 'app-ctrl '
                         - 'attack '
                         - 'content '
                         - 'dlp '
                         - 'emailfilter '
                         - 'event '
                         - 'generic '
                         - 'history '
                         - 'traffic '
                         - 'virus '
                         - 'voip '
                         - 'webfilter '
                         - 'netscan '
                         - 'fct-event '
                         - 'fct-traffic '
                         - 'fct-netscan '
                         - 'waf '
                         - 'gtp '
                         - 'dns '
                         - 'ssh '
                         - 'ssl '
                        choices:
                            - 'none'
                            - 'app-ctrl'
                            - 'attack'
                            - 'content'
                            - 'dlp'
                            - 'emailfilter'
                            - 'event'
                            - 'generic'
                            - 'history'
                            - 'traffic'
                            - 'virus'
                            - 'voip'
                            - 'webfilter'
                            - 'netscan'
                            - 'fct-event'
                            - 'fct-traffic'
                            - 'fct-netscan'
                            - 'waf'
                            - 'gtp'
                            - 'dns'
                            - 'ssh'
                            - 'ssl'
    schema_object1:
        methods: [get]
        description: 'List of SQL index fields.'
        api_categories: [api_tag0]
        api_tag0:
            fields:
                -
                    -
                        type: str
                        choices:
                            - 'case-sensitive'
                            - 'device-type'
                            - 'id'
                            - 'index-field'
                            - 'log-type'
            filter:
                -
                    type: str
            loadsub:
                type: int
                description: 'Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.'
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.'
                 - 'count - Return the number of matching entries instead of the actual entry data.'
                 - 'syntax - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.'
                choices:
                    - 'count'
                    - 'syntax'

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

    - name: REQUESTING /CLI/SYSTEM/SQL/CUSTOM-INDEX
      fmgr_system_sql_customindex:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [add, set, update]>
         params:
            -
               data:
                 -
                     case-sensitive: <value in [disable, enable] default: 'disable'>
                     device-type: <value in [FortiGate, FortiManager, FortiClient, ...] default: 'FortiGate'>
                     id: <value of integer default: 0>
                     index-field: <value of string>
                     log-type: <value in [none, app-ctrl, attack, ...] default: 'traffic'>

    - name: REQUESTING /CLI/SYSTEM/SQL/CUSTOM-INDEX
      fmgr_system_sql_customindex:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         params:
            -
               fields:
                 -
                    - <value in [case-sensitive, device-type, id, ...]>
               filter:
                 - <value of string>
               loadsub: <value of integer>
               option: <value in [count, syntax]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[add, set, update]
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
            example: '/cli/global/system/sql/custom-index'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            type: array
            suboptions:
               case-sensitive:
                  type: str
                  description: |
                     'Disable/Enable case sensitive index.'
                     'disable - Build a case insensitive index.'
                     'enable - Build a case sensitive index.'
                  example: 'disable'
               device-type:
                  type: str
                  description: |
                     'Device type.'
                     'FortiGate - Device type to FortiGate.'
                     'FortiManager - Set device type to FortiManager'
                     'FortiClient - Set device type to FortiClient'
                     'FortiMail - Device type to FortiMail.'
                     'FortiWeb - Device type to FortiWeb.'
                     'FortiCache - Set device type to FortiCache'
                     'FortiSandbox - Set device type to FortiSandbox'
                     'FortiDDoS - Set device type to FortiDDoS'
                     'FortiAuthenticator - Set device type to FortiAuthenticator'
                     'FortiProxy - Set device type to FortiProxy'
                  example: 'FortiGate'
               id:
                  type: int
                  description: 'Add or Edit log index fields.'
                  example: 0
               index-field:
                  type: str
                  description: 'Log field name to be indexed.'
               log-type:
                  type: str
                  description: |
                     'Log type.'
                     'none - none'
                     'app-ctrl '
                     'attack '
                     'content '
                     'dlp '
                     'emailfilter '
                     'event '
                     'generic '
                     'history '
                     'traffic '
                     'virus '
                     'voip '
                     'webfilter '
                     'netscan '
                     'fct-event '
                     'fct-traffic '
                     'fct-netscan '
                     'waf '
                     'gtp '
                     'dns '
                     'ssh '
                     'ssl '
                  example: 'traffic'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/cli/global/system/sql/custom-index'

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
        '/cli/global/system/sql/custom-index'
    ]

    url_schema = [
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'case-sensitive': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'device-type': {
                            'type': 'string',
                            'enum': [
                                'FortiGate',
                                'FortiManager',
                                'FortiClient',
                                'FortiMail',
                                'FortiWeb',
                                'FortiCache',
                                'FortiSandbox',
                                'FortiDDoS',
                                'FortiAuthenticator',
                                'FortiProxy'
                            ]
                        },
                        'id': {
                            'type': 'integer',
                            'default': 0,
                            'example': 0
                        },
                        'index-field': {
                            'type': 'string'
                        },
                        'log-type': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'app-ctrl',
                                'attack',
                                'content',
                                'dlp',
                                'emailfilter',
                                'event',
                                'generic',
                                'history',
                                'traffic',
                                'virus',
                                'voip',
                                'webfilter',
                                'netscan',
                                'fct-event',
                                'fct-traffic',
                                'fct-netscan',
                                'waf',
                                'gtp',
                                'dns',
                                'ssh',
                                'ssl'
                            ]
                        }
                    }
                },
                {
                    'type': 'string',
                    'name': 'url',
                    'api_tag': 0
                }
            ],
            'object1': [
                {
                    'name': 'fields',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'type': 'array',
                        'items': {
                            'type': 'string',
                            'enum': [
                                'case-sensitive',
                                'device-type',
                                'id',
                                'index-field',
                                'log-type'
                            ]
                        }
                    }
                },
                {
                    'name': 'filter',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            'type': 'string',
                            'example': [
                                '<attr>',
                                '==',
                                'test'
                            ]
                        }
                    },
                    'api_tag': 0
                },
                {
                    'type': 'integer',
                    'name': 'loadsub',
                    'api_tag': 0
                },
                {
                    'name': 'option',
                    'type': 'dict',
                    'dict': {
                        'type': 'string',
                        'enum': [
                            'count',
                            'syntax'
                        ]
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
            'add': 'object0',
            'get': 'object1',
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
                'add',
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
