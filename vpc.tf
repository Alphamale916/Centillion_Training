terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "us-east-1"
  
}

resource "aws_vpc" "ref-vpc" {
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "network"
  }
}

resource "aws_subnet" "subnet-1" {
  vpc_id     = aws_vpc.ref-vpc.id
  cidr_block = "10.0.1.0/24"

  tags = {
    Name = "net-subnet"
  }
}