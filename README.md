# **Python Application Deployment to Target Server using Jenkins CI/CD**

## **Project Overview :**

This project demonstrates CI/CD automation of a Python application using:

- Jenkins Pipeline

- GitHub Webhook

- SSH Agent Plugin

- Remote Deployment to Target Server

- Automated Build & Deployment

The application is deployed on a remote server (not on Jenkins server) using secure SSH authentication

---

## **Workflow :**

1. Developer pushes code to GitHub

2. GitHub Webhook triggers Jenkins

3. Jenkins pulls latest code

4. Jenkins installs Python dependencies

5. Jenkins connects to Target Server via SSH

6. Application is deployed on Target Server

---

## **Prerequisites :**

Jenkins Server

1. Jenkins Installed

2. Required Plugins Installed

3. Internet Access

---

### **Jenkins Plugins Used :**

| Plugin Name      | Purpose                                |
| ---------------- | -------------------------------------- |
| Git Plugin       | Pull code from GitHub repository       |
| GitHub Plugin    | Enable webhook integration with GitHub |
| SSH Agent Plugin | Provide SSH access to remote server    |
| Pipeline Plugin  | Execute Jenkinsfile (CI/CD pipeline)   |

---

## **Target Server Security Group :**

| Port | Protocol | Purpose                    |
| ---- | -------- | -------------------------- |
| 22   | TCP      | SSH access to EC2 server   |
| 80   | TCP      | HTTP traffic (Web access)  |
| 443  | TCP      | HTTPS traffic (Secure web) |
| 5000 | TCP      | Python application port    |

---

## **STEP 1: Add SSH Credentials in Jenkins**

Go to:

```
Manage Jenkins → Manage Credentials → Global → Add Credentials
```

Select:

1. Kind: SSH Username with private key

1. Username: ubuntu

1. Private Key: Enter directly and paste private key

1. ID: python-app-key

Save.

---

## **STEP 2: Update Jenkinsfile Environment Variables**

Update:

```
SERVER_IP      = 'YOUR_SERVER_IP'
SSH_CRED = 'python-app-key'
REMOTE_USER    = 'ubuntu'
APP_DIR    = '/home/ubuntu/python-app'
```

### **Environment Variables Explanation :**

- SERVER_IP: Target server public/private IP

- SSH_CRED: Jenkins SSH credential ID

- REMOTE_USER: Target server username

- APP_DIR: Deployment directory

---

## **STEP 3: Configure GitHub Webhook**

Go to GitHub repository:

```
Settings → Webhooks → Add Webhook
```

Payload URL:

```
http://<JENKINS_SERVER_IP>:8080/github-webhook/
```

Content Type:

```
application/json
```

Select:
✔ Just the push event

Save.

---

## **STEP 4: Create Jenkins Pipeline Job**

1. Click New Item

1. Select Pipeline

1. Enter Job Name

1. Select: Pipeline script from SCM

1. SCM: Git

1. Enter Repository URL

1. Branch: main

1. Script Path: Jenkinsfile

1. Enable:
   ✔ GitHub hook trigger for GITScm polling

Save.

---

## **Complete CI/CD Execution Flow**

### **1. Developer Pushes Code**

```bash
git add .
git commit -m "Updated feature"
git push origin main
```

### **2. GitHub Sends Webhook**

GitHub sends trigger to Jenkins.

### **3. Jenkins Pipeline Starts**

- Pulls latest code

- Installs dependencies

- Connects to target server

### **4. Deployment on Target Server**

- Updates code

- Installs dependencies

- Starts Python application
