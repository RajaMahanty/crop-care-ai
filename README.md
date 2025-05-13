# 🌿 CropCareAI: Plant Disease Recognition System

<div align="center">

![CropCareAI Banner](home_page.jpg)

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.17.0-orange)](https://www.tensorflow.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.39.0-red)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

</div>

## 📋 Overview

CropCareAI is an advanced plant disease recognition system that leverages deep learning to identify various plant diseases from images. This tool helps farmers, gardeners, and agricultural professionals quickly detect and address plant health issues, contributing to better crop management and yield optimization.

## ✨ Features

<details>
<summary>🔍 Click to expand features</summary>

### Core Features

```mermaid
graph TD
    A[CropCareAI] --> B[Image Analysis]
    A --> C[Disease Detection]
    A --> D[Treatment Recommendations]
    B --> E[Real-time Processing]
    C --> F[38 Disease Classes]
    D --> G[Detailed Reports]
```

### Supported Plants

```mermaid
mindmap
  root((CropCareAI))
    Apple
      Scab
      Black Rot
      Rust
    Blueberry
      Healthy
    Cherry
      Powdery Mildew
    Corn
      Leaf Spot
      Rust
    Grape
      Black Rot
      Leaf Blight
    Tomato
      Early Blight
      Late Blight
      Leaf Mold
```

</details>

## 🚀 Getting Started

### Prerequisites

| Requirement | Version |
| ----------- | ------- |
| Python      | 3.8+    |
| pip         | Latest  |
| RAM         | 8GB+    |
| Storage     | 1GB+    |

### Installation

```mermaid
graph LR
    A[Clone Repo] --> B[Install Dependencies]
    B --> C[Run Application]
    C --> D[Start Analysis]
```

1. Clone the repository:

```bash
git clone https://github.com/RajaMahanty/crop-care-ai.git
cd crop-care-ai
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
streamlit run main.py
```

## 🎯 Usage

```mermaid
sequenceDiagram
    participant U as User
    participant A as App
    participant M as Model

    U->>A: Upload Image
    A->>M: Process Image
    M->>A: Return Prediction
    A->>U: Show Results
```

## 📊 Model Performance

### Accuracy Metrics

```mermaid
pie title Model Accuracy Distribution
    "Training" : 98.5
    "Validation" : 96.2
    "Test" : 95.8
```

### Performance Statistics

| Metric              | Value |
| ------------------- | ----- |
| Training Accuracy   | 98.5% |
| Validation Accuracy | 96.2% |
| Test Accuracy       | 95.8% |
| Inference Time      | 0.8s  |
| Model Size          | 90MB  |

## 🛠️ Technical Stack

```mermaid
graph TB
    subgraph Frontend
        A[Streamlit]
    end
    subgraph Backend
        B[Python]
    end
    subgraph Deep Learning
        C[TensorFlow/Keras]
    end
    subgraph Processing
        D[OpenCV]
        E[Pillow]
        F[NumPy]
        G[Pandas]
    end
    subgraph Visualization
        H[Matplotlib]
        I[Plotly]
    end
```

## 📚 Dataset Information

### Dataset Distribution

```mermaid
pie title Dataset Split
    "Training" : 70295
    "Validation" : 17572
    "Test" : 33
```

### Dataset Statistics

| Category          | Count  | Percentage |
| ----------------- | ------ | ---------- |
| Training Images   | 70,295 | 80%        |
| Validation Images | 17,572 | 20%        |
| Test Images       | 33     | <1%        |
| Total Images      | 87,900 | 100%       |

## 🔄 Future Enhancements

```mermaid
gantt
    title Future Development Roadmap
    dateFormat  YYYY-MM-DD
    section Phase 1
    Video Analysis    :2024-03-01, 30d
    Mobile App       :2024-04-01, 45d
    section Phase 2
    Weather Integration :2024-05-15, 30d
    Multi-language    :2024-06-15, 30d
```

## 🤝 Contributing

### Development Workflow

```mermaid
graph LR
    A[Fork Repo] --> B[Create Branch]
    B --> C[Make Changes]
    C --> D[Test Changes]
    D --> E[Create PR]
    E --> F[Review]
    F --> G[Merge]
```

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

```mermaid
graph LR
    A[CropCareAI] --> B[PlantVillage Dataset]
    A --> C[Streamlit]
    A --> D[TensorFlow]
    A --> E[Open Source Community]
```

## 📧 Contact

- GitHub Issues: Create an issue
- Repository: [crop-care-ai](https://github.com/RajaMahanty/crop-care-ai)

---

<div align="center">
Made with ❤️ for better agriculture
</div>
