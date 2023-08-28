# Define your AWS provider configuration
provider "aws" {
  region = "us-east-1"  # Change this to your desired region
}

# Create a VPC with public and private subnets
resource "aws_vpc" "my_vpc" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "public_subnet" {
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1a"  # Change this to match your desired availability zone
  map_public_ip_on_launch = true
}

resource "aws_subnet" "private_subnet" {
  vpc_id                  = aws_vpc.my_vpc.id
  cidr_block              = "10.0.2.0/24"
  availability_zone       = "us-east-1a"  # Change this to match your desired availability zone
}

# Create an EC2 instance in the public subnet
resource "aws_instance" "my_instance" {
  ami           = "ami-0c55b159cbfafe1f0"  # Amazon Linux 2 AMI (Change this to your desired AMI)
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.public_subnet.id

  root_block_device {
    volume_type           = "gp2"
    volume_size           = 5
    delete_on_termination = true
  }

  tags = {
    Name    = "AssignmentInstance"
    purpose = "Assignment"
  }
}

# Create a security group
resource "aws_security_group" "my_security_group" {
  name        = "my-security-group"
  description = "My security group"
  vpc_id      = aws_vpc.my_vpc.id

  # Inbound rule for SSH (Port 22)
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]  # Open to all sources (not recommended for production)
  }

  # Outbound rule allowing all traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Associate the security group with the EC2 instance
resource "aws_network_interface_sg_attachment" "my_sg_attachment" {
  security_group_id    = aws_security_group.my_security_group.id
  network_interface_id = aws_instance.my_instance.network_interface_ids[0]
}
