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
  region = "us-east-1"
}

resource "aws_vpc" "mat-vpc" {
  cidr_block = "10.0.0.0/16"
  assign_generated_ipv6_cidr_block = true
  tags = {
    Name = "mat-vpc"
  }
}

resource "aws_internet_gateway" "gateway-1" {
  vpc_id = aws_vpc.mat-vpc.id
}

resource "aws_egress_only_internet_gateway" "egw-1" {
  vpc_id = aws_vpc.mat-vpc.id
  tags = {
    Name = "mat-egw"
  }
}

resource "aws_route_table" "mat-route-table" {
  vpc_id = aws_vpc.mat-vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.gateway-1.id
  }

  route {
    ipv6_cidr_block        = "::/0"
    egress_only_gateway_id = aws_egress_only_internet_gateway.egw-1.id
  }

  tags = {
    Name = "matty"
  }
}

resource "aws_subnet" "subnet-1" {
  vpc_id            = aws_vpc.mat-vpc.id
  cidr_block        = "10.0.1.0/24"
  availability_zone = "us-east-1a"
  tags = {
    Name = "mat-subnet"
  }
}

resource "aws_route_table_association" "a" {
  subnet_id      = aws_subnet.subnet-1.id
  route_table_id = aws_route_table.mat-route-table.id
}

resource "aws_security_group" "allow_web" {
  name        = "allow_web_traffic"
  description = "Allow TLS inbound traffic"
  vpc_id      = aws_vpc.mat-vpc.id

  tags = {
    Name = "allow_web"
  }
}

resource "aws_vpc_security_group_ingress_rule" "allow_web_ipv4" {
  security_group_id = aws_security_group.allow_web.id
  cidr_ipv4         = aws_vpc.mat-vpc.cidr_block
  from_port         = 443
  ip_protocol       = "tcp"
  to_port           = 443
}

resource "aws_vpc_security_group_egress_rule" "allow_all_traffic_ipv4" {
  security_group_id = aws_security_group.allow_web.id
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = "-1"
}

resource "aws_vpc_security_group_egress_rule" "allow_all_traffic_ipv6" {
  security_group_id = aws_security_group.allow_web.id
  cidr_ipv6         = "::/0"
  ip_protocol       = "-1"
}

resource "aws_network_interface" "web-server-interface" {
  subnet_id       = aws_subnet.subnet-1.id
  private_ips     = ["10.0.1.50"]
  security_groups = [aws_security_group.allow_web.id]
}

resource "aws_eip" "web-eip" {
  vpc                       = true
  network_interface         = aws_network_interface.web-server-interface.id
  associate_with_private_ip = "10.0.1.50"
  depends_on                = [aws_internet_gateway.gateway-1]
}

resource "aws_key_pair" "main_key" {
  key_name   = "main-key"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC7hKMvj3WCiWa6KccEJEWtpEwysiHYP+MP2PH74FU7WAYz0CJRVicKrxsLoMhradsOoNEyN/KMetahH4DApsvu4qOM1JcWSvMMEcHealulIzodETxnFYv0PmqyKknNDFgvGdlfM3svy3mJFDHYnzfyZjwU65M0i64UQt2flvD+MrM0Spi7TB9LSRqM9vezJ6DNuSEDbHWK8g2ltuOznflnQRnZD63fqE684rlIGtkBTPr0spTu+QrJxw+e2R+ZGF4d1cdp2t3AQgWxovHAVC9BRJe8mOWRDiZ9pdBPL6oVNB6iWB9OB1BD36wRPk/1vpR+rPggHLi9d8C2/CHzZvqT"
}

resource "aws_instance" "web-server-instance" {
  ami               = "ami-0453ec754f44f9a4a"
  instance_type     = "t2.micro"
  availability_zone = "us-east-1a"
  key_name          = aws_key_pair.main_key.key_name
  network_interface {
    device_index           = 0
    network_interface_id   = aws_network_interface.web-server-interface.id
  }

  user_data = <<-EOF
              #!/bin/bash
              sudo apt update -y
              sudo apt install apache2 -y
              sudo systemctl start apache2
              sudo bash -c 'echo This is my Web server > /var/www/html/index.html'
              EOF

  tags = {
    Name = "web-project"
  }
}
