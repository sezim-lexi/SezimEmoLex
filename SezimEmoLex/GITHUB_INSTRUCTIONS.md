# How to Upload SezimEmoLex to GitHub

This guide will walk you through uploading the SezimEmoLex package to GitHub and making it ready for public use.

---

## Step 1: Create a GitHub Repository

1. Go to [GitHub.com](https://github.com)
2. Click the **"+"** icon in the top-right corner
3. Select **"New repository"**
4. Fill in the form:
   - **Repository name**: `sezim-emolex` (or `SezimEmoLex`)
   - **Description**: `A Kazakh Sentiment & Emotion Lexicon - 8,557 words with 8 emotions and sentiment polarity`
   - **Public** (select this option)
   - **Add a README**: Uncheck this (we already have one)
   - **Add .gitignore**: Uncheck this (we already have one)
   - **Choose a license**: Uncheck this (we already have one)
5. Click **"Create repository"**

---

## Step 2: Upload Files to GitHub

### Option A: Using Git Command Line (Recommended)

```bash
# 1. Navigate to the SezimEmoLex directory
cd /path/to/SezimEmoLex

# 2. Initialize Git (if not already done)
git init

# 3. Add all files
git add .

# 4. Create the first commit
git commit -m "Initial commit: SezimEmoLex v1.0.0 - Kazakh Sentiment & Emotion Lexicon"

# 5. Add the remote repository (replace YOUR-USERNAME)
git remote add origin https://github.com/YOUR-USERNAME/sezim-emolex.git

# 6. Set the main branch
git branch -M main

# 7. Push to GitHub
git push -u origin main
```

### Option B: Using GitHub Web Interface

1. Open your new repository on GitHub
2. Click **"Add file"** → **"Upload files"**
3. Drag and drop all files from the `SezimEmoLex` folder
4. Write a commit message: `Initial commit: SezimEmoLex v1.0.0`
5. Click **"Commit changes"**

---

## Step 3: Verify Your Repository

After uploading, verify that all files are present:

- ✅ `README.md` - Main documentation
- ✅ `pyproject.toml` - Package configuration
- ✅ `CITATION.cff` - Citation metadata
- ✅ `LICENSE` - MIT License for code
- ✅ `data/sezim_emolex.csv` - The lexicon data
- ✅ `data/LICENSE_DATA.md` - CC BY 4.0 License for data
- ✅ `src/sezim_emolex/` - Python package code
- ✅ `tests/test_sezim_emolex.py` - Unit tests
- ✅ `examples/quickstart.ipynb` - Jupyter notebook example

---

## Step 4: Enable GitHub Features

### Add Topics

1. Go to your repository page
2. Click **"Settings"** (gear icon, top-right)
3. Scroll down to **"Topics"**
4. Add relevant topics:
   - `kazakh`
   - `nlp`
   - `sentiment-analysis`
   - `emotion-analysis`
   - `lexicon`
   - `python`

### Enable GitHub Pages (Optional)

If you want to host documentation:

1. Go to **"Settings"** → **"Pages"**
2. Select **"Deploy from a branch"**
3. Choose **"main"** branch and **"/root"** folder
4. Click **"Save"**

### Add a Release

1. Go to **"Releases"** (right sidebar)
2. Click **"Create a new release"**
3. Fill in:
   - **Tag version**: `v1.0.0`
   - **Release title**: `SezimEmoLex v1.0.0`
   - **Description**: 
     ```
     Initial release of SezimEmoLex - A Kazakh Sentiment & Emotion Lexicon
     
     - 8,557 Kazakh words
     - 8 emotions: anger, anticipation, disgust, fear, joy, sadness, surprise, trust
     - Sentiment polarity: positive, negative, neutral
     - Python API similar to NRCLex
     - Full test coverage
     ```
4. Click **"Publish release"**

---

## Step 5: Test Installation

### Install from GitHub

```bash
pip install git+https://github.com/YOUR-USERNAME/sezim-emolex.git
```

### Run Tests

```bash
git clone https://github.com/YOUR-USERNAME/sezim-emolex.git
cd sezim-emolex
pip install -e .
pytest tests/ -v
```

### Quick Test

```python
from sezim_emolex import SezimEmoLex, SezimAnalyzer

# Test 1: Single word
lex = SezimEmoLex("ашу")
print(f"Sentiment: {lex.get_sentiment_label()}")

# Test 2: Text analysis
analyzer = SezimAnalyzer()
result = analyzer.analyze("мен ашуландым")
print(f"Overall sentiment: {result['sentiment_label']}")
```

---

## Step 6: Publish to PyPI (Optional)

If you want to make the package installable with `pip install sezim-emolex`:

### 1. Create PyPI Account

- Go to [PyPI.org](https://pypi.org)
- Click **"Register"**
- Create an account

### 2. Install Build Tools

```bash
pip install build twine
```

### 3. Build the Package

```bash
cd /path/to/SezimEmoLex
python -m build
```

This creates:
- `dist/sezim_emolex-1.0.0.tar.gz` (source distribution)
- `dist/sezim_emolex-1.0.0-py3-none-any.whl` (wheel)

### 4. Upload to PyPI

```bash
python -m twine upload dist/*
```

You'll be prompted for your PyPI credentials.

### 5. Install from PyPI

```bash
pip install sezim-emolex
```

---

## Step 7: Add Badges to README

Update your `README.md` with badges:

```markdown
[![PyPI version](https://badge.fury.io/py/sezim-emolex.svg)](https://badge.fury.io/py/sezim-emolex)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![GitHub Stars](https://img.shields.io/github/stars/YOUR-USERNAME/sezim-emolex.svg)](https://github.com/YOUR-USERNAME/sezim-emolex)
```

---

## Step 8: Update Links in Files

Before uploading, update these placeholders in your files:

| File | Placeholder | Replace With |
|------|-------------|--------------|
| `README.md` | `YOUR-USERNAME` | Your GitHub username |
| `README.md` | `YOUR-USERNAME` | Your GitHub username |
| `pyproject.toml` | `your-username` | Your GitHub username |
| `pyproject.toml` | `nazerke.algashbekova@example.com` | Your email |
| `CITATION.cff` | `Nazerke Algashbekova` | Your name |

---

## Troubleshooting

### Git Authentication Error

If you get a "Permission denied" error:

1. Generate a personal access token on GitHub:
   - Go to **Settings** → **Developer settings** → **Personal access tokens**
   - Click **"Generate new token"**
   - Select `repo` scope
   - Copy the token

2. Use the token instead of your password:
   ```bash
   git remote set-url origin https://YOUR-TOKEN@github.com/YOUR-USERNAME/sezim-emolex.git
   ```

### Tests Fail After Installation

Make sure the data file is included:

```bash
# Check if data file is in the installed package
python -c "from sezim_emolex import SezimEmoLex; lex = SezimEmoLex('абайлау'); print(lex.found)"
```

If it fails, reinstall in development mode:

```bash
pip install -e .
```

---

## Next Steps

1. ✅ Create GitHub repository
2. ✅ Upload files
3. ✅ Enable GitHub features
4. ✅ Test installation
5. ✅ (Optional) Publish to PyPI
6. Share your repository with the community!

---

## Resources

- [GitHub Documentation](https://docs.github.com)
- [Python Packaging Guide](https://packaging.python.org)
- [PyPI Help](https://pypi.org/help/)
- [Creative Commons Licenses](https://creativecommons.org/licenses/)

---

**Good luck! 🚀**
