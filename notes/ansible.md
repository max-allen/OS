Ansible

- Deployments (k8s, EB), Task Automation, Configuration Management
- IaC: Infrastructure as Code. Specified lists of actions run against collections of host machines
- Playbooks (Runbooks)

Clients: AWX, Ansible CLI

### Components

![Component Diagram](https://s3.amazonaws.com/ma.notes.images/ansible_components.png)

**Control node**

System where ansible is installed. Commands (`ansible-playbook`, `ansible-vault`, etc.) are run against control nodes.

**Managed node**

Remote system that Ansible controls. Also known as a _host_.

**Inventory**

List of logically organized managed nodes. Created on the control node to describe host deployments.


