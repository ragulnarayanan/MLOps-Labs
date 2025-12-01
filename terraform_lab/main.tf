terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 5.0"
    }
  }
}

provider "google" {
  project = "evident-alloy-474322-q2"
  region  = "us-central1"
  zone    = "us-central1-a"
}

# VM that will run the currency converter
resource "google_compute_instance" "web_vm" {
  name         = "currency-lab-vm"
  machine_type = "e2-micro"
  zone         = "us-central1-a"

  labels = {
    environment = "lab"
    app         = "currency-converter"
  }

  tags = ["currency-app"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
      size  = 10
    }
  }

  network_interface {
    network = "default"

    access_config {
      # ephemeral public IP
    }
  }

  # Startup script: install Python + Flask and run the web app on port 5000
  metadata_startup_script = <<-EOF
    #!/bin/bash
    set -e

    apt-get update -y
    apt-get install -y python3 python3-pip

    pip3 install flask

    mkdir -p /opt/currency_app
    cd /opt/currency_app

    cat << 'PYAPP' > app.py
    from flask import Flask, request, render_template_string

    app = Flask(__name__)

    PAGE = """
    <!doctype html>
    <title>Currency Converter</title>
    <h1>Currency Converter</h1>
    <p>Rates are approximate and hard-coded for this lab.</p>
    <form method="post">
      <p>
        <label>Amount:
          <input name="amount" value="{{ amount }}" placeholder="100">
        </label>
      </p>
      <p>
        <label>From currency (USD, EUR, INR, JPY):
          <input name="from_ccy" value="{{ from_ccy }}" placeholder="USD">
        </label>
      </p>
      <p>
        <label>To currency (USD, EUR, INR, JPY):
          <input name="to_ccy" value="{{ to_ccy }}" placeholder="INR">
        </label>
      </p>
      <button type="submit">Convert</button>
    </form>

    {% if result %}
      <h2>Result</h2>
      <p>{{ result }}</p>
    {% endif %}
    """

    # base rates relative to USD (simple static demo)
    RATES = {
        "USD": 1.0,
        "EUR": 0.9,
        "INR": 83.0,
        "JPY": 150.0,
    }

    @app.route("/", methods=["GET", "POST"])
    def index():
        result = ""
        amount = ""
        from_ccy = "USD"
        to_ccy = "INR"

        if request.method == "POST":
            amount = request.form.get("amount", "").strip()
            from_ccy = request.form.get("from_ccy", "USD").strip().upper()
            to_ccy = request.form.get("to_ccy", "INR").strip().upper()

            try:
                value = float(amount)
                if from_ccy not in RATES or to_ccy not in RATES:
                    raise ValueError("Unsupported currency code")

                # convert via USD as the base
                usd_amount = value / RATES[from_ccy]
                target_amount = usd_amount * RATES[to_ccy]

                result = f"{value:.2f} {from_ccy} = {target_amount:.2f} {to_ccy}"
            except Exception as e:
                result = f"Error: {e}. Check the amount and currency codes."

        return render_template_string(
            PAGE,
            amount=amount,
            from_ccy=from_ccy,
            to_ccy=to_ccy,
            result=result,
        )

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)
    PYAPP

    # run app in background
    nohup python3 app.py > /var/log/currency_app.log 2>&1 &
  EOF
}

# Firewall rule for HTTP on port 5000
resource "google_compute_firewall" "allow_http_5000" {
  name    = "allow-http-5000"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["5000"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["currency-app"]
}

# Simple storage bucket (lab requirement)
resource "google_storage_bucket" "lab_bucket" {
  name          = "hp-currency-lab-bucket-12345"   # TODO: make globally unique
  location      = "us-central1"
  force_destroy = true
}

output "web_vm_external_ip" {
  description = "External IP of the currency app VM"
  value       = google_compute_instance.web_vm.network_interface[0].access_config[0].nat_ip
}

output "currency_app_url" {
  description = "URL of the currency converter web app"
  value       = "http://${google_compute_instance.web_vm.network_interface[0].access_config[0].nat_ip}:5000"
}
