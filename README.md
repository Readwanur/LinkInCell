# LinkInCell 🔗

[![PyPI version](https://badge.fury.io/py/LinkInCell.svg)](https://badge.fury.io/py/LinkInCell)
[![Python Versions](https://img.shields.io/pypi/pyversions/LinkInCell.svg)](https://pypi.org/project/LinkInCell/)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

**LinkInCell** is a lightweight PyPI package that brings the web to your Jupyter environment. It allows you to seamlessly render fully interactive websites and embedded YouTube videos directly inside your `.ipynb` notebook cells.

---

## ✨ Features

* **Render Any Website:** Display live, interactive web pages within an iframe in your notebook.
* **YouTube Integration:** Native support for embedding and playing YouTube videos without leaving your workflow.
* **Lightweight & Fast:** Minimal dependencies, designed specifically for Jupyter environments.
* **Customizable:** Adjust the width and height of the rendering area to fit your screen perfectly.

## 📦 Installation

You can install `LinkInCell` directly from PyPI using pip:

```bash
pip install LinkInCell
```

```bash
from LinkInCell.youtube import render_youtube

render_youtube("https://www.youtube.com/watch?v=h25pePMdoPA&t=712s")
```

```bash
from LinkInCell.web import render_web

render_web("https://www.google.com/")
```

# How to install this package in your system

```bash
conda create -n LinkInCell_env python=3.8 -y
```

```bash
conda activate LinkInCell_env
```

```bash
pip install -r requirements_dev.txt
```


## 🚀 Usage

Using `LinkInCell` is incredibly simple. Import the package and pass your target URL.

### 1. Rendering a Website

python
from linkincell import render_web

# Render a full webpage inside your notebook cell
render_web("https://en.wikipedia.org/wiki/Python_(programming_language)", width="100%", height="500px")


### 2. Rendering a YouTube Video

python
from linkincell import render_youtube

# Pass the standard YouTube URL or the video ID
render_youtube("https://www.youtube.com/watch?v=dQw4w9WgXcQ", width=800, height=450)


## 🛠️ Requirements

* Python 3.6+
* Jupyter Notebook or JupyterLab
* `IPython` (Usually comes pre-installed with Jupyter)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Since open-source collaboration thrives on shared knowledge, feel free to check the [issues page](#) if you want to contribute.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

Distributed under the Apache License 2.0. See `LICENSE` for more information.

---
*Built for the community, by the community.*