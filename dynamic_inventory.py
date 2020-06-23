#!/usr/bin/env python

import boto3
import json

def main():
    ec2 = boto3.resource('ec2','ap-south-1')
    db_group = get_hosts(ec2,'db')
    app_group = get_hosts(ec2,'app')
    all_group = {'db': db_group, 'app': app_group}
    print (json.dumps(all_group))

def get_hosts(ec2,fv):
    events = []
    filters = {'Name': 'tag:Name', 'Values': [fv]}
    for i in ec2.instances.filter(Filters=[filters]):
       events.append(i.public_ip_address)
    return events

if __name__ == "__main__":
    main()
