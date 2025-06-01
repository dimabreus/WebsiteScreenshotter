# WebsiteScreenshotter

A web app that allows users to take screenshots of any public website.

![Video showcase](https://github.com/user-attachments/assets/3f3f0cd7-0ae4-43f9-bf71-508f26a12230)

---

## 🚀 Installation & Running

### 📋 Prerequisites
- `git`
- `node` (v18+ recommended)
- `npm`
- `python 3.9+`

---

### 🔧 Environment Variables

#### Front-End (`client/.env`)

```env
VITE_API_URL=http://localhost:8800/ # Back-End url
TURNSTILE_SITE_KEY=1x00000000000000000000AA # Cloudflare Turnstile Site Key
```

#### Back-End (`server/.env`)

```env
TURNSTILE_SECRET_KEY=1x0000000000000000000000000000000AA # Cloudflare Turnstile Secret Key
```
---

### 🖼️ Front-End Setup

```bash
git clone https://github.com/dimabreus/WebsiteScreenshotter.git
cd WebsiteScreenshotter/client
npm install
npm run dev
````

Frontend will be available at `http://localhost:5173`.

---

### ⚙️ Back-End Setup

```bash
cd ../server
pip install -r requirements.txt
python src/server/main.py
```

Backend will run on `http://localhost:8800`.

---

## 📡 API

All available endpoints, request/response models, and validation details are documented at:

🔗 [https://websitescreenshotter.onrender.com/docs](https://websitescreenshotter.onrender.com/docs)

---

## ✅ TODO

### Front-End

- Add favicon

### Back-End

- Cache screenshots and reuse them to save resources
