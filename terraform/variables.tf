variable "aws_region" {
  description = "The AWS region to deploy resources in."
  type        = string
  default     = "us-east-1"
}

variable "ec2_instance_type" {
  description = "The EC2 instance type."
  type        = string
  default     = "t2.micro"
}

variable "ec2_ami" {
  description = "The AMI ID for the EC2 instance (Ubuntu 22.04 LTS in us-east-1)."
  type        = string
  default     = "ami-053b0d53c279acc90"
}
