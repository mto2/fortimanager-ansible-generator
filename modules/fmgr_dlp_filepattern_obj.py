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
module: fmgr_dlp_filepattern_obj
short_description: Configure file patterns used by DLP blocking.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/dlp/filepattern/{filepattern}
    - /pm/config/global/obj/dlp/filepattern/{filepattern}
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
            filepattern:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: 'Configure file patterns used by DLP blocking.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                comment:
                    type: str
                    description: 'Optional comments.'
                entries:
                    -
                        file-type:
                            type: str
                            description: 'Select a file type.'
                            choices:
                                - 'unknown'
                                - 'ignored'
                                - 'exe'
                                - 'elf'
                                - 'bat'
                                - 'javascript'
                                - 'html'
                                - 'hta'
                                - 'msoffice'
                                - 'gzip'
                                - 'rar'
                                - 'tar'
                                - 'lzh'
                                - 'upx'
                                - 'zip'
                                - 'cab'
                                - 'bzip2'
                                - 'bzip'
                                - 'activemime'
                                - 'mime'
                                - 'hlp'
                                - 'arj'
                                - 'base64'
                                - 'binhex'
                                - 'uue'
                                - 'fsg'
                                - 'aspack'
                                - 'msc'
                                - 'petite'
                                - 'jpeg'
                                - 'gif'
                                - 'tiff'
                                - 'png'
                                - 'bmp'
                                - 'msi'
                                - 'mpeg'
                                - 'mov'
                                - 'mp3'
                                - 'wma'
                                - 'wav'
                                - 'pdf'
                                - 'avi'
                                - 'rm'
                                - 'torrent'
                                - 'hibun'
                                - '7z'
                                - 'xz'
                                - 'msofficex'
                                - 'mach-o'
                                - 'dmg'
                                - '.net'
                                - 'xar'
                                - 'chm'
                                - 'iso'
                                - 'crx'
                                - 'sis'
                                - 'prc'
                                - 'class'
                                - 'jad'
                                - 'cod'
                        filter-type:
                            type: str
                            description: 'Filter by file name pattern or by file type.'
                            choices:
                                - 'pattern'
                                - 'type'
                        pattern:
                            type: str
                            description: 'Add a file name pattern.'
                id:
                    type: int
                    description: 'ID.'
                name:
                    type: str
                    description: 'Name of table containing the file pattern list.'
    schema_object1:
        methods: [delete]
        description: 'Configure file patterns used by DLP blocking.'
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: 'Configure file patterns used by DLP blocking.'
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
   collections:
     - fortinet.fortimanager
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/DLP/FILEPATTERN/{FILEPATTERN}
      fmgr_dlp_filepattern_obj:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            filepattern: <value of string>
         params:
            -
               data:
                  comment: <value of string>
                  entries:
                    -
                        file-type: <value in [unknown, ignored, exe, ...]>
                        filter-type: <value in [pattern, type]>
                        pattern: <value of string>
                  id: <value of integer>
                  name: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/DLP/FILEPATTERN/{FILEPATTERN}
      fmgr_dlp_filepattern_obj:
         loose_validation: False
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            filepattern: <value of string>
         params:
            -
               option: <value in [object member, chksum, datasrc]>

'''

RETURN = '''
return_of_api_category_0:
   description: items returned for method:[clone, set, update]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            id:
               type: int
               description: 'ID.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/dlp/filepattern/{filepattern}'
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
            example: '/pm/config/adom/{adom}/obj/dlp/filepattern/{filepattern}'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            comment:
               type: str
               description: 'Optional comments.'
            entries:
               type: array
               suboptions:
                  file-type:
                     type: str
                     description: 'Select a file type.'
                  filter-type:
                     type: str
                     description: 'Filter by file name pattern or by file type.'
                  pattern:
                     type: str
                     description: 'Add a file name pattern.'
            id:
               type: int
               description: 'ID.'
            name:
               type: str
               description: 'Name of table containing the file pattern list.'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/dlp/filepattern/{filepattern}'

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
        '/pm/config/adom/{adom}/obj/dlp/filepattern/{filepattern}',
        '/pm/config/global/obj/dlp/filepattern/{filepattern}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'filepattern',
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
                        'comment': {
                            'type': 'string'
                        },
                        'entries': {
                            'type': 'array',
                            'items': {
                                'file-type': {
                                    'type': 'string',
                                    'enum': [
                                        'unknown',
                                        'ignored',
                                        'exe',
                                        'elf',
                                        'bat',
                                        'javascript',
                                        'html',
                                        'hta',
                                        'msoffice',
                                        'gzip',
                                        'rar',
                                        'tar',
                                        'lzh',
                                        'upx',
                                        'zip',
                                        'cab',
                                        'bzip2',
                                        'bzip',
                                        'activemime',
                                        'mime',
                                        'hlp',
                                        'arj',
                                        'base64',
                                        'binhex',
                                        'uue',
                                        'fsg',
                                        'aspack',
                                        'msc',
                                        'petite',
                                        'jpeg',
                                        'gif',
                                        'tiff',
                                        'png',
                                        'bmp',
                                        'msi',
                                        'mpeg',
                                        'mov',
                                        'mp3',
                                        'wma',
                                        'wav',
                                        'pdf',
                                        'avi',
                                        'rm',
                                        'torrent',
                                        'hibun',
                                        '7z',
                                        'xz',
                                        'msofficex',
                                        'mach-o',
                                        'dmg',
                                        '.net',
                                        'xar',
                                        'chm',
                                        'iso',
                                        'crx',
                                        'sis',
                                        'prc',
                                        'class',
                                        'jad',
                                        'cod'
                                    ]
                                },
                                'filter-type': {
                                    'type': 'string',
                                    'enum': [
                                        'pattern',
                                        'type'
                                    ]
                                },
                                'pattern': {
                                    'type': 'string'
                                }
                            }
                        },
                        'id': {
                            'type': 'integer'
                        },
                        'name': {
                            'type': 'string'
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
