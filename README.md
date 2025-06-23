由 **HormigasAIS** 社群創造並為其服務的數位過濾器，目的在於偵測線上影片的真實性，並對抗由合成內容所產生的假消息。 

--- 

## 🌐 這是什麼？ 

本專案是一個**簡約**的網路工具，可讓任何使用者貼上影片的連結（例如來自 YouTube），並接收有關其真實性的**視覺信號： 

- 💡**綠色**：真實可能性高的影片（真實演員、自然場景）。
- 藍色**：人工智慧產生或操控的可能性很高的影片。 

評估由一個名為 **XOXO**的人工智慧微服務執行，它會即時分析視訊中的視覺和情境資料。所有這些都在部署於 **Render** 的分散式架構上執行。 

--- 

## 🧱 專案結構 

AntsAIS-video-intelligence-checker/  
├─── 後端/ # # 在 FastAPI 上的 XOXO 微服務  
│ ├─── api.py  
│ └──── requirements.txt  
├──── frontend/ # 極簡的使用者介面  
│ └── index.html  
├── .github/  
│ └└──工作流程/  
  
├──── render.yaml # 渲染配置  
└└──── README.md # 主要說明文件 

透過 DeepL.com（免費版）翻譯 

--- 

### 🚀 在生產中部署的服務 (Render) 

### 1. 🧠 `xoxo-ai-backend` (IA 後端) 

- URL： [https://xoxo-ai-backend.onrender.com](https://xoxo-ai-backend.onrender.com/)
- 類型：Web 服務 (Python)
- 連接埠：8000  
- 架構：FastAPI  
- 功能： 分析視訊資料並傳送真實性信號。 
- 區域：Oregon 

--- 

### 2. ⚙️ `n8n-automation-xoxo` (Intelligent Automation) 

- URL： [https://n8n-automation-xoxo.onrender.com](https://n8n-automation-xoxo.onrender.com/)
- 類型：Web 服務 (Docker)  
- 平台：n8n 自託管  
- 功能：利用 GitHub 事件和 AI 結果進行智慧型流程協調。 

--- 

### 3. 🧩 `webhook-github-action` (監聽 GitHub) 

- URL： [https://webhook-github-action.onrender.com](https://webhook-github-action.onrender.com/)
- 類型： Web 服務 (Node.js)  
- 功能： 監聽 GitHub 上的變更，並將事件傳送至 n8n 或 FastAPI。 
- 計劃：啟動 

--- 

## ⚙️ 本地執行 

````bash
# 1. 克隆版本庫
git clone https://github.com/Thrumanshow/HormigasAIS-video-intelligence-checker.git
cd HormigasAIS-video-intelligence-checker 

# 2. 執行後端
cd backend
pip install -r requirements.txt
uvicorn api:app --reload 

