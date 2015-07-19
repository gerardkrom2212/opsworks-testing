import boto3

# ====== Stacks ========

def stackId_from_name(name):
    """Return the stack id for a given stack name.
    A stack id is generally needed as a parameter to a number of Opsworks
    methods, like describe_layers().
    """
    stacks = ops_client.describe_stacks()
    if stacks == None: return None

    for stack in stacks['Stacks']:
        if stack['Name'] == name:
            return stack['StackId']
    return None

def stackNames():
    """Return a list of all of the Opsworks stacks"""
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

def instanceId_from_hostname_and_stack(hostname, stackName=None):
    """Return a single ec2 instance whos hostname is *hostname*.
    If stackName not given, limit the host to that Opsworks stack.
    """
    instances = []
    resp = ec2_client.describe_instances()
    # import pprint
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(resp)
    for res in resp['Reservations']:
        instance = res['Instances'][0]
        if 'Tags' in instance.keys():
            tags = instance['Tags']
            for tag in tags:
                if tag['Key'] == 'opsworks:instance' and tag['Value'] == hostname:
                    instances.append(instance)
                    pass
                pass
            pass
        pass

    if stackName is not None:
        for instance in instances:
            tags = instance['Tags']
            for tag in tags:
                if tag['Key'] == 'opsworks:stack' and tag['Value'] == stackName:
                    return instance['InstanceId']
                pass
            pass
        pass
    else:
        return instances[0]['InstanceId']
    return None


def instanceIds_from_stack(stackName):
    """Return all ec2 instance ids in *stackName*"""
    instances = []
    resp = ec2_client.describe_instances()
    for res in resp['Reservations']:
        instance = res['Instances'][0]
        if 'Tags' in instance.keys():
            tags = instance['Tags']
            for tag in tags:
                if tag['Key'] == 'opsworks:stack' and tag['Value'] == stackName:
                    instances.append(instance['InstanceId'])
                    pass
                pass
            pass
        pass
    return instances

def opsInstanceIds_from_stack(stackName):
    """Return all Opsworks instance ids in *stackName*"""
    instances = []
    resp = ops_client.describe_instances()
    # for res in resp['Reservations']:
    #     instance = res['Instances'][0]
    #     if 'Tags' in instance.keys():
    #         tags = instance['Tags']
    #         for tag in tags:
    #             if tag['Key'] == 'opsworks:stack' and tag['Value'] == stackName:
    #                 instances.append(instance['InstanceId'])
    #                 pass
    #             pass
    #         pass
    #     pass
    return instances


# ======== Client Init ==========

ec2_client = boto3.client('ec2')
elb_client = boto3.client('elb')
ops_client = boto3.client('opsworks')
