import uuid


SESSION_BUCKET = '<YOUR_BUCKET>'

raw_annotation_path = 'GDUT-HWD/Annotations'
test_image_base_path = 'img/raw'
detection_image_base_path = 'img/detection'

# Replace before CreateEndpoint
training_job_name = '<YOUR_TRAINNING_JOB_NAME>'  

# Replace before CreateEndpoint
model_data = 's3://{}/output/{}/output/model.tar.gz'.format(SESSION_BUCKET, training_job_name)

endpoint_name = training_job_name
model_name = 'object-detector-hardhat-200ep'

container_image = '811284229777.dkr.ecr.us-east-1.amazonaws.com/object-detection:latest'

# Endpoint instance
deploy_instance_type = 'ml.m4.xlarge'
initial_instance_count = 1

# Classes
object_categories = ['none', 'red', 'yellow', 'white', 'blue']
class_colors = ['grey', 'red', 'yellow', 'white', 'blue']


# Trainning Conf
train_instance_count=1
train_instance_type='ml.p3.2xlarge'
train_volume_size = 50
train_use_spot_instances=True
train_max_wait=360000
train_max_run = 360000
input_mode = 'File'


# Hyperparameters
base_network='resnet-50'
use_pretrained_model=1
num_classes=len(object_categories)
mini_batch_size=16
epochs=200
learning_rate=0.001
lr_scheduler_step='3,6'
lr_scheduler_factor=0.1
optimizer='sgd'
momentum=0.9
weight_decay=0.0005
overlap_threshold=0.5
nms_threshold=0.45
image_shape=512
label_width=1600
num_training_samples=2539
