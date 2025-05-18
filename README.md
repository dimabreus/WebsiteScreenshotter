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

### POST `/take_screenshot`

Takes a screenshot of the provided website.

#### Request body (JSON)

```json
{
  "website": "https://example.com"
}
```

#### Possible responses

| Code | Message                 | Description                   |
| ---- | ----------------------- | ----------------------------- |
| 200  | OK                      | Screenshot taken successfully |
| 400  | Website URL is required | No `website` field in request |
| 400  | Invalid website URL     | Failed basic validation check |

#### Sample 200 OK Response

```json
{
  "code": 200,
  "message": "OK",
  "data": "base64-encoded-image"
}
```

#### 🌐 URL Validation Logic

The provided website URL must be publicly accessible and include a valid protocol (`http://` or `https://`), otherwise the server will reject it.

---

## ✅ TODO

### Front-End

* Show errors under the input field:

  * Client-side URL validation
  * API error messages

### Back-End

* Cache screenshots and reuse them to save resources
* Add rate limiting to the `/take_screenshot` endpoint

