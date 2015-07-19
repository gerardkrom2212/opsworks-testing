import boto3

# ====== Stacks ========

def stackId_from_name(name):
    stacks = ops_client.describe_stacks()
    if stacks == None: return None

    for stack in stacks['Stacks']:
        if stack['Name'] == name:
            return stack['StackId']
    return None

def stackNames():
    stacks = ops_client.describe_stacks()
    if stacks == None: return ''
    return [stack['Name'] for stack in stacks['Stacks']]

# ======== Layers ==========

def layerId_from_stackId_and_name(stackId, layerName):
    resp = ops_client.describe_layers(StackId=stackId)
    for layer in resp['Layers']:
        if layer['Name'] == layerName:
            return layer['LayerId']
    return None


# ======== Load Balancers ==========

def lbNames():
    lbs = elb_client.describe_load_balancers()
    if lbs == None: return ''
    # from trepan.api import debug; debug()
    return [lb['LoadBalancerName'] for lb in lbs['LoadBalancerDescriptions']]

# ======== Instances ==========

def instanceId_from_hostname(host_name, layerName):
    ec2InstanceId = None
    resp = ec2_client.describe_instances()
    # import pprint
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(resp)
    for res in resp['Reservations']:
        instance = res['Instances'][0]
        if 'Tags' in instance.keys():
            tags = instance['Tags']
            for tag in tags:
                if tag['Key'] == 'opsworks:instance' and tag['Value'] == host_name:
                    return instance['InstanceId']
    return None


# ======== Client Init ==========

ec2_client = boto3.client('ec2')
elb_client = boto3.client('elb')
ops_client = boto3.client('opsworks')
