# 🧠 HormigasAIS 影片智慧檢測器

一個由 **HormigasAIS** 社群創建的數位過濾工具，旨在檢測線上影片的真實性，對抗由合成內容所產生的錯誤資訊。

---

## 🌐 這是什麼？

這是一個**極簡風格**的網頁工具，任何使用者都可以貼上影片連結（例如 YouTube），並接收一個**視覺信號**來判斷其真實性：

- 💡 **綠色**：影片極有可能為真實（真人演出、自然場景）。
- 💡 **藍色**：影片極有可能為人工智慧生成或被操縱。

判斷過程由一個名為 **XOXO** 的 AI 微服務實時分析影片的視覺與上下文數據完成。整個架構部署在 **Render** 雲平台上。

---

## 🧱 專案結構

HormigasAIS-video-intelligence-checker/  
├── backend/                         # 使用 FastAPI 的 XOXO 微服務  
│   ├── api.py  
│   └── requirements.txt  
├── frontend/                        # 極簡風格的使用者介面  
│   └── index.html  
├── .github/  
│   └── workflows/  
│       └── deploy.yml              # GitHub Action 自動部署流程  
├── render.yaml                     # Render 雲端部署設定  
└── README.md                       # 專案主要說明文件

---

## 🚀 已部署的服務（Render）

---

### 1. 🧠 `xoxo-ai-backend`（AI 後端）

- URL: [https://thrumanshow.github.io/HormigasAIS-video-intelligence-checker/](https://thrumanshow.github.io/HormigasAIS-video-intelligence-checker/)
- 類型：Web 服務（Python）
- 埠號：8000  
- 框架：FastAPI  
- 功能：分析影片資料並傳回真實性信號  
- 區域：美國奧勒岡州

---

### 2. ⚙️ `n8n-automation-xoxo`（智慧流程自動化）

- URL: [https://n8n-automation-xoxo.onrender.com](https://n8n-automation-xoxo.onrender.com/)
- 類型：Web 服務（Docker）  
- 平台：自架 n8n  
- 功能：根據 GitHub 事件與 AI 結果，編排智慧化流程

---

### 3. 🧩 `webhook-github-action`（GitHub 監聽器）

- URL: [https://webhook-github-action.onrender.com](https://webhook-github-action.onrender.com/)
- 類型：Web 服務（Node.js）  
- 功能：監聽 GitHub 的變更並觸發事件至 n8n 或 FastAPI  
- 方案：Starter 計劃

---

## ⚙️ 本地執行方式

```bash
# 1. 複製此倉庫
git clone https://github.com/Thrumanshow/HormigasAIS-video-intelligence-checker.git
cd HormigasAIS-video-intelligence-checker

# 2. 啟動後端服務
cd backend
pip install -r requirements.txt
uvicorn api:app --reload
