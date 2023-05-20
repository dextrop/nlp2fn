'''
The file check for the environment where jennie is running.
Check for each env
- Angular : check if angular.json and package.json file is present
- React : if package.json is present with react dependencies
- NodeJS : if package.json is present with express dependencies
- Django : if manage.py file is present in the directory
- Chrome Extension: if manifest.json file is present with proper structure
- Golang: check if go.mod file is present in the directory
- Terraform: if any "*.tf" file is present in the directory
- Docker: if any Dockerfile is present in the directory
- Packer: if any "*.pkr.hcl" file is present in the directory
- Jennie: if any jennie.conf file is present in the directory.

Usage:
    DetectEnvironment().identify_platform("/path/to/detect")
'''
import os
import json

PLATFORM_ANGULAR = "angular"
PLATFORM_DJANGO = "django"
PLATFORM_NODEJS = "nodejs"
PLATFORM_REACT = "react"
PLATFORM_CHROME_PLUGIN = "react"
PLATFORM_TERRAFORM = "terraform"
PLATFORM_PACKER = "packer"
PLATFORM_DOCKER = "docker"
PLATFORM_JENNIE = "jennie"
PLATFORM_GOLANG = "golang"

class DetectEnvironment():
    def has_permission(self, directory):
        if os.access(directory, os.R_OK):
            return True
        print(f"No permission to access the directory: {directory}")
        return False

    def isPresent(self, dir, file):
        return os.path.isfile(os.path.join(dir, file))

    def identify_platform(self, directory):
        if not self.has_permission(directory):
            raise ValueError("Unknown due to permission issues")

        if self.isPresent(directory, 'package.json') and self.isPresent(directory, 'angular.json'):
            return PLATFORM_ANGULAR

        if self.isPresent(directory, 'package.json'):
            with open(os.path.join(directory, 'package.json')) as file:
                package_json = json.load(file)
                dependencies = package_json.get('dependencies', {})
                devDependencies = package_json.get('devDependencies', {})
                all_dependencies = {**dependencies, **devDependencies}
                if 'react' in all_dependencies:
                    return PLATFORM_REACT
                elif 'express' in all_dependencies:
                    return PLATFORM_NODEJS

        if os.path.isfile(os.path.join(directory, 'manage.py')):
            return PLATFORM_DJANGO

        if os.path.isfile(os.path.join(directory, 'manifest.json')):
            with open(os.path.join(directory, 'manifest.json')) as file:
                if 'browser_action' in json.load(file) or 'page_action' in json.load(file):
                    return PLATFORM_CHROME_PLUGIN

        if os.path.isfile(os.path.join(directory, 'go.mod')):
            return PLATFORM_GOLANG

        # Additional checks
        if any(fname.endswith('.tf') for fname in os.listdir(directory)):
            return PLATFORM_TERRAFORM

        if 'Dockerfile' in os.listdir(directory):
            with open(os.path.join(directory, 'Dockerfile')) as file:
                if file.read().strip():
                    return PLATFORM_PACKER

        if any(fname.endswith('.pkr.hcl') for fname in os.listdir(directory)):
            return PLATFORM_DOCKER

        if "jennie.conf" in os.listdir(directory):
            return PLATFORM_JENNIE

        raise ValueError('Unknown Platform, jennie is not configured for current environment')
