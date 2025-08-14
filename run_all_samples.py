#!/usr/bin/env python3
"""
🚀 Run All Nova Act Samples
Script to run all sample demos based on official README
"""

import os
import sys
import subprocess
import time
from datetime import datetime

def check_api_key():
    """Check API key"""
    api_key = os.getenv('NOVA_ACT_API_KEY')
    if not api_key:
        print("❌ Missing NOVA_ACT_API_KEY")
        print("\n🔧 How to setup:")
        print("export NOVA_ACT_API_KEY='your_api_key_here'")
        print("\n🔗 Get API key at: https://nova.amazon.com/act")
        return False
    
    print(f"✅ API Key: {api_key[:8]}...")
    return True

def run_sample(sample_file, sample_name, timeout=120):
    """Run a sample with timeout"""
    print(f"\n{'='*60}")
    print(f"🚀 Running {sample_name}")
    print(f"{'='*60}")
    print(f"⏱️ Timeout: {timeout}s")
    
    try:
        result = subprocess.run([sys.executable, sample_file], 
                              capture_output=True, text=True, timeout=timeout)
        
        if result.returncode == 0:
            print(result.stdout)
            print(f"✅ {sample_name} successful!")
            return True
        else:
            print(f"❌ {sample_name} failed:")
            print(result.stderr)
            return False
            
    except subprocess.TimeoutExpired:
        print(f"⏰ {sample_name} timeout (>{timeout}s)")
        print("💡 This sample may need more time")
        return False
    except Exception as e:
        print(f"❌ Error running {sample_name}: {e}")
        return False

