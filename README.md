# ♻️ Waste Classification & Awareness App

**A Deep Learning-Powered Solution for Environmental Awareness and Sustainable Waste Management**

---

## 🌍 Overview

The **Waste Classification & Awareness App** is an intelligent web application that uses deep learning to classify waste materials and educate users about their environmental impact. Users can upload images of waste, get instant classification predictions, and receive comprehensive information about:

- What type of waste it is
- Environmental impact of that waste material
- DIY tips for reducing, reusing, and recycling locally

This project aims to bridge the gap between waste management and individual action, empowering people to make informed decisions about their waste.

---

## ✨ Features

✅ **Real-time Waste Classification** - Upload an image and get instant predictions using a trained neural network
✅ **10 Waste Categories** - Classifies battery, organics, cardboard, glass, metal, paper, plastic, shoes, clothes, and trash
✅ **Environmental Impact Data** - Detailed information about how each waste type affects the environment
✅ **Local Action Guidelines** - DIY tips and techniques for reducing and reusing waste at home
✅ **User-Friendly Interface** - Built with Streamlit for quick, intuitive interactions
✅ **High Accuracy Model** - MobileNetV2-based CNN with **93.96% test accuracy** trained on comprehensive waste datasets
✅ **Responsive Design** - Works on desktop and mobile devices

---

## 🎯 Project Goals

1. **Raise Environmental Awareness** - Help people understand the true impact of their waste
2. **Empower Individual Action** - Provide practical DIY solutions that anyone can implement
3. **Promote Sustainable Practices** - Encourage recycling, composting, and waste reduction


---

## 🛠️ Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **Web Framework** | Streamlit | 1.35.0 |
| **Deep Learning** | TensorFlow | 2.21.0 |
| **Pre-trained Model** | MobileNetV2 | Keras Applications |
| **Model Format** | Keras (.keras) | Native TensorFlow |
| **Numerical Computing** | NumPy | 1.26.4 |
| **Image Processing** | Pillow | 10.0.0 |
| **Python** | Python | 3.11.4 |

---

## 📥 Installation

### Prerequisites
- Python 3.11+ installed on your system
- pip (Python package manager)
- Git (for cloning the repository)

### Steps

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/waste-classifier.git
cd waste_streamlit_app
```

2. **Create Virtual Environment**
```bash
python -m venv venv
```

3. **Activate Virtual Environment**
- **Windows:**
```bash
.\venv\Scripts\Activate.ps1
```
- **Mac/Linux:**
```bash
source venv/bin/activate
```

4. **Install Dependencies**
```bash
pip install -r requirements.txt
```

5. **Create .env File** (Optional)
Create a `.env` file in the project root:
```
MODEL_PATH=waste_classifier_final.keras
IMAGE_SIZE=224
APP_TITLE=♻️ Waste Classification & Awareness App
```

---

## 🚀 Setup Instructions

### First Time Setup
```bash
# 1. Activate virtual environment
.\venv\Scripts\Activate.ps1

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

### Running the App
```bash
# Make sure venv is activated
streamlit run app.py
```

The app will start at `http://localhost:8501`

---

## 💻 Usage

### How to Use

1. **Open the App** - Navigate to the Streamlit interface
2. **Upload Image** - Click "Choose an image..." and select a waste image
3. **Get Classification** - The model predicts the waste type with confidence score
4. **View Information** - See:
   - Waste type category
   - Environmental information
   - Environmental impact statistics
   - DIY local action tips
5. **Take Action** - Follow the recommended practices for that waste type

### Example Workflow
```
Upload waste image → ML model processes (224x224 RGB) 
→ Predicts class (e.g., "plastic") → Shows all information 
→ User learns & takes action
```

---

## 🗑️ Waste Categories

The app classifies waste into 10 categories:

| Category | Type | Reusable | Recyclable |
|----------|------|----------|-----------|
| **Cardboard** | ♻️ Recyclable | ✅ Yes | ✅ Yes |
| **Glass** | 🌿 100% Recyclable | ✅ Multiple reuses | ✅ Yes |
| **Metal** | ⚙️ Infinitely reusable | ✅ Yes | ✅ Yes |
| **Paper** | 📄 Recyclable | ✅ Yes | ✅ Yes |
| **Plastic** | 🚯 Limited recyclability | ⚠️ Partial | ❌ Low rate |
| **Organics** | 🌱 Compostable | ✅ Yes (as compost) | ✅ Yes |
| **Shoes** | 👟 Reusable | ✅ Yes | ✅ Yes |
| **Clothes** | 👕 Reusable | ✅ Yes | ✅ Yes |
| **Battery** | ⚠️ Hazardous | ❌ Special handling | ✅ Yes |
| **Trash** | 🗑️ Non-recyclable | ❌ No | ❌ No |

---

## 📊 Environmental Impact Information

Each waste category includes:

- **Type Classification** - Recyclable, compostable, reusable, or hazardous
- **Detailed Information** - Material composition and recycling potential
- **Environmental Impact** - Statistics on emissions, water usage, pollution
- **Local Action** - DIY methods including:
  - Composting techniques
  - Upcycling ideas
  - Repair methods
  - Recycling center information

---

## 📈 Performance Metrics

### Model Performance
- **Architecture:** MobileNetV2-based Convolutional Neural Network
- **Test Accuracy:** 96.86% (Best Epoch: 15/28)
- **Parameters:** 2,588,490
- **Input Shape:** (224, 224, 3) - RGB images
- **Output:** 10 classes (waste categories)
- **Input Processing:** Normalized to 0-1 range
- **Training:** Validated with early stopping to prevent overfitting

### Prediction Performance
- **Inference Time:** < 1 second per image
- **Memory Usage:** ~500MB-1GB (TensorFlow + Streamlit)
- **Model Load Time:** ~5-10 seconds (first run)
- **App Responsiveness:** Real-time predictions after image upload

### Compatibility
- ✅ All dependencies compatible
- ✅ Model format (.keras) fully supported
- ✅ TensorFlow 2.21.0 optimized
- ✅ Tested on Python 3.11.4

---

## 🔮 Future Features

### Phase 2: Smart Complaint Registration
- **Automatic Detection** - AI identifies large waste accumulation
- **Severity Classification** - Categorizes waste by severity level (small/large)
- **MCD Integration** - Auto-register complaints to Municipal Corporation
- **Real-time Notifications** - Track complaint status and resolution

### Phase 3: Community Features
- **Leaderboards** - Reward top waste managers in communities
- **Social Sharing** - Share environmental tips and achievements
- **Community Map** - Show recycling centers and composting facilities nearby
- **Impact Dashboard** - Track personal environmental impact over time

### Phase 4: Advanced Analytics
- **Trend Analysis** - Identify waste patterns by location/time
- **Predictive Models** - Forecast waste accumulation

---

## 🌐 Deployment

### Current Deployment
- **Platform:** Render
- **URL:** [Your Render URL]
- **Status:** Live and accessible

### How to Deploy on Render

1. Push code to GitHub
2. Create Render account at render.com
3. Create new Web Service
4. Connect GitHub repository
5. Set build command: `pip install -r requirements.txt`
6. Set start command: `streamlit run app.py --server.port=10000`
7. Deploy!

### Environment Variables on Render
Add in Render dashboard:
```
STREAMLIT_SERVER_PORT=10000
STREAMLIT_SERVER_HEADLESS=true
```

---

## 👨‍💻 Author

**Aayush Negi**
- 5th Semester Project
- Focus: Environmental Awareness & Sustainable Waste Management
- GitHub: https://github.com/aayush-9310
- Email: aayushnegi9310@gmail.com

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---