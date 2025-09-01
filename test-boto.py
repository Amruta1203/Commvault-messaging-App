import boto3
ec2 = boto3.resource('ec2',region_name='us-east-1')
for instance in ec2.instances.all():
    print(instance.id, instance.state)

client = boto3.client('ec2',region_name='us-east-1')
response = client.create_vpc(
    CidrBlock='89.207.132.170/16'
)

print(response)
client = boto3.client('rds',region_name='us-east-1')
response = client.create_db_instance(
    AllocatedStorage=5,
    DBInstanceClass='db.t3.micro',
    DBInstanceIdentifier='mymysqlinstance',
    Engine='MySQL',
    MasterUserPassword='Enter your password',
    MasterUsername='Enter your username',
    #EngineVersion='8.0.35'
)

print(response)