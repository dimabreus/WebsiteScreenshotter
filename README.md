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

- Show errors under the input field:
  - Client-side URL validation
  - API error messages

### Back-End

- Cache screenshots and reuse them to save resources

