# fortimanager-ansible-generator
The private and temporary branch of fortimanager-ansible-generator

### 1. install dependencies:
```
#pip3 install -r requirements.txt
```
### 2. generate the modules:
```
#./generate.py
#./prepare_env.sh
#./format_generated_modules_with_autopep8.sh
```
 -  the generated modules are located under directory: `./modules` and sphinx docs material under directory: `./docgen`
 -  it's optional to format the generated modules to pep8 compatible.

### 3. before running test manually, make sure the hosts inventory is correct
 ```
#cd tests_collection
#ansible-playbook -i hosts/ -vvv script_set.yml
```
note some test cases playbook are outdated, upon errors, please refer to the generated document fox a fix.

### 4.  docs generated by Sphinx.

all the generated docs are under `ReadTheDocs`.
https://chillancezen.github.io/index.html


### 4. module naming rules
One module is named after its url, however some text are stripped in order to make the module name as short.


1). replace `/global/` and `/adom/{adom}/` with `/` in url. the domain in a url is selected form domain.

for example, url `/dvmdb/adom/{adom}/script/{script}` and `/dvmdb/global/script/{script}` will be shortened  to `/dvmdb/script/{script}`
    
2). replace all paramters in url with empty string. 

for example, url `/pm/config/obj/wireless-controller/hotspot20/anqp-nai-realm/{anqp-nai-realm}/nai-list/{nai-list}/eap-method/{eap-method}/auth-param` will be shortened to `/pm/config/obj/wireless-controller/hotspot20/anqp-nai-realm/nai-list/eap-method/auth-param`

3. replace all slash `/` with underscore `_` and leave out the leading underscore character.

e.g, `/pm/config/obj/wireless-controller/hotspot20/anqp-nai-realm/nai-list/eap-method/auth-param` will be `pm_config_obj_wireless-controller_hotspot20_anqp-nai-realm_nai-list_eap-method_auth-param`

4. replace all hyphen `-` with underscore `_`

e.g, `pm_config_obj_wireless-controller_hotspot20_anqp-nai-realm_nai-list_eap-method_auth-param` is converted to `pm_config_obj_wireless_controller_hotspot20_anqp_nai_realm_nai_list_eap_method_auth_param`

5. replace all consecutive underscores with single underscore and remove plus character `+`.

6. prefix the module with `fmgr_`.

7. if the url ends with a parameter, it is considered as a per-object url, it usually conflicts with existing module name, we add a suffix `_per_object` to the module name.



