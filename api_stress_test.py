import asyncio
import aiohttp
import time
import json
import random
from typing import List, Dict, Any
from question_bank import question_bank

class APIStressTester:
    def __init__(self, url: str, headers: Dict[str, str], payload: Dict[str, Any], use_random_questions: bool = True):
        self.url = url
        self.headers = headers
        self.payload = payload
        self.use_random_questions = use_random_questions
        self.results = []
        self.question_stats = {}  # 统计问题类型分布
        
    async def send_request(self, session: aiohttp.ClientSession, request_id: int) -> Dict[str, Any]:
        """发送单个请求"""
        start_time = time.time()
        
        # 创建请求payload的副本
        current_payload = self.payload.copy()
        question_category = "fixed"
        
        # 如果使用随机问题，生成新问题
        if self.use_random_questions:
            random_question = question_bank.get_random_question()
            question_category = random_question["category"]
            
            # 更新payload中的问题
            current_payload["inputs"] = {
                "content": random_question["content"]
            }
            current_payload["query"] = random_question["question"]
            
            # 统计问题类型
            if question_category in self.question_stats:
                self.question_stats[question_category] += 1
            else:
                self.question_stats[question_category] = 1
        
        try:
            async with session.post(
                self.url, 
                headers=self.headers, 
                json=current_payload,
                timeout=aiohttp.ClientTimeout(total=60)
            ) as response:
                end_time = time.time()
                response_time = end_time - start_time
                
                # 由于是streaming模式，我们需要读取完整响应
                response_text = await response.text()
                
                return {
                    'request_id': request_id,
                    'status_code': response.status,
                    'response_time': response_time,
                    'response_size': len(response_text),
                    'success': response.status == 200,
                    'error': None,
                    'question_category': question_category
                }
        except Exception as e:
            end_time = time.time()
            response_time = end_time - start_time
            return {
                'request_id': request_id,
                'status_code': 0,
                'response_time': response_time,
                'response_size': 0,
                'success': False,
                'error': str(e),
                'question_category': question_category
            }

    async def run_stress_test(self, concurrent_requests: int = 150):
        """运行压测"""
        print(f"🚀 开始压测，并发数: {concurrent_requests}")
        print(f"📡 目标API: {self.url}")
        print("-" * 50)
        
        connector = aiohttp.TCPConnector(limit=concurrent_requests * 2)
        
        async with aiohttp.ClientSession(connector=connector) as session:
            # 创建并发任务
            tasks = []
            for i in range(concurrent_requests):
                task = asyncio.create_task(self.send_request(session, i + 1))
                tasks.append(task)
            
            # 记录开始时间
            start_time = time.time()
            
            # 等待所有任务完成
            self.results = await asyncio.gather(*tasks, return_exceptions=True)
            
            # 记录结束时间
            end_time = time.time()
            total_time = end_time - start_time
            
            # 打印结果
            self.print_results(total_time)
    
    def print_results(self, total_time: float):
        """打印压测结果"""
        successful_requests = [r for r in self.results if isinstance(r, dict) and r['success']]
        failed_requests = [r for r in self.results if isinstance(r, dict) and not r['success']]
        exception_requests = [r for r in self.results if not isinstance(r, dict)]
        
        total_requests = len(self.results)
        success_count = len(successful_requests)
        failed_count = len(failed_requests)
        exception_count = len(exception_requests)
        
        print(f"\n📊 压测结果统计:")
        print(f"{'='*50}")
        print(f"总请求数: {total_requests}")
        print(f"成功请求: {success_count}")
        print(f"失败请求: {failed_count}")
        print(f"异常请求: {exception_count}")
        print(f"成功率: {success_count/total_requests*100:.2f}%")
        print(f"总耗时: {total_time:.2f}秒")
        print(f"平均QPS: {total_requests/total_time:.2f}")
        
        if successful_requests:
            response_times = [r['response_time'] for r in successful_requests]
            response_times.sort()
            
            print(f"\n⏱️  响应时间统计:")
            print(f"平均响应时间: {sum(response_times)/len(response_times):.3f}秒")
            print(f"最快响应时间: {min(response_times):.3f}秒")
            print(f"最慢响应时间: {max(response_times):.3f}秒")
            print(f"50%响应时间: {response_times[len(response_times)//2]:.3f}秒")
            print(f"95%响应时间: {response_times[int(len(response_times)*0.95)]:.3f}秒")
            print(f"99%响应时间: {response_times[int(len(response_times)*0.99)]:.3f}秒")
        
        if failed_requests:
            print(f"\n❌ 失败请求详情:")
            status_codes = {}
            for req in failed_requests:
                status_code = req['status_code']
                if status_code in status_codes:
                    status_codes[status_code] += 1
                else:
                    status_codes[status_code] = 1
            
            for status_code, count in status_codes.items():
                print(f"状态码 {status_code}: {count}次")
        
        if exception_requests:
            print(f"\n⚠️  异常请求: {exception_count}次")
        
        # 显示问题类型统计
        if self.use_random_questions and self.question_stats:
            print(f"\n🎯 问题类型分布:")
            for category, count in sorted(self.question_stats.items()):
                percentage = (count / total_requests) * 100
                print(f"   {category}: {count}次 ({percentage:.1f}%)")


async def main():
    """主函数"""
    # API配置
    url = "{APIurl}"
    
    headers = {
        "Authorization": "Bearer {APIkey}",
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
    
    # 创建压测实例 (使用随机问题)
    tester = APIStressTester(url, headers, payload, use_random_questions=True)
    
    # 运行压测
    await tester.run_stress_test(concurrent_requests=150)


if __name__ == "__main__":
    print("🔥 API压测工具 - 大模型版")
    print("=" * 50)
    print(f"📊 内置问题库: {question_bank.get_total_questions_count()}个问题")
    print(f"📋 问题类别: {', '.join(question_bank.get_all_categories())}")
    print("🎯 使用随机问题进行压测")
    print()
    
    # 运行异步主函数
    asyncio.run(main()) 


    
