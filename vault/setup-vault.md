# 🔐 Local Vault Setup Guide (Dev Mode)

This guide walks you through setting up **HashiCorp Vault locally in development mode** to securely store and retrieve secrets such as API keys, 
for local testing and future CI/CD integration.

---

## ✅ Prerequisites

- A working terminal (PowerShell, CMD, or Bash)
- Python (for demo app)
- Git (optional, for project version control)
- Optional: Chocolatey (on Windows) for easy installation

---

## 🔧 Step 1: Install Vault CLI

### On Windows (Recommended via Chocolatey)
```powershell
choco install vault
```

Or Manual Download
- Visit: https://developer.hashicorp.com/vault/downloads
- Download the appropriate Vault ZIP for Windows
- Extract to a local folder (e.g., C:\Tools\Vault)
- Add this folder to your System PATH
- Open a new terminal and confirm: 
```powershell
vault --version
```


## 🚀 Step 2: Start Vault in Dev Mode

```powershell
vault server -dev
```

This will:

- Start Vault on http://127.0.0.1:8200

- Unseal automatically for testing

- Output a Root Token (copy and save it this authenticates your session with root-level access)

📌 Important: Leave this terminal running as it is your active Vault server.

## 🌐 Step 3: Set Environment Variables in a New Terminal

Open a new terminal window and run (Replace <your-root-token> with the one shown in Step 2.):
```powershell
$env:VAULT_ADDR = "http://127.0.0.1:8200"
$env:VAULT_TOKEN = "<your-root-token>"
```
To verify the connection:
```powershell
vault status
```
You should see:
Sealed: false
Initialized: true

## 🔑 Step 4: Store a Secret

Store an API key (or any key-value pair):
```powershell
vault kv put secret/devsecops API_KEY="secret-key"
```
To verify:
```powershell
vault kv get secret/devsecops
```

## ⚙️ Step 5: Inject Secret into Flask App (Simulated Local Runtime)

Use the Vault CLI to dynamically fetch the secret and inject it at runtime:
```powershell
$env:API_KEY = $(vault kv get -field=API_KEY secret/devsecops)
python src/app.py
```
OR directly add in the .env file of the project and run by "flask run"

Navigate to:
http://127.0.0.1:5000

You should see the API key rendered in the web response


## ⚠️ Security Note
This setup is for testing and educational purposes only.
Vault dev mode:
- Is insecure (no TLS, no policies)
- Stores everything in memory
- Should never be used in production