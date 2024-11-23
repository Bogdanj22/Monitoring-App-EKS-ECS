import boto3

# Specify the region explicitly
ecr_client = boto3.client('ecr', region_name='eu-central-1')  # Replace with your desired region

repository_name = "my_monitoring_app_image"
response = ecr_client.create_repository(repositoryName=repository_name)

repository_uri = response['repository']['repositoryUri']
print(repository_uri)
