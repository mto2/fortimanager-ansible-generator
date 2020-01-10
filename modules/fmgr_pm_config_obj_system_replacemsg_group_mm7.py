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
module: fmgr_pm_config_obj_system_replacemsg_group_mm7
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/system/replacemsg-group/{replacemsg-group}/mm7
    - /pm/config/global/obj/system/replacemsg-group/{replacemsg-group}/mm7
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
            replacemsg-group:
                type: str
    schema_object0:
        methods: [add, set, update]
        description: 'Replacement message table entries.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    add-smil:
                        type: str
                        description: 'add message encapsulation'
                        choices:
                            - 'disable'
                            - 'enable'
                    addr-type:
                        type: str
                        description: 'from address type'
                        choices:
                            - 'rfc2822-addr'
                            - 'number'
                            - 'short-code'
                    allow-content-adaptation:
                        type: str
                        description: 'allow content adaptations'
                        choices:
                            - 'disable'
                            - 'enable'
                    charset:
                        type: str
                        description: 'character encoding used for replacement message'
                        choices:
                            - 'us-ascii'
                            - 'utf-8'
                    class:
                        type: str
                        description: 'message class'
                        choices:
                            - 'personal'
                            - 'advertisement'
                            - 'informational'
                            - 'auto'
                            - 'not-included'
                    format:
                        type: str
                        description: 'Format flag.'
                        choices:
                            - 'none'
                            - 'text'
                            - 'html'
                            - 'wml'
                    from:
                        type: str
                        description: 'from address'
                    from-sender:
                        type: str
                        description: 'notification message sent from recipient'
                        choices:
                            - 'disable'
                            - 'enable'
                    header:
                        type: str
                        description: 'Header flag.'
                        choices:
                            - 'none'
                            - 'http'
                            - '8bit'
                    image:
                        type: str
                        description: 'Message string.'
                    message:
                        type: str
                        description: 'message text'
                    msg-type:
                        type: str
                        description: 'Message type.'
                    priority:
                        type: str
                        description: 'message priority'
                        choices:
                            - 'low'
                            - 'normal'
                            - 'high'
                            - 'not-included'
                    rsp-status:
                        type: str
                        description: 'response status'
                        choices:
                            - 'success'
                            - 'partial-success'
                            - 'client-err'
                            - 'oper-restrict'
                            - 'addr-err'
                            - 'addr-not-found'
                            - 'content-refused'
                            - 'msg-id-not-found'
                            - 'link-id-not-found'
                            - 'msg-fmt-corrupt'
                            - 'app-id-not-found'
                            - 'repl-app-id-not-found'
                            - 'srv-err'
                            - 'not-possible'
                            - 'msg-rejected'
                            - 'multiple-addr-not-supp'
                            - 'app-addr-not-supp'
                            - 'gen-service-err'
                            - 'improper-ident'
                            - 'unsupp-ver'
                            - 'unsupp-oper'
                            - 'validation-err'
                            - 'service-err'
                            - 'service-unavail'
                            - 'service-denied'
                            - 'app-denied'
                    smil-part:
                        type: str
                        description: 'message encapsulation text'
                    subject:
                        type: str
                        description: 'subject text string'
    schema_object1:
        methods: [get]
        description: 'Replacement message table entries.'
        api_categories: [api_tag0]
        api_tag0:
            attr:
                type: str
                description: 'The name of the attribute to retrieve its datasource. Only used with &lt;i&gt;datasrc&lt;/i&gt; option.'
            fields:
                -
                    -
                        type: str
                        choices:
                            - 'add-smil'
                            - 'addr-type'
                            - 'allow-content-adaptation'
                            - 'charset'
                            - 'class'
                            - 'format'
                            - 'from'
                            - 'from-sender'
                            - 'header'
                            - 'image'
                            - 'message'
                            - 'msg-type'
                            - 'priority'
                            - 'rsp-status'
                            - 'smil-part'
                            - 'subject'
            filter:
                -
                    type: str
            get used:
                type: int
            loadsub:
                type: int
                description: 'Enable or disable the return of any sub-objects. If not specified, the default is to return all sub-objects.'
            option:
                type: str
                description:
                 - 'Set fetch option for the request. If no option is specified, by default the attributes of the objects will be returned.'
                 - 'count - Return the number of matching entries instead of the actual entry data.'
                 - 'object member - Return a list of object members along with other attributes.'
                 - 'datasrc - Return all objects that can be referenced by an attribute. Require <i>attr</i> parameter.'
                 - 'get reserved - Also return reserved objects in the result.'
                 - 'syntax - Return the attribute syntax of a table or an object, instead of the actual entry data. All filter parameters will be ignored.'
                choices:
                    - 'count'
                    - 'object member'
                    - 'datasrc'
                    - 'get reserved'
                    - 'syntax'
            range:
                -
                    type: int
            sortings:
                -
                    varidic.attr_name:
                        type: int
                        choices:
                            - 1
                            - -1

