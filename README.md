# 🧠 HormigasAIS 影片智慧檢測器

[![XOXO AI Backend 狀態](https://img.shields.io/website?url=https%3A%2F%2Fxoxo-ai-backend.onrender.com&label=XOXO%20AI%20Backend&style=flat-square)](https://xoxo-ai-backend.onrender.com)
[![前端頁面狀態](https://img.shields.io/website?url=https%3A%2F%2Fn8n-automation-xoxo.onrender.com&label=n8n%20%2F%20Frontend&style=flat-square)](https://n8n-automation-xoxo.onrender.com)
[![GitHub 最後提交](https://img.shields.io/github/last-commit/Thrumanshow/HormigasAIS-video-intelligence-checker?style=flat-square)](https://github.com/Thrumanshow/HormigasAIS-video-intelligence-checker)

一個由 **HormigasAIS** 社群創建的數位過濾工具，旨在檢測線上影片的真實性，對抗由合成內容所產生的錯誤資訊。

---

## 🌐 這是什麼？

這是一個 **極簡風格** 的網頁工具，任何使用者都可以貼上影片連結（例如 YouTube），並接收一個 **視覺信號** 來判斷其真實性：

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

# HormigasAIS Video Intelligence Checker - SaaS 服務許可證

本倉庫包含 **HormigasAIS Video Intelligence Checker** 服務的官方許可證文件。

## 許可證檔案

1. **繁體中文（原始版）**  
   - 檔案: [LICENSE_SaaS.md](./LICENSE_SaaS.md)  
   - 國際使用與主要法律參考。

2. **西班牙文**  
   - 檔案: [LICENSE_SaaS_ES.md](./LICENSE_SaaS_ES.md)  
   - 官方西班牙文翻譯，供西語使用者使用。

3. **英文**  
   - 檔案: [LICENSE_SaaS_EN.md](./LICENSE_SaaS_EN.md)  
   - 官方英文翻譯，供國際使用者使用。

---     

## 🚀 已部署的服務（Render）

### 1. 🧠 `xoxo-ai-backend`（AI 後端）

- URL: [https://xoxo-ai-backend.onrender.com](https://xoxo-ai-backend.onrender.com/)
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
```
---

```bash
Configuración del servicio xoxo en Termux

Este módulo utiliza termux-services para ejecutar XOXO como un servicio persistente en segundo plano.

1. Crear la estructura del servicio
mkdir -p "$PREFIX/var/service/XOXO"

2. Crear el archivo run
cat > "$PREFIX/var/service/XOXO/run" << 'EOF'
#!/data/data/com.termux/files/usr/bin/sh
# Servicio XOXO - HormigasAIS
while true; do
    echo "XOXO está activo..."
    sleep 5
done
EOF

3. Hacer ejecutable el archivo run
chmod +x "$PREFIX/var/service/XOXO/run"

4. Normalizar el nombre del servicio (Termux solo acepta minúsculas)
if [ -d "$PREFIX/var/service/XOXO" ]; then
    echo "Corrigiendo nombre del servicio XOXO → xoxo..."
    mv "$PREFIX/var/service/XOXO" "$PREFIX/var/service/xoxo"
fi

5. Verificar que termux-services esté instalado
if ! command -v sv >/dev/null 2>&1; then
    echo "⚠️ termux-services no está instalado."
    echo "Instálalo con: pkg install termux-services"
fi

6. Iniciar el servicio
sv up xoxo

7. Verificar el estado del servicio
sv status xoxo
```
