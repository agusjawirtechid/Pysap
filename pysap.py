import requests, threading, json, time, os, uuid, base64

db = "https://grouo-592e9-default-rtdb.asia-southeast1.firebasedatabase.app"
history_file = "history.txt"
config_file = "user_config.txt"

def enc(s):
    s = base64.b64encode(s.encode()).decode()
    s = base64.b64encode(s.encode()).decode()
    return base64.b64encode(s.encode()).decode()

def dec(s):
    s = base64.b64decode(s).decode()
    s = base64.b64decode(s).decode()
    return base64.b64decode(s).decode()

def save_local(user, msg):
    with open(history_file, "a") as f:
        f.write(enc(f"{user}:{msg}") + "\n")

def load_local():
    if not os.path.exists(history_file):
        return []
    lines = open(history_file).read().splitlines()
    decoded = []
    for x in lines:
        try:
            decoded.append(dec(x))
        except:
            pass
    return decoded

def save_user_config(username):
    """Simpan username untuk login otomatis"""
    with open(config_file, "w") as f:
        f.write(enc(username))

def load_user_config():
    """Load username yang tersimpan"""
    if not os.path.exists(config_file):
        return None
    try:
        with open(config_file, "r") as f:
            encrypted_username = f.read().strip()
            return dec(encrypted_username)
    except:
        return None

def color(c,s):
    return f"{c}{s}\033[0m"

def send(user, msg):
    requests.post(f"{db}/chat.json", json={"user":user,"msg":msg,"time":time.time()})

def sys(msg):
    requests.post(f"{db}/chat.json", json={"type":"system","msg":msg,"time":time.time()})

def listen(username):
    url = f"{db}/chat.json"
    etag = None

    while True:
        headers = {"X-Firebase-ETag":"true"}
        if etag:
            headers["If-None-Match"] = etag

        try:
            r = requests.get(url, headers=headers, timeout=60)

            if r.status_code == 200:
                etag = r.headers.get("ETag")
                data = r.json()

                os.system("clear")
                print(color("\033[91m","🔥 Realtime Chat\n"))

                # tampilkan history lokal dulu
                for line in load_local():
                    user, msg = line.split(":",1)
                    if user == username:
                        print(color("\033[93m",f"{user}: {msg}"))
                    else:
                        print(color("\033[92m",f"{user}: {msg}"))

                # tampilkan online history
                if data:
                    sorted_items = sorted(data.items(), key=lambda x: x[1].get("time",0))
                    for _, m in sorted_items:
                        if m.get("type") == "system":
                            print(color("\033[91m",f"⚠ {m['msg']}"))
                        else:
                            if m["user"] == username:
                                print(color("\033[93m",f"{m['user']}: {m['msg']}"))
                            else:
                                print(color("\033[92m",f"{m['user']}: {m['msg']}"))

                print(color("\033[93m",f"\n{username}: "), end="", flush=True)

            elif r.status_code == 304:
                continue

        except requests.exceptions.RequestException:
            print(color("\033[91m", "\nKoneksi terputus, mencoba kembali..."))
            time.sleep(5)
            continue

        time.sleep(0.1)

# ==== LOGIN OTOMATIS ====
saved_username = load_user_config()

if saved_username:
    print(f"Selamat datang kembali, {saved_username}!")
    use_saved = input("Gunakan username ini? (y/n): ").strip().lower()
    
    if use_saved == 'y':
        username = saved_username
    else:
        username = input("Masukkan username baru: ").strip()
        save_user_config(username)
else:
    username = input("Masukkan username: ").strip()
    save_user_config(username)

# Mulai aplikasi
sys(f"{username} JOINED")
os.system("clear")

threading.Thread(target=listen, args=(username,), daemon=True).start()

while True:
    try:
        msg = input(color("\033[93m",f"{username}: "))
        if msg.strip() == "":
            continue
        if msg.lower() == "/logout":
            sys(f"{username} LEFT")
            print("\nLogout berhasil!")
            break
        
        save_local(username, msg)
        send(username, msg)

    except KeyboardInterrupt:
        sys(f"{username} LEFT")
        print("\nKeluar...")
        break