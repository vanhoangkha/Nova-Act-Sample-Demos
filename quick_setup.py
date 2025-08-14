#!/usr/bin/env python3
"""
⚡ Quick Setup for Nova Act Samples
Auto setup script for official samples
"""

import os
import subprocess
import sys

def check_python():
    """Check Python version"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 10):
        print(f"❌ Need Python 3.10+, current: {version.major}.{version.minor}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
    return True

def install_nova_act():
    """Install Nova Act"""
    print("📦 Installing Nova Act...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "nova-act"], 
                      check=True, capture_output=True)
        print("✅ Nova Act installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing Nova Act: {e}")
        print("💡 Try creating virtual environment:")
        print("   python3 -m venv nova_env")
        print("   source nova_env/bin/activate")
        print("   pip install nova-act")
        return False

def check_api_key():
    """Check and guide API key setup"""
    api_key = os.getenv('NOVA_ACT_API_KEY')
    if api_key:
        print(f"✅ API Key is set: {api_key[:8]}...")
        return True
    else:
        print("❌ No API Key found")
        print("\n🔧 How to setup API Key:")
        print("1. Visit: https://nova.amazon.com/act")
        print("2. Register and get API key")
        print("3. Run: export NOVA_ACT_API_KEY='your_api_key_here'")
        print("4. Or add to ~/.bashrc for permanent setup")
        return False

def test_import():
    """Test Nova Act import"""
    try:
        import nova_act
        print("✅ Nova Act import successful")
        return True
    except ImportError as e:
        print(f"❌ Error importing Nova Act: {e}")
        return False

def main():
    print("⚡ Quick Setup for Nova Act Official Samples")
    print("=" * 50)
    print("📚 Based on official README: https://github.com/aws/nova-act")
    
    # Check Python
    if not check_python():
        return
    
    # Install Nova Act
    if not install_nova_act():
        return
    
    # Test import
    if not test_import():
        return
    
    # Check API key
    api_key_ok = check_api_key()
    
    print("\n" + "=" * 50)
    print("📊 SETUP STATUS")
    print("=" * 50)
    print("✅ Python: OK")
    print("✅ Nova Act: OK")
    print(f"{'✅' if api_key_ok else '❌'} API Key: {'OK' if api_key_ok else 'Not setup'}")
    
    if api_key_ok:
        print("\n🎉 Setup complete! You can run samples:")
        print("   python3 run_all_samples.py")
    else:
        print("\n⚠️ Need to setup API Key before running samples")
        print("   After getting API key, run: python3 run_all_samples.py")
    
    print("\n💡 Available Official Samples:")
    samples = [
        "sample_01_coffee_maker.py - Coffee maker order (Quick Start)",
        "sample_02_book_extraction.py - Pydantic schema extraction", 
        "sample_03_parallel_books.py - Parallel processing",
        "sample_04_authentication.py - Authentication & sessions",
        "sample_05_sensitive_data.py - Sensitive data handling",
        "sample_06_file_operations.py - File upload/download",
        "sample_07_advanced_features.py - Logging, video, S3",
        "sample_08_interactive_mode.py - Interactive control"
    ]
    for sample in samples:
        print(f"   • {sample}")
    
    print(f"\n🔗 References:")
    print("   • Nova Act Official: https://github.com/aws/nova-act")
    print("   • API Documentation: https://nova.amazon.com/act")
    print("   • Blog: https://labs.amazon.science/blog/nova-act")

if __name__ == "__main__":
    main()
