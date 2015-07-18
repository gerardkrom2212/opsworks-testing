import boto3

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
    # from trepan.api import debug; debug()
    return [stack['Name'] for stack in stacks['Stacks']]

def layerId_from_stackId_and_name(stackId, layerName):
    resp = ops_client.describe_layers(StackId=stackId)
    for layer in resp['Layers']:
        if layer['Name'] == layerName:
            return layer['LayerId']
    return None


ops_client = boto3.client('opsworks')
elb_client = boto3.client('elb')