'''

EXAMPLES = '''
 - hosts: fortimanager-inventory
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/SYSTEM/REPLACEMSG-GROUP/{REPLACEMSG-GROUP}/MM7
      fmgr_pm_config_obj_system_replacemsg_group_mm7:
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            replacemsg-group: <value of string>
         params:
            -
               data:
                 -
                     add-smil: <value in [disable, enable]>
                     addr-type: <value in [rfc2822-addr, number, short-code]>
                     allow-content-adaptation: <value in [disable, enable]>
                     charset: <value in [us-ascii, utf-8]>
                     class: <value in [personal, advertisement, informational, ...]>
                     format: <value in [none, text, html, ...]>
                     from: <value of string>
                     from-sender: <value in [disable, enable]>
                     header: <value in [none, http, 8bit]>
                     image: <value of string>
                     message: <value of string>
                     msg-type: <value of string>
                     priority: <value in [low, normal, high, ...]>
                     rsp-status: <value in [success, partial-success, client-err, ...]>
                     smil-part: <value of string>
                     subject: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/SYSTEM/REPLACEMSG-GROUP/{REPLACEMSG-GROUP}/MM7
      fmgr_pm_config_obj_system_replacemsg_group_mm7:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            replacemsg-group: <value of string>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [add-smil, addr-type, allow-content-adaptation, ...]>
               filter:
                 - <value of string>
               get used: <value of integer>
               loadsub: <value of integer>
               option: <value in [count, object member, datasrc, ...]>
               range:
                 - <value of integer>
               sortings:
                 -
                     varidic.attr_name: <value in [1, -1]>

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
            example: '/pm/config/adom/{adom}/obj/system/replacemsg-group/{replacemsg-group}/mm7'
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
               add-smil:
                  type: str
                  description: 'add message encapsulation'
               addr-type:
                  type: str
                  description: 'from address type'
               allow-content-adaptation:
                  type: str
                  description: 'allow content adaptations'
               charset:
                  type: str
                  description: 'character encoding used for replacement message'
               class:
                  type: str
                  description: 'message class'
               format:
                  type: str
                  description: 'Format flag.'
               from:
                  type: str
                  description: 'from address'
               from-sender:
                  type: str
                  description: 'notification message sent from recipient'
               header:
                  type: str
                  description: 'Header flag.'
               image:
                  type: str
                  description: 'Message string.'
               message:
                  type: str
                  description: 'message text'
               msg-type:
                  type: str
                  description: 'Message type.'
               priority:
                  type: str
                  description: 'message priority'
               rsp-status:
                  type: str
                  description: 'response status'
               smil-part:
                  type: str
                  description: 'message encapsulation text'
               subject:
                  type: str
                  description: 'subject text string'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/system/replacemsg-group/{replacemsg-group}/mm7'

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
        '/pm/config/adom/{adom}/obj/system/replacemsg-group/{replacemsg-group}/mm7',
        '/pm/config/global/obj/system/replacemsg-group/{replacemsg-group}/mm7'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'replacemsg-group',
            'type': 'string'
        }
    ]

    body_schema = {
        'schema_objects': {
            'object0': [
                {
                    'name': 'data',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'add-smil': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'addr-type': {
                            'type': 'string',
                            'enum': [
                                'rfc2822-addr',
                                'number',
                                'short-code'
                            ]
                        },
                        'allow-content-adaptation': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'charset': {
                            'type': 'string',
                            'enum': [
                                'us-ascii',
                                'utf-8'
                            ]
                        },
                        'class': {
                            'type': 'string',
                            'enum': [
                                'personal',
                                'advertisement',
                                'informational',
                                'auto',
                                'not-included'
                            ]
                        },
                        'format': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'text',
                                'html',
                                'wml'
                            ]
                        },
                        'from': {
                            'type': 'string'
                        },
                        'from-sender': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'header': {
                            'type': 'string',
                            'enum': [
                                'none',
                                'http',
                                '8bit'
                            ]
                        },
                        'image': {
                            'type': 'string'
                        },
                        'message': {
                            'type': 'string'
                        },
                        'msg-type': {
                            'type': 'string'
                        },
                        'priority': {
                            'type': 'string',
                            'enum': [
                                'low',
                                'normal',
                                'high',
                                'not-included'
                            ]
                        },
                        'rsp-status': {
                            'type': 'string',
                            'enum': [
                                'success',
                                'partial-success',
                                'client-err',
                                'oper-restrict',
                                'addr-err',
                                'addr-not-found',
                                'content-refused',
                                'msg-id-not-found',
                                'link-id-not-found',
                                'msg-fmt-corrupt',
                                'app-id-not-found',
                                'repl-app-id-not-found',
                                'srv-err',
                                'not-possible',
                                'msg-rejected',
                                'multiple-addr-not-supp',
                                'app-addr-not-supp',
                                'gen-service-err',
                                'improper-ident',
                                'unsupp-ver',
                                'unsupp-oper',
                                'validation-err',
                                'service-err',
                                'service-unavail',
                                'service-denied',
                                'app-denied'
                            ]
                        },
                        'smil-part': {
                            'type': 'string'
                        },
                        'subject': {
                            'type': 'string'
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
                    'type': 'string',
                    'name': 'attr',
                    'api_tag': 0
                },
                {
                    'name': 'fields',
                    'api_tag': 0,
                    'type': 'array',
                    'items': {
                        'type': 'array',
                        'items': {
                            'type': 'string',
                            'enum': [
                                'add-smil',
                                'addr-type',
                                'allow-content-adaptation',
                                'charset',
                                'class',
                                'format',
                                'from',
                                'from-sender',
                                'header',
                                'image',
                                'message',
                                'msg-type',
                                'priority',
                                'rsp-status',
                                'smil-part',
                                'subject'
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
                    'name': 'get used',
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
                            'object member',
                            'datasrc',
                            'get reserved',
                            'syntax'
                        ]
                    },
                    'api_tag': 0
                },
                {
                    'name': 'range',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            'type': 'integer',
                            'example': [
                                2,
                                5
                            ]
                        }
                    },
                    'api_tag': 0
                },
                {
                    'name': 'sortings',
                    'type': 'dict',
                    'dict': {
                        'type': 'array',
                        'items': {
                            '{attr_name}': {
                                'type': 'integer',
                                'enum': [
                                    1,
                                    -1
                                ]
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