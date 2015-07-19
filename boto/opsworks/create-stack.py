#!/usr/bin/env python
import os, sys
from myboto3 import ops_client, stackNames

stackName = 'BotoTest'
if not(1 <= len(sys.argv) <= 2):
    print("""usage: %s [*StackName*]

Create Opworks stack for php cachet test application.
The default stack is %s.""" % (os.path.basename(sys.argv[0]), stackName))
    sys.exit(1)

if len(sys.argv) == 2: stackName = sys.argv[1]

if stackName in stackNames():
    print("Stack %s already exists, nothing done" % stackName)
    sys.exit(2)

try:
    sshKey = open("/home/rocky/.ssh/bitbucket4behance", 'r').read()
except:
    print("Warning: couldn't read ssh key, using a bogus one")
    sshKey = 'You need to fix this up'


result = ops_client.create_stack(
    # Required parameters
    Name=stackName,
    ServiceRoleArn='arn:aws:iam::587255138864:role/aws-opsworks-service-role',
    DefaultInstanceProfileArn='arn:aws:iam::587255138864:instance-profile/aws-opsworks-ec2-role',  # NOQA

    # Optional parameters, sorted alphabetically
    Attributes={
        'Color': 'rgb(135, 61, 98)'
        },
    ChefConfiguration={
        'BerkshelfVersion': '3.2.0',
        'ManageBerkshelf': True,
        },
    ConfigurationManager={
        'Name': 'Chef',
        'Version': '11.10'
        },
    CustomCookbooksSource={
        'SshKey': sshKey,
        'Type': 'git',
        'Url': 'git@bitbucket.org:rockybernstein/opsworks-testing.git',
        },
    DefaultAvailabilityZone='us-east-1a',
    DefaultOs='Ubuntu 14.04 LTS',
    DefaultRootDeviceType='ebs',
    DefaultSshKeyName='rocky-key-pair-useast1',
    # Would like: "Layer Dependent" below which is
    # what happens when setting up by hand,
    # but that isn't allowed past validation
    HostnameTheme='Fruits',
    Region='us-east-1',
    UseCustomCookbooks=True,
    UseOpsworksSecurityGroups=True,
    )
print(result)
