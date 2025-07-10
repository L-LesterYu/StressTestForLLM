#!/usr/bin/env python3
"""
简化的API压测运行脚本
用户可以在这里快速修改参数
"""

import asyncio
from api_stress_test import APIStressTester
from question_bank import question_bank

# 压测配置参数
CONFIG = {
    # API地址
    "url": "http://10.68.186.130:8080/v1/chat-messages",
    
    # 请求头
    "headers": {
        "Authorization": "Bearer app-iDGyLFqNoZeI309eQCbT7zbo",
        "Content-Type": "application/json"
    },
    
    # 请求参数
    "payload": {
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
    },
    
    # 并发数
    "concurrent_requests": 150,
    
    # 是否使用随机问题（True=使用随机问题，False=使用固定问题）
    "use_random_questions": True
}

async def main():
    """主函数"""
    print("🔥 API压测工具 - 大模型版")
    print("=" * 50)
    print(f"📡 目标API: {CONFIG['url']}")
    print(f"🚀 并发数: {CONFIG['concurrent_requests']}")
    print(f"🎯 使用随机问题: {'是' if CONFIG['use_random_questions'] else '否'}")
    
    if CONFIG['use_random_questions']:
        print(f"📊 问题库统计: {question_bank.get_total_questions_count()}个问题")
        print(f"📋 问题类别: {', '.join(question_bank.get_all_categories())}")
    
    print()
    
    # 创建压测实例
    tester = APIStressTester(
        url=CONFIG["url"],
        headers=CONFIG["headers"],
        payload=CONFIG["payload"],
        use_random_questions=CONFIG["use_random_questions"]
    )
    
    # 运行压测
    await tester.run_stress_test(concurrent_requests=CONFIG["concurrent_requests"])

if __name__ == "__main__":
    # 运行压测
    asyncio.run(main()) 