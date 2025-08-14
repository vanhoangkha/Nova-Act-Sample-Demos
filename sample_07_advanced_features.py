#!/usr/bin/env python3
"""
🚀 Sample 07: Advanced Features
Demo logging, video recording, S3 integration, và các tính năng nâng cao
"""

import os
import tempfile
import logging
from pathlib import Path
from nova_act import NovaAct

def demo_custom_logging():
    """Demo custom logging configuration"""
    
    print("📝 Demo Custom Logging")
    print("-" * 30)
    
    # Tạo custom logs directory
    logs_dir = tempfile.mkdtemp(prefix="nova_act_logs_")
    print(f"📁 Logs directory: {logs_dir}")
    
    try:
        with NovaAct(
            starting_page="https://example.com",
            logs_directory=logs_dir,
            headless=True
        ) as nova:
            
            print("🔍 Thực hiện một số actions để tạo logs...")
            nova.act("find the main heading on the page")
            nova.act("scroll down to see more content")
            nova.act("look for any links on the page")
            
        # Kiểm tra logs được tạo
        logs_path = Path(logs_dir)
        log_files = list(logs_path.rglob("*.html"))
        
        print(f"📊 Tạo được {len(log_files)} log files:")
        for log_file in log_files:
            print(f"   📄 {log_file.name}")
            
        print(f"💡 Xem logs tại: {logs_dir}")
        
    except Exception as e:
        print(f"❌ Lỗi logging: {e}")

def demo_video_recording():
    """Demo video recording"""
    
    print("\n🎥 Demo Video Recording")
    print("-" * 30)
    
    # Tạo directory cho video
    video_dir = tempfile.mkdtemp(prefix="nova_act_video_")
    print(f"🎬 Video directory: {video_dir}")
    
    try:
        with NovaAct(
            starting_page="https://example.com",
            logs_directory=video_dir,
            record_video=True,  # Enable video recording
            headless=True
        ) as nova:
            
            print("🎬 Đang recording video session...")
            
            # Thực hiện các actions để record
            nova.act("scroll to the top of the page")
            nova.act("find and read the main heading")
            nova.act("scroll down slowly to see the content")
            nova.act("scroll back to the top")
            
        # Kiểm tra video files
        video_path = Path(video_dir)
        video_files = list(video_path.rglob("*.webm"))
        
        print(f"🎥 Tạo được {len(video_files)} video files:")
        for video_file in video_files:
            size_mb = video_file.stat().st_size / (1024 * 1024)
            print(f"   🎬 {video_file.name} ({size_mb:.2f} MB)")
            
        print(f"💡 Xem video tại: {video_dir}")
        
    except Exception as e:
        print(f"❌ Lỗi video recording: {e}")

def demo_s3_integration():
    """Demo S3 integration (simulation)"""
    
    print("\n☁️ Demo S3 Integration")
    print("-" * 30)
    
    # Note: Cần AWS credentials để thực sự upload S3
    print("💡 S3 Integration cần AWS credentials")
    print("📋 Ví dụ code cho S3Writer:")
    
    s3_example = '''
import boto3
from nova_act import NovaAct
from nova_act.util.s3_writer import S3Writer

# Tạo boto3 session
boto_session = boto3.Session()

# Tạo S3Writer
s3_writer = S3Writer(
    boto_session=boto_session,
    s3_bucket_name="my-nova-act-bucket",
    s3_prefix="sessions/",
    metadata={"Project": "NovaActDemo"}
)

# Sử dụng với NovaAct
with NovaAct(
    starting_page="https://example.com",
    boto_session=boto_session,
    stop_hooks=[s3_writer]  # Auto upload khi session kết thúc
) as nova:
    nova.act("perform some actions")
    # Files sẽ tự động upload lên S3 khi session kết thúc
'''
    
    print(s3_example)
    
    # Simulate S3 operations
    print("🔄 Simulating S3 operations...")
    print("   📤 Uploading session logs to S3...")
    print("   📤 Uploading video recordings to S3...")
    print("   📤 Uploading screenshots to S3...")
    print("   ✅ S3 upload completed!")
    
    print("\n🔑 Required AWS permissions:")
    print("   • s3:ListObjects on bucket and prefix")
    print("   • s3:PutObject on bucket and prefix")

def demo_proxy_configuration():
    """Demo proxy configuration"""
    
    print("\n🌐 Demo Proxy Configuration")
    print("-" * 30)
    
    # Ví dụ proxy configs
    proxy_configs = [
        {
            "name": "Basic Proxy",
            "config": {
                "server": "http://proxy.example.com:8080"
            }
        },
        {
            "name": "Authenticated Proxy",
            "config": {
                "server": "http://proxy.example.com:8080",
                "username": "myusername",
                "password": "mypassword"
            }
        }
    ]
    
    print("📋 Proxy configuration examples:")
    for proxy in proxy_configs:
        print(f"\n🔧 {proxy['name']}:")
        for key, value in proxy['config'].items():
            if key == 'password':
                print(f"   {key}: {'*' * len(str(value))}")
            else:
                print(f"   {key}: {value}")
    
    print("\n💡 Usage example:")
    proxy_example = '''
proxy_config = {
    "server": "http://proxy.example.com:8080",
    "username": "user",
    "password": "pass"
}

with NovaAct(
    starting_page="https://example.com",
    proxy=proxy_config
) as nova:
    nova.act("browse with proxy")
'''
    print(proxy_example)

