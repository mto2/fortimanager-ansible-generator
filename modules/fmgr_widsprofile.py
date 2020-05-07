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
module: fmgr_widsprofile
short_description: Configure wireless intrusion detection system (WIDS) profiles.
description:
    - This module is able to configure a FortiManager device by allowing the
      user to [ add get set update ] the following apis.
    - /pm/config/adom/{adom}/obj/wireless-controller/wids-profile
    - /pm/config/global/obj/wireless-controller/wids-profile
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
    schema_object0:
        methods: [add, set, update]
        description: 'Configure wireless intrusion detection system (WIDS) profiles.'
        api_categories: [api_tag0]
        api_tag0:
            data:
                -
                    ap-auto-suppress:
                        type: str
                        description: 'Enable/disable on-wire rogue AP auto-suppression (default = disable).'
                        choices:
                            - 'disable'
                            - 'enable'
                    ap-bgscan-disable-day:
                        -
                            type: str
                            choices:
                                - 'sunday'
                                - 'monday'
                                - 'tuesday'
                                - 'wednesday'
                                - 'thursday'
                                - 'friday'
                                - 'saturday'
                    ap-bgscan-disable-end:
                        type: str
                        description: 'End time, using a 24-hour clock in the format of hh:mm, for disabling background scanning (default = 00:00).'
                    ap-bgscan-disable-start:
                        type: str
                        description: 'Start time, using a 24-hour clock in the format of hh:mm, for disabling background scanning (default = 00:00).'
                    ap-bgscan-duration:
                        type: int
                        description: 'Listening time on a scanning channel (10 - 1000 msec, default = 20).'
                    ap-bgscan-idle:
                        type: int
                        description: 'Waiting time for channel inactivity before scanning this channel (0 - 1000 msec, default = 0).'
                    ap-bgscan-intv:
                        type: int
                        description: 'Period of time between scanning two channels (1 - 600 sec, default = 1).'
                    ap-bgscan-period:
                        type: int
                        description: 'Period of time between background scans (60 - 3600 sec, default = 600).'
                    ap-bgscan-report-intv:
                        type: int
                        description: 'Period of time between background scan reports (15 - 600 sec, default = 30).'
                    ap-fgscan-report-intv:
                        type: int
                        description: 'Period of time between foreground scan reports (15 - 600 sec, default = 15).'
                    ap-scan:
                        type: str
                        description: 'Enable/disable rogue AP detection.'
                        choices:
                            - 'disable'
                            - 'enable'
                    ap-scan-passive:
                        type: str
                        description: 'Enable/disable passive scanning. Enable means do not send probe request on any channels (default = disable).'
                        choices:
                            - 'disable'
                            - 'enable'
                    asleap-attack:
                        type: str
                        description: 'Enable/disable asleap attack detection (default = disable).'
                        choices:
                            - 'disable'
                            - 'enable'
                    assoc-flood-thresh:
                        type: int
                        description: 'The threshold value for association frame flooding.'
                    assoc-flood-time:
                        type: int
                        description: 'Number of seconds after which a station is considered not connected.'
                    assoc-frame-flood:
                        type: str
                        description: 'Enable/disable association frame flooding detection (default = disable).'
                        choices:
                            - 'disable'
                            - 'enable'
                    auth-flood-thresh:
                        type: int
                        description: 'The threshold value for authentication frame flooding.'
                    auth-flood-time:
                        type: int
                        description: 'Number of seconds after which a station is considered not connected.'
                    auth-frame-flood:
                        type: str
                        description: 'Enable/disable authentication frame flooding detection (default = disable).'
                        choices:
                            - 'disable'
                            - 'enable'
                    comment:
                        type: str
                        description: 'Comment.'
                    deauth-broadcast:
                        type: str
                        description: 'Enable/disable broadcasting de-authentication detection (default = disable).'
                        choices:
                            - 'disable'
                            - 'enable'
                    deauth-unknown-src-thresh:
                        type: int
                        description: 'Threshold value per second to deauth unknown src for DoS attack (0: no limit).'
                    eapol-fail-flood:
                        type: str
                        description: 'Enable/disable EAPOL-Failure flooding (to AP) detection (default = disable).'
                        choices:
                            - 'disable'
                            - 'enable'
                    eapol-fail-intv:
                        type: int
                        description: 'The detection interval for EAPOL-Failure flooding (1 - 3600 sec).'
                    eapol-fail-thresh:
                        type: int
                        description: 'The threshold value for EAPOL-Failure flooding in specified interval.'
                    eapol-logoff-flood:
                        type: str
                        description: 'Enable/disable EAPOL-Logoff flooding (to AP) detection (default = disable).'
                        choices:
                            - 'disable'
                            - 'enable'
                    eapol-logoff-intv:
                        type: int
                        description: 'The detection interval for EAPOL-Logoff flooding (1 - 3600 sec).'
                    eapol-logoff-thresh:
                        type: int
                        description: 'The threshold value for EAPOL-Logoff flooding in specified interval.'
                    eapol-pre-fail-flood:
                        type: str
                        description: 'Enable/disable premature EAPOL-Failure flooding (to STA) detection (default = disable).'
                        choices:
                            - 'disable'
                            - 'enable'
                    eapol-pre-fail-intv:
                        type: int
                        description: 'The detection interval for premature EAPOL-Failure flooding (1 - 3600 sec).'
                    eapol-pre-fail-thresh:
                        type: int
                        description: 'The threshold value for premature EAPOL-Failure flooding in specified interval.'
                    eapol-pre-succ-flood:
                        type: str
                        description: 'Enable/disable premature EAPOL-Success flooding (to STA) detection (default = disable).'
                        choices:
                            - 'disable'
                            - 'enable'
                    eapol-pre-succ-intv:
                        type: int
                        description: 'The detection interval for premature EAPOL-Success flooding (1 - 3600 sec).'
                    eapol-pre-succ-thresh:
                        type: int
                        description: 'The threshold value for premature EAPOL-Success flooding in specified interval.'
                    eapol-start-flood:
                        type: str
                        description: 'Enable/disable EAPOL-Start flooding (to AP) detection (default = disable).'
                        choices:
                            - 'disable'
                            - 'enable'
                    eapol-start-intv:
                        type: int
                        description: 'The detection interval for EAPOL-Start flooding (1 - 3600 sec).'
                    eapol-start-thresh:
                        type: int
                        description: 'The threshold value for EAPOL-Start flooding in specified interval.'
                    eapol-succ-flood:
                        type: str
                        description: 'Enable/disable EAPOL-Success flooding (to AP) detection (default = disable).'
                        choices:
                            - 'disable'
                            - 'enable'
                    eapol-succ-intv:
                        type: int
                        description: 'The detection interval for EAPOL-Success flooding (1 - 3600 sec).'
                    eapol-succ-thresh:
                        type: int
                        description: 'The threshold value for EAPOL-Success flooding in specified interval.'
                    invalid-mac-oui:
                        type: str
                        description: 'Enable/disable invalid MAC OUI detection.'
                        choices:
                            - 'disable'
                            - 'enable'
                    long-duration-attack:
                        type: str
                        description: 'Enable/disable long duration attack detection based on user configured threshold (default = disable).'
                        choices:
                            - 'disable'
                            - 'enable'
                    long-duration-thresh:
                        type: int
                        description: 'Threshold value for long duration attack detection (1000 - 32767 usec, default = 8200).'
                    name:
                        type: str
                        description: 'WIDS profile name.'
                    null-ssid-probe-resp:
                        type: str
                        description: 'Enable/disable null SSID probe response detection (default = disable).'
                        choices:
                            - 'disable'
                            - 'enable'
                    sensor-mode:
                        type: str
                        description: 'Scan WiFi nearby stations (default = disable).'
                        choices:
                            - 'disable'
                            - 'foreign'
                            - 'both'
                    spoofed-deauth:
                        type: str
                        description: 'Enable/disable spoofed de-authentication attack detection (default = disable).'
                        choices:
                            - 'disable'
                            - 'enable'
                    weak-wep-iv:
                        type: str
                        description: 'Enable/disable weak WEP IV (Initialization Vector) detection (default = disable).'
                        choices:
                            - 'disable'
                            - 'enable'
                    wireless-bridge:
                        type: str
                        description: 'Enable/disable wireless bridge detection (default = disable).'
                        choices:
                            - 'disable'
                            - 'enable'
    schema_object1:
        methods: [get]
        description: 'Configure wireless intrusion detection system (WIDS) profiles.'
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
                            - 'ap-auto-suppress'
                            - 'ap-bgscan-disable-day'
                            - 'ap-bgscan-disable-end'
                            - 'ap-bgscan-disable-start'
                            - 'ap-bgscan-duration'
                            - 'ap-bgscan-idle'
                            - 'ap-bgscan-intv'
                            - 'ap-bgscan-period'
                            - 'ap-bgscan-report-intv'
                            - 'ap-fgscan-report-intv'
                            - 'ap-scan'
                            - 'ap-scan-passive'
                            - 'asleap-attack'
                            - 'assoc-flood-thresh'
                            - 'assoc-flood-time'
                            - 'assoc-frame-flood'
                            - 'auth-flood-thresh'
                            - 'auth-flood-time'
                            - 'auth-frame-flood'
                            - 'comment'
                            - 'deauth-broadcast'
                            - 'deauth-unknown-src-thresh'
                            - 'eapol-fail-flood'
                            - 'eapol-fail-intv'
                            - 'eapol-fail-thresh'
                            - 'eapol-logoff-flood'
                            - 'eapol-logoff-intv'
                            - 'eapol-logoff-thresh'
                            - 'eapol-pre-fail-flood'
                            - 'eapol-pre-fail-intv'
                            - 'eapol-pre-fail-thresh'
                            - 'eapol-pre-succ-flood'
                            - 'eapol-pre-succ-intv'
                            - 'eapol-pre-succ-thresh'
                            - 'eapol-start-flood'
                            - 'eapol-start-intv'
                            - 'eapol-start-thresh'
                            - 'eapol-succ-flood'
                            - 'eapol-succ-intv'
                            - 'eapol-succ-thresh'
                            - 'invalid-mac-oui'
                            - 'long-duration-attack'
                            - 'long-duration-thresh'
                            - 'name'
                            - 'null-ssid-probe-resp'
                            - 'sensor-mode'
                            - 'spoofed-deauth'
                            - 'weak-wep-iv'
                            - 'wireless-bridge'
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
   collections:
     - fortinet.fortimanager
   connection: httpapi
   vars:
      ansible_httpapi_use_ssl: True
      ansible_httpapi_validate_certs: False
      ansible_httpapi_port: 443
   tasks:

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/WIDS-PROFILE
      fmgr_widsprofile:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [add, set, update]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               data:
                 -
                     ap-auto-suppress: <value in [disable, enable]>
                     ap-bgscan-disable-day:
                       - <value in [sunday, monday, tuesday, ...]>
                     ap-bgscan-disable-end: <value of string>
                     ap-bgscan-disable-start: <value of string>
                     ap-bgscan-duration: <value of integer>
                     ap-bgscan-idle: <value of integer>
                     ap-bgscan-intv: <value of integer>
                     ap-bgscan-period: <value of integer>
                     ap-bgscan-report-intv: <value of integer>
                     ap-fgscan-report-intv: <value of integer>
                     ap-scan: <value in [disable, enable]>
                     ap-scan-passive: <value in [disable, enable]>
                     asleap-attack: <value in [disable, enable]>
                     assoc-flood-thresh: <value of integer>
                     assoc-flood-time: <value of integer>
                     assoc-frame-flood: <value in [disable, enable]>
                     auth-flood-thresh: <value of integer>
                     auth-flood-time: <value of integer>
                     auth-frame-flood: <value in [disable, enable]>
                     comment: <value of string>
                     deauth-broadcast: <value in [disable, enable]>
                     deauth-unknown-src-thresh: <value of integer>
                     eapol-fail-flood: <value in [disable, enable]>
                     eapol-fail-intv: <value of integer>
                     eapol-fail-thresh: <value of integer>
                     eapol-logoff-flood: <value in [disable, enable]>
                     eapol-logoff-intv: <value of integer>
                     eapol-logoff-thresh: <value of integer>
                     eapol-pre-fail-flood: <value in [disable, enable]>
                     eapol-pre-fail-intv: <value of integer>
                     eapol-pre-fail-thresh: <value of integer>
                     eapol-pre-succ-flood: <value in [disable, enable]>
                     eapol-pre-succ-intv: <value of integer>
                     eapol-pre-succ-thresh: <value of integer>
                     eapol-start-flood: <value in [disable, enable]>
                     eapol-start-intv: <value of integer>
                     eapol-start-thresh: <value of integer>
                     eapol-succ-flood: <value in [disable, enable]>
                     eapol-succ-intv: <value of integer>
                     eapol-succ-thresh: <value of integer>
                     invalid-mac-oui: <value in [disable, enable]>
                     long-duration-attack: <value in [disable, enable]>
                     long-duration-thresh: <value of integer>
                     name: <value of string>
                     null-ssid-probe-resp: <value in [disable, enable]>
                     sensor-mode: <value in [disable, foreign, both]>
                     spoofed-deauth: <value in [disable, enable]>
                     weak-wep-iv: <value in [disable, enable]>
                     wireless-bridge: <value in [disable, enable]>

    - name: REQUESTING /PM/CONFIG/OBJ/WIRELESS-CONTROLLER/WIDS-PROFILE
      fmgr_widsprofile:
         workspace_locking_adom: <value in [global, custom adom]>
         workspace_locking_timeout: 300
         method: <value in [get]>
         url_params:
            adom: <value in [none, global, custom dom]>
         params:
            -
               attr: <value of string>
               fields:
                 -
                    - <value in [ap-auto-suppress, ap-bgscan-disable-day, ap-bgscan-disable-end, ...]>
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
            example: '/pm/config/adom/{adom}/obj/wireless-controller/wids-profile'
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
               ap-auto-suppress:
                  type: str
                  description: 'Enable/disable on-wire rogue AP auto-suppression (default = disable).'
               ap-bgscan-disable-day:
                  type: array
                  suboptions:
                     type: str
               ap-bgscan-disable-end:
                  type: str
                  description: 'End time, using a 24-hour clock in the format of hh:mm, for disabling background scanning (default = 00:00).'
               ap-bgscan-disable-start:
                  type: str
                  description: 'Start time, using a 24-hour clock in the format of hh:mm, for disabling background scanning (default = 00:00).'
               ap-bgscan-duration:
                  type: int
                  description: 'Listening time on a scanning channel (10 - 1000 msec, default = 20).'
               ap-bgscan-idle:
                  type: int
                  description: 'Waiting time for channel inactivity before scanning this channel (0 - 1000 msec, default = 0).'
               ap-bgscan-intv:
                  type: int
                  description: 'Period of time between scanning two channels (1 - 600 sec, default = 1).'
               ap-bgscan-period:
                  type: int
                  description: 'Period of time between background scans (60 - 3600 sec, default = 600).'
               ap-bgscan-report-intv:
                  type: int
                  description: 'Period of time between background scan reports (15 - 600 sec, default = 30).'
               ap-fgscan-report-intv:
                  type: int
                  description: 'Period of time between foreground scan reports (15 - 600 sec, default = 15).'
               ap-scan:
                  type: str
                  description: 'Enable/disable rogue AP detection.'
               ap-scan-passive:
                  type: str
                  description: 'Enable/disable passive scanning. Enable means do not send probe request on any channels (default = disable).'
               asleap-attack:
                  type: str
                  description: 'Enable/disable asleap attack detection (default = disable).'
               assoc-flood-thresh:
                  type: int
                  description: 'The threshold value for association frame flooding.'
               assoc-flood-time:
                  type: int
                  description: 'Number of seconds after which a station is considered not connected.'
               assoc-frame-flood:
                  type: str
                  description: 'Enable/disable association frame flooding detection (default = disable).'
               auth-flood-thresh:
                  type: int
                  description: 'The threshold value for authentication frame flooding.'
               auth-flood-time:
                  type: int
                  description: 'Number of seconds after which a station is considered not connected.'
               auth-frame-flood:
                  type: str
                  description: 'Enable/disable authentication frame flooding detection (default = disable).'
               comment:
                  type: str
                  description: 'Comment.'
               deauth-broadcast:
                  type: str
                  description: 'Enable/disable broadcasting de-authentication detection (default = disable).'
               deauth-unknown-src-thresh:
                  type: int
                  description: 'Threshold value per second to deauth unknown src for DoS attack (0: no limit).'
               eapol-fail-flood:
                  type: str
                  description: 'Enable/disable EAPOL-Failure flooding (to AP) detection (default = disable).'
               eapol-fail-intv:
                  type: int
                  description: 'The detection interval for EAPOL-Failure flooding (1 - 3600 sec).'
               eapol-fail-thresh:
                  type: int
                  description: 'The threshold value for EAPOL-Failure flooding in specified interval.'
               eapol-logoff-flood:
                  type: str
                  description: 'Enable/disable EAPOL-Logoff flooding (to AP) detection (default = disable).'
               eapol-logoff-intv:
                  type: int
                  description: 'The detection interval for EAPOL-Logoff flooding (1 - 3600 sec).'
               eapol-logoff-thresh:
                  type: int
                  description: 'The threshold value for EAPOL-Logoff flooding in specified interval.'
               eapol-pre-fail-flood:
                  type: str
                  description: 'Enable/disable premature EAPOL-Failure flooding (to STA) detection (default = disable).'
               eapol-pre-fail-intv:
                  type: int
                  description: 'The detection interval for premature EAPOL-Failure flooding (1 - 3600 sec).'
               eapol-pre-fail-thresh:
                  type: int
                  description: 'The threshold value for premature EAPOL-Failure flooding in specified interval.'
               eapol-pre-succ-flood:
                  type: str
                  description: 'Enable/disable premature EAPOL-Success flooding (to STA) detection (default = disable).'
               eapol-pre-succ-intv:
                  type: int
                  description: 'The detection interval for premature EAPOL-Success flooding (1 - 3600 sec).'
               eapol-pre-succ-thresh:
                  type: int
                  description: 'The threshold value for premature EAPOL-Success flooding in specified interval.'
               eapol-start-flood:
                  type: str
                  description: 'Enable/disable EAPOL-Start flooding (to AP) detection (default = disable).'
               eapol-start-intv:
                  type: int
                  description: 'The detection interval for EAPOL-Start flooding (1 - 3600 sec).'
               eapol-start-thresh:
                  type: int
                  description: 'The threshold value for EAPOL-Start flooding in specified interval.'
               eapol-succ-flood:
                  type: str
                  description: 'Enable/disable EAPOL-Success flooding (to AP) detection (default = disable).'
               eapol-succ-intv:
                  type: int
                  description: 'The detection interval for EAPOL-Success flooding (1 - 3600 sec).'
               eapol-succ-thresh:
                  type: int
                  description: 'The threshold value for EAPOL-Success flooding in specified interval.'
               invalid-mac-oui:
                  type: str
                  description: 'Enable/disable invalid MAC OUI detection.'
               long-duration-attack:
                  type: str
                  description: 'Enable/disable long duration attack detection based on user configured threshold (default = disable).'
               long-duration-thresh:
                  type: int
                  description: 'Threshold value for long duration attack detection (1000 - 32767 usec, default = 8200).'
               name:
                  type: str
                  description: 'WIDS profile name.'
               null-ssid-probe-resp:
                  type: str
                  description: 'Enable/disable null SSID probe response detection (default = disable).'
               sensor-mode:
                  type: str
                  description: 'Scan WiFi nearby stations (default = disable).'
               spoofed-deauth:
                  type: str
                  description: 'Enable/disable spoofed de-authentication attack detection (default = disable).'
               weak-wep-iv:
                  type: str
                  description: 'Enable/disable weak WEP IV (Initialization Vector) detection (default = disable).'
               wireless-bridge:
                  type: str
                  description: 'Enable/disable wireless bridge detection (default = disable).'
         status:
            code:
               type: int
            message:
               type: str
         url:
            type: str
            example: '/pm/config/adom/{adom}/obj/wireless-controller/wids-profile'

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
        '/pm/config/adom/{adom}/obj/wireless-controller/wids-profile',
        '/pm/config/global/obj/wireless-controller/wids-profile'
    ]

    url_schema = [
        {
            'name': 'adom',
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
                        'ap-auto-suppress': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ap-bgscan-disable-day': {
                            'type': 'array',
                            'items': {
                                'type': 'string',
                                'enum': [
                                    'sunday',
                                    'monday',
                                    'tuesday',
                                    'wednesday',
                                    'thursday',
                                    'friday',
                                    'saturday'
                                ]
                            }
                        },
                        'ap-bgscan-disable-end': {
                            'type': 'string'
                        },
                        'ap-bgscan-disable-start': {
                            'type': 'string'
                        },
                        'ap-bgscan-duration': {
                            'type': 'integer'
                        },
                        'ap-bgscan-idle': {
                            'type': 'integer'
                        },
                        'ap-bgscan-intv': {
                            'type': 'integer'
                        },
                        'ap-bgscan-period': {
                            'type': 'integer'
                        },
                        'ap-bgscan-report-intv': {
                            'type': 'integer'
                        },
                        'ap-fgscan-report-intv': {
                            'type': 'integer'
                        },
                        'ap-scan': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'ap-scan-passive': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'asleap-attack': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'assoc-flood-thresh': {
                            'type': 'integer'
                        },
                        'assoc-flood-time': {
                            'type': 'integer'
                        },
                        'assoc-frame-flood': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'auth-flood-thresh': {
                            'type': 'integer'
                        },
                        'auth-flood-time': {
                            'type': 'integer'
                        },
                        'auth-frame-flood': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'comment': {
                            'type': 'string'
                        },
                        'deauth-broadcast': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'deauth-unknown-src-thresh': {
                            'type': 'integer'
                        },
                        'eapol-fail-flood': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'eapol-fail-intv': {
                            'type': 'integer'
                        },
                        'eapol-fail-thresh': {
                            'type': 'integer'
                        },
                        'eapol-logoff-flood': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'eapol-logoff-intv': {
                            'type': 'integer'
                        },
                        'eapol-logoff-thresh': {
                            'type': 'integer'
                        },
                        'eapol-pre-fail-flood': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'eapol-pre-fail-intv': {
                            'type': 'integer'
                        },
                        'eapol-pre-fail-thresh': {
                            'type': 'integer'
                        },
                        'eapol-pre-succ-flood': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'eapol-pre-succ-intv': {
                            'type': 'integer'
                        },
                        'eapol-pre-succ-thresh': {
                            'type': 'integer'
                        },
                        'eapol-start-flood': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'eapol-start-intv': {
                            'type': 'integer'
                        },
                        'eapol-start-thresh': {
                            'type': 'integer'
                        },
                        'eapol-succ-flood': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'eapol-succ-intv': {
                            'type': 'integer'
                        },
                        'eapol-succ-thresh': {
                            'type': 'integer'
                        },
                        'invalid-mac-oui': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'long-duration-attack': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'long-duration-thresh': {
                            'type': 'integer'
                        },
                        'name': {
                            'type': 'string'
                        },
                        'null-ssid-probe-resp': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'sensor-mode': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'foreign',
                                'both'
                            ]
                        },
                        'spoofed-deauth': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'weak-wep-iv': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
                            ]
                        },
                        'wireless-bridge': {
                            'type': 'string',
                            'enum': [
                                'disable',
                                'enable'
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
                                'ap-auto-suppress',
                                'ap-bgscan-disable-day',
                                'ap-bgscan-disable-end',
                                'ap-bgscan-disable-start',
                                'ap-bgscan-duration',
                                'ap-bgscan-idle',
                                'ap-bgscan-intv',
                                'ap-bgscan-period',
                                'ap-bgscan-report-intv',
                                'ap-fgscan-report-intv',
                                'ap-scan',
                                'ap-scan-passive',
                                'asleap-attack',
                                'assoc-flood-thresh',
                                'assoc-flood-time',
                                'assoc-frame-flood',
                                'auth-flood-thresh',
                                'auth-flood-time',
                                'auth-frame-flood',
                                'comment',
                                'deauth-broadcast',
                                'deauth-unknown-src-thresh',
                                'eapol-fail-flood',
                                'eapol-fail-intv',
                                'eapol-fail-thresh',
                                'eapol-logoff-flood',
                                'eapol-logoff-intv',
                                'eapol-logoff-thresh',
                                'eapol-pre-fail-flood',
                                'eapol-pre-fail-intv',
                                'eapol-pre-fail-thresh',
                                'eapol-pre-succ-flood',
                                'eapol-pre-succ-intv',
                                'eapol-pre-succ-thresh',
                                'eapol-start-flood',
                                'eapol-start-intv',
                                'eapol-start-thresh',
                                'eapol-succ-flood',
                                'eapol-succ-intv',
                                'eapol-succ-thresh',
                                'invalid-mac-oui',
                                'long-duration-attack',
                                'long-duration-thresh',
                                'name',
                                'null-ssid-probe-resp',
                                'sensor-mode',
                                'spoofed-deauth',
                                'weak-wep-iv',
                                'wireless-bridge'
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
