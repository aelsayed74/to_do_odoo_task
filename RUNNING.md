# Running the Odoo To-Do Module

## Quick Summary

Your Odoo module requires:
1. **PostgreSQL** database
2. **Odoo 16** server
3. Your module in the addons path

---

## Option 1: Docker (Easiest & Recommended)

No need to install anything. Just use Docker:

```bash
# From PowerShell/CMD in project directory
cd e:\to_do_odoo_task
docker-compose up -d
```

Access Odoo at: **http://localhost:8069**

**Advantages:**
- Single command setup
- No local dependencies
- Production-ready

---

## Option 2: WSL with Local Setup

### Prerequisites
- WSL2 with Ubuntu/Debian
- PostgreSQL installed

### Step 1: Quick Setup (5 minutes)

```bash
wsl bash /mnt/e/to_do_odoo_task/setup-wsl.sh
```

### Step 2: Set up PostgreSQL

#### Option A: Docker for PostgreSQL (Recommended)

```bash
docker run -d \
  -e POSTGRES_PASSWORD=odoo \
  -e POSTGRES_USER=odoo \
  -e POSTGRES_DB=odoo \
  -p 5432:5432 \
  postgres:15
```

#### Option B: WSL PostgreSQL

```bash
# In WSL
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
sudo service postgresql start
sudo -u postgres psql -c "CREATE USER odoo WITH CREATEDB PASSWORD 'odoo';"
sudo -u postgres psql -c "ALTER USER odoo SUPERUSER;"
```

### Step 3: Install Odoo from GitHub

```bash
# In WSL (first time only)
mkdir -p ~/odoo-src
cd ~/odoo-src
git clone https://github.com/odoo/odoo.git --depth 1 --branch 16.0 odoo
cd odoo
pip install -e .
```

### Step 4: Run Odoo

```bash
# In WSL, from project directory
cd /mnt/e/to_do_odoo_task
source .venv/bin/activate
odoo -c odoo.conf
```

Access Odoo at: **http://localhost:8069**

---

## Option 3: Windows Native (Advanced)

If you prefer running everything on Windows:

1. **Install PostgreSQL for Windows**
   - Download from: https://www.postgresql.org/download/windows/

2. **Download Odoo 16**
   - From: https://github.com/odoo/odoo/releases/tag/16.0
   - Or: https://www.odoo.com/download

3. **Add module to addons path**
   ```
   C:\path\to\odoo\addons\to_do_odoo_task
   ```

4. **Run Odoo**
   ```bash
   python odoo-bin -c odoo.conf
   ```

---

## Troubleshooting

### PostgreSQL Connection Error

```
ERROR: could not connect to server: Connection refused
```

**Solution:** 
- Ensure PostgreSQL is running
- Check connection details in `odoo.conf`
- Default: localhost, port 5432, user: odoo, password: odoo

### Port Already in Use

```
Address already in use
```

**Solution:**
Change port in `odoo.conf`:
```ini
http_port = 8070
xmlrpc_port = 8072
```

### Module Not Found

```
WARNING: module not found: to.do
```

**Solution:**
- Ensure `--addons-path` includes current directory: `odoo -c odoo.conf`
- Check `__manifest__.py` exists in module root

### Import Errors

```
ModuleNotFoundError: No module named 'odoo'
```

**Solution:**
- Activate virtual environment: `source .venv/bin/activate`
- Ensure Odoo is installed: `pip install -e ~/odoo-src/odoo`

---

## Installation Verification

After setup, verify everything works:

```bash
# Check Python environment
source .venv/bin/activate
python -c "import odoo; print(odoo.__version__)"

# Check PostgreSQL connection
psql -h localhost -U odoo -d odoo -c "SELECT 1;"

# Check module files
ls -la
# Should show: __manifest__.py, models/, views/, reports/, security/
```

---

## Next Steps

1. Create/login to Odoo database at http://localhost:8069
2. Install the "To do" module from Apps
3. Test the module functionality

---

## Recommended Setup Path

1. **For Development:** Use Option 2 (WSL + Local Odoo)
2. **For Testing:** Use Option 1 (Docker)
3. **For Production:** Use Docker with proper configurations