def demo_custom_user_agent():
    """Demo custom user agent"""
    
    print("\n🤖 Demo Custom User Agent")
    print("-" * 30)
    
    custom_agents = [
        "NovaActBot/1.0 (Educational Purpose)",
        "MyApp/2.0 NovaAct Integration",
        "CustomAgent/1.5 (https://mysite.com)"
    ]
    
    print("📋 Custom User Agent examples:")
    for i, agent in enumerate(custom_agents, 1):
        print(f"   {i}. {agent}")
    
    try:
        # Demo với custom user agent
        with NovaAct(
            starting_page="https://httpbin.org/user-agent",
            user_agent=custom_agents[0],
            headless=True
        ) as nova:
            
            print(f"🤖 Sử dụng User Agent: {custom_agents[0]}")
            result = nova.act("get the user agent information displayed on the page")
            print(f"📄 Response: {result.response}")
            
    except Exception as e:
        print(f"❌ Lỗi custom user agent: {e}")

def demo_headless_debugging():
    """Demo headless debugging với remote debugging"""
    
    print("\n🔍 Demo Headless Debugging")
    print("-" * 30)
    
    print("💡 Để debug headless session:")
    print("1. Set environment variable:")
    print("   export NOVA_ACT_BROWSER_ARGS='--remote-debugging-port=9222'")
    print("2. Chạy Nova Act với headless=True")
    print("3. Mở browser tại: http://localhost:9222/json")
    print("4. Copy devtoolsFrontendUrl để debug")
    
    debug_example = '''
# Terminal 1: Set debugging
export NOVA_ACT_BROWSER_ARGS="--remote-debugging-port=9222"

# Terminal 1: Run headless session
with NovaAct(starting_page="https://example.com", headless=True) as nova:
    nova.act("perform actions")
    time.sleep(60)  # Keep session alive for debugging

# Terminal 2: Access debugging
curl http://localhost:9222/json
# Copy devtoolsFrontendUrl and open in browser
'''
    
    print("\n📋 Debug workflow:")
    print(debug_example)

def main():
    """Demo advanced features"""
    
    # Kiểm tra API key
    api_key = os.getenv('NOVA_ACT_API_KEY')
    if not api_key:
        print("❌ Vui lòng set NOVA_ACT_API_KEY")
        return
    
    print("🚀 Sample 07: Advanced Features")
    print("=" * 50)
    print("🎛️ Logging, Video, S3, Proxy, và các tính năng nâng cao")
    
    # Set log level cho demo
    os.environ['NOVA_ACT_LOG_LEVEL'] = str(logging.INFO)
    
    # Danh sách demos
    demos = [
        ("Custom Logging", demo_custom_logging),
        ("Video Recording", demo_video_recording),
        ("S3 Integration", demo_s3_integration),
        ("Proxy Configuration", demo_proxy_configuration),
        ("Custom User Agent", demo_custom_user_agent),
        ("Headless Debugging", demo_headless_debugging)
    ]
    
    print(f"\n📋 Sẽ chạy {len(demos)} advanced demos:")
    for i, (name, _) in enumerate(demos, 1):
        print(f"   {i}. {name}")
    
    # Chạy từng demo
    for demo_name, demo_func in demos:
        print(f"\n{'='*50}")
        print(f"🎯 {demo_name}")
        print(f"{'='*50}")
        
        try:
            demo_func()
        except KeyboardInterrupt:
            print("⏸️ Demo bị dừng bởi user")
            break
        except Exception as e:
            print(f"❌ Lỗi trong {demo_name}: {e}")
        
        print(f"✅ Hoàn thành {demo_name}")
    
    print(f"\n💡 Ví dụ này minh họa:")
    print("   • logs_directory cho custom logging")
    print("   • record_video=True cho video recording")
    print("   • S3Writer cho cloud storage")
    print("   • proxy configuration")
    print("   • user_agent customization")
    print("   • Remote debugging cho headless mode")
    print("   • NOVA_ACT_LOG_LEVEL environment variable")
    print("   • NOVA_ACT_BROWSER_ARGS cho browser options")
    
    print(f"\n🚀 Advanced Features Checklist:")
    print("   ✅ Custom logging directory")
    print("   ✅ Video recording")
    print("   ✅ S3 integration setup")
    print("   ✅ Proxy configuration")
    print("   ✅ Custom user agent")
    print("   ✅ Headless debugging")
    print("   ✅ Environment variables")

if __name__ == "__main__":
    main()
