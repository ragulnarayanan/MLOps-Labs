# Terraform GCP Lab – Currency Converter App  

### Changes I Made in This Lab
This lab originally required only creating a simple VM using Terraform.  
I enhanced the assignment into a complete cloud deployment project by adding:

- A fully working **Flask Currency Converter App**.
- A complete startup script that installs Python, pip, and Flask automatically.
- A new **firewall rule** publicly exposing port **5000**.
- A **Cloud Storage bucket** created using Terraform.
- Helpful **Terraform outputs** (`app_url`, `web_vm_external_ip`).
- Step-by-step screenshots stored in the `assets/` folder.

---

# Overview
This project uses **Terraform** to deploy an end-to-end cloud environment on **Google Cloud Platform (GCP)** and automatically run a **Currency Converter Flask Web App** on a Compute Engine VM.

Once deployed, the app is accessible at:

"http://<EXTERNAL_IP>:5000"

---

# What Terraform Builds

## Compute Engine VM – `currency-lab-vm`
Terraform automatically provisions:

- Machine: **e2-micro**
- OS: **Debian 11**
- Zone: **us-central1-a**
- Network tag: `currency-app`
- Startup script that:
  - Updates apt packages  
  - Installs Python3 + pip  
  - Installs Flask  
  - Creates `/opt/currency_app/app.py`  
  - Runs the Flask app on **port 5000**

---

## Firewall Rule – `allow-http-5000`
- Network: `default`
- Opens **TCP 5000** to the internet
- Applies only to VMs with the tag `currency-app`

---

## Cloud Storage Bucket – `hp-currency-lab-bucket-12345`
- Region: `us-central1`
- `force_destroy = true` (so `terraform destroy` works cleanly)

---

## Terraform Outputs
After deployment, Terraform prints:

- **`web_vm_external_ip`**
- **`currency_app_url`** → `http://<EXTERNAL_IP>:5000`

---

## How to Run

From the repo root:

    cd Terraform_Labs

### Authenticate to GCP

Export a service-account key:

    export GOOGLE_APPLICATION_CREDENTIALS="D:/terraform-key.json"

Make sure `main.tf` has the correct `project` ID.

### Terraform workflow

    terraform init
    terraform plan
    terraform apply

After `apply` you should see something like:

    Outputs:
    app_url        = "http://<EXTERNAL_IP>:5000"
    vm_external_ip = "<EXTERNAL_IP>"

### Open the app

Visit `app_url` in the browser and use the form to convert between currencies.

### Destroy when done

    terraform destroy

This removes the VM, firewall rule, and bucket.
