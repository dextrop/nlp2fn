'''
The main purpose of configparser is to parse jennie.conf file for further execution.
File Structure should be

[basic]

name=Saurabh Pandey
title=SomeTitle
description=Some description for this automation.
image=/some/path/a.png
platform=angular
tag=google-login, login-automation

[automation-conf]

Download Filepath
Create angular component

usage :
    try
        detail_dict, automation_arr = ConfigParser('jennie.conf').Parse()
    except Exception as e:
        // handle error.
'''

class ConfigParser():
    def __init__(self, filepath):
        self.filepath = filepath
        self.required_keys = ['name', 'title', 'description', 'platform']

    def validateKeys(self, json_obj):
        missing_key = next((key for key in self.required_keys if key not in json_obj), None)
        return missing_key is None, missing_key

    def Parse(self):
        fileContent = open(self.filepath, 'r').read()
        if (len(fileContent.split("[basic]")) > 1):
            basicDetails = fileContent.split("[basic]")[1].split("[automation]")[0]
            if (len(fileContent.split("[automation]")) > 1):
                automationDetail = fileContent.split("[automation]")[1]
            else:
                raise ValueError("Missing [automation] details")
        else:
            raise ValueError("Missing [basic] details")


        detail_dict = {}
        automation_arr = []
        for line in basicDetails.split("\n"):
            if len(line) > 3:
                try:
                    key, value = line.split('=')
                    detail_dict[key.strip()] = value.strip()
                except Exception as e:
                    raise Exception(
                        "Unable to parse detail, incorrect value, [detail] file include values without key pair")

        are_details_valid, missing_key = self.validateKeys(detail_dict)
        if not are_details_valid:
            raise ValueError(f"Missing {missing_key} in [basic] configration")

        for line in automationDetail.split("\n"):
            if len(line) > 3:
                automation_arr.append(line)

        return detail_dict, automation_arr