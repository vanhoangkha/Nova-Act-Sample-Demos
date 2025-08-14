# 🚀 Nova Act Sample Demos

[![Nova Act](https://img.shields.io/badge/Nova%20Act-Latest-blue)](https://nova.amazon.com/act)
[![Python](https://img.shields.io/badge/Python-3.10%2B-green)](https://python.org)
[![Official](https://img.shields.io/badge/Based%20On-Official%20README-brightgreen)](https://github.com/aws/nova-act)

**Complete sample demos collection** based on the official Nova Act README - Amazon's browser automation SDK.

> 🎯 **Based on**: [Official README](https://github.com/aws/nova-act) with all features and best practices

## ⚡ Quick Start (30 seconds)

```bash
# 1. Auto setup
python3 quick_setup.py

# 2. Set API key (get from nova.amazon.com/act)
export NOVA_ACT_API_KEY="your_api_key_here"

# 3. Run all official samples
python3 run_all_samples.py
```

## 🎯 Available Demos

### 📚 **Official Samples** (Based on official README)

#### ☕ 1. Coffee Maker Order (`sample_01_coffee_maker.py`) ⭐
- Order coffee maker on Amazon
- Following Quick Start guide from official README
- **Features**: Basic act() usage, Amazon automation
- **Duration**: ~3 minutes

#### 📖 2. Book Extraction (`sample_02_book_extraction.py`) ⭐⭐
- Extract NYT bestseller book list with Pydantic
- Schema validation and structured data
- **Features**: Pydantic BaseModel, Schema validation
- **Duration**: ~2 minutes

#### ⚡ 3. Parallel Processing (`sample_03_parallel_books.py`) ⭐⭐⭐
- Collect books from multiple years with ThreadPoolExecutor
- Multiple NovaAct instances running in parallel
- **Features**: ThreadPoolExecutor, Error handling
- **Duration**: ~5 minutes

#### 🔐 4. Authentication & Sessions (`sample_04_authentication.py`) ⭐⭐⭐
- Persistent browser state with user_data_dir
- Session management and parallel processing with cloning
- **Features**: user_data_dir, Session persistence, BOOL_SCHEMA
- **Duration**: ~4 minutes

#### 🔒 5. Sensitive Data Handling (`sample_05_sensitive_data.py`) ⭐⭐
- Handle passwords and sensitive information safely
- CAPTCHA handling and security best practices
- **Features**: getpass, Playwright keyboard, CAPTCHA handling
- **Duration**: ~3 minutes

#### 📁 6. File Operations (`sample_06_file_operations.py`) ⭐⭐⭐
- Upload/download files with Playwright integration
- Multiple files, drag & drop, page content download
- **Features**: File upload, Download capture, Multiple files
- **Duration**: ~3.5 minutes

#### 🚀 7. Advanced Features (`sample_07_advanced_features.py`) ⭐⭐⭐⭐
- Logging, video recording, S3 integration, proxy
- Production-ready features and configurations
- **Features**: Custom logging, Video recording, S3, Proxy
- **Duration**: ~2.5 minutes

#### 🎮 8. Interactive Mode (`sample_08_interactive_mode.py`) ⭐⭐
- Interactive control and debugging
- Step-by-step workflow with user input
- **Features**: Interactive session, Debugging, Breakpoints
- **Duration**: ~5 minutes (interactive)

## 🛠️ Installation & Usage

### 📋 Requirements
- **Python 3.10+**
- **Nova Act API Key** from [nova.amazon.com/act](https://nova.amazon.com/act)
- **Internet connection**

### ⚡ Quick Setup
```bash
# Clone repository
git clone https://github.com/vanhoangkha/nova-act-samples.git
cd nova-act-samples

# Auto setup
python3 quick_setup.py

# Set API key
export NOVA_ACT_API_KEY="your_api_key_here"

# Run official samples
python3 run_all_samples.py
```

### 🎮 Run Individual Demos

**Official samples:**
```bash
python3 sample_01_coffee_maker.py        # Coffee maker order
python3 sample_02_book_extraction.py     # Pydantic extraction
python3 sample_03_parallel_books.py      # Parallel processing
python3 sample_04_authentication.py      # Authentication
python3 sample_05_sensitive_data.py      # Sensitive data
python3 sample_06_file_operations.py     # File operations
python3 sample_07_advanced_features.py   # Advanced features
python3 sample_08_interactive_mode.py    # Interactive mode
```

**Run all:**
```bash
python3 run_all_samples.py              # Run all official samples
```

## 💡 Code Examples

### Quick Start - Coffee Maker
```python
from nova_act import NovaAct

with NovaAct(starting_page="https://www.amazon.com") as nova:
    nova.act("search for a coffee maker")
    nova.act("select the first result")
    nova.act("scroll down or up until you see 'add to cart' and then click 'add to cart'")
```

### Pydantic Schema Extraction
```python
from pydantic import BaseModel
from nova_act import NovaAct

class Book(BaseModel):
    title: str
    author: str

class BookList(BaseModel):
    books: list[Book]

with NovaAct(starting_page="https://example.com") as nova:
    result = nova.act("Return the books", schema=BookList.model_json_schema())
    if result.matches_schema:
        book_list = BookList.model_validate(result.parsed_response)
```

### Parallel Processing
```python
from concurrent.futures import ThreadPoolExecutor
from nova_act import NovaAct, ActError

def get_books(year):
    with NovaAct(starting_page=f"https://example.com/{year}") as nova:
        # Extract books for this year
        pass

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = {executor.submit(get_books, year): year for year in [2020, 2021, 2022]}
    for future in as_completed(futures.keys()):
        try:
            result = future.result()
        except ActError as exc:
            print(f"Error: {exc}")
```

## 🔧 Troubleshooting

### ❌ API Key Error
```bash
# Check API key
echo $NOVA_ACT_API_KEY

# Set API key
export NOVA_ACT_API_KEY="your_key_here"
```

### ❌ "Missing X server" Error
Samples are configured with `headless=True` to run on servers.

### ❌ Samples Running Slowly
Normal - Nova Act needs time to analyze web pages (2-5 minutes/sample).

### ❌ Interactive Samples
Some samples require user interaction (authentication, interactive mode).

## 📁 Repository Structure

```
Nova-Act-sample/
├── 📄 README.md                        # Main guide
├── ⚡ quick_setup.py                   # Auto setup
├── 🚀 run_all_samples.py              # Run all official samples
└── 📚 Official Samples:
    ├── ☕ sample_01_coffee_maker.py        # Coffee maker order
    ├── 📖 sample_02_book_extraction.py     # Pydantic extraction
    ├── ⚡ sample_03_parallel_books.py      # Parallel processing
    ├── 🔐 sample_04_authentication.py      # Authentication
    ├── 🔒 sample_05_sensitive_data.py      # Sensitive data
    ├── 📁 sample_06_file_operations.py     # File operations
    ├── 🚀 sample_07_advanced_features.py   # Advanced features
    └── 🎮 sample_08_interactive_mode.py    # Interactive mode
```

## 🎓 Learning Nova Act

### Step 1: Understand Basics
```python
# Nova Act works by sending natural language commands
with NovaAct(starting_page="https://example.com") as nova:
    result = nova.act("Click the login button")
    print(result.response)
```

### Step 2: Prescriptive Prompting
```python
# ❌ DON'T - Too general
nova.act("Find my recent order and reorder it")

# ✅ DO - Specific steps
nova.act("Click the hamburger menu icon")
nova.act("Go to Order History")
nova.act("Find my most recent order from India Palace and reorder it")
```

### Step 3: Schema-based Extraction
```python
# Use schema for structured data
from pydantic import BaseModel

class Product(BaseModel):
    name: str
    price: str

result = nova.act("Extract product info", schema=Product.model_json_schema())
if result.matches_schema:
    product = Product.model_validate(result.parsed_response)
```

### Step 4: Advanced Features
```python
# Parallel processing, authentication, file operations, etc.
# See official samples for detailed learning
```

## 🌟 Key Features

### 🤖 **Core Features**
- **Prescriptive Prompting**: Break tasks into specific steps
- **Schema-based Extraction**: Pydantic integration for structured data
- **Error Handling**: Robust error management with ActError
- **Session Management**: Persistent authentication and state

### ⚡ **Advanced Features**
- **Parallel Processing**: Multiple browser instances with ThreadPoolExecutor
- **File Operations**: Upload/download automation
- **Interactive Mode**: Real-time control and debugging
- **Production Ready**: Video recording, S3 integration, custom logging

### 🛡️ **Security Features**
- **Sensitive Data Handling**: Safe password input with getpass
- **CAPTCHA Support**: Manual CAPTCHA solving workflow
- **Proxy Support**: Proxy configuration for network routing
- **User Agent**: Custom user agent configuration

## 📚 Documentation & Support

- **Nova Act Official**: [GitHub](https://github.com/aws/nova-act)
- **API Documentation**: [nova.amazon.com/act](https://nova.amazon.com/act)
- **Blog Post**: [labs.amazon.science/blog/nova-act](https://labs.amazon.science/blog/nova-act)
- **Issues**: [GitHub Issues](https://github.com/vanhoangkha/nova-act-samples/issues)

## 🤝 Contributing

1. Fork repository
2. Create new branch (`git checkout -b feature/new-sample`)
3. Commit changes (`git commit -m 'Add new sample'`)
4. Push branch (`git push origin feature/new-sample`)
5. Create Pull Request

## ⚠️ Important Notes

1. **⚠️** Nova Act may encounter prompt injections from third-party websites
2. **🔒** Do not share your API key
3. **🛡️** Do not provide sensitive information to Nova Act
4. **👀** Monitor Nova Act and use according to Acceptable Use Policy
5. **🤖** Look for `NovaAct` in user agent string to identify agent

---

⭐ **Star this repository** if samples are helpful!

🔗 **Get API key**: [nova.amazon.com/act](https://nova.amazon.com/act)

💡 **Start with**: `sample_01_coffee_maker.py` to understand how Nova Act works!