def main():
    print("🎯 Nova Act - Official Sample Demos")
    print("=" * 60)
    print("📚 Based on official README: https://github.com/aws/nova-act")
    
    # Check API key
    if not check_api_key():
        return
    
    # Sample list based on README
    samples = [
        {
            "file": "sample_01_coffee_maker.py",
            "name": "Coffee Maker Order (Quick Start)",
            "description": "Order coffee maker on Amazon - following Quick Start guide",
            "timeout": 180,
            "difficulty": "⭐",
            "features": ["Basic act() usage", "Amazon automation"]
        },
        {
            "file": "sample_02_book_extraction.py",
            "name": "Book Extraction with Pydantic",
            "description": "Extract book list with Pydantic schema",
            "timeout": 120,
            "difficulty": "⭐⭐",
            "features": ["Pydantic BaseModel", "Schema validation", "Structured data"]
        },
        {
            "file": "sample_03_parallel_books.py",
            "name": "Parallel Processing",
            "description": "Collect books from multiple years with ThreadPoolExecutor",
            "timeout": 300,
            "difficulty": "⭐⭐⭐",
            "features": ["ThreadPoolExecutor", "Multiple NovaAct instances", "Error handling"]
        },
        {
            "file": "sample_04_authentication.py",
            "name": "Authentication & Sessions",
            "description": "Persistent browser state with user_data_dir",
            "timeout": 240,
            "difficulty": "⭐⭐⭐",
            "features": ["user_data_dir", "Session persistence", "BOOL_SCHEMA"]
        },
        {
            "file": "sample_05_sensitive_data.py",
            "name": "Sensitive Data Handling",
            "description": "Handle passwords and sensitive information safely",
            "timeout": 180,
            "difficulty": "⭐⭐",
            "features": ["getpass", "Playwright keyboard", "CAPTCHA handling"]
        },
        {
            "file": "sample_06_file_operations.py",
            "name": "File Upload & Download",
            "description": "Upload/download files with Playwright integration",
            "timeout": 200,
            "difficulty": "⭐⭐⭐",
            "features": ["File upload", "Download capture", "Multiple files"]
        },
        {
            "file": "sample_07_advanced_features.py",
            "name": "Advanced Features",
            "description": "Logging, video recording, S3, proxy configuration",
            "timeout": 150,
            "difficulty": "⭐⭐⭐⭐",
            "features": ["Custom logging", "Video recording", "S3 integration", "Proxy"]
        },
        {
            "file": "sample_08_interactive_mode.py",
            "name": "Interactive Mode",
            "description": "Interactive control and debugging",
            "timeout": 300,
            "difficulty": "⭐⭐",
            "features": ["Interactive session", "Step-by-step", "Debugging"]
        }
    ]
    
    # Statistics
    total_count = len(samples)
    
    print(f"\n📋 Will run {total_count} official samples:")
    for i, sample in enumerate(samples, 1):
        print(f"\n   {i}. {sample['name']} {sample['difficulty']}")
        print(f"      📝 {sample['description']}")
        print(f"      ⏱️ Timeout: {sample['timeout']}s")
        print(f"      🔧 Features: {', '.join(sample['features'])}")
    
    print(f"\n⚠️ IMPORTANT NOTES:")
    print("• These samples are based on Nova Act official README")
    print("• Some samples need user interaction (authentication, interactive mode)")
    print("• Samples use real websites and may take time")
    print("• Results may vary depending on when you run them")
    
    # Confirm run
    response = input(f"\n❓ Do you want to run all {total_count} samples? (y/N): ")
    if response.lower() != 'y':
        print("❌ Cancelled running samples")
        return
    
    print(f"\n⏱️ Starting samples...")
    start_time = time.time()
    
    # Run each sample
    success_count = 0
    results = []
    
    for i, sample in enumerate(samples, 1):
        if os.path.exists(sample["file"]):
            print(f"\n📊 Progress: {i}/{total_count}")
            
            sample_start = time.time()
            success = run_sample(sample["file"], sample["name"], sample["timeout"])
            sample_duration = time.time() - sample_start
            
            results.append({
                "name": sample["name"],
                "success": success,
                "duration": sample_duration,
                "difficulty": sample["difficulty"],
                "features": sample["features"]
            })
            
            if success:
                success_count += 1
            
            # Rest between samples
            if i < total_count:
                print("⏸️ Resting 5 seconds before next sample...")
                time.sleep(5)
        else:
            print(f"❌ File not found: {sample['file']}")
            results.append({
                "name": sample["name"],
                "success": False,
                "duration": 0,
                "difficulty": sample["difficulty"],
                "features": sample["features"]
            })
    
    # Summary
    end_time = time.time()
    total_duration = end_time - start_time
    
    print(f"\n{'='*60}")
    print("📊 OFFICIAL SAMPLES SUMMARY RESULTS")
    print(f"{'='*60}")
    print(f"⏰ Start time: {datetime.fromtimestamp(start_time).strftime('%H:%M:%S')}")
    print(f"⏰ End time: {datetime.fromtimestamp(end_time).strftime('%H:%M:%S')}")
    print(f"⏱️ Total time: {total_duration/60:.1f} minutes")
    print(f"✅ Successful: {success_count}/{total_count}")
    print(f"📈 Success rate: {success_count/total_count*100:.1f}%")
    
    print(f"\n📋 DETAILED RESULTS:")
    print("-" * 60)
    for result in results:
        status = "✅" if result["success"] else "❌"
        duration_str = f"{result['duration']:.1f}s" if result['duration'] > 0 else "N/A"
        print(f"{status} {result['name']} {result['difficulty']}")
        print(f"   ⏱️ Duration: {duration_str}")
        print(f"   🔧 Features: {', '.join(result['features'][:2])}...")
    
    # Analyze results
    if success_count == total_count:
        print("\n🎉 All samples ran successfully!")
        print("🏆 Nova Act works great with all features!")
    elif success_count > total_count * 0.7:
        print(f"\n🎯 Good results! {success_count}/{total_count} samples successful")
        print("💡 Some samples may need adjustments or user interaction")
    elif success_count > 0:
        print(f"\n⚠️ Average results: {success_count}/{total_count} samples successful")
        print("🔍 Check logs to understand failure reasons")
    else:
        print("\n❌ All samples failed")
        print("🔍 Check internet connection, API key and environment")
    
    print(f"\n💡 SUGGESTIONS:")
    print("• Run individual samples for detailed debugging")
    print("• Some samples need user interaction")
    print("• Use headless=False to see browser directly")
    print("• Check logs in each sample")
    
    print(f"\n🔗 References:")
    print("• Nova Act Official: https://github.com/aws/nova-act")
    print("• API Documentation: https://nova.amazon.com/act")
    print("• Blog Post: https://labs.amazon.science/blog/nova-act")

if __name__ == "__main__":
    main()
