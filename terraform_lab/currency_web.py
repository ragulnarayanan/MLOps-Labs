from flask import Flask, request, render_template_string

app = Flask(__name__)

PAGE = """
<!doctype html>
<title>Currency Converter</title>
<h1>Currency Converter</h1>
<p>Rates are approximate and hard-coded for this demo.</p>
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
    app.run(debug=True)
