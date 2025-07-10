#!/usr/bin/env python3
"""
API参数格式调试脚本
测试不同的参数格式组合
"""

import requests
import json
import time

def test_api_format(test_name, payload):
    """测试特定格式的API请求"""
    print(f"\n🔍 测试 {test_name}")
    print("=" * 50)
    
    url = "http://10.68.186.130:8080/v1/chat-messages"
    headers = {
        "Authorization": "Bearer app-iDGyLFqNoZeI309eQCbT7zbo",
        "Content-Type": "application/json"
    }
    
    print(f"📄 请求参数: {json.dumps(payload, indent=2, ensure_ascii=False)}")
    print("-" * 30)
    
    try:
        response = requests.post(
            url=url,
            headers=headers,
            json=payload,
            timeout=30
        )
        
        print(f"📊 状态码: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ 请求成功！")
            response_text = response.text
            print(f"📄 响应内容: {response_text[:200]}...")
            return True
        else:
            print(f"❌ 请求失败！")
            print(f"📄 错误响应: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ 请求异常: {e}")
        return False

def main():
    """主函数 - 测试多种参数格式"""
    print("🔥 API参数格式调试工具")
    print("=" * 50)
    
    # 测试1: inputs中包含content
    format1 = {
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
    
    # 测试2: 直接包含content字段
    format2 = {
        "inputs": {},
        "query": "What are the specs of the iPhone 13 Pro Max?",
        "content": "What are the specs of the iPhone 13 Pro Max?",
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
    
    # 测试3: 去掉files数组
    format3 = {
        "inputs": {
            "content": "What are the specs of the iPhone 13 Pro Max?"
        },
        "query": "What are the specs of the iPhone 13 Pro Max?",
        "response_mode": "streaming",
        "conversation_id": "",
        "user": "abc-123"
    }
    
    # 测试4: 简化版本
    format4 = {
        "inputs": {},
        "query": "What are the specs of the iPhone 13 Pro Max?",
        "response_mode": "streaming",
        "user": "abc-123"
    }
    
    # 测试5: 非streaming模式
    format5 = {
        "inputs": {
            "content": "What are the specs of the iPhone 13 Pro Max?"
        },
        "query": "What are the specs of the iPhone 13 Pro Max?",
        "response_mode": "blocking",
        "conversation_id": "",
        "user": "abc-123"
    }
    
    # 测试6: 使用message格式
    format6 = {
        "inputs": {},
        "query": "What are the specs of the iPhone 13 Pro Max?",
        "response_mode": "streaming",
        "conversation_id": "",
        "user": "abc-123",
        "files": []
    }
    
    test_formats = [
        ("格式1: inputs中包含content", format1),
        ("格式2: 直接包含content字段", format2),
        ("格式3: 去掉files数组", format3),
        ("格式4: 简化版本", format4),
        ("格式5: 非streaming模式", format5),
        ("格式6: 空files数组", format6)
    ]
    
    successful_formats = []
    
    for test_name, payload in test_formats:
        if test_api_format(test_name, payload):
            successful_formats.append(test_name)
    
    print(f"\n🎯 测试结果总结:")
    print("=" * 50)
    if successful_formats:
        print("✅ 成功的格式:")
        for fmt in successful_formats:
            print(f"   - {fmt}")
    else:
        print("❌ 没有成功的格式")
    
    print("\n💡 建议:")
    print("   - 检查API文档确认正确的参数格式")
    print("   - 尝试使用其他认证方式")
    print("   - 确认API版本是否正确")

if __name__ == "__main__":
    main() 