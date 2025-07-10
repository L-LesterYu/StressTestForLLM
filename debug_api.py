#!/usr/bin/env python3
"""
API调试脚本
用于测试单个API请求是否能正常访问
"""

import requests
import json
import time

def test_api_single_request():
    """测试单个API请求"""
    print("🔍 API调试测试")
    print("=" * 50)
    
    # API配置
    url = "http://10.68.186.130:8080/v1/chat-messages"
    headers = {
        "Authorization": "Bearer app-iDGyLFqNoZeI309eQCbT7zbo",
        "Content-Type": "application/json"
    }
    
    payload = {
        "inputs": {
            "content": "What are the specs of the iPhone 13 Pro Max?"
        },
        "query": "What are the specs of the iPhone 13 Pro Max?",
        "response_mode": "streaming",
        "conversation_id": "",
        "user": "abc-123",
        "files": [
            {
                "type": "image",
                "transfer_method": "remote_url",
                "url": "https://cloud.dify.ai/logo/logo-site.png"
            }
        ]
    }
    
    print(f"📡 测试地址: {url}")
    print(f"📋 请求头: {headers}")
    print(f"📄 请求参数: {json.dumps(payload, indent=2, ensure_ascii=False)}")
    print("-" * 50)
    
    try:
        # 发送请求
        print("🚀 发送请求...")
        start_time = time.time()
        
        response = requests.post(
            url=url,
            headers=headers,
            json=payload,
            timeout=30,
            stream=True  # 因为是streaming模式
        )
        
        end_time = time.time()
        response_time = end_time - start_time
        
        print(f"⏱️  响应时间: {response_time:.3f}秒")
        print(f"📊 状态码: {response.status_code}")
        print(f"📋 响应头: {dict(response.headers)}")
        
        if response.status_code == 200:
            print("✅ 请求成功！")
            print("\n📄 响应内容:")
            print("-" * 30)
            
            # 读取流式响应
            content = ""
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')
                    print(decoded_line)
                    content += decoded_line + "\n"
                    
            print(f"\n📊 响应内容长度: {len(content)}字符")
            
        else:
            print(f"❌ 请求失败！状态码: {response.status_code}")
            print(f"📄 错误响应: {response.text}")
            
    except requests.exceptions.ConnectionError as e:
        print(f"❌ 连接错误: {e}")
        print("💡 可能原因:")
        print("   - API服务器未启动")
        print("   - 网络连接问题")
        print("   - IP地址或端口错误")
        
    except requests.exceptions.Timeout as e:
        print(f"❌ 超时错误: {e}")
        print("💡 可能原因:")
        print("   - API响应时间过长")
        print("   - 网络延迟较高")
        
    except requests.exceptions.RequestException as e:
        print(f"❌ 请求错误: {e}")
        
    except Exception as e:
        print(f"❌ 未知错误: {e}")

def test_simple_ping():
    """测试简单的连通性"""
    print("\n🏓 测试基本连通性")
    print("=" * 30)
    
    # 先测试最基本的连接
    import socket
    
    try:
        host = "10.68.186.130"
        port = 8080
        
        print(f"🔗 测试连接 {host}:{port}")
        
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(10)
        result = sock.connect_ex((host, port))
        sock.close()
        
        if result == 0:
            print("✅ 网络连接正常")
        else:
            print(f"❌ 网络连接失败，错误代码: {result}")
            
    except Exception as e:
        print(f"❌ 网络测试失败: {e}")

if __name__ == "__main__":
    # 先测试网络连通性
    test_simple_ping()
    
    # 再测试API请求
    test_api_single_request() 