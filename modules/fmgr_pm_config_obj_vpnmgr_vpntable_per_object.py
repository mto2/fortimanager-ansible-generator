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
module: fmgr_pm_config_obj_vpnmgr_vpntable_per_object
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ clone delete get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/vpnmgr/vpntable/{vpntable}
    - /pm/config/global/obj/vpnmgr/vpntable/{vpntable}
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
            vpntable:
                type: str
    schema_object0:
        methods: [clone, set, update]
        description: ''
        api_categories: [api_tag0]
        api_tag0:
            data:
                authmethod:
                    type: str
                    choices:
                        - 'psk'
                        - 'rsa-signature'
                        - 'signature'
                auto-zone-policy:
                    type: str
                    default: 'enable'
                    choices:
                        - 'disable'
                        - 'enable'
                certificate:
                    type: str
                description:
                    type: str
                dpd:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                        - 'on-idle'
                        - 'on-demand'
                dpd-retrycount:
                    type: int
                dpd-retryinterval:
                    -
                        type: int
                fcc-enforcement:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                hub2spoke-zone:
                    type: str
                ike-version:
                    type: str
                    choices:
                        - '1'
                        - '2'
                ike1dhgroup:
                    -
                        type: str
                        choices:
                            - '1'
                            - '2'
                            - '5'
                            - '14'
                            - '15'
                            - '16'
                            - '17'
                            - '18'
                            - '19'
                            - '20'
                            - '21'
                            - '27'
                            - '28'
                            - '29'
                            - '30'
                            - '31'
                            - '32'
                ike1dpd:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ike1keylifesec:
                    type: int
                ike1localid:
                    type: str
                ike1mode:
                    type: str
                    choices:
                        - 'main'
                        - 'aggressive'
                ike1natkeepalive:
                    type: int
                ike1nattraversal:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                        - 'forced'
                ike1proposal:
                    type: str
                    choices:
                        - 'des-md5'
                        - 'des-sha1'
                        - '3des-md5'
                        - '3des-sha1'
                        - 'aes128-md5'
                        - 'aes128-sha1'
                        - 'aes192-md5'
                        - 'aes192-sha1'
                        - 'aes256-md5'
                        - 'aes256-sha1'
                        - 'des-sha256'
                        - '3des-sha256'
                        - 'aes128-sha256'
                        - 'aes192-sha256'
                        - 'aes256-sha256'
                        - 'des-sha384'
                        - 'des-sha512'
                        - '3des-sha384'
                        - '3des-sha512'
                        - 'aes128-sha384'
                        - 'aes128-sha512'
                        - 'aes192-sha384'
                        - 'aes192-sha512'
                        - 'aes256-sha384'
                        - 'aes256-sha512'
                        - 'aria128-md5'
                        - 'aria128-sha1'
                        - 'aria128-sha256'
                        - 'aria128-sha384'
                        - 'aria128-sha512'
                        - 'aria192-md5'
                        - 'aria192-sha1'
                        - 'aria192-sha256'
                        - 'aria192-sha384'
                        - 'aria192-sha512'
                        - 'aria256-md5'
                        - 'aria256-sha1'
                        - 'aria256-sha256'
                        - 'aria256-sha384'
                        - 'aria256-sha512'
                        - 'seed-md5'
                        - 'seed-sha1'
                        - 'seed-sha256'
                        - 'seed-sha384'
                        - 'seed-sha512'
                        - 'aes128gcm-prfsha1'
                        - 'aes128gcm-prfsha256'
                        - 'aes128gcm-prfsha384'
                        - 'aes128gcm-prfsha512'
                        - 'aes256gcm-prfsha1'
                        - 'aes256gcm-prfsha256'
                        - 'aes256gcm-prfsha384'
                        - 'aes256gcm-prfsha512'
                        - 'chacha20poly1305-prfsha1'
                        - 'chacha20poly1305-prfsha256'
                        - 'chacha20poly1305-prfsha384'
                        - 'chacha20poly1305-prfsha512'
                ike2autonego:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ike2dhgroup:
                    -
                        type: str
                        choices:
                            - '1'
                            - '2'
                            - '5'
                            - '14'
                            - '15'
                            - '16'
                            - '17'
                            - '18'
                            - '19'
                            - '20'
                            - '21'
                            - '27'
                            - '28'
                            - '29'
                            - '30'
                            - '31'
                            - '32'
                ike2keepalive:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                ike2keylifekbs:
                    type: int
                ike2keylifesec:
                    type: int
                ike2keylifetype:
                    type: str
                    choices:
                        - 'seconds'
                        - 'kbs'
                        - 'both'
                ike2proposal:
                    type: str
                    choices:
                        - 'null-md5'
                        - 'null-sha1'
                        - 'des-null'
                        - '3des-null'
                        - 'des-md5'
                        - 'des-sha1'
                        - '3des-md5'
                        - '3des-sha1'
                        - 'aes128-md5'
                        - 'aes128-sha1'
                        - 'aes192-md5'
                        - 'aes192-sha1'
                        - 'aes256-md5'
                        - 'aes256-sha1'
                        - 'aes128-null'
                        - 'aes192-null'
                        - 'aes256-null'
                        - 'null-sha256'
                        - 'des-sha256'
                        - '3des-sha256'
                        - 'aes128-sha256'
                        - 'aes192-sha256'
                        - 'aes256-sha256'
                        - 'des-sha384'
                        - 'des-sha512'
                        - '3des-sha384'
                        - '3des-sha512'
                        - 'aes128-sha384'
                        - 'aes128-sha512'
                        - 'aes192-sha384'
                        - 'aes192-sha512'
                        - 'aes256-sha384'
                        - 'aes256-sha512'
                        - 'null-sha384'
                        - 'null-sha512'
                        - 'aria128-null'
                        - 'aria128-md5'
                        - 'aria128-sha1'
                        - 'aria128-sha256'
                        - 'aria128-sha384'
                        - 'aria128-sha512'
                        - 'aria192-null'
                        - 'aria192-md5'
                        - 'aria192-sha1'
                        - 'aria192-sha256'
                        - 'aria192-sha384'
                        - 'aria192-sha512'
                        - 'aria256-null'
                        - 'aria256-md5'
                        - 'aria256-sha1'
                        - 'aria256-sha256'
                        - 'aria256-sha384'
                        - 'aria256-sha512'
                        - 'seed-null'
                        - 'seed-md5'
                        - 'seed-sha1'
                        - 'seed-sha256'
                        - 'seed-sha384'
                        - 'seed-sha512'
                        - 'aes128gcm'
                        - 'aes256gcm'
                        - 'chacha20poly1305'
                inter-vdom:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                intf-mode:
                    type: str
                    choices:
                        - 'off'
                        - 'on'
                localid-type:
                    type: str
                    choices:
                        - 'auto'
                        - 'fqdn'
                        - 'user-fqdn'
                        - 'keyid'
                        - 'address'
                        - 'asn1dn'
                name:
                    type: str
                negotiate-timeout:
                    type: int
                    default: 30
                npu-offload:
                    type: str
                    default: 'enable'
                    choices:
                        - 'disable'
                        - 'enable'
                pfs:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                psk-auto-generate:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                psksecret:
                    -
                        type: str
                replay:
                    type: str
                    choices:
                        - 'disable'
                        - 'enable'
                rsa-certificate:
                    type: str
                spoke2hub-zone:
                    type: str
                topology:
                    type: str
                    choices:
                        - 'meshed'
                        - 'star'
                        - 'dialup'
                vpn-zone:
                    type: str
    schema_object1:
        methods: [delete]
        description: ''
        api_categories: [api_tag0]
        api_tag0:
    schema_object2:
        methods: [get]
        description: ''
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

    - name: REQUESTING /PM/CONFIG/OBJ/VPNMGR/VPNTABLE/{VPNTABLE}
      fmgr_pm_config_obj_vpnmgr_vpntable_per_object:
         method: <value in [clone, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vpntable: <value of string>
         params:
            -
               data:
                  authmethod: <value in [psk, rsa-signature, signature]>
                  auto-zone-policy: <value in [disable, enable] default: 'enable'>
                  certificate: <value of string>
                  description: <value of string>
                  dpd: <value in [disable, enable, on-idle, ...]>
                  dpd-retrycount: <value of integer>
                  dpd-retryinterval:
                    - <value of integer>
                  fcc-enforcement: <value in [disable, enable]>
                  hub2spoke-zone: <value of string>
                  ike-version: <value in [1, 2]>
                  ike1dhgroup:
                    - <value in [1, 2, 5, ...]>
                  ike1dpd: <value in [disable, enable]>
                  ike1keylifesec: <value of integer>
                  ike1localid: <value of string>
                  ike1mode: <value in [main, aggressive]>
                  ike1natkeepalive: <value of integer>
                  ike1nattraversal: <value in [disable, enable, forced]>
                  ike1proposal: <value in [des-md5, des-sha1, 3des-md5, ...]>
                  ike2autonego: <value in [disable, enable]>
                  ike2dhgroup:
                    - <value in [1, 2, 5, ...]>
                  ike2keepalive: <value in [disable, enable]>
                  ike2keylifekbs: <value of integer>
                  ike2keylifesec: <value of integer>
                  ike2keylifetype: <value in [seconds, kbs, both]>
                  ike2proposal: <value in [null-md5, null-sha1, des-null, ...]>
                  inter-vdom: <value in [disable, enable]>
                  intf-mode: <value in [off, on]>
                  localid-type: <value in [auto, fqdn, user-fqdn, ...]>
                  name: <value of string>
                  negotiate-timeout: <value of integer default: 30>
                  npu-offload: <value in [disable, enable] default: 'enable'>
                  pfs: <value in [disable, enable]>
                  psk-auto-generate: <value in [disable, enable]>
                  psksecret:
                    - <value of string>
                  replay: <value in [disable, enable]>
                  rsa-certificate: <value of string>
                  spoke2hub-zone: <value of string>
                  topology: <value in [meshed, star, dialup]>
                  vpn-zone: <value of string>

    - name: REQUESTING /PM/CONFIG/OBJ/VPNMGR/VPNTABLE/{VPNTABLE}
      fmgr_pm_config_obj_vpnmgr_vpntable_per_object:
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
            vpntable: <value of string>
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
            example: '/pm/config/adom/{adom}/obj/vpnmgr/vpntable/{vpntable}'
return_of_api_category_0:
   description: items returned for method:[get]
   returned: always
   suboptions:
      id:
         type: int
      result:
         data:
            authmethod:
               type: str
            auto-zone-policy:
               type: str
               example: 'enable'
            certificate:
               type: str
            description:
               type: str
            dpd:
               type: str
            dpd-retrycount:
               type: int
            dpd-retryinterval:
               type: array
               suboptions:
                  type: int
            fcc-enforcement:
               type: str
            hub2spoke-zone:
               type: str
            ike-version:
               type: str
            ike1dhgroup:
               type: array
               suboptions:
                  type: str
            ike1dpd:
               type: str
            ike1keylifesec:
               type: int
            ike1localid:
               type: str
            ike1mode:
               type: str
            ike1natkeepalive:
               type: int
            ike1nattraversal:
               type: str
            ike1proposal:
               type: str
            ike2autonego:
               type: str
            ike2dhgroup:
               type: array
               suboptions:
                  type: str
            ike2keepalive:
               type: str
            ike2keylifekbs:
               type: int
            ike2keylifesec:
               type: int
            ike2keylifetype:
               type: str
            ike2proposal:
               type: str
            inter-vdom:
               type: str
            intf-mode:
               type: str
            localid-type:
               type: str
            name:
               type: str
            negotiate-timeout:
               type: int
               example: 30
            npu-offload:
               type: str
               example: 'enable'
            pfs:
               type: str
            psk-auto-generate:
               type: str
            psksecret:
               type: array
               suboptions:
                  type: str
            replay:
               type: str
            rsa-certificate:
               type: str
            spoke2hub-zone:
               type: str
            topology:
               type: str
            vpn-zone:
               type: str
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/vpnmgr/vpntable/{vpntable}'

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
        '/pm/config/adom/{adom}/obj/vpnmgr/vpntable/{vpntable}',
        '/pm/config/global/obj/vpnmgr/vpntable/{vpntable}'
    ]

    url_schema = [
        {
            'name': 'adom',
            'type': 'string'
        },
        {
            'name': 'vpntable',
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
                        'authmethod': {
                            'type': 'string',
                            'enum': [
                                'psk',
                                'rsa-signature',
                                'signature'
                            ]
                        },
                        'auto-zone-policy': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'certificate': {
                            'type': 'string'
                        },
                        'description': {
                            'type': 'string'
                        },
                        'dpd': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable',
                                'on-idle',
                                'on-demand'
                            ]
                        },
                        'dpd-retrycount': {
                            'type': 'integer'
                        },
                        'dpd-retryinterval': {
                            'type': 'array',
                            'items': {
                                'type': 'integer'
                            }
                        },
                        'fcc-enforcement': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'hub2spoke-zone': {
                            'type': 'string'
                        },
                        'ike-version': {
                            'type': 'string',
                            'enum': [
                                '1',
                                '2'
                            ]
                        },
                        'ike1dhgroup': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    '1',
                                    '2',
                                    '5',
                                    '14',
                                    '15',
                                    '16',
                                    '17',
                                    '18',
                                    '19',
                                    '20',
                                    '21',
                                    '27',
                                    '28',
                                    '29',
                                    '30',
                                    '31',
                                    '32'
                                ]
                            }
                        },
                        'ike1dpd': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ike1keylifesec': {
                            'type': 'integer'
                        },
                        'ike1localid': {
                            'type': 'string'
                        },
                        'ike1mode': {
                            'type': 'string',
                            'enum': [
                                'main',
                                'aggressive'
                            ]
                        },
                        'ike1natkeepalive': {
                            'type': 'integer'
                        },
                        'ike1nattraversal': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable',
                                'forced'
                            ]
                        },
                        'ike1proposal': {
                            'type': 'string',
                            'enum': [
                                'des-md5',
                                'des-sha1',
                                '3des-md5',
                                '3des-sha1',
                                'aes128-md5',
                                'aes128-sha1',
                                'aes192-md5',
                                'aes192-sha1',
                                'aes256-md5',
                                'aes256-sha1',
                                'des-sha256',
                                '3des-sha256',
                                'aes128-sha256',
                                'aes192-sha256',
                                'aes256-sha256',
                                'des-sha384',
                                'des-sha512',
                                '3des-sha384',
                                '3des-sha512',
                                'aes128-sha384',
                                'aes128-sha512',
                                'aes192-sha384',
                                'aes192-sha512',
                                'aes256-sha384',
                                'aes256-sha512',
                                'aria128-md5',
                                'aria128-sha1',
                                'aria128-sha256',
                                'aria128-sha384',
                                'aria128-sha512',
                                'aria192-md5',
                                'aria192-sha1',
                                'aria192-sha256',
                                'aria192-sha384',
                                'aria192-sha512',
                                'aria256-md5',
                                'aria256-sha1',
                                'aria256-sha256',
                                'aria256-sha384',
                                'aria256-sha512',
                                'seed-md5',
                                'seed-sha1',
                                'seed-sha256',
                                'seed-sha384',
                                'seed-sha512',
                                'aes128gcm-prfsha1',
                                'aes128gcm-prfsha256',
                                'aes128gcm-prfsha384',
                                'aes128gcm-prfsha512',
                                'aes256gcm-prfsha1',
                                'aes256gcm-prfsha256',
                                'aes256gcm-prfsha384',
                                'aes256gcm-prfsha512',
                                'chacha20poly1305-prfsha1',
                                'chacha20poly1305-prfsha256',
                                'chacha20poly1305-prfsha384',
                                'chacha20poly1305-prfsha512'
                            ]
                        },
                        'ike2autonego': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ike2dhgroup': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    '1',
                                    '2',
                                    '5',
                                    '14',
                                    '15',
                                    '16',
                                    '17',
                                    '18',
                                    '19',
                                    '20',
                                    '21',
                                    '27',
                                    '28',
                                    '29',
                                    '30',
                                    '31',
                                    '32'
                                ]
                            }
                        },
                        'ike2keepalive': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ike2keylifekbs': {
                            'type': 'integer'
                        },
                        'ike2keylifesec': {
                            'type': 'integer'
                        },
                        'ike2keylifetype': {
                            'type': 'string',
                            'enum': [
                                'seconds',
                                'kbs',
                                'both'
                            ]
                        },
                        'ike2proposal': {
                            'type': 'string',
                            'enum': [
                                'null-md5',
                                'null-sha1',
                                'des-null',
                                '3des-null',
                                'des-md5',
                                'des-sha1',
                                '3des-md5',
                                '3des-sha1',
                                'aes128-md5',
                                'aes128-sha1',
                                'aes192-md5',
                                'aes192-sha1',
                                'aes256-md5',
                                'aes256-sha1',
                                'aes128-null',
                                'aes192-null',
                                'aes256-null',
                                'null-sha256',
                                'des-sha256',
                                '3des-sha256',
                                'aes128-sha256',
                                'aes192-sha256',
                                'aes256-sha256',
                                'des-sha384',
                                'des-sha512',
                                '3des-sha384',
                                '3des-sha512',
                                'aes128-sha384',
                                'aes128-sha512',
                                'aes192-sha384',
                                'aes192-sha512',
                                'aes256-sha384',
                                'aes256-sha512',
                                'null-sha384',
                                'null-sha512',
                                'aria128-null',
                                'aria128-md5',
                                'aria128-sha1',
                                'aria128-sha256',
                                'aria128-sha384',
                                'aria128-sha512',
                                'aria192-null',
                                'aria192-md5',
                                'aria192-sha1',
                                'aria192-sha256',
                                'aria192-sha384',
                                'aria192-sha512',
                                'aria256-null',
                                'aria256-md5',
                                'aria256-sha1',
                                'aria256-sha256',
                                'aria256-sha384',
                                'aria256-sha512',
                                'seed-null',
                                'seed-md5',
                                'seed-sha1',
                                'seed-sha256',
                                'seed-sha384',
                                'seed-sha512',
                                'aes128gcm',
                                'aes256gcm',
                                'chacha20poly1305'
                            ]
                        },
                        'inter-vdom': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'intf-mode': {
                            'type': 'string',
                            'enum': [
                                'off',
                                'on'
                            ]
                        },
                        'localid-type': {
                            'type': 'string',
                            'enum': [
                                'auto',
                                'fqdn',
                                'user-fqdn',
                                'keyid',
                                'address',
                                'asn1dn'
                            ]
                        },
                        'name': {
                            'type': 'string'
                        },
                        'negotiate-timeout': {
                            'type': 'integer',
                            'default': 30,
                            'example': 30
                        },
                        'npu-offload': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'pfs': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'psk-auto-generate': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'psksecret': {
                            'type': 'array',
                            'items': {
                                'type': 'string'
                            }
                        },
                        'replay': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'rsa-certificate': {
                            'type': 'string'
                        },
                        'spoke2hub-zone': {
                            'type': 'string'
                        },
                        'topology': {
                            'type': 'string',
                            'enum': [
                                'meshed',
                                'star',
                                'dialup'
                            ]
                        },
                        'vpn-zone': {
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