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
module: fmgr_pm_config_obj_firewall_proxy_address_per_object
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/firewall/proxy-address/{proxy-address}
    - /pm/config/global/obj/firewall/proxy-address/{proxy-address}
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
            proxy-address:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'Web proxy address configuration.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                case-sensitivity:
                    type: str
                    description: 'Enable to make the pattern case sensitive.'
                    choices:
                        - 'disable'
                        - 'enable'
                category:
                    type: str
                    description: 'FortiGuard category ID.'
                color:
                    type: int
                    description: 'Integer value to determine the color of the icon in the GUI (1 - 32, default = 0, which sets value to 1).'
                comment:
                    type: str
                    description: 'Optional comments.'
                header:
                    type: str
                    description: 'HTTP header name as a regular expression.'
                header-group:
                    -
                        case-sensitivity:
                            type: str
                            description: 'Case sensitivity in pattern.'
                            choices:
                                - 'disable'
                                - 'enable'
                        header:
                            type: str
                            description: 'HTTP header regular expression.'
                        header-name:
                            type: str
                            description: 'HTTP header.'
                        id:
                            type: int
                            description: 'ID.'
                header-name:
                    type: str
                    description: 'Name of HTTP header.'
                host:
                    type: str
                    description: 'Address object for the host.'
                host-regex:
                    type: str
                    description: 'Host name as a regular expression.'
                method:
                    -
                        type: str
                        choices:
                            - 'delete'
                            - 'get'
                            - 'head'
                            - 'options'
                            - 'post'
                            - 'put'
                            - 'trace'
                            - 'connect'
                name:
                    type: str
                    description: 'Address name.'
                path:
                    type: str
                    description: 'URL path as a regular expression.'
                query:
                    type: str
                    description: 'Match the query part of the URL as a regular expression.'
                referrer:
                    type: str
                    description: 'Enable/disable use of referrer field in the HTTP header to match the address.'
                    choices:
                        - 'disable'
                        - 'enable'
                tagging:
                    -
                        category:
                            type: str
                            description: 'Tag category.'
                        name:
                            type: str
                            description: 'Tagging entry name.'
                        tags:
                            -
                                type: str
                type:
                    type: str
                    description: 'Proxy address type.'
                    choices:
                        - 'host-regex'
                        - 'url'
                        - 'category'
                        - 'method'
                        - 'ua'
                        - 'header'
                        - 'src-advanced'
                        - 'dst-advanced'
                ua:
                    -
                        type: str
                        choices:
                            - 'chrome'
                            - 'ms'
                            - 'firefox'
                            - 'safari'
                            - 'other'
                uuid:
                    type: str
                    description: 'Universally Unique Identifier (UUID; automatically assigned but can be manually reset).'
                visibility:
                    type: str
                    description: 'Enable/disable visibility of the object in the GUI.'
                    choices:
                        - 'disable'
                        - 'enable'
    schema_object1:
        methods: [delete]
        description: 'Web proxy address configuration.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'Web proxy address configuration.'
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

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/PROXY-ADDRESS/{PROXY-ADDRESS}
      fmgr_pm_config_obj_firewall_proxy_address_per_object:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            proxy-address: <value of string>
         params:
            -
               data:
                  case-sensitivity: <value in [disable, enable]>
                  category: <value of string>
                  color: <value of integer>
                  comment: <value of string>
                  header: <value of string>
                  header-group:
                    -
                        case-sensitivity: <value in [disable, enable]>
                        header: <value of string>
                        header-name: <value of string>
                        id: <value of integer>
                  header-name: <value of string>
                  host: <value of string>
                  host-regex: <value of string>
                  method:
                    - <value in [delete, get, head, ...]>
                  name: <value of string>
                  path: <value of string>
                  query: <value of string>
                  referrer: <value in [disable, enable]>
                  tagging:
                    -
                        category: <value of string>
                        name: <value of string>
                        tags:
                          - <value of string>
                  type: <value in [host-regex, url, category, ...]>
                  ua:
                    - <value in [chrome, ms, firefox, ...]>
                  uuid: <value of string>
                  visibility: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/OBJ/FIREWALL/PROXY-ADDRESS/{PROXY-ADDRESS}
      fmgr_pm_config_obj_firewall_proxy_address_per_object:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            proxy-address: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[clone, delete, set, update]
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
            example: '/pm/config/adom/{adom}/obj/firewall/proxy-address/{proxy-address}'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            case-sensitivity:
               type: str
               description: 'Enable to make the pattern case sensitive.'
            category:
               type: str
               description: 'FortiGuard category ID.'
            color:
               type: int
               description: 'Integer value to determine the color of the icon in the GUI (1 - 32, default = 0, which sets value to 1).'
            comment:
               type: str
               description: 'Optional comments.'
            header:
               type: str
               description: 'HTTP header name as a regular expression.'
            header-group:
               type: array
               suboptions:
                  case-sensitivity:
                     type: str
                     description: 'Case sensitivity in pattern.'
                  header:
                     type: str
                     description: 'HTTP header regular expression.'
                  header-name:
                     type: str
                     description: 'HTTP header.'
                  id:
                     type: int
                     description: 'ID.'
            header-name:
               type: str
               description: 'Name of HTTP header.'
            host:
               type: str
               description: 'Address object for the host.'
            host-regex:
               type: str
               description: 'Host name as a regular expression.'
            method:
               type: array
               suboptions:
                  type: str
            name:
               type: str
               description: 'Address name.'
            path:
               type: str
               description: 'URL path as a regular expression.'
            query:
               type: str
               description: 'Match the query part of the URL as a regular expression.'
            referrer:
               type: str
               description: 'Enable/disable use of referrer field in the HTTP header to match the address.'
            tagging:
               type: array
               suboptions:
                  category:
                     type: str
                     description: 'Tag category.'
                  name:
                     type: str
                     description: 'Tagging entry name.'
                  tags:
                     type: array
                     suboptions:
                        type: str
            type:
               type: str
               description: 'Proxy address type.'
            ua:
               type: array
               suboptions:
                  type: str
            uuid:
               type: str
               description: 'Universally Unique Identifier (UUID; automatically assigned but can be manually reset).'
            visibility:
               type: str
               description: 'Enable/disable visibility of the object in the GUI.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/firewall/proxy-address/{proxy-address}'

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
        '/pm/config/adom/{adom}/obj/firewall/proxy-address/{proxy-address}',
        '/pm/config/global/obj/firewall/proxy-address/{proxy-address}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'proxy-address',
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
                        'case-sensitivity': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'category': {
                            'type': 'string'
                        },
                        'color': {
                            'type': 'integer'
                        },
                        'comment': {
                            'type': 'string'
                        },
                        'header': {
                            'type': 'string'
                        },
                        'header-group': {
                            'type': 'array',
                            'items': {
                                'case-sensitivity': {
                                    'type': 'string',
                                    'enum': [
                                        'disable',
                                        'enable'
                                    ]
                                },
                                'header': {
                                    'type': 'string'
                                },
                                'header-name': {
                                    'type': 'string'
                                },
                                'id': {
                                    'type': 'integer'
                                }
                            }
                        },
                        'header-name': {
                            'type': 'string'
                        },
                        'host': {
                            'type': 'string'
                        },
                        'host-regex': {
                            'type': 'string'
                        },
                        'method': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'delete',
                                    'get',
                                    'head',
                                    'options',
                                    'post',
                                    'put',
                                    'trace',
                                    'connect'
                                ]
                            }
                        },
                        'name': {
                            'type': 'string'
                        },
                        'path': {
                            'type': 'string'
                        },
                        'query': {
                            'type': 'string'
                        },
                        'referrer': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'tagging': {
                            'type': 'array',
                            'items': {
                                'category': {
                                    'type': 'string'
                                },
                                'name': {
                                    'type': 'string'
                                },
                                'tags': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'string'
                                    }
                                }
                            }
                        },
                        'type': {
                            'type': 'string',
                            'enum': [
                                'host-regex',
                                'url',
                                'category',
                                'method',
                                'ua',
                                'header',
                                'src-advanced',
                                'dst-advanced'
                            ]
                        },
                        'ua': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'chrome',
                                    'ms',
                                    'firefox',
                                    'safari',
                                    'other'
                                ]
                            }
                        },
                        'uuid': {
                            'type': 'string'
                        },
                        'visibility': {
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
            ]
        },
        'method_mapping': {
            'clone': 'object0',
            'delete': 'object1',
            'get': 'object2',
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